(libneuroml)=
# libNeuroML

libNeuroML is a Python package for working with models specified in NeuroML version 2.
It provides a native Python object model corresponding to the NeuroML schema.
This allows users to build their NeuroML models natively in Python without having to work directly with the underlying XML representation.
Additionally, libNeuroML includes functions for the conversion of the Python representation of the NeuroML model to and from the XML representation.

```{admonition} Use pyNeuroML
:class: dropdown
{ref}`pyNeuroML <pyneuroml>` builds on libNeuroML and includes additional utility functions.
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

The core classes in NeuroML are Python representations of the Component Types defined in the {ref}`NeuroML standard <userdocs:neuromlv2>`.
These can be used to build NeuroML models in Python, and these models can then be exported to the standard XML NeuroML representation.
These core classes also contain some utility functions to make it easier for users to carry out common tasks.

```{figure} ../../images/libneuroml.png
:alt: Examples of mapping between Component names in the NeuroML schema and their corresponding libNeuroML Python classes.
:align: center

Examples of mapping between Component names in the NeuroML schema and their corresponding libNeuroML Python classes.
```

Each NeuroML Component Type is represented here as a Python class.
Due to implementation limitations, whereas NeuroML Component Types use [lower camel case naming](https://en.wikipedia.org/wiki/Camel_case), the Python classes here use [upper camel case naming](https://en.wikipedia.org/wiki/Camel_case).
So, for example, the `adExIaFCell` Component Type in the NeuroML schema becomes the `AdExIaFCell` class here, and `expTwoSynapse` becomes the `ExpTwoSynapse` class.

The `child` and `children` elements that NeuroML Component Types can have are represented in the Python classes as variables.
The variable names, to distinguish them from class names, use [snake case](https://en.wikipedia.org/wiki/Snake_case).
So for example, the `cell` NeuroML Component Type has a corresponding `Cell` Python class here.
The `biophysicalProperties` child Component Type in `cell` is represented as the `biophysical_properties` list variable in the `Cell` Python class.
The class signatures list all the child/children elements and text fields that the corresponding Component Type possesses.
To again use the `Cell` class as an example, the construction signature is this:

```{code-block} python
class neuroml.nml.nml.Cell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, morphology_attr=None, biophysical_properties_attr=None, morphology=None, biophysical_properties=None, extensiontype_=None, **kwargs_)
```
As can be seen here, it includes both the `biophysical_properties` and `morphology` child elements as variables.

Please see the examples in the {ref}`NeuroML documentation <userdocs:getting_started_neuroml>` to see usage examples of libNeuroML.
Please also note that this module is also included in the top level of the `neuroml` package, so you can use these classes by importing neuroml:

```{code-block} python
from neuroml import AdExIaFCell
```


(libneuroml:gethelp)=
## Getting help

For any questions regarding libNeuroML, please open an issue on the GitHub issue tracker [here](https://github.com/NeuralEnsemble/libNeuroML/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(libneuroml:development)=
## Development

libNeuroML is developed on GitHub at [https://github.com/NeuralEnsemble/libNeuroML](https://github.com/NeuralEnsemble/libNeuroML) under the [BSD 3 clause license](https://github.com/NeuralEnsemble/libNeuroML/blob/master/LICENSE).
The repository contains the complete source code along with instructions on building/installing libNeuroML.
Please follow the instructions there to build libNeuroML from source.
