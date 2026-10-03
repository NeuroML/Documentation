(userdocs:software)=
# Software and Tools

## Core NeuroML Tools

The NeuroML initiative supports **a core set of libraries** (mainly in Python and Java) to enable the creation/validation/analysis/simulation of NeuroML models as well as to facilitate adding support for the language to other applications.  

```{figure} ../../images/pynml_jnml.svg
:alt: jNeuroML and pyNeuroML
:align: center
:width: 500px

Relationship between {ref}`jLEMS <jlems>`, {ref}`jNeuroML <jneuroml>`, the {ref}`NeuroML 2 LEMS definitions <userdocs:neuromlv2>`, {ref}`libNeuroML <libNeuroML>`, {ref}`pyLEMS <pylems>` and {ref}`pyNeuroML <pyNeuroML>`.

```

### Python based applications

For most users, {ref}`pyNeuroML <pyNeuroML>` will provide all of the key functionality for building, validating, simulating, visualising, and converting NeuroML 2 and LEMS models. It builds on {ref}`libNeuroML <libNeuroML>` and {ref}`pyLEMS <pylems>` and bundles all of the functionality of {ref}`jNeuroML <jNeuroML>` to provide access to this through a Python interface.


### Java based applications

{ref}`jNeuroML <jNeuroML>` (for validating, simulating and converting NeuroML 2 models) and {ref}`jLEMS <jLEMS>` (for simulating LEMS models) are the key applications
created in Java for supporting NeuroML 2/LEMS.

### NeuroML support in other languages

There are preliminary APIs for using NeuroML in {ref}`C++ <neuromlc++>` and {ref}`MATLAB <matlab>`.

## Other NeuroML supporting applications

Many other simulators, applications and libraries support NeuroML. See {ref}`here <userdocs:supporting>` for more details.

A number of databases and neuroinformatics initiatives support NeuroML as a core interchange format. See {ref}`here <userdocs:finding_models>` for more details.
