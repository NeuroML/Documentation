(pyneuroml)=
# pyNeuroML

```{admonition} Suggested NeuroML tool
:class: dropdown
pyNeuroML is the suggested software tool for working with NeuroML.
It builds on {ref}`jNeuroML <jneuroml>`, {ref}`libNeuroML <libneuroml>`, and {ref}`pyLEMS <pylems>`.
```
```{admonition} Citation
:class: dropdown
Please cite Vella et al. ({cite}`Vella2014`) if you use pyNeuroML.
```

pyNeuroML is a Python package that allows you to work with NeuroML models using the Python programming language.
It includes all the API functions provided by {ref}`libNeuroML <libNeuroML>` and {ref}`pyLEMS <pylems>`, and also wraps all the functions that {ref}`jNeuroML <jNeuroML>` provides, which can therefore be used from within Python itself.

With pyNeuroML you can:

- **Create** NeuroML models and simulations
- **Validate** NeuroML v1.8.1 and v2.x files
- **Simulate** NeuroML 2 models
- **Export** NeuroML 2 and LEMS files to many formats such as Neuron, Brian, Matlab, etc.
- **Import** other languages into LEMS (e.g. SBML)
- **Visualise** NeuroML models and simulations

```{figure} ../../images/pynml_jnml.svg
:alt: jNeuroML and pyNeuroML
:align: center
:width: 500px

Relationship between {ref}`jLEMS <jlems>`, {ref}`jNeuroML <jneuroml>`, the {ref}`NeuroML 2 LEMS definitions <userdocs:neuromlv2>`, {ref}`libNeuroML <libNeuroML>`, {ref}`pyLEMS <pylems>` and {ref}`pyNeuroML <pyNeuroML>`.

```

(pyneuroml:quickstart)=
## Quick start

(pyneuroml:install_python_and_java)=
### Install Python and the Java Runtime Environment

[Python](https://www.python.org/) is generally pre-installed on all computers nowadays.
However, if you do not have Python installed on your system, please follow the official [installation instructions](https://www.python.org/downloads/) to install Python on your computer.
A number of Free/Open source Integrated Development Environments (IDEs) are also available that make working with Python (even) easier.
An example list is [here](https://opensource.com/resources/python/ides).

Since pyNeuroML wraps around jNeuroML which is written in Java, you will need a Java Runtime Environment (JRE) installed on your system.
On most Linux systems [Free/Open source OpenJDK runtime environment](https://openjdk.java.net/) is already pre-installed.
You can also install Oracle's proprietary Java platform from their [download page](https://www.oracle.com/java/technologies/javase-downloads.html) if you prefer.
Please refer to your operating system's documentation to install a JRE.

(pyneuroml:install_with_pip)=
### Install pyNeuroML with pip

```{admonition} Tip: Use a virtual environment
:class: tip dropdown

While using Python packages, it is suggested to use a virtual environment to isolate the software you install from each other.
Learn more about using virtual environments in Python [here](https://docs.python.org/3/tutorial/venv.html).
```

The easiest way to install the latest version of pyNeuroML is using the default Python package manager, `pip`:

```{code-block} console
pip install pyneuroml
```

By default, this will only install the minimal set of packages required to use pyNeuroML.
To use pyNeuroML with specific {ref}`supporting tools <userdocs:supporting:apps>`, please install them as required:


- simulation backends

  - {code}`pip install pyneuroml[neuron]`:       NEURON
  - {code}`pip install pyneuroml[brian]`:        Brian2
  - {code}`pip install pyneuroml[netpyne]`:      NetPyNE
  - {code}`pip install pyneuroml[tellurium]`:    Tellurium

- COMBINE formats (SEDML/SBML):

  - {code}`pip install pyneuroml[combine]`

- analysis and visualization

  - {code}`pip install pyneuroml[analysis]`

- visualization

  - VisPy:

    - {code}`pip install pyneuroml[vispy]`:        Qt6 (default): 
    - {code}`pip install pyneuroml[vispy-qt5]`  :   Qt5
    - {code}`pip install pyneuroml[vispy-common]`: to manually use another [supported backend](https://vispy.org/installation): 

  - {code}`pip install pyneuroml[povray]`:         Povray
  - {code}`pip install pyneuroml[plotly]`:       PlotLy

- model fitting

  - {code}`pip install pyneuroml[tune]`

- HDF5 support

  - {code}`pip install pyneuroml[hdf5]`

- Neuroscience Gateway (NSG) support

  - {code}`pip install pyneuroml[nsg]`

- RDF annotations

  - {code}`pip install pyneuroml[annotations]`

A number of "meta" packages are also available:

- {code}`pip install pyneuroml[all]`: install everything
- {code}`pip install pyneuroml[dev]`: install for development
- {code}`pip install pyneuroml[doc]`: install for building documentation

(pyneuroml:optional)=
### Installing optional dependencies

The optional "extras" provided by pyNeuroML may require some additional software to be installed that is not Python based, and so cannot be automatically installed using {code}`pip`:


#### NEURON

For compiling NEURON mod files, you also need a C compiler and the `make` utility installed on your computer.
Additionally, to run parallel simulations the [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) libraries are also needed.
Please see the [NEURON installation documentation](https://www.neuron.yale.edu/neuron/download) for more information on installing NEURON on your computer.

#### Povray

Requires the installation of the [Povray](http://www.povray.org/) tool.

#### Vispy

Requires installation of a [back end](https://vispy.org/installation).
The default is [Qt6](https://www.qt.io/), but one can also use Qt5, or a different back end.
Vispy also makes use of GPUs via [OpenGL](https://en.wikipedia.org/wiki/OpenGL).
So a recent GPU is recommended for larger scale models.


For more information on individual simulation backends and extras, please refer to their respective documentations.

(pyneuroml:install_fedora)=
### Installation on Fedora Linux

On [Fedora](https://getfedora.org) Linux systems, the [NeuroFedora](https://neuro.fedoraproject.org) community provides pyNeuroML as a package in their [extras repository](https://docs.fedoraproject.org/en-US/neurofedora/copr/) and can be installed using the following commands:

```{code-block} console
sudo dnf copr enable @neurofedora/neurofedora-extra
sudo dnf install python3-pyneuroml
```

Optional packages can also be installed using the default package manager:

```
sudo dnf install python3-brian2 python3-neuron neuron-devel python3-netpyne
```

MPI builds of these tools are also available in the NeuroFedora repositories.
Please see the [project documentation](https://docs.fedoraproject.org/en-US/neurofedora/mpi/) on installing and using them.

(pyneuroml:docs)=
## Documentation

pyNeuroML provides a set of command line utilities along with an API to use from within Python scripts:

```{admonition} TODO!
:class: dropdown
Check that all of these have usage documentation that is viewable using the `-h` flag.
Issue filed: https://github.com/NeuroML/pyNeuroML/issues/87
```

- pynml
- pynml-channelanalysis
- pynml-modchananalysis
- pynml-plotspikes
- pynml-povray
- pynml-sonata
- pynml-summary
- pynml-tune

These utilities are self-documented.
So, to learn how these utilities are to be used, run them with the `-h` flag.
For example:

```{code-block} console
pynml -h
usage: pynml [-h|--help] [<shared options>] <one of the mutually-exclusive options>

pyNeuroML v0.5.9: Python utilities for NeuroML2
    libNeuroML v0.2.54
    jNeuroML v0.10.2

optional arguments:
  -h, --help            show this help message and exit

Shared options:
  These options can be added to any of the mutually-exclusive options

  -verbose              Verbose output
  -java_max_memory MAX  Java memory for jNeuroML, e.g. 400M, 2G (used in
                        -Xmx argument to java)
  -nogui                Suppress GUI,
                        i.e. show no plots, just save results
  <LEMS/NeuroML 2 file>
                        LEMS/NeuroML 2 file to process

...
```
(pyneuroml:api_docs)=
### API documentation

Detailed API documentation for pyNeuroML can be found [here](https://pyneuroml.readthedocs.io/en/development/).

The pyNeuroML API is also self documented.
You can use Python's in-built documentation viewer `pydoc` to view the documentation for any of the package's modules and their functions:
```{code-block} console

pydoc pyneuroml
Help on package pyneuroml:

NAME
    pyneuroml

PACKAGE CONTENTS
    analysis (package)
    lems (package)
    neuron (package)
    plot (package)
    povray (package)
    pynml
    swc (package)
    tune (package)

DATA
    JNEUROML_VERSION = '0.10.2'

VERSION
    0.5.9

FILE
    /usr/lib/python3.9/site-packages/pyneuroml/__init__.py

```
```{code-block} console
pydoc pyneuroml.analysis

Help on package pyneuroml.analysis in pyneuroml:

NAME
    pyneuroml.analysis

PACKAGE CONTENTS
    ChannelDensityPlot
    ChannelHelper
    NML2ChannelAnalysis

FUNCTIONS
    analyse_spiketime_vs_dt(nml2_file, target, duration, simulator, cell_v_path, dts, verbose=False, spike_threshold_mV=0, show_plot_already=True, save_figure_to=None, num_of_last_spikes=None)

    generate_current_vs_frequency_curve(nml2_file, cell_id, start_amp_nA=-0.1, end_amp_nA=0.1, step_nA=0.01, custom_amps_nA=[], analysis_duration=1000, analysis_delay=0, pre_zero_pulse=0, post_zero_pulse=0, dt=0.05, temperature='32degC', spike_threshold_mV=0.0, plot_voltage_traces=False, plot_if=True, plot_iv=False, xlim_if=None, ylim_if=None, xlim_iv=None, ylim_iv=None, label_xaxis=True, label_yaxis=True, show_volts_label=True, grid=True, font_size=12, if_iv_color='k', linewidth=1, bottom_left_spines_only=False, show_plot_already=True, save_voltage_traces_to=None, save_if_figure_to=None, save_iv_figure_to=None, save_if_data_to=None, save_iv_data_to=None, simulator='jNeuroML', num_processors=1, include_included=True, title_above_plot=False, return_axes=False, verbose=False)

FILE
    /usr/lib/python3.9/site-packages/pyneuroml/analysis/__init__.py

```
Most IDEs are able to show you this information as you use them in your Python scripts.

(pyneuroml:gethelp)=
## Getting help

For any questions regarding pyNeuroML, please open an issue on the GitHub issue tracker [here](https://github.com/NeuroML/pyNeuroML/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(pyneuroml:development)=
## Development

pyNeuroML is developed on GitHub at [https://github.com/NeuroML/pyNeuroML](https://github.com/NeuroML/pyNeuroML) under the [LPGL-3.0 license](https://github.com/NeuroML/pyNeuroML/blob/master/LICENSE.lesser).
The repository contains the complete source code along with instructions on building/installing pyNeuroML.
Please follow the instructions there to build pyNeuroML from source.
