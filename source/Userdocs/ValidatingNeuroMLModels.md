(userdocs:validating_models)=
# Validating NeuroML Models

```{admonition} WIP
:class: warning
This document is a work in progress. Please see the related ticket here: https://github.com/NeuroML/Documentation/issues/36
```

```{admonition} Validate NeuroML 2 files before using them.
:class: tip
It is good practice to validate NeuroML 2 files to check them for correctness before using them.
```

Models described in NeuroML must adhere to the NeuroML {ref}`specification <userdocs:specification>`.
This allows all NeuroML models to be checked for correctness: **validation**.
There are a number of ways of **validating** NeuroML model files.

(userdocs:validating_models:cli)=
## Using the command line tools

Both `pynml` (provided by {ref}`pyNeuroML <pyneuroml>`) and `jnml` (provided by {ref}`jNeuroML <jneuroml>`) can validate individual NeuroML files:

```{code-block} console
Usage:

# For NeuroML 2
pynml <NML file> -validate
jnml <NML file> -validate

# For NeuroML 1 (deprecated)
pynml <NML file> -validatev1
jnml <NML file> -validatev1
```

Please note that this will validate only the included NeuroML file, against the NeuroML 2 schema.
If these files include other NeuroML 2 files, they will not be taken into consideration.
To validate NeuroML 2 files **recursively** (i.e., by taking the included files into account also), one must currently use the Python API as documented next.

(userdocs:validating_models:python)=
## Using the Python API

The {ref}`pyNeuroML <pyneuroml>` Python API provides a number of methods to validate NeuroML 2 files.
The first is the aptly named `validate_neuroml2` function:

```{code-block} python

from pyneuroml.pynml import validate_neuroml2

...

validate_neuroml2(nml_filename)
```
Similarly, the `validate_neuroml1` function can be used to validate NeuroML v1 files.

Like `pynml`, this only validates single NeuroML 2 files, and does not process included files.
To validate a NeuroML 2 file and all the files it includes, you can use the `read_neuroml2_file` function:

```{code-block} python

from pyneuroml.pynml import read_neuroml2_file


....


read_neuroml2_file(nml_filename, include_includes=True, check_validity_pre_include=True)
```

This will read (load) the provided NeuroML 2 file and all the files that are recursively included by it, and validate them all while it loads them.
