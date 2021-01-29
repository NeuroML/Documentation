# A two population network of regular spiking Izhikevich neurons

Now that we have defined a cell, let us see how a network of these cells may be declared and simulated.
We will create a small network of cells, simulate this network, and generate a plot of the spike times of the cells (a raster plot):


```{figure} ../Userdocs/NML2_examples/example-izhikevich2007network-sim-spikes.png
:alt: Spike times of neurons recorded from the simulation
:align: center

Spike times of neurons recorded from the simulation.
```

The Python script used to generate this plot is below:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
----
```
As with the previous example, we will step through this script to see how the various components of the network are declared in NeuroML before running the simulation and generating the plot.


## Declaring the model in NeuroML

To declare the complete network model, we must again first declare its core entities:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 22-30
----
```
Here, we create a new document, declare the Izhikevich neuron, and also declare the synapse that we are going to use to connect one population of neurons to the other.
Here are intend to use the [ExpOne Synapse](https://www.neuroml.org/NeuroML2CoreTypes/Synapses.html#expOneSynapse), where the conductance of the synapse increases instantaneously by a constant value `gbase` on receiving a spike, and then decays exponentially with a decay constant `tauDecay`.
Now we can declare our cell populations:
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 32-41
----
```
<!-- TODO: Ask Padraig what the projection format is: is it using [] or do we also use /../../../ here? -->

Next, we create projections between the two populations based on some probability of connection.
To do this, we iterate over each post-synaptic neuron for each pre-synaptic neuron and draw a random number between 0 and 1.
If the drawn number is less than the required probability of connection, the connection is created.

While we are iterating over all our pre-synaptic cells here, we also add external inputs to them.
(This could have been done in a different loop, but it is convenient to also do this here.)
```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 43-61
----
```
We can now save and validate our model, as before:


```{literalinclude} ./NML2_examples/izhikevich-network.py
----
language: python
lines: 63-67
----
```
### The generated NeuroML model

Let us take a look at the generated NeuroML model

```{literalinclude} ./NML2_examples/izhikevich2007_network.nml
----
language: xml
```

It is easy to see how the model is clearly declared in the NeuroML file.
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
*   0 connections in 0 projections
*
*   0 inputs in 0 input lists
*
*******************************************************
```

<!-- TODO: Ask Padraig why it isn't showing projections: likely something wrong in my script/NeuroML --->
<!-- TODO: Ask Padraig if it makes sense to visualise this network as png when the cells don't have locations: should I add locations? -->
