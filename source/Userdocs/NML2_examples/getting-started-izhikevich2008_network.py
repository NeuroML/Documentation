#!/usr/bin/env python3
"""
Create a simple network with two populations.
"""

from neuroml import NeuroMLDocument
from neuroml import Izhikevich2007Cell
from neuroml import Network
from neuroml import ExpOneSynapse
from neuroml import Population
from neuroml import SynapticConnection
import neuroml.writers as writers
from neuroml.utils import validate_neuroml2
import random

nml_doc = NeuroMLDocument(id="IzNet")

iz0 = Izhikevich2007Cell(
    id="iz2007RS0", v0="-60mV", C="100pF",
    k="0.7nS_per_mV", vr="-60mV", vt="-40mV", vpeak="35mV", a="0.03per_ms",
    b="-2nS", c="-50.0mV", d="100pA"
)
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

random.seed(42)
prob_connection = 0.5
for pre in range(0, size0):
    for post in range(0, size1):
        # 'from_' is used since 'from' is Python keyword
        if random.random() <= prob_connection:
            syn = SynapticConnection(
                from_="%s[%i]" % (pop0.id, pre), synapse=syn0.id,
                to="%s[%i]" % (pop1.id, post)
            )
            net.synaptic_connections.append(syn)

nml_file = 'izhikevich2007_network.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)

print("Written network file to: " + nml_file)
validate_neuroml2(nml_file)
