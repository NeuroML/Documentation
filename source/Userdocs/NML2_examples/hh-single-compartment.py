#!/usr/bin/env python3
"""
Create a network with a single HH cell, and simulate it.

File: hh-single-compartment.py

Copyright 2023 NeuroML contributors
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import math
import neuroml
from neuroml import NeuroMLDocument
from neuroml import Network, Population
from neuroml import PulseGenerator, ExplicitInput
import numpy as np
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
from neuroml.utils import component_factory


def main():
    """Main function

    Include the NeuroML model into a LEMS simulation file, run it, plot some
    data.
    """
    # Simulation bits
    sim_id = "HH_single_compartment_example_sim"
    simulation = LEMSSimulation(
        sim_id=sim_id, duration=300, dt=0.01, simulation_seed=123
    )
    # Include the NeuroML model file
    simulation.include_neuroml2_file(create_network())
    # Assign target for the simulation
    simulation.assign_simulation_target("single_hh_cell_network")

    # Recording information from the simulation
    simulation.create_output_file(id="output0", file_name=sim_id + ".dat")
    simulation.add_column_to_output_file(
        "output0", column_id="pop0[0]/v", quantity="pop0[0]/v"
    )
    simulation.add_column_to_output_file(
        "output0", column_id="pop0[0]/iChannels", quantity="pop0[0]/iChannels"
    )
    simulation.add_column_to_output_file(
        "output0",
        column_id="pop0[0]/na/iDensity",
        quantity="pop0[0]/biophys/membraneProperties/na_channels/iDensity/",
    )
    simulation.add_column_to_output_file(
        "output0",
        column_id="pop0[0]/k/iDensity",
        quantity="pop0[0]/biophys/membraneProperties/k_channels/iDensity/",
    )

    # Save LEMS simulation to file
    sim_file = simulation.save_to_file()

    # Run the simulation using the default jNeuroML simulator
    pynml.run_lems_with_jneuroml(sim_file, max_memory="2G", nogui=True, plot=False)
    # Plot the data
    plot_data(sim_id)


def plot_data(sim_id):
    """Plot the sim data.

    Load the data from the file and plot the graph for the membrane potential
    using the pynml generate_plot utility function.

    :sim_id: ID of simulaton

    """
    data_array = np.loadtxt(sim_id + ".dat")
    pynml.generate_plot(
        [data_array[:, 0]],
        [data_array[:, 1]],
        "Membrane potential",
        show_plot_already=False,
        save_figure_to=sim_id + "-v.png",
        xaxis="time (s)",
        yaxis="membrane potential (V)",
    )
    pynml.generate_plot(
        [data_array[:, 0]],
        [data_array[:, 2]],
        "channel current",
        show_plot_already=False,
        save_figure_to=sim_id + "-i.png",
        xaxis="time (s)",
        yaxis="channel current (A)",
    )
    pynml.generate_plot(
        [data_array[:, 0], data_array[:, 0]],
        [data_array[:, 3], data_array[:, 4]],
        "current density",
        labels=["Na", "K"],
        show_plot_already=False,
        save_figure_to=sim_id + "-iden.png",
        xaxis="time (s)",
        yaxis="current density (A_per_m2)",
    )


def create_na_channel():
    """Create the Na channel.

    This will create the Na channel and save it to a file.
    It will also validate this file.

    returns: name of the created file
    """
    na_channel = component_factory(
        "IonChannelHH",
        id="na_channel",
        notes="Sodium channel for HH cell",
        conductance="10pS",
        species="na",
        validate=False,
    )
    gate_m = component_factory(
        "GateHHRates",
        id="m",
        instances="3",
        notes="m gate for na channel",
        validate=False,
    )
    m_forward_rate = component_factory(
        "HHRate", type="HHExpLinearRate", rate="1per_ms", midpoint="-40mV", scale="10mV"
    )
    m_reverse_rate = component_factory(
        "HHRate", type="HHExpRate", rate="4per_ms", midpoint="-65mV", scale="-18mV"
    )

    gate_m.add(m_forward_rate, hint="forward_rate", validate=False)
    gate_m.add(m_reverse_rate, hint="reverse_rate")
    na_channel.add(gate_m)

    gate_h = component_factory(
        "GateHHRates",
        id="h",
        instances="1",
        notes="h gate for na channel",
        validate=False,
    )
    h_forward_rate = component_factory(
        "HHRate", type="HHExpRate", rate="0.07per_ms", midpoint="-65mV", scale="-20mV"
    )
    h_reverse_rate = component_factory(
        "HHRate", type="HHSigmoidRate", rate="1per_ms", midpoint="-35mV", scale="10mV"
    )
    gate_h.add(h_forward_rate, hint="forward_rate", validate=False)
    gate_h.add(h_reverse_rate, hint="reverse_rate")
    na_channel.add(gate_h)

    na_channel_doc = component_factory(
        "NeuroMLDocument", id="na_channel", notes="Na channel for HH neuron"
    )
    na_channel_fn = "HH_example_na_channel.nml"
    na_channel_doc.add(na_channel)
    na_channel_doc.validate(recursive=True)

    pynml.write_neuroml2_file(
        nml2_doc=na_channel_doc, nml2_file_name=na_channel_fn, validate=True
    )

    return na_channel_fn


def create_k_channel():
    """Create the K channel

    This will create the K channel and save it to a file.
    It will also validate this file.

    :returns: name of the K channel file
    """
    k_channel = component_factory(
        "IonChannelHH",
        id="k_channel",
        notes="Potassium channel for HH cell",
        conductance="10pS",
        species="k",
        validate=False,
    )
    gate_n = component_factory(
        "GateHHRates",
        id="n",
        instances="4",
        notes="n gate for k channel",
        validate=False,
    )
    n_forward_rate = component_factory(
        "HHRate",
        type="HHExpLinearRate",
        rate="0.1per_ms",
        midpoint="-55mV",
        scale="10mV",
    )
    n_reverse_rate = component_factory(
        "HHRate", type="HHExpRate", rate="0.125per_ms", midpoint="-65mV", scale="-80mV"
    )
    gate_n.add(n_forward_rate, hint="forward_rate", validate=False)
    gate_n.add(n_reverse_rate, hint="reverse_rate")
    k_channel.add(gate_n)

    k_channel_doc = component_factory(
        "NeuroMLDocument", id="k_channel", notes="k channel for HH neuron"
    )
    k_channel_fn = "HH_example_k_channel.nml"
    k_channel_doc.add(k_channel)
    k_channel_doc.validate(recursive=True)

    pynml.write_neuroml2_file(
        nml2_doc=k_channel_doc, nml2_file_name=k_channel_fn, validate=True
    )

    return k_channel_fn


def create_leak_channel():
    """Create a leak channel

    This will create the leak channel and save it to a file.
    It will also validate this file.

    :returns: name of leak channel nml file
    """
    leak_channel = component_factory(
        "IonChannelHH", id="leak_channel", conductance="10pS", notes="Leak conductance"
    )
    leak_channel_doc = component_factory(
        "NeuroMLDocument", id="leak_channel", notes="leak channel for HH neuron"
    )
    leak_channel_fn = "HH_example_leak_channel.nml"
    leak_channel_doc.add(leak_channel)
    leak_channel_doc.validate(recursive=True)

    pynml.write_neuroml2_file(
        nml2_doc=leak_channel_doc, nml2_file_name=leak_channel_fn, validate=True
    )

    return leak_channel_fn


def create_cell():
    """Create the cell.

    :returns: name of the cell nml file
    """
    # Create the nml file and add the ion channels
    hh_cell_doc = NeuroMLDocument(id="cell", notes="HH cell")
    hh_cell_fn = "HH_example_cell.nml"

    # Define a cell
    hh_cell = hh_cell_doc.add(
        "Cell", id="hh_cell", notes="A single compartment HH cell"
    )  # type: neuroml.Cell
    hh_cell.info(show_contents=True)

    # Channel density for Na channel
    hh_cell.add_channel_density(
        hh_cell_doc,
        cd_id="na_channels",
        cond_density="120.0 mS_per_cm2",
        erev="50.0 mV",
        ion="na",
        ion_channel="na_channel",
        ion_chan_def_file=create_na_channel(),
    )

    # Channel density for k channel
    hh_cell.add_channel_density(
        hh_cell_doc,
        cd_id="k_channels",
        cond_density="360 S_per_m2",
        erev="-77mV",
        ion="k",
        ion_channel="k_channel",
        ion_chan_def_file=create_k_channel(),
    )
    # Leak channel
    hh_cell.add_channel_density(
        hh_cell_doc,
        cd_id="leak_channels",
        cond_density="3.0 S_per_m2",
        erev="-54.3mV",
        ion="non_specific",
        ion_channel="leak_channel",
        ion_chan_def_file=create_leak_channel(),
    )

    # Other membrane properties
    hh_cell.add_membrane_property("SpikeThresh", value="-20mV")
    hh_cell.set_specific_capacitance("1.0 uF_per_cm2")
    hh_cell.set_init_memb_potential("-65mV")

    hh_cell.set_resistivity("0.03 kohm_cm")

    # We want a diameter such that area is 1000 micro meter^2
    # surface area of a sphere is 4pi r^2 = 4pi diam^2
    diam = math.sqrt(1000 / math.pi)
    hh_cell.add_segment(
        prox=[0, 0, 0, diam],
        dist=[0, 0, 0, diam],
        name="soma",
        parent=None,
        fraction_along=1.0,
        group="soma_0",
    )

    hh_cell_doc.validate(recursive=True)
    pynml.write_neuroml2_file(
        nml2_doc=hh_cell_doc, nml2_file_name=hh_cell_fn, validate=True
    )
    return hh_cell_fn


def create_network():
    """Create the network

    :returns: name of network nml file
    """
    net_doc = component_factory(
        "NeuroMLDocument", id="network", notes="HH cell network"
    )
    net_doc_fn = "HH_example_net.nml"
    net_doc.add("IncludeType", href=create_cell())
    net = net_doc.add("Network", id="single_hh_cell_network", validate=False)

    # Create a population: convenient to create many cells of the same type
    pop = net.add(
        "Population",
        id="pop0",
        notes="A population for our cell",
        component="hh_cell",
        size=1,
    )

    # Input
    pulsegen = net_doc.add(
        "PulseGenerator",
        id="pg",
        notes="Simple pulse generator",
        delay="100ms",
        duration="100ms",
        amplitude="0.08nA",
    )

    exp_input = net.add("ExplicitInput", target="pop0[0]", input="pg")

    net_doc.validate(recursive=True)

    pynml.write_neuroml2_file(
        nml2_doc=net_doc, nml2_file_name=net_doc_fn, validate=True
    )
    return net_doc_fn


if __name__ == "__main__":
    main()
