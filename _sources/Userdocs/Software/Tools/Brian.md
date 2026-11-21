(userdocs:brian)=
# Brian and NeuroML

![Brian logo](../../../images/tools/brian2.png)

[Brian](https://briansimulator.org/) is an easy to use, Python based simulator of spiking networks.

## Converting NeuroML model to Brian

{ref}`jNeuroML <jneuroml>` or {ref}`pyNeuroML <pyNeuroML>` can be used to convert NeuroML2/LEMS models to [Brian version 2](https://github.com/brian-team/brian2). This involves pointing at a {ref}`LEMS Simulation file <userdocs:lemssimulation>` describing what to simulate, and using the `-brian2` option:

```{code-block} console
# Using jnml
jnml <LEMS simulation file> -brian2

# Using pynml
pynml <LEMS simulation file> -brian2
```

This command generates a Python script (a file ending in `_brian2.py`) which can be run in Python and will simulate the model and plot/save the results, as outlined in the {ref}`LEMS Simulation file <userdocs:lemssimulation>`.

Notes:

- Only single compartment cells can be converted to Brian format so far. While there is support in Brian for multicompartmental cell simulation, this is not yet covered in the jNeuroML based export.
- There has been support for converting NeuroML models to Brian v1 (using `-brian`), but since this version of Brian is deprecated, and only supports Python 2, this export is no longer actively developed.
- There is limited support for executing networks of cells in Brian, and the most likely route for adding this functionality is via {ref}`NeuroMLlite <NeuroMLlite>`.


## Examples

Example code for interactions between NeuroML models and Brian can be found [here](https://github.com/OpenSourceBrain/BrianShowcase).
