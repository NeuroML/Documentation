(userdocs:getting_started:single_comparment_example)=
# Simulating a single compartment Hodgkin-Huxley neuron

In this section we will model and simulate a Hodgkin-Huxley (HH) neuron ({cite}`Hodgkin1952`).
A Hodgkin-Huxley neuron includes Sodium (Na), Potassium (K), and leak ion channels.
For more information on this neuron model, please see [this tutorial](https://hodgkin-huxley-tutorial.readthedocs.io/en/latest/index.html).

```{figure} ../Userdocs/NML2_examples/HH_single_compartment_example_sim-v.png
:alt: Membrane potential for neuron recorded from the simulation
:align: center

Membrane potential of the simulated Hodgkin-Huxley neuron.
```
This plot, saved as `HH_single_compartment_example_sim-v.pn` is generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
----
```

## Declaring the model in NeuroML

Similar to previous examples, we will first declare the model, visualise it, and then simulate it.
The HH neuron model is more complex that the Izhikevich neuron model we have seen so far.
For example, it includes voltage-gated ion channels.
We will first implement these ion channels in NeuroML, then add them to a cell.
We will then create a network of one cell which will will stimulate with external input to record the membrane potential.

As you can also see in the script, since this is a slightly more complex model, we have modularised our code into different functions that carry out different tasks.
Let us now step through the script in a bottom-up fashion.
We start with the ion channels and build the network simulation.

### Declaring ion channels

Let us look at the definition of the Sodium (Na) channel in NeuroML:

```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 83-120
----
```
Here, we define the two gates, `m` and `h`, with their forward and reverse rates and add them to the channel.
Next, we create a NeuroML document and save this channel (only this channel that we've just defined) to a NeuroML file and validate it.
So we now have our Na channel defined in a separate NeuroML file that can be used in multiple models and shared:

```{literalinclude} ./NML2_examples/HH_example_na_channel.nml
----
language: xml
```

The various rate equations that can be used here are defined in the NeuroML {ref}`schema <schema:channels>`.

Also note that since we'll want to *include* this file in other NeuroML files, we make the function return the name of the file.
This is an implementation detail, and there are other ways of doing this too.
We could have hard-coded this in all our functions or defined it as a global variable in the script for example.
If we were using object-oriented programming, we could have created a class and stored this information as a class or object variable.

The K and leak channels are defined in a similar way:

```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 123-171
----
```
They are also saved in their own NeuroML files, which have also been validated.
The file for the K channel:
```{literalinclude} ./NML2_examples/HH_example_k_channel.nml
----
language: xml
```

For the leak channel:
```{literalinclude} ./NML2_examples/HH_example_leak_channel.nml
----
language: xml
```

### Declaring the cell

Now that we have declared our ion channels, we can start constructing our cell in a different function.
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 174-252
----
```
Let us walk through this function:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 180-186
----
```

First, before we do anything else, we create a new NeuroML document that we will use to save this cell.
Now, since the ion-channels were created in other files, we need to make this document aware of their declarations.
To do this, we *include* the other files into this one using the `IncludeType` construct.
Each document we want to include gets appended to the list of `includes` for the document.

Now we can proceed to building our cell using the {ref}`Cell NeuroML component type <schema:cell>`.
As the schema document shows, a `Cell` component has two children: {ref}`morphology <schema:morphology>`, and {ref}`biophysical properties <schema:biophysicalproperties>`.
Let us first look at setting up the biophysical properties:


```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 190-234
----
```

Biophysical properties are themselves split into two:
- the {ref}`membrane properties <schema:membraneproperties>`
- the {ref}`intracellular properties <schema:intracellularproperties>`

Let us look at membrane properties first.
The {ref}`schema <schema:membraneproperties>` shows that membrane properties has two *child* elements:

- {ref}`initMembPotential <schema:initmembpotential>`
- {ref}`spikeThresh <schema:spikethresh>`

and three *children* elements:

- {ref}`specificCapacitances <schema:specificcapacitance>`
- {ref}`populations <schema:basechannelpopulation>`
- {ref}`channelDensities <schema:basechanneldensity>`

<!---
TODO: what is the difference between child and children elements?
-->
The difference between *child* elements and *children* elements is that ...

```{admonition} Child elements vs Children elements
:class: tip
The difference between *child* elements and *children* elements is that...
```

So, we start with the ion-channels which are distributed along the membrane with some density.
We create new {ref}`ChannelDensity <schema:channeldensity>` objects for each of our defined ion-channels (Na, K, leak) and append these to the list of channel densities in the membrane properties.
For example, for the Na channels:

```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 202-206
----
```
and similarly for the K and leak channels.
Next, we add the other child and children elements: the `specificCapacitance`, the `spikeThreshold`, the `initMembPotential`.
This completes the membrane properties.
Similarly we add the intracellular properties next: {ref}`Resistivity <schema:resistivity>`.

Next, we add the {ref}`Morphology <schema:morphology>` related information for our cell.
Here, we are only creating a single compartment cell with only one segment.
We will look into multi-compartment cells with more segments in later examples:

```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 236-247
----
```
A {ref}`segment <schema:segment>` has `proximal` and `distal` child elements which describe the extent of the segment.
These are described using a {ref}`Point3DWithDiam <schema:point3dwithdiam>` object.


This completes our cell.
We add it to our NeuroML document, and save (and validate) it.
The resulting NeuroML file is:


```{literalinclude} ./NML2_examples/HH_example_cell.nml
----
language: xml
```

We now have our cell defined in a separate NeuroML file, that can be re-used and shared.

### Declaring the network

We now use our cell in a network.
A {ref}`network in NeuroML <schema:network>` has multiple children elements: `regions`, `populations`, `projections`, `synapticConnections`, `inputs` and so on.
Here we are going to only create a network with one cell, and an external input to the cell:


```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 255-282
----
```

We start in the same way, by creating a new NeuroML document and including our cell file into it.
We then create a {ref}`population <schema:population>` comprising of a single cell.
We create a {ref}`pulse generator <schema:pulsegenerator>` as an {ref}`explicit input <schema:explicitinput>`, which targets our population.
Note that as the schema documentation for `ExplicitInput` notes, any current source (any component that *extends* {ref}`basePointCurrent <schema:basepointcurrent>`) can be used as an `ExplicitInput`.

We add all of these to the {ref}`network <schema:network>` and save (and validate) our network file.
The NeuroML file generated is below:


```{literalinclude} ./NML2_examples/HH_example_net.nml
----
language: xml
```

### The generated NeuroML model

Before we look at simulating the model, we can inspect our model to check for correctness.
All our NeuroML files were validated when they were created already, so we do not need to run this step again.
However, if required, this can be easily done:

```{code-block} console
pynml -validate HH_*nml

```
Next, we can visualise our model using the information noted in the {ref}`visualising NeuroML models <userdocs:visualising_models>` page:

```{code-block} console
pynml-summary HH_example_net.nml
*******************************************************
* NeuroMLDocument: network
*
*  PulseGenerator: ['pg']
*
*  Network: single_hh_cell_network
*
*   1 cells in 1 populations
*     Population: pop0 with 1 components of type hh_cell
*
*   0 connections in 0 projections
*
*   0 inputs in 0 input lists
*
*   1 explicit inputs (outside of input lists)
*     Explicit Input of type pg to pop0(cell 0), destination: unspecified
*
*******************************************************
```

Since our model is a single compartment model with only one cell, it doesn't have any 3D structure to visualise.
We can check the connectivity graph of the model:

```{code-block} console
pynml -graph 10 HH_example_net.nml
```

which will give us this figure:
```{figure} ./NML2_examples/single_hh_cell_network.gv.png
:alt: Level 10 network graph generated by pynml
:align: center
:scale: 60 %

Level 10 network graph generated by pynml
```

#### Analysing channels

Finally, we can analyse the ion channels that we've declared using the `pynml-channelanalysis` utility:

```{code-block} console
pynml-channelanalysis HH_example_k_channel.nml

```
This generates graphs to show the behaviour of the channel:

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/HH_example_k_channel_2.png
:alt: Steady state behaviour of the K ion channel
:align: center
:scale: 60 %

Steady state behaviour of the K ion channel.
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>


```{figure} ./NML2_examples/HH_example_k_channel_1.png
:alt: Time course of the K ion channel
:align: center
:scale: 60 %

Time course of the K ion channel.
```

</center>

</div>
</div>
</div>

Similarly, we can get these for the Na channel also:
```{code-block} console
pynml-channelanalysis HH_example_na_channel.nml

```

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/HH_example_na_channel_2.png
:alt: Steady state behaviour of the Na ion channel
:align: center
:scale: 60 %

Steady state behaviour of the Na ion channel.
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>


```{figure} ./NML2_examples/HH_example_na_channel_1.png
:alt: Time course of the Na ion channel
:align: center
:scale: 60 %

Time course of the Na ion channel.
```

</center>

</div>
</div>
</div>

## Simulating the model

Now that we have declared our network model and all its components, we can simulate it.
We do this in the `main` function:

```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 34-62
----
```
