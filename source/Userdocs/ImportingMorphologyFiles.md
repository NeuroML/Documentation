(userdocs:importing_morphology_files)=
# Importing Morphology Files

A number of formats are used in Neuroscience to store neuronal morphologies obtained from experiments where neuronal reconstructions is possible.
This page provides general information on these formats, and documents how they may be converted to NeuroML for use in computational models.

## Cell validity

In general, it is usually necessary to examine converted cells before they are used in simulations.
This is because reconstructions may not always contain all the information necessary to simulate the cell.

Two potential problems that must be checked are:

- Point of connection of dendritic branches to the soma: e.g., in Neurolucida, there is no explicit soma but usually only an outline.
- Zero length sections: NEURON can work with zero segment lengths (consecutive pt3d points being equal), but a standard mapping of this may not be supported in other simulators such as GENESIS.

An incomplete list of checks to make to ensure a valid cell is (taken from {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>`):

- Only one segment should be without a parent (root)
- All segments must have sections
- All segments must have endpoints
- All segments must have unique IDs
- All segments must have unique names
- All sections must have unique names
- Segments after the first in a section must only be connected to 1 parent
- Only one segment may be spherical and must belong to the {code}`soma_group` SegmentGroup
- The cell must have at least one segment
- The cell must have at least one soma section, i.e., which is in the {code}`soma_group`
- The cell must have a cell name

## Formats

### GENESIS

The format for a GENESIS cell description is given [here](http://www.genesis-sim.org/GENESIS/Hyperdoc/Manual-25.html#readcell).
### NEURON

There is no fixed format in NEURON for specifying morphologies.
However, cells created in NEURON may be exported to NeuroML2 format using {ref}`pyNeuroML <pyneuroml>` ([example](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/export_nml2.py)).

### CVapp (SWC files)

The SWC format was developed to cover most of the information common between Neurolucida, NEURON, and GENESIS formats.
It is used by resources such as NeuroMorpho.org.

Information on the SWC format can be found in the [NeuroMorpho FAQ](http://neuromorpho.org/myfaq.jsp) under the "What is SWC format" entry.

### Neurolucida


## Tools

### neuroConstruct

### 
