#!/usr/bin/env python3
"""
Create a simple network with two populations.
"""

from neuroml import NeuroMLDocument
from neuroml import Izhikevich2007Cell
from neuroml import Network
from neuroml import ExpOneSynapse
from neuroml import Population
from neuroml import Projection
from neuroml import PulseGenerator
from neuroml import ExplicitInput
from neuroml import Connection
import neuroml.writers as writers
import random
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
import numpy as np


nml_doc = NeuroMLDocument(id="IzNet")

iz0 = Izhikevich2007Cell(
    id="iz2007RS0", v0="-60mV", C="100pF", k="0.7nS_per_mV", vr="-60mV",
    vt="-40mV", vpeak="35mV", a="0.03per_ms", b="-2nS", c="-50.0mV", d="100pA")
nml_doc.izhikevich2007_cells.append(iz0)

syn0 = ExpOneSynapse(id="syn0", gbase="65nS", erev="0mV", tau_decay="3ms")
nml_doc.exp_one_synapses.append(syn0)

net = Network(id="IzNet")
nml_doc.networks.append(net)

size0 = 5
pop0 = Population(id="IzPop0", component=iz0.id, size=size0)
net.populations.append(pop0)

size1 = 5
pop1 = Population(id="IzPop1", component=iz0.id, size=size1)
net.populations.append(pop1)

proj = Projection(id='proj', presynaptic_population=pop0.id,
                  postsynaptic_population=pop1.id, synapse=syn0.id)
net.projections.append(proj)

random.seed(921)
prob_connection = 0.5
count = 0
for pre in range(0, size0):
    pg = PulseGenerator(
        id="pulseGen_%i" % pre, delay="0ms", duration="10000ms",
        amplitude="%f nA" % (0.1 * random.random())
    )
    nml_doc.pulse_generators.append(pg)

    exp_input = ExplicitInput(target="%s[%i]" % (pop0.id, pre), input=pg.id)
    net.explicit_inputs.append(exp_input)

    for post in range(0, size1):
        if random.random() <= prob_connection:
            syn = Connection(id=count,
                             pre_cell_id="../%s[%i]" % (pop0.id, pre),
                             synapse=syn0.id,
                             post_cell_id="../%s[%i]" % (pop1.id, post))
            proj.connections.append(syn)
            count += 1

nml_file = 'izhikevich2007_network.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)

print("Written network file to: " + nml_file)
pynml.validate_neuroml2(nml_file)

simulation_id = "example_izhikevich2007network_sim"
simulation = LEMSSimulation(sim_id=simulation_id,
                            duration=10000, dt=0.1, simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

simulation.create_event_output_file(
    "pop0", "%s.spikes.dat" % simulation_id, format='ID_TIME'
)

for pre in range(0, size0):
    simulation.add_selection_to_event_output_file(
        "pop0", pre, 'IzPop0[{}]'.format(pre), 'spike')

lems_simulation_file = simulation.save_to_file()

pynml.run_lems_with_jneuroml_neuron(
    lems_simulation_file, max_memory="2G", nogui=True, plot=False
)

# Load the data from the file and plot the spike times
# using the pynml generate_plot utility function.
data_array = np.loadtxt("%s.spikes.dat" % simulation_id)
pynml.generate_plot(
    [data_array[:, 1]], [data_array[:, 0]],
    "Spike times", show_plot_already=False,
    save_figure_to="%s-spikes.png" % simulation_id,
    xaxis="time (s)", yaxis="cell ID",
    linestyles='', linewidths='0', markers=['.'],
)
