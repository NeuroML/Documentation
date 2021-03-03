(libneuroml)=
# libNeuroML

libNeuroML is a Python API package for working with models specified in NeuroML version 2.
```{admonition} Use pyNeuroML
:class: dropdown
{ref}`pyNeuroML <pyneuroml>` builds on libNeuroML and includes additional functions.
```
```{admonition} Citation
:class: dropdown
Please cite Vella et al. ({cite}`Vella2014`) if you use libNeuroML.
```

(libneuroml:quickstart)=
## Quick start

(libneuroml:install_python)=
### Install Python

[Python](https://www.python.org/) is generally pre-installed on all computers nowadays.
However, if you do not have Python installed on your system, please follow the official [installation instructions](https://www.python.org/downloads/) to install Python on your computer.
A number of Free/Open source Integrated Development Environments (IDEs) are also available that make working with Python (even) easier.
An example list is [here](https://opensource.com/resources/python/ides).

(libneuroml:install_with_pip)=
### Install libNeuroML with pip
```{admonition} Tip: Use a virtual environment
:class: tip dropdown

While using Python packages, it is suggested to use a virtual environment to isolate the software you install from each other.
Learn more about using virtual environments in Python [here](https://docs.python.org/3/tutorial/venv.html).
```

The easiest way to install the latest version of libNeuroML is using the default Python package manager, `pip`:
```{code-block} console
pip install libNeuroML
```
(libneuroml:install_fedora)=
### Installation on Fedora Linux

On [Fedora](https://getfedora.org) Linux systems, the [NeuroFedora](https://neuro.fedoraproject.org) community provides libNeuroML in the [standard Fedora repos](https://src.fedoraproject.org/rpms/python-libNeuroML) and can be installed using the following commands:

```{code-block} console
sudo dnf install python3-libNeuroML
```
(libneuroml:docs)=
## Documentation

Detailed API documentation for libNeuroML can be found [here](https://libneuroml.readthedocs.io/en/latest/).
For more information on libNeuroML, please see Vella et al. ({cite}`Vella2014`) and Cannon et al. ({cite}`Cannon2014`).

(libneuroml:gethelp)=
### Getting help

For any questions regarding libNeuroML, please open an issue on the GitHub issue tracker [here](https://github.com/NeuralEnsemble/libNeuroML/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(libneuroml:development)=
## Development

libNeuroML is developed on GitHub at [https://github.com/NeuralEnsemble/libNeuroML](https://github.com/NeuralEnsemble/libNeuroML) under the [BSD 3 clause license](https://github.com/NeuralEnsemble/libNeuroML/blob/master/LICENSE).
The repository contains the complete source code along with instructions on building/installing libNeuroML.
Please follow the instructions there to build libNeuroML from source.
