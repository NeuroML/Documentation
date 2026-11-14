(userdocs:moose)=
# MOOSE and NeuroML


[MOOSE](https://moose.ncbs.res.in/) is the Multiscale Object-Oriented Simulation Environment. It is the base and numerical core for large, detailed multi-scale simulations that span computational neuroscience and systems biology. It is based on a complete reimplementation of the GENESIS 2 core.

Some tests of using MOOSE with NeuroML models and example code can be found in the [MOOSE Showcase](https://github.com/OpenSourceBrain/MOOSEShowcase) repository.


## Simulating NeuroML models in MOOSE


You can export NeuroML models to the MOOSE simulator format using {ref}`jNeuroML <jneuroml>` or {ref}`pyNeuroML <pyNeuroML>`, pointing at a {ref}`LEMS Simulation file <userdocs:lemssimulation>` describing what to simulate, and using the `-moose` option:

```{code-block} console
# Using jnml
jnml <LEMS simulation file> -moose

# Using pynml
pynml <LEMS simulation file> -moose
```
