(userdocs:lemssimulation)=
# LEMS Simulation files

For many users, the most obvious place that LEMS is used is in the LEMS Simulation file (usually {ref}`LEMS_*.xml <userdocs:conventions:files>`).

## Specification of format

See <a href="Schemas/Simulation.html">here</a> for definition of the main elements used in the file, including {ref}`schema:display`,  {ref}`schema:outputfile`, etc.

## Quantities and paths

Specifying the quantities to save/display in a LEMS Simulation file is an important and sometimes confusing process. There is a {ref}`dedicated page <userdocs:quantitiesandrecording>` on quantities and paths in LEMS and NeuroML2.

## Creating LEMS Simulation files

Perhaps the easiest way to create a LEMS Simulation file is to base it off of an existing example.

```{literalinclude} ./NML2_examples/lems_sim/LEMS_SimulationExample.xml
----
language: xml
```

Alternatively, it is possible to create a LEMS Simulation file in Python file using pyNeuroML:

```{literalinclude} ./NML2_examples/lems_sim/create_lems.py
----
language: python
```

See [this example](https://github.com/NeuroML/pyNeuroML/blob/master/examples/create_new_lems_file.py) for more details.

## What about SED-ML?

The Simulation Experiment Description Markup Language ([SED-ML](https://sed-ml.org/)) is used by a number of other initiatives such as SBML for specifying simulation setup, execution and basic analysis.

We chose to have a LEMS specific format for specifying simulations in NeuroML2 as opposed to natively supporting SED-ML, mainly because of the tight link to the LEMS language and {ref}`jLEMS <jLEMS>` package, i.e. all of the NeuroML2 elements and elements in a LEMS simulation file have underlying definitions in the LEMS language. However it is possible to convert the LEMS simulation to the equivalent in SED-ML.

### Exporting LEMS simulation descriptions to SED-ML


```{code-block} console
# Using jnml
jnml <LEMS simulation file> -sedml

# Using pynml
pynml <LEMS simulation file> -sedml
```
