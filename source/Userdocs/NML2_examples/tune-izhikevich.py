#!/usr/bin/env python3
"""
Example file showing the tuning of an Izhikevich neuron using pyNeuroML.

File: source/Userdocs/NML2_examples/tune-izhikevich.py

Copyright 2021 NeuroML contributors
"""


from pyneuroml.tune.NeuroMLTuner import run_optimisation


neuroml_file = "izhikevich2007_single_cell_network.nml"
sim_time = 100.

# format is type:id/variable:id/units
# supported types: cell/channel/izhikevich2007cell
# supported variables:
#  - channel: vShift
#  - cell: channelDensity, vShift_channelDensity, channelDensityNernst,
#  erev_id, erev_ion, specificCapacitance, resistivity
#  - izhikevich2007Cell: all available attributes
known_target_values = {
    "izhikevich2007Cell:izh2007RS0/a/per_ms": 0.03,
    "izhikevich2007Cell:izh2007RS0/b/nS": -2.,
    "izhikevich2007Cell:izh2007RS0/c/mV": -50.0
}

parameters = [
    "izhikevich2007Cell:izh2007RS0/a/per_ms",
    "izhikevich2007Cell:izh2007RS0/b/nS",
    "izhikevich2007Cell:izh2007RS0/c/mV"
]

min_constraints = [0., -4., -100.0]
max_constraints = [0.1, 2.0, 0.0]


# data to fit to:
# format: populationid/cell instance/component type/variable
# variable from pyelectro, for example:
# https://pyelectro.readthedocs.io/en/latest/pyelectro.html?highlight=mean_spike_frequency#pyelectro.analysis.mean_spike_frequency
mean_spike_frequency = "IzhPop0/0/izh2007RS0/v:mean_spike_frequency"
average_maximum = "IzhPop0/0/izh2007RS0/v:average_maximum"
average_minimum = "IzhPop0/0/izh2007RS0/v:average_minimum"

# value of the target data
target_data = {
    mean_spike_frequency: 18.6,
    average_maximum: 30.0,
    average_minimum: -65.0,
}

# weights can be set to the different
weights = {
    mean_spike_frequency: 1.0,
    average_maximum: 1.0,
    average_minimum: 1.0
}

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
    known_target_values=known_target_values,
)
