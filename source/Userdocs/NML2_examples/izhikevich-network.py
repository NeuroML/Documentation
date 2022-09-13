#!/usr/bin/env python3
"""
Create a simple network with two populations.
"""

import random
import numpy as np

from pyneuroml.utils import component_factory
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
import neuroml.writers as writers


nml_doc = component_factory("NeuroMLDocument", id="IzNet")

iz0 = component_factory(
    "Izhikevich2007Cell",
    id="iz2007RS0",
    v0="-60mV",
    C="100pF",
    k="0.7nS_per_mV",
    vr="-60mV",
    vt="-40mV",
    vpeak="35mV",
    a="0.03per_ms",
    b="-2nS",
    c="-50.0mV",
    d="100pA",
)

# Inspect the component, also show all members:
iz0.info(True)

# Add the component to the document, so that it can be used
nml_doc.add(iz0)

# Create a component of type ExpOneSynapse, and add it to the document
syn0 = component_factory(
    "ExpOneSynapse", id="syn0", gbase="65nS", erev="0mV", tau_decay="3ms"
)
nml_doc.add(syn0)

# Check what we have so far:
nml_doc.info(True)
# Also try:
print(nml_doc.summary())

# create the network: turned of validation because we will add populations next
net = component_factory("Network", id="IzNet", validate=False)

nml_doc.add(net)

# create the first population
size0 = 5
pop0 = component_factory("Population", id="IzPop0", component=iz0.id, size=size0)
# Set optional color property. Note: used later when generating plots
pop0.add(component_factory("Property", tag="color", value="0 0 .8"))
net.add(pop0)

# create the second population
size1 = 5
pop1 = component_factory("Population", id="IzPop1", component=iz0.id, size=size1)
pop1.add(component_factory("Property", tag="color", value=".8 0 0"))
net.add(pop1)

# network should be valid now that it contains populations
net.validate()

# create a projection from one population to another
proj = component_factory(
    "Projection",
    id="proj",
    presynaptic_population=pop0.id,
    postsynaptic_population=pop1.id,
    synapse=syn0.id,
)
net.add(proj)

# We do two things in the loop:
# - add pulse generator inputs to population 1 to make neurons spike
# - create synapses between the two populations with a particular probability
random.seed(123)
prob_connection = 0.8
count = 0
for pre in range(0, size0):
    # pulse generator as explicit stimulus
    pg = component_factory(
        "PulseGenerator",
        id="pg_%i" % pre,
        delay="0ms",
        duration="10000ms",
        amplitude="%f nA" % (0.1 + 0.1 * random.random()),
    )
    nml_doc.add(pg)

    exp_input = component_factory(
        "ExplicitInput", target="%s[%i]" % (pop0.id, pre), input=pg.id
    )
    net.add(exp_input)

    # synapses between populations
    for post in range(0, size1):
        if random.random() <= prob_connection:
            syn = component_factory(
                "Connection",
                id=count,
                pre_cell_id="../%s[%i]" % (pop0.id, pre),
                post_cell_id="../%s[%i]" % (pop1.id, post),
            )
            proj.add(syn)
            count += 1

nml_doc.info(True)
print(nml_doc.summary())

# write model to file and validate
nml_file = "izhikevich2007_network.nml"
writers.NeuroMLWriter.write(nml_doc, nml_file)

print("Written network file to: " + nml_file)
pynml.validate_neuroml2(nml_file)

# Create simulation, and record data
simulation_id = "example_izhikevich2007network_sim"
simulation = LEMSSimulation(
    sim_id=simulation_id, duration=1000, dt=0.1, simulation_seed=123
)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

simulation.create_event_output_file(
    "pop0", "%s.0.spikes.dat" % simulation_id, format="ID_TIME"
)
for pre in range(0, size0):
    simulation.add_selection_to_event_output_file(
        "pop0", pre, "IzPop0[{}]".format(pre), "spike"
    )

simulation.create_event_output_file(
    "pop1", "%s.1.spikes.dat" % simulation_id, format="ID_TIME"
)
for pre in range(0, size1):
    simulation.add_selection_to_event_output_file(
        "pop1", pre, "IzPop1[{}]".format(pre), "spike"
    )

lems_simulation_file = simulation.save_to_file()

# Run the simulation
pynml.run_lems_with_jneuroml_neuron(
    lems_simulation_file, max_memory="2G", nogui=True, plot=False
)

# Load the data from the file and plot the spike times
# using the pynml generate_plot utility function.
data_array_0 = np.loadtxt("%s.0.spikes.dat" % simulation_id)
data_array_1 = np.loadtxt("%s.1.spikes.dat" % simulation_id)
times_0 = data_array_0[:, 1]
times_1 = data_array_1[:, 1]
ids_0 = data_array_0[:, 0]
ids_1 = [id + size0 for id in data_array_1[:, 0]]
pynml.generate_plot(
    [times_0, times_1],
    [ids_0, ids_1],
    "Spike times",
    show_plot_already=False,
    save_figure_to="%s-spikes.png" % simulation_id,
    xaxis="time (s)",
    yaxis="cell ID",
    colors=["b", "r"],
    linewidths=["0", "0"],
    markers=[".", "."],
)
