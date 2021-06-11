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
from neuroml import IncludeType
from neuroml import Resistivity
from neuroml import Morphology, Segment, Point3DWithDiam
from neuroml import Network, Population
from neuroml import PulseGenerator, ExplicitInput
from neuroml.writers import NeuroMLWriter
import numpy as np
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation


def main():
    """Main function """

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

    # Include our cell
    nml_doc.includes.append(IncludeType(href=create_network()))
    NeuroMLWriter.write(nml_doc, nml_fn)

    # Simulation bits
    sim_id = "HH_single_compartment_example_sim"
    simulation = LEMSSimulation(sim_id=sim_id, duration=300, dt=0.01,
                                simulation_seed=123)
    simulation.assign_simulation_target("single_hh_cell_network")
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
    plot_data(sim_id)


def plot_data(sim_id):
    """Plot the sim data

    :sim_id: ID of simulaton

    """
    # Load the data from the file and plot the graph for the membrane potential
    # using the pynml generate_plot utility function.
    data_array = np.loadtxt(sim_id + ".v.dat")
    pynml.generate_plot(
        [data_array[:, 0]], [data_array[:, 1]],
        "Membrane potential", show_plot_already=False,
        save_figure_to=sim_id + "-v.png",
        xaxis="time (s)", yaxis="membrane potential (V)"
    )


def create_na_channel():
    """Create the Na channel.

    This will create the Na channel and save it to a file.
    It will also validate this file.

    returns: name of the created file
    """
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

    na_channel_doc = NeuroMLDocument(id="na_channel",
                                     notes="Na channel for HH neuron")
    na_channel_fn = "HH_example_na_channel.nml"
    na_channel_doc.ion_channel_hhs.append(na_channel)

    pynml.write_neuroml2_file(nml2_doc=na_channel_doc,
                              nml2_file_name=na_channel_fn, validate=True)

    return na_channel_fn


def create_k_channel():
    """Create the K channel

    :returns: name of the K channel file

    """
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

    k_channel_doc = NeuroMLDocument(id="k_channel",
                                    notes="k channel for HH neuron")
    k_channel_fn = "HH_example_k_channel.nml"
    k_channel_doc.ion_channel_hhs.append(k_channel)

    pynml.write_neuroml2_file(nml2_doc=k_channel_doc,
                              nml2_file_name=k_channel_fn, validate=True)

    return k_channel_fn


def create_leak_channel():
    """Create a leak channel

    :returns: name of leak channel nml file

    """
    leak_channel = IonChannelHH(id="leak_channel", conductance="10pS",
                                notes="Leak conductance")
    leak_channel_doc = NeuroMLDocument(id="leak_channel",
                                       notes="leak channel for HH neuron")
    leak_channel_fn = "HH_example_leak_channel.nml"
    leak_channel_doc.ion_channel_hhs.append(leak_channel)

    pynml.write_neuroml2_file(nml2_doc=leak_channel_doc,
                              nml2_file_name=leak_channel_fn, validate=True)

    return leak_channel_fn


def create_cell():
    """Create the cell

    :returns: name of the cell nml file

    """
    # Create the nml file and add the ion channels
    hh_cell_doc = NeuroMLDocument(id="cell",
                                  notes="HH cell")
    hh_cell_fn = "HH_example_cell.nml"
    hh_cell_doc.includes.append(IncludeType(href=create_na_channel()))
    hh_cell_doc.includes.append(IncludeType(href=create_k_channel()))
    hh_cell_doc.includes.append(IncludeType(href=create_leak_channel()))

    # Define a cell
    hh_cell = Cell(id="hh_cell", notes="A single compartment HH cell")

    # Define its biophysical properties
    bio_prop = BiophysicalProperties(id="hh_b_prop")
    #  notes="Biophysical properties for HH cell")

    # Membrane properties are a type of biophysical properties
    mem_prop = MembraneProperties()
    # Add membrane properties to the biophysical properties
    bio_prop.membrane_properties = mem_prop

    # Append to cell
    hh_cell.biophysical_properties = bio_prop

    # Channel density for Na channel
    na_channel_density = ChannelDensity(
        id="na_channels", cond_density="120.0 mS_per_cm2", erev="50.0 mV",
        ion="na", ion_channel="na_channel"
    )
    mem_prop.channel_densities.append(na_channel_density)

    # Channel density for k channel
    k_channel_density = ChannelDensity(id="k_channels",
                                       cond_density="360 S_per_m2",
                                       erev="-77mV", ion="k",
                                       ion_channel="k_channel")
    mem_prop.channel_densities.append(k_channel_density)

    # Leak channel
    leak_channel_density = ChannelDensity(id="leak_channels",
                                          cond_density="3.0 S_per_m2",
                                          erev="-54.3mV", ion="non_specific",
                                          ion_channel="leak_channel")
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
    diam = math.sqrt(1000 / math.pi)
    proximal = distal = Point3DWithDiam(x="0", y="0", z="0", diameter=str(diam))
    seg.proximal = proximal
    seg.distal = distal
    # TODO: why do we need to add both segments and segment groups? When should
    # segment_groups be used, and for what?
    morph.segments.append(seg)
    hh_cell.morphology = morph

    hh_cell_doc.cells.append(hh_cell)
    pynml.write_neuroml2_file(nml2_doc=hh_cell_doc,
                              nml2_file_name=hh_cell_fn, validate=True)
    return hh_cell_fn


def create_network():
    """Create the network

    :returns: name of network nml file

    """
    net_doc = NeuroMLDocument(id="network",
                              notes="HH cell network")
    net_doc_fn = "HH_example_net.nml"
    net_doc.includes.append(IncludeType(href=create_cell()))
    # Create a population: convenient to create many cells of the same type
    pop = Population(id="pop0", notes="A population for our cell",
                     component="hh_cell", size=1)
    # Input
    pulsegen = PulseGenerator(id="pg", notes="Simple pulse generator",
                              delay="100ms", duration="100ms", amplitude="0.08nA")

    # TODO: why do we need an ExplicitInput? Why not directly connect to pulsegen?
    # TODO: what is the difference between target and destination (not explained in
    # the docs)
    exp_input = ExplicitInput(target="pop0[0]", input="pg")

    net = Network(id="single_hh_cell_network",
                  note="A network with a single population")
    net_doc.pulse_generators.append(pulsegen)
    net.explicit_inputs.append(exp_input)
    net.populations.append(pop)
    net_doc.networks.append(net)

    pynml.write_neuroml2_file(nml2_doc=net_doc,
                              nml2_file_name=net_doc_fn, validate=True)

    return net_doc_fn


if __name__ == "__main__":
    main()
