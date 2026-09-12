(userdocs:getting_started:single_compartment_example)=
# Simulating a single compartment Hodgkin-Huxley neuron

In this section we will model and simulate a Hodgkin-Huxley (HH) neuron ({cite}`Hodgkin1952`).
A Hodgkin-Huxley neuron includes Sodium (Na), Potassium (K), and leak ion channels.
For further information on this neuron model, please see [here](https://hodgkin-huxley-tutorial.readthedocs.io/en/latest/index.html).

```{figure} ../Userdocs/NML2_examples/HH_single_compartment_example_sim-v.png
:alt: Membrane potential for neuron recorded from the simulation
:align: center

Membrane potential of the simulated Hodgkin-Huxley neuron.
```
This plot, saved as `HH_single_compartment_example_sim-v.png` is generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
----
```
(userdocs:getting_started:single_compartment_example:model)=
## Declaring the model in NeuroML

Similar to previous examples, we will first declare the model, visualise it, and then simulate it.
The HH neuron model is more complex than the {ref}`Izhikevich neuron model <userdocs:getting_started:single_example>` we have seen so far.
For example, it includes voltage-gated ion channels.
We will first implement these ion channels in NeuroML, then add them to a cell.
We will then create a network of one cell which will will stimulate with external input to record the membrane potential.

As you can also see in the script, since this is a slightly more complex model, we have modularised our code into different functions that carry out different tasks.
Let us now step through the script in a bottom-up fashion.
We start with the ion channels and build the network simulation.

(userdocs:getting_started:single_compartment_example:model:channels)=
### Declaring ion channels

```{admonition} Note: you might not need to define your ion channels in Python every time....
In this example, all parts of the model, including the ion channels, are defined from scratch in Python and then NeuroML files in XML are generated and saved. For many modelling projects however, ion channel XML files will be reused from other models, and can just be included in the cells that use them with: `<include href="my_channel.nml"/>`. See {ref}` here <userdocs:finding_models>` for tips on where to find ion channel models in NeuroML.
```

Let us look at the definition of the Sodium (Na) channel in NeuroML:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 106-168
----
```
Here, we define the two gates, `m` and `h`, with their forward and reverse rates and add them to the channel.
Next, we create a NeuroML document and save this channel (only this channel that we've just defined) to a NeuroML file and validate it.
So we now have our Na channel defined in a separate NeuroML file that can be used in multiple models and shared:
```{literalinclude} ./NML2_examples/HH_example_na_channel.nml
----
language: xml
```
The various rate equations ({ref}`HHExpLinearRate <schema:HHExpLinearRate>`, {ref}`HHExpRate <schema:HHExpRate>`, {ref}`HHSigmoidRate <schema:HHSigmoidRate>` that can be used in the gate (here {ref}`gateHHrates <schema:gateHHrates>`, but other forms such as {ref}`gateHHtauInf <schema:gateHHtauInf>` and {ref}`gateHHInstantaneous <schema:gateHHInstantaneous>` can be used) are defined in the NeuroML {ref}`schema <schema:channels_>`.

Also note that since we'll want to *include* this file in other NeuroML files, we make the function return the name of the file.
This is an implementation detail, and there are other ways of doing this too.
We could have hard-coded this in all our functions or defined it as a global variable in the script for example.
If we were using object-oriented programming, we could have created a class and stored this information as a class or object variable.

The K and leak channels are defined in a similar way:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 171-245
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
(userdocs:getting_started:single_compartment_example:model:cell)=
### Declaring the cell

Now that we have declared our ion channels, we can start constructing our {ref}`cell <schema:cell>` in a different function.
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 247-318
----
```
Let us walk through this function:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 161-168
----
```
We start by creating a new NeuroML document that we will use to save this cell, and adding the cell to it.

A {ref}`Cell <schema:cell>` component has a number of child/children components that we need to now populate:
```{code-block} pycon
Cell -- Cell with  **segment** s specified in a  **morphology**  element along with details on its  **biophysicalProperties** . NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v**  of this cell represents the membrane potential in that isopotential segment.

Please see the NeuroML standard schema documentation at https://docs.neuroml.org/Userdocs/NeuroMLv2.html for more information.

Valid members for Cell are:
* morphology_attr (class: NmlId, Optional)
* biophysical_properties_attr (class: NmlId, Optional)
* morphology (class: Morphology, Optional)
        * Contents ('ids'/<objects>): 'morphology'

* neuro_lex_id (class: NeuroLexId, Optional)
* metaid (class: MetaId, Optional)
* biophysical_properties (class: BiophysicalProperties, Optional)
        * Contents ('ids'/<objects>): 'biophys'

* id (class: NmlId, Required)
        * Contents ('ids'/<objects>): hh_cell

* notes (class: xs:string, Optional)
        * Contents ('ids'/<objects>): A single compartment HH cell

* properties (class: Property, Optional)
* annotation (class: Annotation, Optional)
```
We can see that the {ref}`morphology <schema:morphology>` and {ref}`biophysical properties <schema:biophysicalproperties>` components have already been initialised for us.
We now need to add the required components to them.

We begin with the biophysical properties.
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
```{admonition} Child elements vs Children elements
:class: tip
When an element specifies a **Child** subelement, it will only have one of these present (it could have zero). **Children** explicitly says that there can be zero, one or many subelements.
```

So, we start with the ion-channels which are distributed along the membrane with some density.
A number of helpful functions are available to us: `add_channel_density`, `add_membrane_property`, `set_specific_capacitance`, `set_init_memb_potential`:
For example, for the Na channels:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 262-271
----
```
and similarly for the K and leak channels.
Now, since the ion-channels were created in other files, we need to make this document aware of their declarations.
To do this, reference the other files in the `ion_chan_def_file` argument of the `add_channel_density` method.
Under the hood, this will `include` the ion channel definition file we have created in this cell document using an `IncludeType` component.
Each document we want to include gets appended to the list of `includes` for the document.

Next, we add the other child and children elements: the {ref}`Specific Capacitance <schema:specificcapacitance>`, the {ref}`Spike Threshold <schema:spikethresh>`, the {ref}`InitMembPotential <schema:initmembpotential>`.
This completes the membrane properties.
We then add the intracellular properties next: {ref}`Resistivity <schema:resistivity>`.
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 294-299
----
```
Next, we add the {ref}`Morphology <schema:morphology>` related information for our cell.
Here, we are only creating a single compartment cell with only one segment.
We will look into multi-compartment cells with more segments in later examples:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 303-311
----
```
A {ref}`segment <schema:segment>` has `proximal` and `distal` child elements which describe the extent of the segment.
These are described using a {ref}`Point3DWithDiam <schema:point3dwithdiam>` object, which the `add_segment` function creates for us.


This completes our cell.
We add it to our NeuroML document, and save (and validate) it.
The resulting NeuroML file is:
```{literalinclude} ./NML2_examples/HH_example_cell.nml
----
language: xml
```
We now have our cell defined in a separate NeuroML file, that can be re-used and shared.

(userdocs:getting_started:single_compartment_example:model:network)=
### Declaring the network

We now use our cell in a network.
A {ref}`network in NeuroML <schema:network>` has multiple children elements: {ref}`populations <schema:population>`, {ref}`projections <schema:projection>`, {ref}`inputLists <schema:inputList>` and so on.
Here we are going to only create a network with one cell, and an {ref}`explicit input <schema:explicitinput>` to the cell:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 320-358
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
(userdocs:getting_started:single_compartment_example:model:generatedmodel)=
### The generated NeuroML model

Before we look at simulating the model, we can inspect our model to check for correctness.
All our NeuroML files were validated when they were created already, so we do not need to run this step again.
However, if required, this can be easily done:
```{code-block} console
pynml -validate HH_*nml
```
Next, we can visualise our model using the information noted in the {ref}`visualising NeuroML models <userdocs:visualising_models>` page (including the `-v` verbose option for more information on the cell):
```{code-block} console
pynml-summary HH_example_net.nml -v
*******************************************************
* NeuroMLDocument: network
*
*  IonChannelHH: ['k_channel', 'leak_channel', 'na_channel']
*  PulseGenerator: ['pg']
*
*  Cell: hh_cell
*    <Segment|0|soma>
*      Parent segment: None (root segment)
*      (0.0, 0.0, 0.0), diam 17.841241161527712um -> (0.0, 0.0, 0.0), diam 17.841241161527712um; seg length: 0.0 um
*      Surface area: 1000.0 um2, volume: 2973.5401935879518 um3
*    Total length of 1 segment: 0.0 um; total area: 1000.0 um2
*
*    Channel density: na_channels on all;       conductance of 120.0 mS_per_cm2 through ion chan na_channel with ion na, erev: 50.0 mV
*      Channel is on <Segment|0|soma>,  total conductance: 1200.0 S_per_m2 x 1e-09 m2 = 1.2000000000000002e-06 S (1200000.0000000002 pS)
*    Channel density: k_channels on all;        conductance of 360 S_per_m2 through ion chan k_channel with ion k, erev: -77mV
*      Channel is on <Segment|0|soma>,  total conductance: 360.0 S_per_m2 x 1e-09 m2 = 3.6000000000000005e-07 S (360000.00000000006 pS)
*    Channel density: leak_channels on all;     conductance of 3.0 S_per_m2 through ion chan leak_channel with ion non_specific, erev: -54.3mV
*      Channel is on <Segment|0|soma>,  total conductance: 3.0 S_per_m2 x 1e-09 m2 = 3.0000000000000004e-09 S (3000.0000000000005 pS)
*
*    Specific capacitance on all: 1.0 uF_per_cm2
*      Capacitance of <Segment|0|soma>, total capacitance: 0.01 F_per_m2 x 1e-09 m2 = 1.0000000000000001e-11 F (10.000000000000002 pF)
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
(userdocs:getting_started:single_compartment_example:model:generatedmodel:analysingchannels)=
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

(userdocs:getting_started:single_compartment_example:simulating)=
## Simulating the model

Now that we have declared and inspected our network model and all its components, we can proceed to simulate it.
We do this in the `main` function:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 22-63
----
```
Here we first create a `LEMSSimulation` instance and include our network NeuroML file in it.
We must inform LEMS what the target of the simulation is.
In our case, it's the id of our network, `single_hh_cell_network`:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 29-36
----
```
We also want to record some information, so we create an output file first with an `id` of `output0`:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 39
----
```
Now, we can record any quantity that is exposed by NeuroML (any `exposure`).
For example, we add a column for the membrane potential `v` of the {ref}`cell <schema:cell>` which would be the *0th* (and only) cell in our population `pop0`: `pop0[0]/v`.
We can also record the current in the channels: `pop[0]/iChannels`
We can also record the {ref}`current density <schema:channeldensity>` `iDensity` for the channels, so we also record these.
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 40-55
----
```
We then save the LEMS simulation file, run our simulation with the default {ref}`jNeuroML <jneuroml>` simulator.

(userdocs:getting_started:single_compartment_example:plotting)=
## Plotting the recorded variables

To plot the variables that we recorded, we read the data and use the `generate_plot` utility function:
```{literalinclude} ./NML2_examples/hh-single-compartment.py
----
language: python
lines: 66-103
----
```
This generates the following graphs:

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/HH_single_compartment_example_sim-v.png
:alt: Membrane potential
:align: center
:scale: 60 %

Membrane potential
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/HH_single_compartment_example_sim-i.png
:alt: Channel current
:align: center
:scale: 60 %

Channel current.
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/HH_single_compartment_example_sim-iden.png
:alt: Channel current densities
:align: center
:scale: 60 %

Channel current densities
```

</center>

</div>
</div>
</div>


This concludes out third example.
Here we have seen how to create, simulate, record, and visualise a single compartment Hodgkin-Huxley neuron.
In the next section, you will find an interactive notebook where you can play with this example.
