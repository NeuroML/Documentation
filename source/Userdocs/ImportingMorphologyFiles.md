(userdocs:importing_morphology_files)=
# Importing Morphology Files

A number of formats are used in neuroscience to store neuronal morphologies obtained from experiments involving neuronal reconstructions.
This page provides general information on these formats, and documents how they may be converted to NeuroML for use in computational models.

(userdocs:importing_morphology_files:terminology)=
## Terminology

```{figure} ../images/crook2007-morphml-figure1.png
:alt: Figure 1 from {cite}`Crook2007` showing different representations of neuronal morphology.
:align: center
:width: 500px

Figure 1 from {cite}`Crook2007` (all properties of MorphML are now included in NeuroML v2). A schematic comparing handling of morphological information for a simple cell by different applications. a) Original cell structure.  b) Schematic of Neurolucida reconstruction where the soma is represented by an outline and three-dimensional points are specified along each branch. c) NEURON simulator format where cell structure is specified in sections. Only the center of the section is simulated unless the nseg parameter is greater than one. d) GENESIS simulator representation using compartments that are cylinders except for the soma, which can be spherical. The optimal length of each compartment is determined by the electrotonic length. e) MorphML representation where any of the information shown in panels b through d can be encoded.
```

All formats have their own terminology that is used to refer to different parts of the cell.

In [NEURON](https://neuronsimulator.github.io/nrn/python/modelspec/programmatic/topology/geometry.html):

- a {code}`section` is an unbranched contiguous cell region
- the morphology of a cell is defined by 3D points, `pt3D`
- for simulation, one can specify how many segments a section should be divided into, given by {code}`nseg`

In NeuroML:

- segments are 3D points describing the cell morphology
- continuous, unbranched segments groups, would form a section
- the {code}`numberInternalDivisions` property can be used to set the number of divisions a segment or segment group should be divided into for simulation

(userdocs:importing_morphology_files:validity)=
## Cell validity

In general, it is usually necessary to examine NeuroML cells converted from various formats, especially experimental reconstructions, before they can be used in simulations.
This is because reconstructions may not always contain all the information necessary to simulate the cell.

Two potential problems that must be checked are:

- Point of connection of dendritic branches to the soma: e.g., in Neurolucida, there is no explicit soma but usually only an outline.
- Zero length sections: NEURON can work with zero segment lengths (consecutive `pt3d` points being equal), but a standard mapping of this may not be supported in other simulators such as GENESIS.

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

The NeuroML validation tools will check for some of these and report errors where possible.

(userdocs:importing_morphology_files:formats)=
## Formats

(userdocs:importing_morphology_files:formats:neuron)=
### NEURON

There is no fixed format in NEURON for specifying morphologies.
However, cells created in NEURON may be exported to NeuroML2 format using the [`export_to_neuroml2`](https://pyneuroml.readthedocs.io/en/stable/pyneuroml.neuron.html#pyneuroml.neuron.export_to_neuroml2) method included in {ref}`pyNeuroML <pyneuroml>` ([example](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/export_nml2.py)).

(userdocs:importing_morphology_files:formats:genesis)=
### GENESIS

The format for a GENESIS cell description is given [here](http://www.genesis-sim.org/GENESIS/Hyperdoc/Manual-25.html#readcell).

(userdocs:importing_morphology_files:formats:cvapp_swc)=
### CVapp (SWC files)

The SWC format was developed to cover most of the information common between Neurolucida, NEURON, and GENESIS formats.
It is used by resources such as NeuroMorpho.org.

Information on the SWC format can be found in the [NeuroMorpho FAQ](http://neuromorpho.org/myfaq.jsp) under the "What is SWC format" entry.

(userdocs:importing_morphology_files:formats:neurolucida)=
### Neurolucida

The [Neurolucida](http://www.mbfbioscience.com/neurolucida) file format is used by MicroBrightField products to store information on neuronal reconstructions.
Both binary and ASCII format files can be generated by these products.
The format allows recording of various anatomical features, not only neuronal processes such as dendrites and cell bodies, but can record other micro-anatomical features of potential interest to anatomists.
Not all of these features will be relevant when constructing a single cell computational model.

(userdocs:importing_morphology_files:tools)=
## Tools

(userdocs:importing_morphology_files:tools:neuroconstruct)=
### neuroConstruct

{ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>` includes functionality to interactively import GENESIS, NEURON, CVapp (SWC), Neurolucida, and older MorphML formats to NeuroML2.
Please see the [neuroConstruct documentation](http://www.neuroconstruct.org/docs/import.html) for more information.


Conversion of neuroConstruct's importing functions into pure Python for inclusion in {ref}`pyNeuroML <pyneuroml>` [is a work in progress](https://github.com/NeuroML/pyNeuroML/issues/89).
Please contact us if you would like to help with this task.

(userdocs:importing_morphology_files:tools:pyneuroml)=
### pyNeuroML

{ref}`pyNeuroML <pyneuroml>` includes functionality to convert NEURON files into NeuroML using the [`export_to_neuroml2`](https://pyneuroml.readthedocs.io/en/stable/pyneuroml.neuron.html#pyneuroml.neuron.export_to_neuroml2) method included in {ref}`pyNeuroML <pyneuroml>` ([example](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/export_nml2.py)).
