#!/usr/bin/env python3
"""
Simulating a regular spiking Izhikevich neuron with NeuroML.

File: izhikevich-single-neuron.py
"""

from neuroml import NeuroMLDocument
import neuroml.writers as writers
from neuroml.utils import validate_neuroml2
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
from pyneuroml.utils import component_factory
import numpy as np


# Create a new NeuroML model document
# component_factory: form one: provide class as argument
nml_doc = component_factory(NeuroMLDocument, id="IzhSingleNeuron")

# Inspect it:
nml_doc.info()

# Also see contents:
nml_doc.info(show_contents=True)

# Define the Izhikevich cell and add it to the model in the document
# component_factory: form two: provide name of NeuroML class as string
# advantage of this form: do not need to import all the ComponentType classes
# before using them
izh0 = component_factory(
    "Izhikevich2007Cell",
    id="izh2007RS0", v0="-60mV", C="100pF", k="0.7nS_per_mV", vr="-60mV",
    vt="-40mV", vpeak="35mV", a="0.03per_ms", b="-2nS", c="-50.0mV", d="100pA")

# Exercise 1: give wrong units of a parameter/parameters
# Exercise 2: skip out a few parameters

# Inspect the component
izh0.info()

# Inspect the component, also show all members:
izh0.info(True)

# add: is smart enough to add the izh0 object in the right place
# one can also go:
# nml_doc.izhikevich2007_cells.append(izh0)
nml_doc.add(izh0)
nml_doc.info(show_contents=True)

# Create a network and add it to the model
# net = component_factory("Network", id="IzNet")
# Throws an error: why?
# Because a Population is necessary in a Network, but we have not provided one.
# Two workarounds:
# - create population first, and pass that to component_factory here
# - disable validation
net = component_factory("Network", id="IzNet", validate=False)
nml_doc.add(net)

# Create a population of defined cells and add it to the model
size0 = 1
pop0 = component_factory("Population", id="IzhPop0", component=izh0.id, size=size0)
net.add(pop0)
net.info()

# Define an external stimulus and add it to the model
pg = component_factory(
    "PulseGenerator",
    id="pulseGen_%i" % 0, delay="0ms", duration="1000ms",
    amplitude="0.07 nA"
)
nml_doc.add(pg)
exp_input = component_factory("ExplicitInput", target="%s[%i]" % (pop0.id, 0), input=pg.id)
net.add(exp_input)

# Write the NeuroML model to a file
nml_file = 'izhikevich2007_single_cell_network.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)
print("Written network file to: " + nml_file)

# Validate the NeuroML model against the NeuroML schema
validate_neuroml2(nml_file)

################################################################################
# The NeuroML file has now been created and validated. The rest of the code
# involves writing a LEMS simulation file to run an instance of the model

# Create a simulation instance of the model
simulation_id = "example-single-izhikevich2007cell-sim"
simulation = LEMSSimulation(sim_id=simulation_id,
                            duration=1000, dt=0.1, simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

# Define the output file to store simulation outputs
# we record the neuron's membrane potential
simulation.create_output_file(
    "output0", "%s.v.dat" % simulation_id
)
simulation.add_column_to_output_file("output0", 'IzhPop0[0]', 'IzhPop0[0]/v')

# Save the simulation to a file
lems_simulation_file = simulation.save_to_file()

# Run the simulation using the jNeuroML simulator
pynml.run_lems_with_jneuroml(
    lems_simulation_file, max_memory="2G", nogui=True, plot=False
)

# Load the data from the file and plot the graph for the membrane potential
# using the pynml generate_plot utility function.
data_array = np.loadtxt("%s.v.dat" % simulation_id)
pynml.generate_plot(
    [data_array[:, 0]], [data_array[:, 1]],
    "Membrane potential", show_plot_already=False,
    save_figure_to="%s-v.png" % simulation_id,
    xaxis="time (s)", yaxis="membrane potential (V)"
)
