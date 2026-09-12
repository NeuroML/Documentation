(pylems)=
# pyLEMS

pyLEMS is a Python package which provides an API, as well as a simulator for the [LEMS](http://lems.github.io/LEMS) language.
It can also be used to run NeuroML2 models.
```{admonition} Use pyNeuroML
:class: dropdown
{ref}`pyNeuroML <pyneuroml>` builds on pyLEMS and includes additional functions.
```

```{admonition} Citation
:class: dropdown
Please cite Vella et al. ({cite}`Vella2014`) if you use pyLEMS.
```

(pylems:quickstart)=
## Quick start

(pylems:install_python)=
### Install Python

[Python](https://www.python.org/) is generally pre-installed on all computers nowadays.
However, if you do not have Python installed on your system, please follow the official [installation instructions](https://www.python.org/downloads/) to install Python on your computer.
A number of Free/Open source Integrated Development Environments (IDEs) are also available that make working with Python (even) easier.
An example list is [here](https://opensource.com/resources/python/ides).

(pylems:install_with_pip)=
### Install pyLEMS with pip
```{admonition} Tip: Use a virtual environment
:class: tip dropdown

While using Python packages, it is suggested to use a virtual environment to isolate the software you install from each other.
Learn more about using virtual environments in Python [here](https://docs.python.org/3/tutorial/venv.html).
```

The easiest way to install the latest version of pyLEMS is using the default Python package manager, `pip`:
```{code-block} console
pip install pyLEMS
```
(pylems:install_fedora)=
### Installation on Fedora Linux

On [Fedora](https://getfedora.org) Linux systems, the [NeuroFedora](https://neuro.fedoraproject.org) community provides pyLEMS in the [standard Fedora repos](https://src.fedoraproject.org/rpms/python-pyLEMS) and can be installed using the following commands:

```{code-block} console
sudo dnf install python3-pyLEMS
```
(pylems:docs)=
## Documentation

Detailed API documentation for PyLEMS can be found [here](https://pylems.readthedocs.io/en/development/).
pyLEMS provides the `pylems` command line utility that can be used to simulate LEMS files.
`pylems` is self documented, and you can learn about its usage using the `-h` flag:

```{code-block} console
pylems -h
usage: pylems [-h] [-I <Include directory>] [-nogui] [-dlems] <LEMS file>

positional arguments:
  <LEMS file>           LEMS file to be simulated

optional arguments:
  -h, --help            show this help message and exit
  -I <Include directory>
                        Directory to be searched for included files
  -nogui                If this is specified, just parse & simulate the model, but don't show any plots
  -dlems                If this is specified, export the LEMS file as dLEMS (distilled LEMS in JSON format, see https://github.com/borismarin/som-codegen)
```

To simulate a LEMS file:

```{code-block} console
pylems lemsexample.xml

```
Please note that if you are simulating a NeuroML file you will have to also specify the location of the {ref}`NeuroML 2 LEMS definitions <schema:neuromlcorecomptypes_>` with the `-I` option.
We suggest that you use {ref}`pyNeuroML <pyNeuroML>` where this is not required:
```{code-block} console
pylems -I <dir of NeuroML2 install>/NeuroML2CoreTypes/  LEMS_NeuroML2_Model.xml
```

For more information on pyLEMS, please see Vella et al. ({cite}`Vella2014`) and Cannon et al. ({cite}`Cannon2014`).

(pylems:api_docs)=
### API documentation

Detailed API documentation for pyNeuroML can be found [here](https://pylems.readthedocs.io/en/development/index.html).

The pyLEMS API is also self documented.
You can use Python's in-built documentation viewer `pydoc` to view the documentation for any of the package's modules and their functions:

```{code-block} console
Help on package lems:

NAME
    lems

DESCRIPTION
    @author: Gautham Ganapathy
    @organization: LEMS (http://neuroml.org/lems/, https://github.com/organizations/LEMS)
    @contact: gautham@lisphacker.org

PACKAGE CONTENTS
    api
    base (package)
    dlems (package)
    model (package)
    parser (package)
    run
    sim (package)

DATA
    logger = <Logger LEMS (WARNING)>

VERSION
    0.5.2

FILE
    /usr/lib/python3.9/site-packages/lems/__init__.py

```
Most IDEs are able to show you this information as you use them in your Python scripts.

(pylems:gethelp)=
## Getting help

For any questions regarding pyLEMS, please open an issue on the GitHub issue tracker [here](https://github.com/LEMS/pylems/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(pylems:development)=
## Development

pyLEMS is developed on GitHub at [https://github.com/LEMS/pylems](https://github.com/LEMS/pylems) under the [LGPL-3.0 license](https://github.com/LEMS/pylems/blob/master/LICENSE.lesser).
The repository contains the complete source code along with instructions on building/installing pyLEMS.
Please follow the instructions there to build pyLEMS from source.
