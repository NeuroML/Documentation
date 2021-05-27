#!/usr/bin/env python3
"""
Creating a Hodgkin-Huxley, single compartment cell, in NeuroML

File: HH.py

Copyright 2021 NeuroML contributors
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import math
from neuroml import NeuroMLDocument
from neuroml import Cell
from neuroml import IonChannelHH
from neuroml import GateHHRates
from neuroml import BiophysicalProperties
from neuroml import MembraneProperties
from neuroml import ChannelDensity
from neuroml import HHRate
from neuroml import SpikeThresh
from neuroml import SpecificCapacitance
from neuroml import InitMembPotential
from neuroml import IntracellularProperties
from neuroml import Resistivity
from neuroml import Morphology, Segment, Point3DWithDiam
from neuroml import Network, Population
from neuroml import PulseGenerator, ExplicitInput
import numpy as np
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation


# TODO: Draw ascii diagram showing the full hierarchy
# TODO: Ask Padraig how to modularise the code: should one go bottom up: define
# rates, then gates, then channels, then cell, network and so on. OR, should
# one create the network first, then cells, and go top-down? OR is there a
# better way: define everything you need first, and then put it together? The
# third seems best tbh.

# Create the nml document
nml_doc = NeuroMLDocument(id="HH_single_complartment",
                          notes="Single compartment cell with HH channels")
nml_fn = "HH_single_compartment_example.nml"

# Define a cell
hh_cell = Cell(id="hh_cell", notes="A single compartment HH cell")
nml_doc.cells.append(hh_cell)

# Define its biophysical properties
bio_prop = BiophysicalProperties(id="hh_b_prop")
#  notes="Biophysical properties for HH cell")

# Membrane properties are a type of biophysical properties
mem_prop = MembraneProperties()
# Add membrane properties to the biophysical properties
bio_prop.membrane_properties = mem_prop

# Append to cell
hh_cell.biophysical_properties = bio_prop

# Define ion channels
# Na channel
na_channel = IonChannelHH(id="na_channel", notes="Sodium channel for HH cell",
                          conductance="10pS", species="na")
gate_m = GateHHRates(id="na_m", instances="3", notes="m gate for na channel")
# TODO~: Ask Padraig: how does one know that HHExpRate etc are to be used as a
# type, and is not a class itself like all the other constructs? In the
# documentation, they're all listed in the same way.
m_forward_rate = HHRate(type="HHExpLinearRate", rate="1per_ms",
                        midpoint="-40mV", scale="10mV")
m_reverse_rate = HHRate(type="HHExpRate", rate="4per_ms", midpoint="-65mV",
                        scale="-18mV")
gate_m.forward_rate = m_forward_rate
gate_m.reverse_rate = m_reverse_rate
na_channel.gate_hh_rates.append(gate_m)

gate_h = GateHHRates(id="na_h", instances="1", notes="h gate for na channel")
h_forward_rate = HHRate(type="HHExpRate", rate="0.07per_ms",
                        midpoint="-65mV", scale="-20mV")
h_reverse_rate = HHRate(type="HHSigmoidRate", rate="1per_ms", midpoint="-35mV",
                        scale="10mV")
gate_h.forward_rate = h_forward_rate
gate_h.reverse_rate = h_reverse_rate
na_channel.gate_hh_rates.append(gate_h)

# Channel density for Na channel
na_channel_density = ChannelDensity(
    id="na_channels", cond_density="120.0 mS_per_cm2", erev="50.0 mV",
    ion="na", ion_channel="na_channel"
)
nml_doc.ion_channel.append(na_channel)
mem_prop.channel_densities.append(na_channel_density)

# K channel
k_channel = IonChannelHH(id="k_channel", notes="Potassium channel for HH cell",
                         conductance="10pS", species="k")
gate_n = GateHHRates(id="k_n", instances="4", notes="n gate for k channel")
n_forward_rate = HHRate(type="HHExpLinearRate", rate="0.1per_ms",
                        midpoint="-55mV", scale="10mV")
n_reverse_rate = HHRate(type="HHExpRate", rate="0.125per_ms", midpoint="-65mV",
                        scale="-80mV")
gate_n.forward_rate = n_forward_rate
gate_n.reverse_rate = n_reverse_rate
k_channel.gate_hh_rates.append(gate_n)

# Channel density for k channel
k_channel_density = ChannelDensity(id="k_channels",
                                   cond_density="360 S_per_m2",
                                   erev="-77mV", ion="k",
                                   ion_channel="k_channel")
nml_doc.ion_channel.append(k_channel)
mem_prop.channel_densities.append(k_channel_density)

# Leak channel
leak_channel = IonChannelHH(id="leak_channel", conductance="10pS",
                            notes="Leak conductance")
leak_channel_density = ChannelDensity(id="leak_channels",
                                      cond_density="3.0 S_per_m2",
                                      erev="-54.3mV", ion="non_specific",
                                      ion_channel="leak_channel")
nml_doc.ion_channel.append(leak_channel)
mem_prop.channel_densities.append(leak_channel_density)

# Other membrane properties
# TODO: why are these lists? Can a membrane have more than one threshold?
mem_prop.spike_threshes.append(SpikeThresh(value="-20mV"))
mem_prop.specific_capacitances.append(
    SpecificCapacitance(value="1.0 uF_per_cm2")
)
mem_prop.init_memb_potentials.append(InitMembPotential(value="-65mV"))

intra_prop = IntracellularProperties()
intra_prop.resistivities.append(Resistivity(value="0.03 kohm_cm"))

# Add to biological properties
bio_prop.intracellular_properties = intra_prop


# Morphology
# TODO: libNeuroML says Morphology has "notes", but LEMS doesn't seem to like
# it.
morph = Morphology(id="hh_cell_morph")
#  notes="Simple morphology for the HH cell")
seg = Segment(id="0", name="soma", notes="Soma segment")
# We want a diameter such that area is 1000 micro meter^2
# surface area of a sphere is 4pi r^2 = 4pi diam^2
diam = math.sqrt(1000/math.pi)
proximal = distal = Point3DWithDiam(x="0", y="0", z="0", diameter=str(diam))
seg.proximal = proximal
seg.distal = distal
# TODO: why do we need to add both segments and segment groups? When should
# segment_groups be used, and for what?
morph.segments.append(seg)
hh_cell.morphology = morph

# Create a population: convenient to create many cells of the same type
pop = Population(id="pop0", notes="A population for our cell",
                 component="hh_cell", size=1)

# Input
pulsegen = PulseGenerator(id="pg", notes="Simple pulse generator",
                          delay="100ms", duration="100ms", amplitude="0.08nA")
nml_doc.pulse_generators.append(pulsegen)
# TODO: why do we need an ExplicitInput? Why not directly connect to pulsegen?
# TODO: what is the difference between target and destination (not explained in
# the docs)
exp_input = ExplicitInput(target="pop0[0]", input="pg")

net = Network(id="single_hh_cell_network",
              note="A network with a single population")
net.populations.append(pop)
net.explicit_inputs.append(exp_input)
nml_doc.networks.append(net)
# Already validates also
pynml.write_neuroml2_file(nml2_doc=nml_doc,
                          nml2_file_name=nml_fn, validate=True)


# Simulation bits
sim_id = "HH_single_compartment_example_sim"
simulation = LEMSSimulation(sim_id=sim_id, duration=300, dt=0.01,
                            simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_fn)

# Recording bits
simulation.create_output_file(id="output0", file_name=sim_id + ".v.dat")
simulation.add_column_to_output_file("output0", column_id="pop0[0]",
                                     quantity="pop0[0]/v")
# TODO: what is `fopen`? Probably "fraction open"
# TODO: how do I recored channel currents?

sim_file = simulation.save_to_file()

# Run the simulation using the jNeuroML simulator
pynml.run_lems_with_jneuroml(
    sim_file, max_memory="2G", nogui=True, plot=False
)

# Load the data from the file and plot the graph for the membrane potential
# using the pynml generate_plot utility function.
data_array = np.loadtxt(sim_id + ".v.dat")
pynml.generate_plot(
    [data_array[:, 0]], [data_array[:, 1]],
    "Membrane potential", show_plot_already=False,
    save_figure_to=sim_id + "-v.png",
    xaxis="time (s)", yaxis="membrane potential (V)"
)
