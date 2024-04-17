(userdocs:finding_models)=
# Finding and sharing NeuroML models


There are an increasing number of repositories where you can find NeuroML models, many of which will are accepting submissions from the community who wish to share their work in this format.

(userdocs:finding_models:neuromldb)=
## NeuroML-DB: The NeuroML Database

```{admonition} Read the NeuroML-DB preprint!
:class: tip
A preprint of a manuscript describing NeuroML-DB and its current features is available [here](https://www.biorxiv.org/content/10.1101/2021.09.11.459920v1).
```

```{figure} ../images/NML-DB.png
:alt: NeuroML Database
:align: center

The NeuroML Database contains NeuroML files for many [cells](https://neuroml-db.org/model_info?model_id=NMLCL000938) (left above), [channels](https://neuroml-db.org/model_info?model_id=NMLCH000103) (right) and synapses taken from Open Source Brain, Blue Brain Project, Allen Institute and more.  

```

The [NeuroML Database](https://neuroml-db.org/) is a relational database that provides a means for sharing NeuroML model descriptions and their components.
One of its goals is to contribute to an efficient tool chain for model development using NeuroML.
This emphasis allows the database design and subsequent searching to take advantage of this specific format.
In particular, the NeuroML database allows for efficient searches over the components of models and metadata that are associated with a hierarchical NeuroML model description.

The NeuroML Database is developed and maintained by the [ICON Lab](https://iconlab.asu.edu/) at [Arizona State University](https://asu.edu/).

To submit your NeuroML model to NeuroML-DB, please see the information on [this page](https://neuroml-db.org/about).


(userdocs:finding_models:osbv1)=
## Open Source Brain

```{figure} ../images/OSBv1.png
:alt: Open Source Brain
:align: center

Examples of NeuroML 2 models visualised on Open Source Brain. A) [Hodgkin Huxley model](https://www.opensourcebrain.org/projects/hodgkin-huxley-tutorial?explorer=https%3A%2F%2Fraw.githubusercontent.com%2Fopensourcebrain%2Ftutorials%2Fdevelopment%2Fmodels%2FhodgkinHuxley%2FGEPPETTO.json) interactive tutorial. B) Integrate and fire network model of cortical column ([Potjans and Diesmann 2014](https://www.opensourcebrain.org/projects/potjansdiesmann2014)), showing network connectivity. C) Cortical model with multicompartmental cells ([Traub et al. 2005](https://www.opensourcebrain.org/projects/thalamocortical)), showing network properties and simulated membrane potential activity. D) Model of C. elegans nervous system from [OpenWorm project](https://www.opensourcebrain.org/projects/c302/). All visualisation/analysis/simulation enabled due to models being in standardised NeuroML format.

```

[Open Source Brain](https://www.opensourcebrain.org) is a platform for sharing, viewing, analysing, and simulating standardized models from different brain regions and species.
An index of various NeuroML models on Open Source Brain and their validation status can be seen [here](https://github.com/OpenSourceBrain/.github/blob/main/testsheet/README.md).

To add your NeuroML model to Open Source Brain, please see the information on {ref}`this page <userdocs:creating_models:converting_conductance>`.

(userdocs:finding_models:others)=
## Other related projects
```{note}
Needs introductory text.
```

(userdocs:finding_models:NeuroMorpho)=
## NeuroMorpho.Org


[NeuroMorpho.Org](https://neuromorpho.org) is a database of digitally reconstructed neurons. This resource can be used to retrieve reconstructed neuronal morphologies of multiple cell types from a number of species. The database can be browsed by neuron type, brain area, species, contributing lab, or cells can be searched for according to various morphometric criteria or the associated metadata.

There is a utility present on the site to view the cells in 3D (based on Robert Cannon's Cvapp), which can also save the morphologies in NeuroML 2 format.

A tutorial on getting data from NeuroMorpho.Org in NeuroML format can be found [here](https://github.com/NeuralEnsemble/NeuroinformaticsTutorial/blob/master/Exercises/Exercise1_NeuroMorpho_to_OSB.md).


(userdocs:finding_models:OpenWorm)=
## OpenWorm

The [OpenWorm project](http://www.openworm.org) aims to create a simulation platform to build digital <i>in-silico</i> living systems, starting with a C. elegans virtual organism simulation. The simulations and associated tools are being developed in a fully open source manner.

NeuroML is being used for the description of the 302 neurons in the [worm's nervous system](https://www.opensourcebrain.org/projects/c302/), both for morphological description of the cells and their electrical properties.



(userdocs:finding_models:AllenInstitute)=
## Allen Institute

Multiple cell models as produced by the [Allen Institute](https://alleninstitute.org/) as part of their large scale brain modelling efforts are available in NeuroML format [here](https://github.com/OpenSourceBrain/AllenInstituteNeuroML).


(userdocs:finding_models:BlueBrainProject)=
## Blue Brain Project

The detailed cortical cell models from the [Blue Brain Project](http://bluebrain.epfl.ch) have been converted to NeuroML format, along with the ion channels from the [Channelpedia database](https://channelpedia.epfl.ch). See [here](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase) for details.
