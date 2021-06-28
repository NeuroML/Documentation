#!/usr/bin/env python3
"""
Multi-compartmental OLM cell example

File:

Copyright 2021 NeuroML contributors
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

from neuroml import (NeuroMLDocument, IncludeType, Population, PulseGenerator,
                     ExplicitInput, Network, SegmentGroup, Member)
from CellBuilder import (create_cell, add_segment, add_channel_density,
                         set_init_memb_potential, set_resistivity,
                         set_specific_capacitance)
from pyneuroml import pynml


def main():
    """Main worker function. """
    nml_doc = NeuroMLDocument(id="oml_example", notes="Example of a multi-compartmental OLM cell")


def create_network():
    """Create the network

    :returns: name of network nml file
    """
    net_doc = NeuroMLDocument(id="network",
                              notes="OLM cell network")
    net_doc_fn = "OLM_example_net.nml"
    net_doc.includes.append(IncludeType(href=create_cell()))
    # Create a population: convenient to create many cells of the same type
    pop = Population(id="pop0", notes="A population for our cell", component="hh_cell", size=1)
    # Input
    pulsegen = PulseGenerator(id="pg", notes="Simple pulse generator", delay="100ms", duration="100ms", amplitude="0.08nA")

    exp_input = ExplicitInput(target="pop0[0]", input="pg")

    net = Network(id="single_olm_cell_network", note="A network with a single population")
    net_doc.pulse_generators.append(pulsegen)
    net.explicit_inputs.append(exp_input)
    net.populations.append(pop)
    net_doc.networks.append(net)

    pynml.write_neuroml2_file(nml2_doc=net_doc, nml2_file_name=net_doc_fn, validate=True)
    return net_doc_fn


def create_olm_cell():
    """Create the complete cell.

    :returns: cell object
    """
    nml_cell_doc = NeuroMLDocument(id="oml_cell")
    cell = create_cell("olm")
    nml_cell_file = cell.id + ".cell.nml"

    # Add two soma segments
    diam = 10.0
    soma_0 = add_segment(cell,
                         prox=[0.0, 0.0, 0.0, diam],
                         dist=[0.0, 1.0, 0.0, diam],
                         name="Seg0_soma_0",
                         group="soma_0")

    soma_1 = add_segment(cell,
                         prox=None,
                         dist=[0.0, 1.0 + 1.0, 0.0, diam],
                         name="Seg1_soma_0",
                         parent=soma_0,
                         group="soma_0")

    # Add axon segments
    diam = 1.5
    axon_0 = add_segment(cell,
                         prox=[0.0, 0.0, 0.0, diam],
                         dist=[0.0, -7.5, 0.0, diam],
                         name="Seg1_axon_0",
                         parent=soma_0,
                         fraction_along=0.0,
                         group="axon_0")
    axon_1 = add_segment(cell,
                         prox=None,
                         dist=[0.0, -1.5, 0.0, diam],
                         name="Seg1_axon_0",
                         parent=axon_0,
                         group="axon_0")

    # Add 2 dendrite segments
    diam = 3.0
    dend_0_0 = add_segment(cell,
                           prox=[0.0, 2.0, 0.0, diam],
                           dist=[1.0, 1.2, 0.0, diam],
                           name="Seg0_dend_0",
                           parent=soma_1,
                           fraction_along=0.0,
                           group="dend_0")
    dend_0_1 = add_segment(cell,
                           prox=[0.0, 2.0, 0.0, diam],
                           dist=[-1.0, 1.2, 0.0, diam],
                           name="Seg0_dend_1",
                           parent=soma_1,
                           group="dend_0")

    dend_1_0 = add_segment(cell,
                           prox=None,
                           dist=[1.77, 1.97, 0.0, diam],
                           name="Seg1_dend_0",
                           parent=dend_0_0,
                           fraction_along=0.0,
                           group="dend_1")
    dend_1_1 = add_segment(cell,
                           prox=None,
                           dist=[-1.77, 1.97, 0.0, diam],
                           name="Seg1_dend_1",
                           parent=dend_0_1,
                           fraction_along=0.0,
                           group="dend_1")

    # Add a segment group for all dendrites
    den_seg_group = SegmentGroup(id="dendrite_group")
    cell.morphology.segment_groups.append(den_seg_group)
    den_seg_group.members.append(Member(segments=dend_0_0.id))
    den_seg_group.members.append(Member(segments=dend_0_1.id))
    den_seg_group.members.append(Member(segments=dend_1_0.id))
    den_seg_group.members.append(Member(segments=dend_1_1.id))

    # Other cell properties
    set_init_memb_potential(cell, "-67mV")
    set_resistivity(cell, "0.15 kohm_cm")
    set_specific_capacitance(cell, "1.3 uF_per_cm2")

    # channels
    # leak
    add_channel_density(cell, nml_cell_doc,
                        cd_id="leak_all",
                        cond_density="0.01 mS_per_cm2",
                        ion_channel="leak_chan",
                        ion_chan_def_file="olm-example/leak_chan.channel.nml",
                        erev="-67mV",
                        ion="non_specific")
    # HCNolm_soma
    add_channel_density(cell, nml_cell_doc,
                        cd_id="HCNolm_soma",
                        cond_density="0.5 mS_per_cm2",
                        ion_channel="HCNolm",
                        ion_chan_def_file="olm-example/HCNolm.channel.nml",
                        erev="-32.9mV",
                        ion="h",
                        group="soma_0")
    # Kdrfast_soma
    add_channel_density(cell, nml_cell_doc,
                        cd_id="Kdrfast_soma",
                        cond_density="73.37 mS_per_cm2",
                        ion_channel="Kdrfast",
                        ion_chan_def_file="olm-example/Kdrfast.channel.nml",
                        erev="-77mV",
                        ion="k",
                        group="soma_0")
    # Kdrfast_dendrite
    add_channel_density(cell, nml_cell_doc,
                        cd_id="Kdrfast_dendrite",
                        cond_density="105.8 mS_per_cm2",
                        ion_channel="Kdrfast",
                        ion_chan_def_file="olm-example/Kdrfast.channel.nml",
                        erev="-77mV",
                        ion="k",
                        group="dendrite_group")
    # Kdrfast_axon
    add_channel_density(cell, nml_cell_doc,
                        cd_id="Kdrfast_axon",
                        cond_density="117.392 mS_per_cm2",
                        ion_channel="Kdrfast",
                        ion_chan_def_file="olm-example/Kdrfast.channel.nml",
                        erev="-77mV",
                        ion="k",
                        group="axon_0")
    # KvAolm_soma
    add_channel_density(cell, nml_cell_doc,
                        cd_id="KvAolm_soma",
                        cond_density="4.95 mS_per_cm2",
                        ion_channel="KvAolm",
                        ion_chan_def_file="olm-example/KvAolm.channel.nml",
                        erev="-77mV",
                        ion="k",
                        group="soma_0")
    # KvAolm_dendrite
    add_channel_density(cell, nml_cell_doc,
                        cd_id="KvAolm_dendrite",
                        cond_density="2.8 mS_per_cm2",
                        ion_channel="KvAolm",
                        ion_chan_def_file="olm-example/KvAolm.channel.nml",
                        erev="-77mV",
                        ion="k",
                        group="dendrite_group")
    # Nav_soma
    add_channel_density(cell, nml_cell_doc,
                        cd_id="Nav_soma",
                        cond_density="10.7 mS_per_cm2",
                        ion_channel="Nav",
                        ion_chan_def_file="olm-example/Nav.channel.nml",
                        erev="50mV",
                        ion="na",
                        group="soma_0")
    # Nav_dendrite
    add_channel_density(cell, nml_cell_doc,
                        cd_id="Nav_dendrite",
                        cond_density="23.4 mS_per_cm2",
                        ion_channel="Nav",
                        ion_chan_def_file="olm-example/Nav.channel.nml",
                        erev="50mV",
                        ion="na",
                        group="dendrite_group")
    # Nav_axon
    add_channel_density(cell, nml_cell_doc,
                        cd_id="Nav_axon",
                        cond_density="17.12 mS_per_cm2",
                        ion_channel="Nav",
                        ion_chan_def_file="olm-example/Nav.channel.nml",
                        erev="50mV",
                        ion="na",
                        group="axon_0")

    nml_cell_doc.cells.append(cell)
    pynml.write_neuroml2_file(nml_cell_doc, nml_cell_file, True, True)

if __name__ == "__main__":
    #  main()
    create_olm_cell()
