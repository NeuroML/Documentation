(userdocs:simulators)=
# Simulating NeuroML Models

```{admonition} Work in progress
:class: note
This page is a work in progress. Please see
```

```{admonition} Validate NeuroML 2 files before using them.
:class: tip
It is good practice to {ref}`validate NeuroML 2 files <userdocs:validating_models>` to check them for correctness before simulating them.
```
(userdocs:simulating_models:osb)=
## Using Open Source Brain

Models that have already been converted to NeuroML and added to the [Open Source Brain](https://www.opensourcebrain.org/) platform can also be simulated there.


(userdocs:simulating_models:jlems)=
## Using jLEMS

jLEMS is the default implementation of LEMS, and can be used to simulate single compartment models written in NeuroML/LEMS.
It is included in both `jnml` and `pynml`, and can be used as shown:

```{code-block} console
# With jnml
jnml <LEMS simulation file>

# With pynml
pynml <LEMS simulation file>
```

You can also run LEMS simulations using jLEMS using the {ref}`pyNeuroML <pyneuroml>` API:

```{code-block} python
from pyneuroml.pynml import run_lems_with_jneuroml


...

run_lems_with_jneuroml(lems_file_name)
```

(userdocs:simulating_models:neuron)=
## Using NEURON

For more complex models that can not be simulated using jLEMS, we can use the NEURON simulator, also using `jnml` or `pynml`:

```{code-block} console
# With jnml
jnml <LEMS simulation file> -neuron -run

# Wity pynml
pynml -neuron -run <LEMS simulation file>
```

These commands generate a PyNeuron script and run it (a file ending in `_nrn.py`).
So you must have NEURON installed on your system, with its Python bindings (PyNeuron).
Skipping the `-run` flag will generate the Python script but will not run it: you can run it manually later.

You can also run LEMS simulations using the NEURON simulator using the {ref}`pyNeuroML <pyneuroml>` API:

```{code-block} python
from pyneuroml.pynml import run_lems_with_jneuroml_neuron


...

run_lems_with_jneuroml_neuron(lems_file_name)
```

(userdocs:simulating_models:netpyne)=
## Using NetPyNE

You can also generate and run [NetPyNE](https://netpyne.org) code from NeuroML.
To generate and run NetPyNE code, use `jnml`:

```{code-block} console
jnml -netpyne -run <LEMS simulation file>
```

The generated file name will end in `_netpyne.py`.

You can also run LEMS simulations using the NetPyNE simulator using the {ref}`pyNeuroML <pyneuroml>` API:

```{code-block} python
from pyneuroml.pynml import run_lems_with_jneuroml_netpyne


...

run_lems_with_jneuroml_netpyne(lems_file_name)
```

(userdocs:simulating_models:brian2)=
## Using Brian2

You can export single component NeuroML models to Python scripts for running them using the [Brian2](https://briansimulator.org) simulator:

```{code-block} console
# Using jnml
jnml <LEMS simulation file> -brian2

# Using pynml
pynml <LEMS simulation file> -brian
```

You can also run LEMS simulations using the Brian2 simulator using the {ref}`pyNeuroML <pyneuroml>` API:

```{code-block} python
from pyneuroml.pynml import run_lems_with_jneuroml_brian2


...

run_lems_with_jneuroml_brian2(lems_file_name)
```

(userdocs:simulating_models:moose)=
## Using MOOSE

You can export NeuroML models to the MOOSE simulator format using `jnml`:

```{code-block} console
# Using jnml
jnml <LEMS simulation file> -moose
```
