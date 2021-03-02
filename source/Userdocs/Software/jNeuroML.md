(jneuroml)=
# jNeuroML

jNeuroML is a comprehensive application built in Java for handling LEMS and NeuroML 2.

It bundles {ref}`jLEMS <jLEMS>` together with the LEMS definitions for {ref}`NeuroML 2 ComponentTypes <userdocs:neuromlv2>`. The aim is to
allow easy access to a range of NeuroML2/LEMS functionality through a simple command line interface (**jnml**), or in other Java based
applications when used as a library.

jNeuroML can:

- **Validate** NeuroML v1.8.1 and v2.x files
- **Simulate** most NeuroML 2 models (simulation should be specified in the [Simulation element in LEMS file](https://github.com/NeuroML/NeuroML2/blob/master/LEMSexamples/LEMS_NML2_Ex5_DetCell.xml))
- **Export** NeuroML 2 and LEMS to many formats such as Neuron, Brian, Matlab, etc.
- **Import** other languages into LEMS (e.g. SBML)

## Quick start

To get a precompiled binary for jNeuroML, go to [https://github.com/NeuroML/jNeuroML/releases](https://github.com/NeuroML/jNeuroML/releases), download the latest **jNeuroML.zip** file and you have everything you need. Unzip on your local machine and go into the *jNeuroMLJar* directory.

You can also check out the most recent verson of the jar file using:

```
    svn checkout svn://svn.code.sf.net/p/neuroml/code/jNeuroMLJar
    cd jNeuroMLJar
```

More information on installation from source etc. can be found [here](https://github.com/NeuroML/jNeuroML).

## Source

jNeuroML is under development on GitHub at [https://github.com/NeuroML/jNeuroML](https://github.com/NeuroML/jNeuroML).

## Documentation

Information on usage of the command line application can be found with the -h option:
```
>> jnml -h
 jNeuroML v0.10.1
Usage:

    jnml LEMSFile.xml
           Load LEMSFile.xml using jLEMS, parse it and validate it as LEMS, and execute the model it contains

    jnml LEMSFile.xml -nogui
           As above, parse and execute the model and save results, but don't show GUI

    ...
```

More information can be found [here](https://github.com/NeuroML/jNeuroML).

## Issue tracker

To report any issues related to jNeuroML, please open an issue [here](https://github.com/NeuroML/jNeuroML/issues).
