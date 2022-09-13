#!/usr/bin/env python3
"""
Create a simple network with two populations.
"""

from neuroml import NeuroMLDocument
import neuroml.writers as writers
import random
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
import numpy as np
from pyneuroml.utils import component_factory

# component_factory: form one: provide class as argument
nml_doc = component_factory(NeuroMLDocument, id="IzNet")

# component_factory: form two: provide name of NeuroML class as string
# advantage of this form: do not need to import all the ComponentType classes
# before using them
iz0 = component_factory("Izhikevich2007Cell",
                        id="iz2007RS0", v0="-60mV", C="100pF", k="0.7nS_per_mV", vr="-60mV",
                        vt="-40mV", vpeak="35mV", a="0.03per_ms", b="-2nS", c="-50.0mV", d="100pA")

# Inspect the component
iz0.info()

# Inspect the component, also show all members:
iz0.info(True)

# Add the component to the document, so that it can be used
nml_doc.add(iz0)

# Create a component of type ExpOneSynapse, and add it to the document
syn0 = component_factory("ExpOneSynapse", id="syn0", gbase="65nS", erev="0mV", tau_decay="3ms")
nml_doc.add(syn0)

# Check what we have so far:
nml_doc.info(True)

# Create a network
# net = component_factory("Network", id="IzNet")
# Throws an error: why?
# Because a Population is necessary in a Network, but we have not provided one.
# Two workarounds:
# - create population first, and pass that to component_factory here
# - disable validation

net = component_factory("Network", id="IzNet", validate=False)

nml_doc.add(net)

size0 = 5
pop0 = component_factory("Population", id="IzPop0", component=iz0.id, size=size0)
# Set optional color property. Note: used later when generating graphs etc.
pop0.add(component_factory("Property", tag='color', value='0 0 .8'))
net.add(pop0)

size1 = 5
pop1 = component_factory("Population", id="IzPop1", component=iz0.id, size=size1)
pop1.add(component_factory("Property", tag='color', value='.8 0 0'))
net.add(pop1)

# can also use this form, but remember to (will not be validated!):
# from neuroml import Property
# pop1.add(Property(tag='color', value='.8 0 0'))

proj = component_factory("Projection", id='proj', presynaptic_population=pop0.id,
                         postsynaptic_population=pop1.id, synapse=syn0.id)
net.add(proj)
# No more
# net.projections.append(proj)

random.seed(123)
prob_connection = 0.8
count = 0
for pre in range(0, size0):
    pg = component_factory("PulseGenerator",
                           id="pg_%i" % pre, delay="0ms", duration="10000ms",
                           amplitude="%f nA" % (0.1 + 0.1 * random.random())
                           )
    nml_doc.add(pg)

    exp_input = component_factory("ExplicitInput", target="%s[%i]" % (pop0.id, pre), input=pg.id)
    net.add(exp_input)

    for post in range(0, size1):
        if random.random() <= prob_connection:
            syn = component_factory("Connection", id=count,
                                    pre_cell_id="../%s[%i]" % (pop0.id, pre),
                                    post_cell_id="../%s[%i]" % (pop1.id, post))
            proj.add(syn)
            count += 1

nml_doc.info(True)
print(nml_doc.summary())

nml_file = 'izhikevich2007_network.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)

print("Written network file to: " + nml_file)
pynml.validate_neuroml2(nml_file)

simulation_id = "example_izhikevich2007network_sim"
simulation = LEMSSimulation(sim_id=simulation_id,
                            duration=1000, dt=0.1, simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

simulation.create_event_output_file(
    "pop0", "%s.0.spikes.dat" % simulation_id, format='ID_TIME'
)
for pre in range(0, size0):
    simulation.add_selection_to_event_output_file(
        "pop0", pre, 'IzPop0[{}]'.format(pre), 'spike')

simulation.create_event_output_file(
    "pop1", "%s.1.spikes.dat" % simulation_id, format='ID_TIME'
)
for pre in range(0, size1):
    simulation.add_selection_to_event_output_file(
        "pop1", pre, 'IzPop1[{}]'.format(pre), 'spike')

lems_simulation_file = simulation.save_to_file()

pynml.run_lems_with_jneuroml_neuron(
    lems_simulation_file, max_memory="2G", nogui=True, plot=False
)

# Load the data from the file and plot the spike times
# using the pynml generate_plot utility function.
data_array_0 = np.loadtxt("%s.0.spikes.dat" % simulation_id)
data_array_1 = np.loadtxt("%s.1.spikes.dat" % simulation_id)
times_0 = data_array_0[:,1]
times_1 = data_array_1[:,1]
ids_0 = data_array_0[:,0]
ids_1 = [id+size0 for id in data_array_1[:,0]]
pynml.generate_plot(
    [times_0,times_1], [ids_0,ids_1],
    "Spike times", show_plot_already=False,
    save_figure_to="%s-spikes.png" % simulation_id,
    xaxis="time (s)", yaxis="cell ID",
    colors=['b','r'],
    linewidths=['0','0'], markers=['.','.'],
)
