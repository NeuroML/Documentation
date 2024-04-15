#!/usr/bin/env python3
"""
Post process and add biophysics to cells.

We make any updates to the morphology, and add biophysics.

File: NeuroML2/postprocess_cells.py
"""


import random

import yaml
import neuroml
from neuroml.loaders import read_neuroml2_file
from pyneuroml.pynml import write_neuroml2_file, run_lems_with_jneuroml_neuron
from pyneuroml.lems import generate_lems_file_for_neuroml
from pyneuroml.plot import generate_plot
from pyneuroml.neuron import morphinfo, getinfo, load_hoc_or_python_file
from neuroml.utils import component_factory

random.seed(1412)


def load_and_setup_cell(cellname: str):
    """Load a cell, and clean it to prepare it for further modifications.

    These operations are common for all cells.

    :param cellname: name of cell.
        the file containing the cell should then be <cell>.morph.cell.nml
    :returns: document with cell
    :rtype: neuroml.NeuroMLDocument

    """
    celldoc = read_neuroml2_file(
        f"{cellname}.morph.cell.nml"
    )  # type: neuroml.NeuroMLDocument
    cell = celldoc.cells[0]  # type: neuroml.Cell
    celldoc.networks = []
    cell.id = cellname
    cell.notes = cell.notes.replace("GGN_20170309_sc_0_0", cellname)
    cell.notes += ". Reference: Subhasis Ray, Zane N Aldworth, Mark A Stopfer (2020) Feedback inhibition and its control in an insect olfactory circuit eLife 9:e53281."

    [
        default_all_group,
        default_soma_group,
        default_dendrite_group,
        default_axon_group,
    ] = cell.setup_default_segment_groups(
        use_convention=True,
        default_groups=["all", "soma_group", "dendrite_group", "axon_group"],
    )

    # populate default groups
    for sg in cell.morphology.segment_groups:
        if "soma" in sg.id and sg.id != "soma_group":
            default_soma_group.add(neuroml.Include(segment_groups=sg.id))
        if "axon" in sg.id and sg.id != "axon_group":
            default_axon_group.add(neuroml.Include(segment_groups=sg.id))
        if "dend" in sg.id and sg.id != "dendrite_group":
            default_dendrite_group.add(neuroml.Include(segment_groups=sg.id))

    cell.optimise_segment_groups()

    return celldoc


def postprocess_GGN():
    """Post process GGN and add biophysics."""
    cellname = "GGN"
    celldoc = load_and_setup_cell(cellname)
    cell = celldoc.cells[0]  # type: neuroml.Cell

    # biophysics
    # all
    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="pas",
        ion_channel="pas",
        cond_density="0.00003 S_per_cm2",
        erev="-51 mV",
        group_id="all",
        ion="non_specific",
        ion_chan_def_file="channels/pas.channel.nml",
    )
    cell.set_resistivity("0.1 kohm_cm", group_id="all")
    cell.set_specific_capacitance("1 uF_per_cm2", group_id="all")
    cell.set_init_memb_potential("-80mV")

    # L1 validation
    # cell.validate(recursive=True)
    cell.summary(morph=False, biophys=True)
    # use pynml writer to also run L2 validation
    write_neuroml2_file(celldoc, f"{cellname}.cell.nml")


def postprocess_KC():
    """Manually create KC and add biophysics."""
    celldoc = component_factory(
        "NeuroMLDocument", id="KC_doc"
    )  # type: neuroml.NeuroMLDocument
    cell = celldoc.add("Cell", id="KC", validate=False)  # type: neuroml.Cell
    cell.setup_nml_cell()
    cell.add_segment([0, 0, 0, 20], [0, 0, 6.366, 20], seg_type="soma")

    # biophysics
    # all
    cell.set_resistivity("35.4 ohm_cm", group_id="all")
    cell.set_specific_capacitance("1 uF_per_cm2", group_id="all")
    cell.set_init_memb_potential("-70mV")
    cell.set_spike_thresh("-10mV")

    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="pas",
        ion_channel="pas",
        cond_density="9.75e-5 S_per_cm2",
        erev="-70 mV",
        group_id="all",
        ion="non_specific",
        ion_chan_def_file="channels/pas.channel.nml",
    )

    # K
    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="kv",
        ion_channel="kv",
        cond_density="1.5e-3 S_per_cm2",
        erev="-81 mV",
        group_id="all",
        ion="k",
        ion_chan_def_file="channels/kv.channel.nml",
    )
    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="ka",
        ion_channel="ka",
        cond_density="1.4525e-2 S_per_cm2",
        erev="-81 mV",
        group_id="all",
        ion="k",
        ion_chan_def_file="channels/ka.channel.nml",
    )
    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="kst",
        ion_channel="kst",
        cond_density="2.0275e-3 S_per_cm2",
        erev="-81 mV",
        group_id="all",
        ion="k",
        ion_chan_def_file="channels/kst.channel.nml",
    )
    # Na
    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="naf",
        ion_channel="naf",
        cond_density="3.5e-2 S_per_cm2",
        erev="58 mV",
        group_id="all",
        ion="na",
        ion_chan_def_file="channels/naf.channel.nml",
    )
    cell.add_channel_density(
        nml_cell_doc=celldoc,
        cd_id="nas",
        ion_channel="nas",
        cond_density="3e-3 S_per_cm2",
        erev="58 mV",
        group_id="all",
        ion="na",
        ion_chan_def_file="channels/nas.channel.nml",
    )

    # L1 validation
    # cell.validate(recursive=True)
    cell.summary(morph=False, biophys=True)
    # use pynml writer to also run L2 validation
    write_neuroml2_file(celldoc, "KC.cell.nml")


def step_current_omv_kc():
    """Create a step current simulation OMV LEMS file"""
    # read the cell file, modify it, write a new one
    netdoc = read_neuroml2_file("KC.cell.nml")
    kc_cell = netdoc.cells[0]
    net = netdoc.add(neuroml.Network, id="KC_net", validate=False)
    pop = net.add(neuroml.Population, id="KC_pop", component=kc_cell.id, size=1)

    # should be same as test_kc.py
    pg = netdoc.add(
        neuroml.PulseGenerator(
            id="pg", delay="100ms", duration="500ms",
            amplitude="16pA"
        )
    )

    # Add these to cells
    input_list = net.add(
        neuroml.InputList(id="input_list", component=pg.id, populations=pop.id)
    )
    aninput = input_list.add(
        neuroml.Input(
            id="0",
            target="../%s[0]" % (pop.id),
            destination="synapses",
            segment_id="0",
        )
    )
    write_neuroml2_file(netdoc, "KC.net.nml")

    generate_lems_file_for_neuroml(
        sim_id="KC_step_test",
        target=net.id,
        neuroml_file="KC.net.nml",
        duration="700ms",
        dt="0.01ms",
        lems_file_name="LEMS_KC_step_test.xml",
        nml_doc=netdoc,
        gen_spike_saves_for_all_somas=True,
        target_dir=".",
        gen_saves_for_quantities={
            "k.dat": ["KC_pop[0]/biophys/membraneProperties/kv/iDensity"]
        },
        copy_neuroml=False
    )

    data = run_lems_with_jneuroml_neuron(
        "LEMS_KC_step_test.xml", load_saved_data=True, compile_mods=True
    )

    print(data.keys())

    # print(data)
    generate_plot(
        xvalues=[data["t"]],
        yvalues=[data["KC_pop[0]/v"]],
        title="Membrane potential: KC",
    )


if __name__ == "__main__":
    postprocess_GGN()
    postprocess_KC()
    step_current_omv_kc()
