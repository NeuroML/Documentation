(userdocs:neuroml_support_approaches)=
# Approaches to adding NeuroML support

There are a number of ways that a neuronal simulator can add "support for NeuroML", depending on how deeply it embeds the elements of the language.

## Commonly used approaches

(userdocs:neuroml_support_approaches:native)=
### 1) Native support for NeuroML elements

A simulator may have equivalent internal representation of the core concepts from NeuroML2/LEMS, and so be able to natively read/write these formats.

This is the approach taken in {ref}`jNeuroML <jNeuroML>` and {ref}`EDEN <userdocs:eden>`.


(userdocs:neuroml_support_approaches:native_import)=
### 2) Native ability to import NeuroML elements

This is the approach taken in {ref}`MOOSE <userdocs:supporting:apps:moose>` and {ref}`Arbor <userdocs:arbor>`.

(userdocs:neuroml_support_approaches:native_export)=
### 3) Native ability to export NeuroML elements

This is the approach taken in {ref}`NEURON <userdocs:neuron>`.

(userdocs:neuroml_support_approaches:mapping)=
### 4) 3rd party mapping to simulator's own format

This is the approach taken in {ref}`NEURON <userdocs:neuron>` via {ref}`jNeuroML <jNeuroML>`.
