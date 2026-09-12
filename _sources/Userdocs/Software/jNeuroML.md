(jneuroml)=
# jNeuroML

jNeuroML is a Free/Open Source Java tool for working with LEMS and NeuroML 2.
It includes the `jnml` command line application, and can also be used as a Java library.

With jNeuroML you can:

- **Validate** NeuroML v1.8.1 and v2.x files
- **Simulate** NeuroML 2 models
- **Export** NeuroML 2 and LEMS files to many formats such as Neuron, Brian, Matlab, etc.
- **Import** other languages into LEMS (e.g. SBML)
- **Visualise** NeuroML models and simulations

```{admonition} Use pyNeuroML
:class: dropdown
{ref}`pyNeuroML <pyneuroml>` builds on jNeuroML and includes additional functions.
```
(jneuroml:quickstart)=
## Quick start

(jneuroml:install_java)=
### Install the Java Runtime Environment

Since jNeuroML is written in Java, you will need a Java Runtime Environment (JRE) installed on your system.
On most Linux systems [Free/Open source OpenJDK runtime environment](https://openjdk.java.net/) is already pre-installed.
You can also install Oracle's proprietary Java platform from their [download page](https://www.oracle.com/java/technologies/javase-downloads.html) if you prefer.
Please refer to your operating system's documentation to install a JRE.

(jneuroml:install_jar)=
### Installation using pre-compiled JAR

jNeuroML is provided as a pre-compiled ready-to-use Java JAR file that can be used on any computer that has Java installed.
Please download it from the [GitHub release page](https://github.com/NeuroML/jNeuroML/releases) and unzip (extract) it in a preferred folder on your computer:

```{code-block} console
cd <folder where you downloaded the jNeuroML zip file>
unzip jNeuroML.zip
```
This will extract the zip file to a new folder which will contain the pre-compiled JAR file and runner scripts:

```{code-block} console
ls jNeuroMLJar/
jNeuroML-0.10.2-jar-with-dependencies.jar  jnml  jnml.bat  README
```

```{admonition} TODO
:class: dropdown
Add instructions on using the installer script.
https://github.com/NeuroML/jNeuroML/pull/76
```

(jneuroml:install_fedora)=
### Installation on Fedora Linux

On [Fedora](https://getfedora.org) Linux systems, the [NeuroFedora](https://neuro.fedoraproject.org) community provides jNeuroML as a package in their [extras repository](https://docs.fedoraproject.org/en-US/neurofedora/copr/) and can be installed using the following commands:

```{code-block} console
sudo dnf copr enable @neurofedora/neurofedora-extra
sudo dnf install jneuroml
```

(jneuroml:docs)=
## Documentation

Information on usage of the `jnml` command line application can be found with the -h option:

```{code-block} console
jnml -h

 jNeuroML v0.10.1
Usage:

    jnml LEMSFile.xml
           Load LEMSFile.xml using jLEMS, parse it and validate it as LEMS, and execute the model it contains

    jnml LEMSFile.xml -nogui
           As above, parse and execute the model and save results, but don't show GUI

    ...
```
(jneuroml:api_docs)=
### API documentation

The jNeuroML API is self documented.
Please refer to the various packages to learn their usage:

- [NeuroML/jNeuroML](https://github.com/NeuroML/jNeuroML) (API Documentation [here](http://neuroml.github.io/jNeuroML))
- [NeuroML/org.neuroml.model](https://github.com/NeuroML/org.neuroml.model) (API Documentation [here](http://neuroml.github.io/org.neuroml.model/index.html))
- [NeuroML/org.neuroml.model.injectingplugin](https://github.com/NeuroML/org.neuroml.model.injectingplugin) (API Documentation [here](http://neuroml.github.io/org.neuroml.model.injectingplugin/index.html))
- [NeuroML/org.neuroml.import: Import other formats into LEMS & combine with NeuroML models](https://github.com/NeuroML/org.neuroml.import) (API documentation [here](http://neuroml.github.io/org.neuroml.import/))
- [NeuroML/org.neuroml.export: Export from NeuroML & LEMS](https://github.com/NeuroML/org.neuroml.export) (API Documentation [here](http://neuroml.github.io/org.neuroml.export/index.html))

(jneuroml:gethelp)=
## Getting help

For any questions regarding jNeuroML, please open an issue on the GitHub issue tracker [here](https://github.com/NeuroML/jNeuroML/issues).
Any bugs and feature requests can also be filed there.

You can also use any of the {ref}`communication channels of the NeuroML community <contact>`.

(jneuroml:development)=
## Development

jNeuroML is developed on GitHub at [https://github.com/NeuroML/jNeuroML](https://github.com/NeuroML/jNeuroML) under the [LPGL-3.0 license](https://github.com/NeuroML/jNeuroML/blob/master/LICENSE.lesser).
The repository contains the complete source code along with instructions on building/installing jNeuroML.
Please follow the instructions there to build jNeuroML from source.

(jneuroml:nightlies)=
### Nightly (pre-release) jar builds:

```{warning}
Please note that these JARs are considered experimental and should only be used for testing purposes.
```

In case you want to use a development (un-released) version of jNeuroML, you can download a development build following the steps below.
You will need to have the [Subversion](https://subversion.apache.org/) tool installed on your system.

```{code-block} console
svn checkout svn://svn.code.sf.net/p/neuroml/code/jNeuroMLJar
cd jNeuroMLJar
```

