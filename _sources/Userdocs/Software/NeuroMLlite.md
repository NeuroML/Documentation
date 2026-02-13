(neuromllite)=
# NeuroMLlite

NeuroMLlite is a common framework for reading/writing/generating network specifications which builds on NeuroML 2.
It is intended to provide a high level specification which can be used to generate networks in NeuroML and many other formats---including graphical and in neuronal simulator formats.

```{admonition} Note: NeuroMLlite is under active development
:class: note dropdown
Please [watch the GitHub repository](https://github.com/NeuroML/NeuroMLlite) to receive regular updates on its progress.
```

(neuromllite:quickstart)=
## Quick start

(neuromllite:install_python)=
### Install Python

[Python](https://www.python.org/) is generally pre-installed on all computers nowadays.
However, if you do not have Python installed on your system, please follow the official [installation instructions](https://www.python.org/downloads/) to install Python on your computer.
A number of Free/Open source Integrated Development Environments (IDEs) are also available that make working with Python (even) easier.
An example list is [here](https://opensource.com/resources/python/ides).

(neuromllite:install_with_pip)=
### Install NeuroMLlite with pip
```{admonition} Tip: Use a virtual environment
:class: tip dropdown

While using Python packages, it is suggested to use a virtual environment to isolate the software you install from each other.
Learn more about using virtual environments in Python [here](https://docs.python.org/3/tutorial/venv.html).
```

The easiest way to install the latest version of libNeuroML is using the default Python package manager, `pip`:
```{code-block} console
pip install neuromllite
```
(neuromllite:install_fedora)=
### Installation on Fedora Linux

On [Fedora](https://getfedora.org) Linux systems, the [NeuroFedora](https://neuro.fedoraproject.org) community provides pyNeuroML as a package in their [extras repository](https://docs.fedoraproject.org/en-US/neurofedora/copr/) and can be installed using the following commands:

```{code-block} console
sudo dnf copr enable @neurofedora/neurofedora-extra
sudo dnf install python3-neuromllite
```

(neuromllite:docs)=
## Documentation

Along with a Python API, NeuroMLlite also provides a graphical user interface `nmllite-ui` that can be used to create network models and export or simulate them using different simulators supported by NeuroML.

```{code-block} console
nmllite-ui

NMLlite-UI v0.2.4: A GUI for loading NeuroMLlite files

Usage:
    nmllite-ui Sim_xxx.json
         Load a NeuroMLlite file containing a Simulation, which refers to the Network to run
```
```{figure} ../../images/nmllite-example.png
:alt: Screenshot of NeuroMLlite UI showing an example simulation.
:align: center

Screenshot of NeuroMLlite UI showing an example simulation
```

(neuromllite:api_docs)=
### API documentation

```{admonition} TODO!
:class: dropdown
Generate and publish API documentation for NeuroMLlite.
Issue filed: https://github.com/NeuroML/NeuroMLlite/issues/10
```
The NeuroMLlite API is self documented.
You can use Python's in-built documentation viewer `pydoc` to view the documentation for any of the package's modules and their functions:

```{code-block} console
Help on package neuromllite:

NAME
    neuromllite

PACKAGE CONTENTS
    ArborHandler
    BBPConnectomeReader
    BaseTypes
    ConnectivityHandler
    DefaultNetworkHandler
    GraphVizHandler
    MatrixHandler
    NetworkGenerator
    NeuronHandler
    PsyNeuLinkHandler
    PsyNeuLinkReader
    PyNNHandler
    SonataHandler
    SonataReader
    gui (package)
    sweep (package)
    utils

...
```

Most IDEs are able to show you this information as you use them in your Python scripts.

A number of examples showing how the NeuroMLlite Python API is to be used are also included in the [GitHub repository](https://github.com/NeuroML/NeuroMLlite/tree/master/examples).
For instance, [Example4.py](https://github.com/NeuroML/NeuroMLlite/blob/master/examples/Example4.py) can be run in the following ways to generate different representations of the created network model.
Please see the [Readme file](https://github.com/NeuroML/NeuroMLlite/blob/master/README.md) included in the repository for more example usage.
```{code-block} console
python Example4.py                  # Generate the network in JSON
python Example4.py -nml             # Generate the network in NeuroML2
python Example4.py -jnml            # Generate the network in NeuroML2 & run using jNeuroML
python Example4.py -jnmlnetpyne     # Generate the network in NeuroML2 & run using NetPyNE
python Example4.py -jnmlnrn         # Generate the network in NeuroML2 & run using NEURON
python Example4.py -netpyne         # Generate & run the network directly in NetPyNE
python Example4.py -pynnnest        # Generate & run the network in NEST using PyNN
python Example4.py -pynnnrn         # Generate & run the network in NEURON using PyNN
python Example4.py -pynnbrian       # Generate & run the network in Brian using PyNN
...
```

(neuromllite:gethelp)=
## Getting help

For any questions regarding NeuroMLlite, please open an issue on the GitHub issue tracker [here](https://github.com/NeuroML/NeuroMLlite/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(neuromllite:development)=
## Development

pyNeuroML is developed on GitHub at [https://github.com/NeuroML/NeuroMLlite](https://github.com/NeuroML/NeuroMLlite) under the [LPGL-3.0 license](https://github.com/NeuroML/NeuroMLlite/blob/master/LICENSE.lesser).
The repository contains the complete source code along with instructions on building/installing pyNeuroML.
Please follow the instructions there to build pyNeuroML from source.
