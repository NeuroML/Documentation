#!/usr/bin/env python3
"""
Example file showing the tuning of an Izhikevich neuron using pyNeuroML.

File: source/Userdocs/NML2_examples/tune-izhikevich.py

Copyright 2021 NeuroML contributors
"""


from pyneuroml.tune.NeuroMLTuner import run_optimisation
import pynwb  # type: ignore
import numpy as np
from pyelectro.utils import simple_network_analysis
from typing import List, Dict, Tuple
from pyneuroml.pynml import write_neuroml2_file
from pyneuroml.pynml import generate_plot
from pyneuroml.pynml import run_lems_with_jneuroml
from neuroml import (
    NeuroMLDocument,
    Izhikevich2007Cell,
    PulseGenerator,
    Network,
    Population,
    ExplicitInput,
)
from hdmf.container import Container
from pyneuroml.lems.LEMSSimulation import LEMSSimulation

import sys


def get_data_metrics(datafile: Container) -> Tuple[Dict, Dict, Dict]:
    """Analyse the data to get metrics to tune against.

    :returns: metrics from pyelectro analysis, currents, and the membrane potential values

    """
    analysis_results = {}
    currents = {}
    memb_vals = {}
    total_acquisitions = len(datafile.acquisition)

    for acq in range(1, total_acquisitions):
        print("Going over acquisition # {}".format(acq))

        # stimulus lasts about 1000ms, so we take about the first 1500 ms
        data_v = (
            datafile.acquisition["CurrentClampSeries_{:02d}".format(acq)].data[:15000] * 1000.0
        )
        # get sampling rate from the data
        sampling_rate = datafile.acquisition[
            "CurrentClampSeries_{:02d}".format(acq)
        ].rate
        # generate time steps from sampling rate
        data_t = np.arange(0, len(data_v) / sampling_rate, 1.0 / sampling_rate) * 1000.0
        # run the analysis
        analysis_results[acq] = simple_network_analysis({acq: data_v}, data_t)

        # extract current from description, but can be extracted from other
        # locations also, such as the CurrentClampStimulus series.
        data_i = (
            datafile.acquisition["CurrentClampSeries_{:02d}".format(acq)]
            .description.split("(")[1]
            .split("~")[1]
            .split(" ")[0]
        )
        currents[acq] = data_i
        memb_vals[acq] = (data_t, data_v)

    return (analysis_results, currents, memb_vals)


def tune_izh_model(acq_list: List, metrics_from_data: Dict, currents: Dict) -> Dict:
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
    sim_time = 1500.0
    # Create a NeuroML template network simulation file that we will use for
    # the tuning
    template_doc = NeuroMLDocument(id="IzhTuneNet")
    # Add an Izhikevich cell with some parameters to the document
    template_doc.izhikevich2007_cells.append(
        Izhikevich2007Cell(
            id="Izh2007",
            C="100pF",
            v0="-60mV",
            k="0.7nS_per_mV",
            vr="-60mV",
            vt="-40mV",
            vpeak="35mV",
            a="0.03per_ms",
            b="-2nS",
            c="-50.0mV",
            d="100pA",
        )
    )
    template_doc.networks.append(Network(id="Network0"))
    # Add a cell for each acquisition list
    popsize = len(acq_list)
    template_doc.networks[0].populations.append(
        Population(id="Pop0", component="Izh2007", size=popsize)
    )

    # Add a current source for each cell, matching the currents that
    # were used in the experimental study.
    counter = 0
    for acq in acq_list:
        template_doc.pulse_generators.append(
            PulseGenerator(
                id="Stim{}".format(counter),
                delay="80ms",
                duration="1000ms",
                amplitude="{}pA".format(currents[acq]),
            )
        )
        template_doc.networks[0].explicit_inputs.append(
            ExplicitInput(
                target="Pop0[{}]".format(counter), input="Stim{}".format(counter)
            )
        )
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

    # we want to tune these parameters within these ranges
    # param: (min, max)
    parameters = {
        "izhikevich2007Cell:Izh2007/C/pF": (100, 300),
        "izhikevich2007Cell:Izh2007/k/nS_per_mV": (0.01, 2),
        "izhikevich2007Cell:Izh2007/vr/mV": (-70, -50),
        "izhikevich2007Cell:Izh2007/vt/mV": (-60, 0),
        "izhikevich2007Cell:Izh2007/vpeak/mV": (35, 70),
        "izhikevich2007Cell:Izh2007/a/per_ms": (0.001, 0.4),
        "izhikevich2007Cell:Izh2007/b/nS": (-10, 10),
        "izhikevich2007Cell:Izh2007/c/mV": (-65, -10),
        "izhikevich2007Cell:Izh2007/d/pA": (50, 500),
    }  # type: Dict[str, Tuple[float, float]]

    # Set up our target data and so on
    ctr = 0
    target_data = {}
    weights = {}
    for acq in acq_list:
        # data to fit to:
        # format: path/to/variable:metric
        # metric from pyelectro, for example:
        # https://pyelectro.readthedocs.io/en/latest/pyelectro.html?highlight=mean_spike_frequency#pyelectro.analysis.mean_spike_frequency
        mean_spike_frequency = "Pop0[{}]/v:mean_spike_frequency".format(ctr)
        average_last_1percent = "Pop0[{}]/v:average_last_1percent".format(ctr)
        first_spike_time = "Pop0[{}]/v:first_spike_time".format(ctr)

        # each metric can have an associated weight
        weights[mean_spike_frequency] = 1
        weights[average_last_1percent] = 1
        weights[first_spike_time] = 1

        # value of the target data from our data set
        target_data[mean_spike_frequency] = metrics_from_data[acq][
            "{}:mean_spike_frequency".format(acq)
        ]
        target_data[average_last_1percent] = metrics_from_data[acq][
            "{}:average_last_1percent".format(acq)
        ]
        target_data[first_spike_time] = metrics_from_data[acq][
            "{}:first_spike_time".format(acq)
        ]

        # only add these if the experimental data includes them
        # these are only generated for traces with spikes
        if "{}:average_maximum".format(acq) in metrics_from_data[acq]:
            average_maximum = "Pop0[{}]/v:average_maximum".format(ctr)
            weights[average_maximum] = 1
            target_data[average_maximum] = metrics_from_data[acq][
                "{}:average_maximum".format(acq)
            ]
        if "{}:average_minimum".format(acq) in metrics_from_data[acq]:
            average_minimum = "Pop0[{}]/v:average_minimum".format(ctr)
            weights[average_minimum] = 1
            target_data[average_minimum] = metrics_from_data[acq][
                "{}:average_minimum".format(acq)
            ]

        ctr = ctr + 1

    # simulator to use
    simulator = "jNeuroML"

    return run_optimisation(
        # Prefix for new files
        prefix="TuneIzh",
        # Name of the NeuroML template file
        neuroml_file=template_filename,
        # Name of the network
        target="Network0",
        # Parameters to be fitted
        parameters=list(parameters.keys()),
        # Our max and min constraints
        min_constraints=[v[0] for v in parameters.values()],
        max_constraints=[v[1] for v in parameters.values()],
        # Weights we set for parameters
        weights=weights,
        # The experimental metrics to fit to
        target_data=target_data,
        # Simulation time
        sim_time=sim_time,
        # EC parameters
        population_size=100,
        max_evaluations=500,
        num_selected=30,
        num_offspring=50,
        mutation_rate=0.9,
        num_elites=3,
        # Seed value
        seed=12345,
        # Simulator
        simulator=simulator,
        dt=0.025,
        show_plot_already='-nogui' not in sys.argv,
        save_to_file="fitted_izhikevich_fitness.png",
        save_to_file_scatter="fitted_izhikevich_scatter.png",
        save_to_file_hist="fitted_izhikevich_hist.png",
        save_to_file_output="fitted_izhikevich_output.png",
        num_parallel_evaluations=4,
    )


def run_fitted_cell_simulation(
    sweeps_to_tune_against: List, tuning_report: Dict, simulation_id: str
) -> None:
    """Run a simulation with the values obtained from the fitting

    :param tuning_report: tuning report from the optimser
    :type tuning_report: Dict
    :param simulation_id: text id of simulation
    :type simulation_id: str

    """
    # get the fittest variables
    fittest_vars = tuning_report["fittest vars"]
    C = str(fittest_vars["izhikevich2007Cell:Izh2007/C/pF"]) + "pF"
    k = str(fittest_vars["izhikevich2007Cell:Izh2007/k/nS_per_mV"]) + "nS_per_mV"
    vr = str(fittest_vars["izhikevich2007Cell:Izh2007/vr/mV"]) + "mV"
    vt = str(fittest_vars["izhikevich2007Cell:Izh2007/vt/mV"]) + "mV"
    vpeak = str(fittest_vars["izhikevich2007Cell:Izh2007/vpeak/mV"]) + "mV"
    a = str(fittest_vars["izhikevich2007Cell:Izh2007/a/per_ms"]) + "per_ms"
    b = str(fittest_vars["izhikevich2007Cell:Izh2007/b/nS"]) + "nS"
    c = str(fittest_vars["izhikevich2007Cell:Izh2007/c/mV"]) + "mV"
    d = str(fittest_vars["izhikevich2007Cell:Izh2007/d/pA"]) + "pA"

    # Create a simulation using our obtained parameters.
    # Note that the tuner generates a graph with the fitted values already, but
    # we want to keep a copy of our fitted cell also, so we'll create a NeuroML
    # Document ourselves also.
    sim_time = 1500.0
    simulation_doc = NeuroMLDocument(id="FittedNet")
    # Add an Izhikevich cell with some parameters to the document
    simulation_doc.izhikevich2007_cells.append(
        Izhikevich2007Cell(
            id="Izh2007",
            C=C,
            v0="-60mV",
            k=k,
            vr=vr,
            vt=vt,
            vpeak=vpeak,
            a=a,
            b=b,
            c=c,
            d=d,
        )
    )
    simulation_doc.networks.append(Network(id="Network0"))
    # Add a cell for each acquisition list
    popsize = len(sweeps_to_tune_against)
    simulation_doc.networks[0].populations.append(
        Population(id="Pop0", component="Izh2007", size=popsize)
    )

    # Add a current source for each cell, matching the currents that
    # were used in the experimental study.
    counter = 0
    for acq in sweeps_to_tune_against:
        simulation_doc.pulse_generators.append(
            PulseGenerator(
                id="Stim{}".format(counter),
                delay="80ms",
                duration="1000ms",
                amplitude="{}pA".format(currents[acq]),
            )
        )
        simulation_doc.networks[0].explicit_inputs.append(
            ExplicitInput(
                target="Pop0[{}]".format(counter), input="Stim{}".format(counter)
            )
        )
        counter = counter + 1

    # Print a summary
    print(simulation_doc.summary())

    # Write to a neuroml file and validate it.
    reference = "FittedIzhFergusonPyr3"
    simulation_filename = "{}.net.nml".format(reference)
    write_neuroml2_file(simulation_doc, simulation_filename, validate=True)

    simulation = LEMSSimulation(
        sim_id=simulation_id,
        duration=sim_time,
        dt=0.1,
        target="Network0",
        simulation_seed=54321,
    )
    simulation.include_neuroml2_file(simulation_filename)
    simulation.create_output_file("output0", "{}.v.dat".format(simulation_id))
    counter = 0
    for acq in sweeps_to_tune_against:
        simulation.add_column_to_output_file(
            "output0", "Pop0[{}]".format(counter), "Pop0[{}]/v".format(counter)
        )
        counter = counter + 1
    simulation_file = simulation.save_to_file()
    # simulate
    run_lems_with_jneuroml(simulation_file, max_memory="2G", nogui=True, plot=False)


def plot_sim_data(
    sweeps_to_tune_against: List, simulation_id: str, memb_pots: Dict
) -> None:
    """Plot data from our fitted simulation

    :param simulation_id: string id of simulation
    :type simulation_id: str
    """
    # Plot
    data_array = np.loadtxt("%s.v.dat" % simulation_id)

    # construct data for plotting
    counter = 0
    time_vals_list = []
    sim_v_list = []
    data_v_list = []
    data_t_list = []
    stim_vals = []
    for acq in sweeps_to_tune_against:
        stim_vals.append("{}pA".format(currents[acq]))

        # remains the same for all columns
        time_vals_list.append(data_array[:, 0] * 1000.0)
        sim_v_list.append(data_array[:, counter + 1] * 1000.0)

        data_v_list.append(memb_pots[acq][1])
        data_t_list.append(memb_pots[acq][0])

        counter = counter + 1

    # Model membrane potential plot
    generate_plot(
        xvalues=time_vals_list,
        yvalues=sim_v_list,
        labels=stim_vals,
        title="Membrane potential (model)",
        show_plot_already=False,
        save_figure_to="%s-model-v.png" % simulation_id,
        xaxis="time (ms)",
        yaxis="membrane potential (mV)",
    )
    # data membrane potential plot
    generate_plot(
        xvalues=data_t_list,
        yvalues=data_v_list,
        labels=stim_vals,
        title="Membrane potential (exp)",
        show_plot_already=False,
        save_figure_to="%s-exp-v.png" % simulation_id,
        xaxis="time (ms)",
        yaxis="membrane potential (mV)",
    )


if __name__ == "__main__":

    # set the default size for generated plots
    # https://matplotlib.org/stable/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file
    import matplotlib as mpl
    mpl.rcParams["figure.figsize"] = [18, 12]

    io = pynwb.NWBHDF5IO("./FergusonEtAl2015_PYR3.nwb", "r")
    datafile = io.read()

    analysis_results, currents, memb_pots = get_data_metrics(datafile)

    # Choose what sweeps to tune against.
    # There are 33 sweeps: 1..33.
    # sweeps_to_tune_against = [1, 2, 15, 30, 31, 32, 33]
    sweeps_to_tune_against = [16,21]
    report = tune_izh_model(sweeps_to_tune_against, analysis_results, currents)

    simulation_id = "fitted_izhikevich_sim"
    run_fitted_cell_simulation(sweeps_to_tune_against, report, simulation_id)

    plot_sim_data(sweeps_to_tune_against, simulation_id, memb_pots)

    # close the data file
    io.close()
