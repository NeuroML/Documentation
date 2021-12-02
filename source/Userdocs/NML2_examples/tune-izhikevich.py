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


def get_data_metrics() -> typing.Dict:
    """Analyse the data to get metrics to tune against.
    :returns: TODO

    """

    analysis_results = {}
    with pynwb.NWBHDF5IO("./FergusonEtAl2015_PYR3.nwb", 'r') as io:
        datafile = io.read()
        # let's get the first series
        total_acquisitions = len(datafile.acquisition)
        for acq in range(1, total_acquisitions):
            print("Looking at {}".format(acq))
            print(datafile.acquisition['CurrentClampSeries_{:02d}'.format(acq)])
            data_v = datafile.acquisition['CurrentClampSeries_{:02d}'.format(acq)].data[:] * 1000.
            print(datafile.stimulus['CurrentClampStimulusSeries_{:02d}'.format(acq)])
            data_i = datafile.stimulus['CurrentClampStimulusSeries_{:02d}'.format(acq)].data[:]
            print(data_i)
            sampling_rate = datafile.acquisition['CurrentClampSeries_{:02d}'.format(acq)].rate
            data_t = np.arange(0, len(data_i) / sampling_rate, 1. / sampling_rate) * 1000.

            analysis_results[acq] = (simple_network_analysis({acq: data_v}, data_t))
            # TODO: get value of current from stimulus and set that for the
            # pulsegenerator

    return analysis_results


def tune_izh_model(data_params):
    """Tune the model against the data."""

    neuroml_file = "izhikevich2007_single_cell_network.nml"
    sim_time = 1000.

# format is type:id/variable:id/units
# supported types: cell/channel/izhikevich2007cell
# supported variables:
#  - channel: vShift
#  - cell: channelDensity, vShift_channelDensity, channelDensityNernst,
#  erev_id, erev_ion, specificCapacitance, resistivity
#  - izhikevich2007Cell: all available attributes

    acq = data_params[0]
    metrics = data_params[1]

    # parameters from the izhikevich cell model that we want to fit
    parameters = [
        "izhikevich2007Cell:izh2007RS0/C/pF",
        "izhikevich2007Cell:izh2007RS0/k/nS_per_mV",
        "izhikevich2007Cell:izh2007RS0/vr/mV",
        "izhikevich2007Cell:izh2007RS0/vt/mV",
        "izhikevich2007Cell:izh2007RS0/vpeak/mV",
        "izhikevich2007Cell:izh2007RS0/a/per_ms",
        "izhikevich2007Cell:izh2007RS0/b/nS",
        "izhikevich2007Cell:izh2007RS0/c/mV",
        "izhikevich2007Cell:izh2007RS0/d/pA"
        "pulseGenerator:pulseGen0/duration/ms",
        "pulseGenerator:pulseGen0/amplitude/nA",
    ]

    # <izhikevich2007Cell id="izh2007RS0" C="100pF" v0="-60mV" k="0.7nS_per_mV" vr="-60mV" vt="-40mV" vpeak="35mV" a="0.03per_ms" b="-2nS" c="-50.0mV" d="100pA"/>
    # one for each parameter
    min_constraints = [80, -80, 0.5, -80, -80, 20, 0.0, -4, -80, 80]
    max_constraints = [120, -40, 0.9, -40, -20, 50, 0.05, 0., -20, 120]

    # data to fit to:
    # format: populationid/cell instance/component type/variable
    # variable from pyelectro, for example:
    # https://pyelectro.readthedocs.io/en/latest/pyelectro.html?highlight=mean_spike_frequency#pyelectro.analysis.mean_spike_frequency
    mean_spike_frequency = "IzhPop0/0/izh2007RS0/v:mean_spike_frequency"
    average_last_1percent = "IzhPop0/0/izh2007RS0/v:average_last_1percent"

    # these are only generated for traces with spikes
    average_maximum = "IzhPop0/0/izh2007RS0/v:average_maximum"
    average_minimum = "IzhPop0/0/izh2007RS0/v:average_minimum"

    weights = {
        mean_spike_frequency: 5,
        average_last_1percent: 1
    }

    # value of the target data from our data set
    target_data = {
        mean_spike_frequency: metrics["{}:mean_spike_frequency".format(acq)],
        average_last_1percent: metrics["{}:average_last_1percent".format(acq)],
    }

    # only add these if the experimental data includes them
    if "{}:average_maximum".format(acq) in metrics:
        weights[average_maximum] = 1
        target_data[average_maximum] =  metrics["{}:average_maximum".format(acq)]
    if "{}:average_minimum".format(acq) in metrics:
        weights[average_minimum] = 1
        target_data[average_minimum] =  metrics["{}:average_minimum".format(acq)]

# simulator to use
    simulator = "jNeuroML"

    run_optimisation(
        prefix="TuneIzh",
        neuroml_file=neuroml_file,
        target="IzhNet",
        parameters=parameters,
        max_constraints=max_constraints,
        min_constraints=min_constraints,
        weights=weights,
        target_data=target_data,
        sim_time=sim_time,
        population_size=20,
        max_evaluations=100,
        num_selected=10,
        num_offspring=10,
        mutation_rate=0.5,
        num_elites=3,
        seed=12345,
        simulator=simulator,
        nogui=True,
    )


if __name__ == "__main__":
    analysis_results = get_data_metrics()
    # for r in analysis_results.items():
    # r = list(analysis_results.items())[0]
    # tune_izh_model(r)

