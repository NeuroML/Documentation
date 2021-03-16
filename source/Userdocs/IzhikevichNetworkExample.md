(userdocs:gettingstarted:izhikevichnetwork)=
# A two population network of regular spiking Izhikevich neurons

Now that we have defined a cell, let us see how a network of these cells may be declared and simulated.
We will create a small network of cells, simulate this network, and generate a plot of the spike times of the cells (a raster plot):


```{figure} ../Userdocs/NML2_examples/example_izhikevich2007network_sim-spikes.png
:alt: Spike times of neurons recorded from the simulation
:align: center

Spike times of neurons recorded from the simulation.
```

The Python script used to create the model, simulate it, and generate this plot is below:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
----
```
As with the previous example, we will step through this script to see how the various components of the network are declared in NeuroML before running the simulation and generating the plot.


(userdocs:gettingstarted:izhikevichnetwork:declaring)=
## Declaring the model in NeuroML

To declare the complete network model, we must again first declare its core entities:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 22-30
----
```
Here, we create a new document, declare the Izhikevich neuron, and also declare the synapse that we are going to use to connect one population of neurons to the other.
Here we intend to use the [ExpOne Synapse](https://www.neuroml.org/NeuroML2CoreTypes/Synapses.html#expOneSynapse), where the conductance of the synapse increases instantaneously by a constant value `gbase` on receiving a spike, and then decays exponentially with a decay constant `tauDecay`.
We can now declare our cell populations:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 32-41
----
```

Next, we create projections between the two populations based on some probability of connection.
To do this, we iterate over each post-synaptic neuron for each pre-synaptic neuron and draw a random number between 0 and 1.
If the drawn number is less than the required probability of connection, the connection is created.

While we are iterating over all our pre-synaptic cells here, we also add external inputs to them.
(This could have been done in a different loop, but it is convenient to also do this here.)
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 43-67
----
```
We can now save and validate our model, as before:


```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 69-73
----
```
### The generated NeuroML model

Let us take a look at the generated NeuroML model

```{literalinclude} ./NML2_examples/izhikevich2007_network.nml
----
language: xml
```

It is easy to see how the model is clearly declared in the NeuroML file.
Observe how entities are referenced in NeuroML depending on their location in the document architecture.
Here, `population` and `projection` are at the same level.
The synaptic connections using the `connection` tag are at the next level.
So, in the `connection` tags, populations are to be referred to as `../` which indicates the previous level.
The `explicitInput` tag is at the same level as the `population` and `projection` tags, so we do *not* need to use `../` here to reference them.

Another point worth noting here is that because we've defined a population of the same components by specifying a size rather than by individually adding components to it, we can refer to the entities of the population using the common `[..]` index operator.
<!-- TODO: why are the pulseGens not referred to as ../PulseGens? They're at the previous level too. Are they the top level and thus considered to be global? -->

The advantage of such a declarative format is that we can also easily get information on our model from the NeuroML file.
pyNeuroML includes the helper `pynml-summary` script:

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
*   9 connections in 1 projections
*     Projection: proj from IzPop0 to IzPop1, synapse: syn0
*       9 connections: [(Connection 0: 0 -> 0), ...]
*
*   0 inputs in 0 input lists
*
*******************************************************

```
<!-- TODO: Ask Padraig what's the difference between direct Synapses and projections, and when should they be used? -->

We can also generate a graphical summary of our model using `pynml`:
```{code-block} console
$ pynml izhikevich2007_network.nml -graph 2
neuromllite >>> Initiating GraphViz handler, level 2, engine: dot, seed: 1234
Parsing: izhikevich2007_network.nml
Loaded: izhikevich2007_network.nml as NeuroMLDocument
....
```

This generates the following model summary diagram:
```{figure} ../Userdocs/NML2_examples/IzNet.gv.png
:alt: Model summary graph generated using pynml and the dot tool.
:align: center
:scale: 50%

A summary graph of the model generated using pynml and the dot tool.
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
lines: 75-89
----
```
The generated LEMS file is here:

```{literalinclude} ./NML2_examples/LEMS_example_izhikevich2007network_sim.xml
----
language: xml
```

<!-- BUG in pynml needs fixing: https://github.com/NeuralEnsemble/libNeuroML/issues/91 -->
Where we had generated a graphical summary of the model before, we can now also generate graphical summaries of the simulation using `jnml`:
```{code-block} console
$ jnml LEMS_example_izhikevich2007network_sim.xml -graph
 jNeuroML v0.10.1
 (INFO) Reading from: .../NeuroML-Documentation/source/Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.xml
 (INFO) simCpt: Component(id=example_izhikevich2007network_sim type=Simulation)
 Writing to: .../NeuroML-Documentation/source/Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.gv
 Have successfully run command: dot -Tpng  .../NeuroML-Documentation/source/Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.gv -o .../NeuroML-Documentation/source/Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.png
```

Here is the generated summary graph:
```{figure} ../Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.png
:alt: Model summary graph generated using jnml.
:align: center
:scale: 50%

A summary graph of the model generated using jnml.
```
It shows a top-down breakdown of the simulation: from the network, to the populations, to the cell types, leading up to the components that these cells are made of (more on Components later).
Let us add the necessary code to run our simulation, this time using the well known NEURON simulator:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 91-93
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
lines: 95-104
----
```
Observe how we are using the same `generate_plot` utility function as before: it is general enough to plot different recorded quantities.
Under the hood, it passes this information to Python's Matplotlib library.


This concludes our second example.
Here, we have seen how to create, simulate, and record from a simple two population network of single compartment point neurons.
The next section is an interactive notebook that you can use to play with this example.
After that we will move on to the next example: a single but more detailed multi-compartmental neuron model.
