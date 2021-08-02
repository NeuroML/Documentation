(userdocs:lemssimulation)=
# LEMS Simulation files

For many users, the most obvious place that LEMS is used is in the LEMS Simulation file (usually LEMS_*.xml).

## Specification of format

See <a href="Schemas/Simulation.html">here</a> for definition of the main elements used in the file, including {ref}`schema:display`,  {ref}`schema:outputfile`, etc.


## Quantities and paths

Specifying the quantities to save/display in a LEMS Simulation file is an important and sometimes confusing process. There is a {ref}`dedicated page <userdocs:quantitiesandrecording>` on quantities and paths in LEMS and NeuroML2.


## What about SED-ML?

The Simulation Experiment Description Markup Language ([SED-ML](https://sed-ml.org/)) is used by a number of other initiatives such as SBML for specifying simulation setup, execution and basic analysis.

### Exporting LEMS simulation descriptions to SED-ML


```{code-block} console
# Using jnml
jnml <LEMS simulation file> -sedml

# Using pynml
pynml <LEMS simulation file> -sedml
```
