(userdocs:lemssimulation)=
# LEMS Simulation files

For many users, the most obvious place that LEMS is used is in the LEMS Simulation file (usually {ref}`LEMS_*.xml <userdocs:conventions:files>`).

In short, what a file like this does is:

- point at the NeuroML file containing the model to simulate
- include any other LEMS file it needs, including the {ref}`NeuroML core type definitions <userdocs:neuromlv2inlems>`
- specify how long to run the simulation for and the simulation timestep (dt)
- say what to display when the simulation has finished (e.g. membrane potentials of selected cells)
- say what to save to file, e.g. voltage traces, spike times

These files are criucial in many of the workflows for {ref}`simulating NeuroML models <userdocs:simulators>`.

## Specification of format

See {ref}`here <schema:simulation_>` for definition of the main elements used in the file, including {ref}`schema:display`,  {ref}`schema:outputfile`, etc.

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
