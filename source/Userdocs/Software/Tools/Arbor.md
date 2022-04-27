(userdocs:arbor)=
# Arbor and NeuroML

![Arbor logo](../../../images/tools/arbor.png)

[Arbor](https://arbor-sim.org/) is a high performance multicompartmental neural simulation library. Addition of support for NeuroML2 and LEMS is under active development.

## Importing NeuroML into Arbor

The current approach to supporting NeuroML in Arbor involves {ref}`importing NeuroML to Arbor's internal format <userdocs:neuroml_support_approaches:native_import>`.

See [here](https://docs.arbor-sim.org/en/stable/fileformat/neuroml.html) for Arbor's own documentation on this. It involves calling the [neuroml()](https://docs.arbor-sim.org/en/stable/python/morphology.html#arbor.neuroml) method in arbor pointing at the NeuroML file containing the cell you wish to load:

```{code-block} python
nml = arbor.neuroml('mymorphology.cell.nml')

```
See [here](https://github.com/OpenSourceBrain/ArborShowcase/blob/main/NeuroML2/test_arbor.py) for a worked example of this.


## Using Arbor with NeuroMLlite

There is preliminary support for building network specified in {ref}`NeuroMLlite <NeuroMLlite>` format directly in Arbor. See [here](https://github.com/NeuroML/NeuroMLlite/tree/master/examples/arbor) for an example.

## Examples

Example code for interactions between NeuroML models and Arbor can be found in the [Arbor Showcase](https://github.com/OpenSourceBrain/ArborShowcase) repository.
