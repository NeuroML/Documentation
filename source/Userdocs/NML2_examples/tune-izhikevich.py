#!/usr/bin/env python3
"""
Example file showing the tuning of an Izhikevich neuron using pyNeuroML.

File: source/Userdocs/NML2_examples/tune-izhikevich.py

Copyright 2021 NeuroML contributors
"""


from pyneuroml.tune.NeuroMLTuner import run_optimisation
import pynwb
import numpy as np
from pyelectro.utils import simple_network_analysis
import typing
from pyneuroml.pynml import read_neuroml2_file
from pyneuroml.pynml import validate_neuroml2
from pyneuroml.pynml import write_neuroml2_file
from neuroml import (NeuroMLDocument, Izhikevich2007Cell, PulseGenerator,
                     Network, Population, ExplicitInput)


def get_data_metrics() -> typing.Tuple[typing.Dict, typing.Dict]:
    """Analyse the data to get metrics to tune against.

    :returns: metrics from pyelectro analysis, current that was used

    """
    analysis_results = {}
    currents = {}
    with pynwb.NWBHDF5IO("./FergusonEtAl2015_PYR3.nwb", 'r') as io:
        datafile = io.read()
        # let's get the first series
        total_acquisitions = len(datafile.acquisition)
        for acq in range(1, total_acquisitions):
            print("Going over acquisition # {}".format(acq))

            data_v = datafile.acquisition['CurrentClampSeries_{:02d}'.format(acq)].data[:] * 1000.
            sampling_rate = datafile.acquisition['CurrentClampSeries_{:02d}'.format(acq)].rate
            # generate time steps from sampling rate
            data_t = np.arange(0, len(data_v) / sampling_rate, 1. / sampling_rate) * 1000.
            analysis_results[acq] = (simple_network_analysis({acq: data_v}, data_t))

            # extract current from description, but can be extracted from other
            # locations also, such as the CurrentClampStimulus series.
            data_i = datafile.acquisition['CurrentClampSeries_{:02d}'.format(acq)].description.split('(')[1].split('~')[1].split(' ')[0]
            currents[acq] = data_i

    return (analysis_results, currents)


def tune_izh_model(acq_list: typing.List, metrics_from_data: typing.Dict,
                   currents: typing.Dict) -> None:
    """Tune networks model against the data.

    Here we generate a network with the necessary number of Izhikevich cells,
    one for each current stimulus, and tune them against the experimental data.

    :param acq_list: list of indices of acquisitions/sweeps to tune against
    :type acq_list: list
    :param metrics_from_data: dictionary with the sweep number as index, and
        the dictionary containing metrics generated from the analysis
    :type metrics_from_data: dict
    :param currents: dictionary with sweep number as index and stimulus current
        value
    """

    # length of simulation of the cells---should match the length of the
    # experiment
    sim_time = 2000.
    # Create a NeuroML template network simulation file that we will use for
    # the tuning
    template_doc = NeuroMLDocument(id="IzhTuneNet")
    # Add an Izhikevich cell with some parameters to the document
    template_doc.izhikevich2007_cells.append(Izhikevich2007Cell(id="Izh2007", C="100pF", v0="-60mV",
                                                                k="0.7nS_per_mV", vr="-60mV",
                                                                vt="-40mV", vpeak="35mV",
                                                                a="0.03per_ms", b="-2nS", c="-50.0mV", d="100pA"))
    template_doc.networks.append(Network(id="Network0"))
    # Add a cell for each acquisition list
    popsize = len(acq_list)
    template_doc.networks[0].populations.append(Population(id="Pop0",
                                                           component="Izh2007", size=popsize))

    # Add a current source for each cell, matching the currents that
    # were used in the experimental study.
    counter = 0
    for acq in acq_list:
        template_doc.pulse_generators.append(PulseGenerator(id="Stim{}".format(counter),
                                                            delay="0ms", duration="1000ms",
                                                            amplitude="{}pA".format(currents[acq]))
                                             )
        template_doc.networks[0].explicit_inputs.append(ExplicitInput(target="Pop0[{}]".format(counter),
                                                                      input="Stim{}".format(counter)))
        counter = counter + 1

    # Print a summary
    print(template_doc.summary())

    # Write to a neuroml file and validate it.
    reference = "TuneIzhFergusonPyr3"
    template_filename = "{}.net.nml".format(reference)
    write_neuroml2_file(template_doc, template_filename, validate=True)

    # Now for the tuning bits

    # format is type:id/variable:id/units
    # supported types: cell/channel/izhikevich2007cell
    # supported variables:
    #  - channel: vShift
    #  - cell: channelDensity, vShift_channelDensity, channelDensityNernst,
    #  erev_id, erev_ion, specificCapacitance, resistivity
    #  - izhikevich2007Cell: all available attributes

    # we want to tune these parameters
    parameters = [
        "izhikevich2007Cell:Izh2007/C/pF",
        "izhikevich2007Cell:Izh2007/k/nS_per_mV",
        "izhikevich2007Cell:Izh2007/vr/mV",
        "izhikevich2007Cell:Izh2007/vt/mV",
        "izhikevich2007Cell:Izh2007/vpeak/mV",
        "izhikevich2007Cell:Izh2007/a/per_ms",
        "izhikevich2007Cell:Izh2007/b/nS",
        "izhikevich2007Cell:Izh2007/c/mV",
        "izhikevich2007Cell:Izh2007/d/pA"
    ]

    # parameters from the izhikevich cell models that we want to fit
    # one for each parameter: [ C, k, vr, vt, vpeak, a, b, c, d ]
    min_constraints = [80, 0.5, -80, -80, 20, 0.0, -4, -80, 80]
    max_constraints = [120, 0.9, -40, -20, 50, 0.05, 0., -20, 120]

    ctr = 0

    target_data = {}
    weights = {}

    # Set up our target data and so on
    for acq in acq_list:
        # data to fit to:
        # format: populationid/cell instance/component type/variable
        # variable from pyelectro, for example:
        # https://pyelectro.readthedocs.io/en/latest/pyelectro.html?highlight=mean_spike_frequency#pyelectro.analysis.mean_spike_frequency
        mean_spike_frequency = "Pop0/{}/Izh2007/v:mean_spike_frequency".format(ctr)
        average_last_1percent = "Pop0/{}/Izh2007/v:average_last_1percent".format(ctr)

        # these are only generated for traces with spikes
        average_maximum = "Pop0/{}/Izh2007/v:average_maximum".format(ctr)
        average_minimum = "Pop0/{}/Izh2007/v:average_minimum".format(ctr)

        weights[mean_spike_frequency] = 5
        weights[average_last_1percent] = 1

        # value of the target data from our data set
        target_data[mean_spike_frequency] = metrics_from_data[acq]["{}:mean_spike_frequency".format(acq)]
        target_data[average_last_1percent] = metrics_from_data[acq]["{}:average_last_1percent".format(acq)]

        # only add these if the experimental data includes them
        if "{}:average_maximum".format(acq) in metrics_from_data[acq]:
            weights[average_maximum] = 1
            target_data[average_maximum] = metrics_from_data[acq]["{}:average_maximum".format(acq)]
        if "{}:average_minimum".format(acq) in metrics_from_data[acq]:
            weights[average_minimum] = 1
            target_data[average_minimum] = metrics_from_data[acq]["{}:average_minimum".format(acq)]

        ctr = ctr + 1

    # simulator to use
    simulator = "jNeuroML"

    run_optimisation(
        # Prefix for new files
        prefix="TuneIzh",
        # Name of the NeuroML template file
        neuroml_file=template_filename,
        # Name of the network
        target="Network0",
        # Parameters to be fitted
        parameters=parameters,
        # Our max and min constraints
        max_constraints=max_constraints,
        min_constraints=min_constraints,
        # Weights we set for parameters
        weights=weights,
        # The experimental metrics to fit to
        target_data=target_data,
        # Simulation time
        sim_time=sim_time,
        # EC parameters
        population_size=20,
        max_evaluations=100,
        num_selected=10,
        num_offspring=10,
        mutation_rate=0.5,
        num_elites=3,
        # Seed value
        seed=12345,
        # Simulator
        simulator=simulator,
        nogui=True,
    )


if __name__ == "__main__":
    analysis_results, currents = get_data_metrics()
    # Get tuned models against any of the sweeps:
    # Note: (1 is the key in the dictionary, not the index)
    # tune_izh_model(1, analysis_results[1], float(currents[1]))
    # tune_izh_model(33, analysis_results[33], float(currents[33]))

    """

    for i in len(analysis_results):
        tune_izh_model(list(analysis_results.items())[i], currents[i])
    """
    tune_izh_model([1, 33], analysis_results, currents)
