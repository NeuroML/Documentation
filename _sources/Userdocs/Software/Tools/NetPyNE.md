(userdocs:netpyne)=
# NetPyNE and NeuroML

![NetPyNE logo](../../../images/tools/netpyne.png)

[NetPyNE](http://netpyne.org) is a Python package to facilitate the development, simulation, parallelization, analysis, and optimization of biological neuronal networks using the NEURON simulator. NetPyNE can import from and export to NeuroML. NetPyNE also provides a web based [Graphical User Interface](https://github.com/MetaCell/NetPyNE-UI/wiki).

## Importing NeuroML into NetPyNE

An example of how to import a network in NeuroML into NetPyNE can be found [here](https://github.com/Neurosim-lab/netpyne/blob/development/examples/NeuroMLImport/SimpleNet_import.py).

## Exporting NeuroML from NetPyNE

An example of how to export a network built using NetPyNE to NeuroML can be found [here](https://github.com/OpenSourceBrain/NetPyNEShowcase/blob/master/NetPyNE/HHSmall/HH_export.py).

## Running NetPyNE on OSBv2

Building and running NetPyNE models will be a core feature of Open Source Brain v2.0. See [here](https://docs.opensourcebrain.org/OSBv2/NetPyNE.html) for more details.

## NeuroMLlite

NetPyNE is also a key target for cross simulator network creation using {ref}`NeuroMLlite <neuromllite>`. There are ongoing plans for greater alignment between formats used for network specification in NetPyNE and NeuroMLlite.
