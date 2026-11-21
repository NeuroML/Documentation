(userdocs:gettingstarted:izhikevichnetwork)=
# A two population network of regular spiking Izhikevich neurons

Now that we have defined a cell, let us see how a network of these cells may be declared and simulated.
We will create a small network of cells, simulate this network, and generate a plot of the spike times of the cells (a raster plot):


```{figure} ../Userdocs/NML2_examples/example_izhikevich2007network_sim-spikes.png
:alt: Spike times of neurons recorded from the simulation
:align: center

Spike times of neurons in 2 populations recorded from the simulation.
```

The Python script used to create the model, simulate it, and generate this plot is below.
Please note that this example uses the {ref}`NEURON <userdocs:neuron>` simulator to simulate the model.
Please ensure that the `NEURON_HOME` environment variable is correctly set as noted {ref}`here <userdocs:neuron:envvar>`.

```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
----
```
As with the previous example, we will step through this script to see how the various components of the network are declared in NeuroML before running the simulation and generating the plot.
We will use the same helper functions to inspect the model as we build it: `component_factory`, `add`, `info`, `summary`.


(userdocs:gettingstarted:izhikevichnetwork:declaring)=
## Declaring the model in NeuroML

To declare the complete network model, we must again first declare its core entities:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 15-37
----
```
Here, we create a new document, declare the {ref}`Izhikevich neuron<schema:izhikevich2007Cell>`, and also declare the synapse that we are going to use to connect one population of neurons to the other.
We use the {ref}`ExpOne Synapse<schema:exponesynapse>` here, where the conductance of the synapse increases instantaneously by a constant value `gbase` on receiving a spike, and then decays exponentially with a decay constant `tauDecay`.

Let's inspect our model document so far:
```
nml_doc.info(True)
Please see the NeuroML standard schema documentation at https://docs.neuroml.org/Userdocs/NeuroMLv2.html for more information.

Valid members for NeuroMLDocument are:
...
* izhikevich2007_cells (class: Izhikevich2007Cell, Optional)
        * Contents ('ids'/<objects>): ['iz2007RS0']

* ad_ex_ia_f_cells (class: AdExIaFCell, Optional)
* fitz_hugh_nagumo_cells (class: FitzHughNagumoCell, Optional)
* fitz_hugh_nagumo1969_cells (class: FitzHughNagumo1969Cell, Optional)
* pinsky_rinzel_ca3_cells (class: PinskyRinzelCA3Cell, Optional)
* pulse_generators (class: PulseGenerator, Optional)
* pulse_generator_dls (class: PulseGeneratorDL, Optional)
* id (class: NmlId, Required)
        * Contents ('ids'/<objects>): IzNet

* sine_generators (class: SineGenerator, Optional)
...
* IF_curr_exp (class: IF_curr_exp, Optional)
* exp_one_synapses (class: ExpOneSynapse, Optional)
        * Contents ('ids'/<objects>): ['syn0']

* IF_cond_alpha (class: IF_cond_alpha, Optional)
* exp_two_synapses (class: ExpTwoSynapse, Optional)
...
```
Let's also get a summary:
```
print(nml_doc.summary())
*******************************************************
* NeuroMLDocument: IzNet
*
*  ExpOneSynapse: ['syn0']
*  Izhikevich2007Cell: ['iz2007RS0']
*
*******************************************************
```

We can now declare our {ref}`network <schema:network>` with 2 {ref}`populations <schema:population>` of these cells.
Note: setting a color as a  {ref}`property <schema:property>` is optional, but is used in when we generate our plots below.
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 43-57
----
```

We can test to see if the network is now valid, since we have added the required populations to it:
```
net.validate()
```
This function does not return anything if the component is valid.
If it is invalid, however, it will throw a `ValueError`.

We can now create {ref}`projections <schema:projection>` between the two populations based on some probability of connection.
To do this, we iterate over each post-synaptic neuron for each pre-synaptic neuron and draw a random number between 0 and 1.
If the drawn number is less than the required probability of connection, the connection is created.

While we are iterating over all our pre-synaptic cells here, we also add external inputs to them using {ref}`ExplicitInputs <schema:explicitinput>`
(this could have been done in a different loop, but it is convenient to also do this here).
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 62-101
----
```

Let us inspect our model again to confirm that we have it set up correctly.
```
nml_doc.info(True)
Please see the NeuroML standard schema documentation at https://docs.neuroml.org/Userdocs/NeuroMLv2.html for more information.

Valid members for NeuroMLDocument are:
* biophysical_properties (class: BiophysicalProperties, Optional)
* SpikeSourcePoisson (class: SpikeSourcePoisson, Optional)
* cells (class: Cell, Optional)
* networks (class: Network, Optional)
        * Contents ('ids'/<objects>): ['IzNet']

* cell2_ca_poolses (class: Cell2CaPools, Optional)
...
* izhikevich2007_cells (class: Izhikevich2007Cell, Optional)
        * Contents ('ids'/<objects>): ['iz2007RS0']

* ad_ex_ia_f_cells (class: AdExIaFCell, Optional)
* fitz_hugh_nagumo_cells (class: FitzHughNagumoCell, Optional)
* fitz_hugh_nagumo1969_cells (class: FitzHughNagumo1969Cell, Optional)
* pinsky_rinzel_ca3_cells (class: PinskyRinzelCA3Cell, Optional)
* pulse_generators (class: PulseGenerator, Optional)
        * Contents ('ids'/<objects>): ['pg_0', 'pg_1', 'pg_2', 'pg_3', 'pg_4']

* pulse_generator_dls (class: PulseGeneratorDL, Optional)
* id (class: NmlId, Required)
        * Contents ('ids'/<objects>): IzNet

...
* exp_one_synapses (class: ExpOneSynapse, Optional)
        * Contents ('ids'/<objects>): ['syn0']

* IF_cond_alpha (class: IF_cond_alpha, Optional)
..


print(nml_doc.summary())
*******************************************************
* NeuroMLDocument: IzNet
*
*  ExpOneSynapse: ['syn0']
*  Izhikevich2007Cell: ['iz2007RS0']
*  PulseGenerator: ['pg_0', 'pg_1', 'pg_2', 'pg_3', 'pg_4']
*
*  Network: IzNet
*
*   10 cells in 2 populations
*     Population: IzPop0 with 5 components of type iz2007RS0
*       Properties: color=0 0 .8;
*     Population: IzPop1 with 5 components of type iz2007RS0
*       Properties: color=.8 0 0;
*
*   20 connections in 1 projections
*     Projection: proj from IzPop0 to IzPop1, synapse: syn0
*       20 connections: [(Connection 0: 0 -> 0), ...]
*
*   0 inputs in 0 input lists
*
*   5 explicit inputs (outside of input lists)
*     Explicit Input of type pg_0 to IzPop0(cell 0), destination: unspecified
*     Explicit Input of type pg_1 to IzPop0(cell 1), destination: unspecified
*     Explicit Input of type pg_2 to IzPop0(cell 2), destination: unspecified
*     Explicit Input of type pg_3 to IzPop0(cell 3), destination: unspecified
*     Explicit Input of type pg_4 to IzPop0(cell 4), destination: unspecified
*
*******************************************************

```
We can now save and validate our model.
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 105-110
----
```
### The generated NeuroML model

Let us take a look at the generated NeuroML model

```{literalinclude} ./NML2_examples/izhikevich2007_network.nml
----
language: xml
```

It should now be easy to see how the model is clearly declared in the NeuroML file.
Observe how entities are referenced in NeuroML depending on their location in the document architecture.
Here, {ref}`population <schema:population>` and {ref}`projection <schema:projection>` are at the same level.
The synaptic connections using the {ref}`connection <schema:connection>` tag are at the next level.
So, in the {ref}`connection <schema:connection>` tags, populations are to be referred to as `../` which indicates the previous level.
The {ref}`explicitinput <schema:explicitinput>` tag is at the same level as the {ref}`population <schema:population>` and {ref}`projection <schema:projection>` tags, so we do *not* need to use `../` here to reference them.

Another point worth noting here is that because we have defined a population of the same components by specifying a size rather than by individually adding components to it, we can refer to the entities of the population using the common `[..]` index operator.
<!-- TODO: why are the pulseGens not referred to as ../PulseGens? They're at the previous level too. Are they the top level and thus considered to be global? -->

The advantage of such a declarative format is that we can also easily get information on our model from the NeuroML file.
Similar to the `summary()` function that we have used so far, {ref}`pyNeuroML <pyNeuroML>` also includes the helper `pynml-summary` script that can be used to get summaries of NeuroML models from their NeuroML files:
```{code-block} console
$ pynml-summary izhikevich2007_network.nml
*******************************************************
* NeuroMLDocument: IzNet
*
*   ExpOneSynapse: ['syn0']
*   Izhikevich2007Cell: ['iz2007RS0']
*   PulseGenerator: ['pulseGen_0', 'pulseGen_1', 'pulseGen_2', 'pulseGen_3', 'pulseGen_4']
*
*  Network: IzNet
*
*   10 cells in 2 populations
*     Population: IzPop0 with 5 components of type iz2007RS0
*     Population: IzPop1 with 5 components of type iz2007RS0
*
*   20 connections in 1 projections
*     Projection: proj from IzPop0 to IzPop1, synapse: syn0
*       20 connections: [(Connection 0: 0 -> 0), ...]
*
*   0 inputs in 0 input lists
*
*   5 explicit inputs (outside of input lists)
*     Explicit Input of type pulseGen_0 to IzPop0(cell 0), destination: unspecified
*     Explicit Input of type pulseGen_1 to IzPop0(cell 1), destination: unspecified
*     Explicit Input of type pulseGen_2 to IzPop0(cell 2), destination: unspecified
*     Explicit Input of type pulseGen_3 to IzPop0(cell 3), destination: unspecified
*     Explicit Input of type pulseGen_4 to IzPop0(cell 4), destination: unspecified
*
*******************************************************

```
<!-- TODO: Ask Padraig what's the difference between direct Synapses and projections, and when should they be used? -->

We can also generate a graphical summary of our model using `pynml` from {ref}`pyNeuroML <pyNeuroML>`:
```{code-block} console
$ pynml izhikevich2007_network.nml -graph 3
```
This generates the following model summary diagram:
```{figure} ../Userdocs/NML2_examples/IzNet.gv.png
:alt: Model summary graph generated using pynml and the dot tool.
:align: center
:scale: 50%

A summary graph of the model generated using pynml and the dot tool.
```
Other options for `pynml` produce other views, e.g individual connections:
```{code-block} console
$ pynml izhikevich2007_network.nml -graph -1
```

```{figure} ../Userdocs/NML2_examples/IzNet-1.gv.png
:alt: Model summary graph showing individual connections between cells in the populations.
:align: center
:scale: 70%

Model summary graph showing individual connections between cells in the populations.
```
In our very simple network here, neurons do not have morphologies and are not distributed in space.
In later examples, however, we will also see how summary figures of the network that show the morphologies, locations of different layers and neurons, and so on can also be generated using the NeuroML tools.

(userdocs:gettingstarted:izhikevichnetwork:simulating)=
## Simulating the model

Now that we have our model set up, we can proceed to simulating it.
We create our simulation, and setup the information we want to record from it.
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 112-137
----
```
The generated LEMS file is here:
```{literalinclude} ./NML2_examples/LEMS_example_izhikevich2007network_sim.xml
----
language: xml
```
<!-- BUG in pynml needs fixing: https://github.com/NeuralEnsemble/libNeuroML/issues/91 -->
Where we had generated a graphical summary of the model before, we can now also generate graphical summaries of the simulation using `pynml` and the `-lems-graph` option. This dives deeper into the LEMS definition of the cells, showing more of the underlying dynamics of the components:
```{code-block} console
$ pynml LEMS_example_izhikevich2007network_sim.xml -lems-graph
```
Here is the generated summary graph:
```{figure} ../Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.png
:alt: Model summary graph generated using pynml.
:align: center
:scale: 50%

A summary graph of the model generated using pynml -lems-graph.
```
It shows a top-down breakdown of the simulation: from the network, to the populations, to the cell types, leading up to the components that these cells are made of (more on Components later).
Let us add the necessary code to run our simulation, this time using the well known NEURON simulator:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 138-141
----
```
(userdocs:gettingstarted:izhikevichnetwork:plotting)=
## Plotting recorded spike times
To analyse the outputs from the simulation, we can again plot the information we recorded.
In the previous example, we had recorded and plotted the membrane potentials from our cell.
Here, we have recorded the spike times.
So let us plot them to generate our figure:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 143-162
----
```
Observe how we are using the same `generate_plot` utility function as before: it is general enough to plot different recorded quantities.
Under the hood, it passes this information to Python's Matplotlib library. This produces the raster plot shown at the top of the page.

This concludes our second example.
Here, we have seen how to create, simulate, and record from a simple two population network of single compartment point neurons.
The next section is an interactive notebook that you can use to play with this example.
After that we will move on to the next example: a neuron model using Hodgkin Huxley style ion channels.
