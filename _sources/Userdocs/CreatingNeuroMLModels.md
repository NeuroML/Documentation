(userdocs:creating_models)=
# Creating NeuroML models

There are 3 main ways of developing a new model of a neuronal system in NeuroML

**1) Reuse elements from previous NeuroML models**

There are an increasing number of resources where you can find and analyse previously developed NeuroML models to use as the basis for a new model. See {ref}`here <userdocs:finding_models>` for details.

(userdocs:creating_models:from_scratch)=
**2) Writing models from scratch using Python NeuroML tools**

The toolchain around NeuroML means that it is possible to create a model in NeuroML format from the start. Please see the {ref}`Getting Started with NeuroML section <userdocs:getting_started_neuroml>` for quick examples on how you can use {ref}`pyNeuroML <pyneuroml>` to create NeuroML models and run them.

(userdocs:creating_models:from_published)=
**3) Convert a published model developed in a simulator specific format to NeuroML**

Most computational models used in publications are released in the particular format used by the authors during their research, often in a general purpose simulator like {ref}`NEURON <userdocs:supporting:apps:neuron>`. Many of these can be found on [ModelDB](https://senselab.med.yale.edu/ModelDB/default). Converting one of these to NeuroML format will mean that all further developments/modifications of the model will be standards compliant, and will give access to all of the NeuroML compliant tools for visualising/analysing/optimising/sharing the model, as well as providing multiple options for executing the model across multiple simulators.

The next page is a **step by step guide** to creating a new NeuroML model based on an existing published model, verifying its behaviour, and sharing it with the community on the Open Source Brain platform.
