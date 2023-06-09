(userdocs:validating_models)=
# Validating NeuroML Models
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
jnml -validate <NML file(s)>
pynml <NML file(s)> -validate

# For NeuroML 1 (deprecated)
jnml -validatev1 <NML file>
pynml <NML file(s)> -validatev1
```

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

If you are loading NeuroML files into your Python script, the `read_neuroml2_file` function also includes validation:

```{code-block} python

from pyneuroml.pynml import read_neuroml2_file


....


read_neuroml2_file(nml_filename, include_includes=True, check_validity_pre_include=True)
```

This will read (load) the provided NeuroML 2 file and all the files that are recursively included by it, and validate them all while it loads them.

(userdocs:validating_models:tests)=
## List of validation tests


These tests are made against the Schema document.
```{list-table}
:header-rows: 1
:name: validation-tests-schema

* - Test
  - Description
* - Check names
  - Check that names of all elements, attributes, parameters match those provided in the schema
* - Check types
  - Check that the types of all included elements
* - Check values
  - Check that values follow given restrictions
* - Check inclusion
  - Check that required elements are included
* - Check cardinality
  - Check the number of elements
* - Check hierarchy
  - Check that child/children elements are included in the correct parent elements
* - Check sequence order
  - Check that child/children elements are included in the correct order

```

These are additional validation tests that are run on models (defined [here](https://github.com/NeuroML/org.neuroml.model/blob/development/src/main/java/org/neuroml/model/util/NeuroML2Validator.java#L57)):
```{list-table}
:header-rows: 1
:name: validation-tests-additional

* - Test
  - Description
* - Check top level ids
  - Check that top level (root) elements have unique ids
* - Check {ref}`Network <schema:Network>` level ids
  - Check that child/children of the {ref}`Network <schema:Network>` element have unique ids
* - Check {ref}`Cell <schema:Cell>` {ref}`Segment <schema:Segment>` ids
  - Check that all {ref}`Segment <schema:Segment>`s in a {ref}`Cell <schema:Cell>` have unique ids
* - Check single {ref}`Segment <schema:Segment>` without parent
  - Check that only one {ref}`Segment <schema:Segment>` is without parents (the soma {ref}`Segment <schema:Segment>`)
* - Check {ref}`SegmentGroup <schema:SegmentGroup>` ids
  - Check that all {ref}`SegmentGroup <schema:SegmentGroup>`s in a {ref}`Cell <schema:Cell>` have unique ids
* - Check {ref}`Member <schema:Member>` segment ids exist
  - Check that {ref}`Segment <schema:Segment>`s referred to in {ref}`SegmentGroup <schema:SegmentGroup>` {ref}`Member <schema:Member>`s exist
* - Check {ref}`SegmentGroup <schema:SegmentGroup>` definition
  - Check that {ref}`SegmentGroup <schema:SegmentGroup>`s being referenced are defined
* - Check {ref}`SegmentGroup <schema:SegmentGroup>` definition order
  - Check that {ref}`SegmentGroup <schema:SegmentGroup>`s are defined before being referenced
* - Check included {ref}`SegmentGroup <schema:SegmentGroup>`s
  - Check that {ref}`SegmentGroup <schema:SegmentGroup>`s referenced by {ref}`Include <schema:Include>` elements of other {ref}`SegmentGroup <schema:SegmentGroup>`s exist
* - Check `numberInternalDivisions`
  - Check that {ref}`SegmentGroup <schema:SegmentGroup>`s define `numberInternalDivisions` (used by simulators to discretize un-branched branches into compartments for simulation)
* - Check included model files
  - Check that model files included by other files exist
* - Check {ref}`Population <schema:Population>` component
  - Check that a component id provided to a {ref}`Population <schema:Population>` exists
* - Check ion channel exists
  - Check that an ion channel used to define a {ref}`ChannelDensity <schema:ChannelDensity>` element exists
* - Check concentration model species
  - Check that the species used in {ref}`ConcentrationModel <schema:ConcentrationModel>` elements are defined
* - Check {ref}`Population <schema:Population>` size
  - Check that the `size` attribute of a {ref}`PopulationList <schema:PopulationList>` matches the number of defined {ref}`Instance <schema:Instance>`s
* - Check {ref}`Projection <schema:Projection>` component
  - Check that {ref}`Population <schema:Population>`s used in the {ref}`Projection <schema:Projection>` elements exist
* - Check {ref}`Connection <schema:Connection>` {ref}`Segment <schema:Segment>`
  - Check that the {ref}`Segment <schema:Segment>` used in {ref}`Connection <schema:Connection>` elements exist
* - Check {ref}`Connection <schema:Connection>` pre/post cells
  - Check that the pre- and post-synaptic cells used in {ref}`Connection <schema:Connection>` elements exist and are correctly specified
* - Check {ref}`Synapse <schema:Synapses_>`
  - Check that the {ref}`Synapse <schema:Synapses_>` component used in a {ref}`Projection <schema:Projection>` element exists
* - Check root id
  - Check that the root {ref}`Segment <schema:Segment>` in a {ref}`Cell <schema:Cell>` morphology has id \(0\)


```
