(pyneuroml)=
# PyNeuroML

```{admonition} Suggested NeuroML tool
:class: dropdown
PyNeuroML is the suggested software tool for working with NeuroML.
It builds on {ref}`jNeuroML <jneuroml>`, {ref}`libNeuroML <libneuroml>`, and {ref}`PyLEMS <pylems>`.
```
```{admonition} Citation
:class: dropdown
Please cite Vella et al. ({cite}`Vella2014`) if you use PyNeuroML.
```

PyNeuroML is a Python package that allows you to work with NeuroML models using the Python programming language.
It includes all the API functions provided by {ref}`libNeuroML <libNeuroML>` and {ref}`pyLEMS <pylems>`, and also wraps all the functions that {ref}`jNeuroML <jNeuroML>` provides, which can therefore be used from within Python itself.

With PyNeuroML you can:

- **Create** NeuroML models and simulations
- **Validate** NeuroML v1.8.1 and v2.x files
- **Simulate** NeuroML 2 models
- **Export** NeuroML 2 and LEMS files to many formats such as Neuron, Brian, Matlab, etc.
- **Import** other languages into LEMS (e.g. SBML)
- **Visualise** NeuroML models and simulations

(pyneuroml:quickstart)=
## Quick start

(pyneuroml:install_python_and_java)=
### Install Python and the Java Runtime Environment

[Python](https://www.python.org/) is generally pre-installed on all computers nowadays.
However, if you do not have Python installed on your system, please follow the official [installation instructions](https://www.python.org/downloads/) to install Python on your computer.
A number of Free/Open source Integrated Development Environments (IDEs) are also available that make working with Python (even) easier.
An example list is [here](https://opensource.com/resources/python/ides).

Since PyNeuroML wraps around jNeuroML which is written in Java, you will need a Java Runtime Environment (JRE) installed on your system.
On most Linux systems [Free/Open source OpenJDK runtime environment](https://openjdk.java.net/) is already pre-installed.
You can also install Oracle's proprietary Java platform from their [download page](https://www.oracle.com/java/technologies/javase-downloads.html) if you prefer.
Please refer to your operating system's documentation to install a JRE.

(pyneuroml:install_with_pip)=
### Install PyNeuroML with pip

```{admonition} Tip: Use a virtual environment
:class: tip dropdown

While using Python packages, it is suggested to use a virtual environment to isolate the software you install from each other.
Learn more about using virtual environments in Python [here](https://docs.python.org/3/tutorial/venv.html).
```

The easiest way to install the latest version of PyNeuroML is using the default Python package manager, `pip`:

```{code-block} console
pip install pyneuroml
```
(pyneuroml:install_fedora)=
### Installation on Fedora Linux

On [Fedora](https://getfedora.org) Linux systems, the [NeuroFedora](https://neuro.fedoraproject.org) community provides PyNeuroML as a package in their [extras repository](https://docs.fedoraproject.org/en-US/neurofedora/copr/) and can be installed using the following commands:

```{code-block} console
sudo dnf copr enable @neurofedora/neurofedora-extra
sudo dnf install python3-pyneuroml
```
(pyneuroml:docs)=
## Documentation

PyNeuroML provides a set of command line utilities along with an API to use from within Python scripts:

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

```{admonition} TODO!
:class: dropdown
Generate and publish API documentation for PyNeuroML.
Issue filed: https://github.com/NeuroML/pyNeuroML/issues/86
```
The PyNeuroML API is also self documented.
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
### Getting help

For any questions regarding PyNeuroML, please open an issue on the GitHub issue tracker [here](https://github.com/NeuroML/pyNeuroML/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(pyneuroml:development)=
## Development

PyNeuroML is developed on GitHub at [https://github.com/NeuroML/pyNeuroML](https://github.com/NeuroML/pyNeuroML) under the [LPGL-3.0 license](https://github.com/NeuroML/pyNeuroML/blob/master/LICENSE.lesser).
The repository contains the complete source code along with instructions on building/installing PyNeuroML.
Please follow the instructions there to build PyNeuroML from source.
