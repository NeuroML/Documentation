(history)=
# A brief history of NeuroML

% TODO: update links to refer to pages in the new docs here.

## The early days

The concept of NeuroML was first introduced in an article by Goddard et al. (2001) {cite}`Goddard2001`, following meetings at the University of Edinburgh where initial templates and an overall structure for a model description language for computational modelling in neuroscience were discussed.
The proposal extended general purpose structures for neuroscience data proposed by Gardner et al. (2001) {cite}`Gardner2001`.

At that time, the design principles for NeuroML were closely linked with a specific software architecture in which a base application loads a range of plug-ins to handle different aspects of a simulation experiment.
The simulation platform [Neosim](http://www.neurogems.org/neosim2/) provided an implementation of this approach (Howell et al. 2003 {cite}`Howell2003`), and early NeuroML development was closely aligned to this architecture.
Fred Howell and Robert Cannon developed a software library, the NeuroML Development Kit (NDK), to simplify the process of working with XML serializations of models.
This library implemented a particular dialect of XML but did not define particular structures at the model description level.
Instead, Neosim plug-in developers were free to develop their own structures and serialize them via the NDK, in the hope that some consensus would emerge around the most useful ones.

In practice, few developers beyond the Edinburgh group developed or used such structures and the resulting XML was too application specific to gain wider adoption.
The Neosim project was completed in 2005.

## NeuroML v1.x

Based on discussions with Howell and Cannon about the need to develop a consensus for describing widely used model components, Sharon Crook worked with the neuroanatomy community on a language for describing neuronal morphologies in XML, **MorphML** (Qi and Crook 2004 {cite}`Qi2004`).
At the same time, Padraig Gleeson, working with Angus Silver, was developing {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>`, for generating neuronal simulations for the NEURON and GENESIS simulators (Gleeson et al. 2007 {cite}`Gleeson2007`), which had its own internal simulator independent representation for morphologies, channel and networks.

It was agreed that these efforts should be merged under the banner of NeuroML, and the {ref}`v1.x structure of NeuroML <userdocs:neuromlv1>` was created.
A modular approach containing **MorphML**, **ChannelML** and **NetworkML** was adopted to allow application developers to support only those parts of the language needed by their application (Crook et al. 2007 {cite}`Crook2007`, Gleeson et al. 2010 {cite}`Gleeson2010`).
XML schema files for this version of the standard have been available since 2006.
The motivation, structure and functionality of this version is described in detail in Gleeson et al. 2010, while the specification of the language is outlined in the [Supporting Information](http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1000815#s5) of that publication.

For converting NeuroML v1 models/files to NeuroML2, users can use {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>`.

## NeuroML v2.x - introducing LEMS...

NeuroML2 development was started in 2011.
The main motivation for NeuroML2 was the lack of extensibility of NeuroML v1.x; every new model type which was introduced into the language required an update to the Schema, updates to the text documentation and an implementation in each of the native formats of the target simulators.
NeuroML2 is built on the **LEMS (Low Entropy Model Specification) language**, which allows machine readable definitions of the cell, channel and synapse models which form the core of the language.
This increases transparency of model structure and dynamics and facilitates automatic mapping of the models to multiple simulation formats.
More details on the structure of LEMS and how it is used in NeuroML2 can be found in Cannon et al. 2014 {cite}`Cannon2014` and {ref}`here <userdocs:specification>`.

In parallel with development of NeuroML2 and LEMS, software libraries for reading, writing and running simulations using the languages are under active development in Java ({ref}`jNeuroML <jNeuroML>`) and Python ({ref}`libNeuroML <libNeuroML>` and {ref}`pyLEMS <pyLEMS>` (see Vella et al. 2014 {cite}`Vella2014`) and {ref}`pyNeuroML <pyNeuroML>`).

The NeuroML specifications are developed by the {ref}`NeuroML Editorial Board <neuromlorg:board>` and overseen by its {ref}`Scientific Committee <neuromlorg:ScientificCommittee>`.
NeuroML specifications and the associated libraries are developed on GitHub and an overview of current activities can be found [here](https://github.com/NeuroML/NeuroML2/projects/1).


```{admonition} Recent releases of NeuroML2
For full details on the recent releases of NeuroML see: [here](https://github.com/NeuroML/NeuroML2/blob/master/HISTORY.md).
```


## The future

{ref}`NeuroMLlite <neuromllite>` is under active development, which will significantly enhance the range of network models which can be expressed (in a concise JSON based format) and run in NeuroML supporting simulators. This work will form the basis of NeuroML v3.0.
