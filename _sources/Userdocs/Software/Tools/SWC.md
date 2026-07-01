(userdocs:swc)=
# SWC and NeuroML

The SWC format was developed to cover most of the information common between Neurolucida, NEURON, and GENESIS formats.
It is used by resources such as NeuroMorpho.org.

Information on the SWC format can be found in the [NeuroMorpho FAQ](http://neuromorpho.org/myfaq.jsp) under the "What is SWC format" entry.

Recommended applications for converting SWC into NeuroML are CVApp and neuroConstruct (see below).

## Tools

A number of tools support conversion of SWC to NeuroML.

(userdocs:cvapp:tools:cvapp)=
### CVApp

[CVApp](https://github.com/NeuroML/Cvapp-NeuroMorpho.org) is a standalone Java tool that can visualize SWC files (for example from [NeuroMorpho.org](https://neuromorpho.org)) and export them into NeuroML2.

```{figure} ../../../images/cvapp.png
:alt: Screenshot of CVApp
:align: center
:width: 80%

Screenshot of CVApp
```

One can select "NeuroMLv2" from the "Save As" drop down box to export the loaded reconstruction to NeuroML.

(userdocs:cvapp:tools:neuroconstruct)=
### neuroConstruct

{ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>` includes functionality to interactively convert CVapp (SWC) files to NeuroML2.
Please see the [neuroConstruct documentation](http://www.neuroconstruct.org/docs/import.html) for more information.
