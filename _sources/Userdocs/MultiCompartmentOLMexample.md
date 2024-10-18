(userdocs:getting_started:multi_compartment_example)=
# Simulating a multi compartment OLM neuron

In this section we will model and simulate a multi-compartment Oriens-lacunosum moleculare (OLM) interneuron cell from the rodent hippocampal CA1 network model developed by Bezaire et al. ({cite}`Bezaire2016`).
The complete network model can be seen [here on GitHub](https://github.com/mbezaire/ca1), and [here on Open Source Brain](https://www.opensourcebrain.org/projects/nc_ca1).

```{figure} ../Userdocs/NML2_examples/olm.cell.xy.png
:alt: Morphology of constructed OLM cell in xy plane
:align: center
:width: 50%

Morphology of OLM cell in xy plane
```
```{figure} ../Userdocs/NML2_examples/olm_example_sim_seg0_soma0-v.png
:alt: Membrane potential for neuron recorded from the simulation at the soma
:align: center
:width: 50%

Membrane potential of the simulated OLM cell at the soma.
```
This plot, saved as `olm_example_sim_seg0_soma0-v.png` is generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
----
```
## Declaring the model in NeuroML

Similar to previous examples, we will first declare the model, visualise it, and then simulate it.
The OLM model is slightly more complex than the HH neuron model we had worked with in the {ref}`previous tutorial <userdocs:getting_started:single_compartment_example>` since it includes multiple compartments.
However, where we had declared the ion-channels ourselves in the previous example, here will will not do so.
We will *include* channels that have been pre-defined in NeuroML to demonstrate how components defined in NeuroML can be easily re-used in models.

We will follow the same method as before.
We will first define the cell, create a network with one instance of the cell, and then simulate it to record and plot the membrane potential from different segments.

### Declaring the cell

To keep our Python script modularised, we start constructing our {ref}`cell <schema:cell>` in a separate function.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 111-290
----
```
Let us walk through this function:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 116-123
----
```
We create a new model document that will hold the cell model.
Then, we create and add a new {ref}`Cell <schema:cell>` using the `add` method to the document.
We also provide a `neuro_lex_id` here, which is the [NeuroLex ontology identifier](https://scicrunch.org/scicrunch/interlex/view/ilx_0105030?searchTerm=oriens-lacunosum%20moleculare).
This allows us to better connect models to biological concepts.

As we have seen in the {ref}`single Izhikevich neuron example <userdocs:getting_started:single_example:supplementary:add>`, the `add` method calls the `component_factory` to create the component object for us.
For the `Cell` component type, it does a number of extra things for us to set up, or initialise, the cell.

We have a number of ways of inspecting the cell.
The `summary` function provides a very short summary of the cell.
This is useful to quickly get a high level overview of it:
```pycon
>>> cell.summary()
*******************************************************
* Cell: olm
* Notes: None
* Segments: 0
* SegmentGroups: 4
*******************************************************
```
We can also use the general {ref}`info function <userdocs:getting_started:single_example:supplementary:info>` to inspect the cell:
```pycon
>>> cell.info(show_contents=True)
Cell -- Cell with  **segment** s specified in a  **morphology**  element along with details on its  **biophysicalProperties** . NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v**  of this cell represents the membrane potential in that isopotential segment.

Please see the NeuroML standard schema documentation at https://docs.neuroml.org/Userdocs/NeuroMLv2.html for more information.

Valid members for Cell are:
* biophysical_properties_attr (class: NmlId, Optional)
* morphology (class: Morphology, Optional)
        * Contents ('ids'/<objects>): 'morphology'

* neuro_lex_id (class: NeuroLexId, Optional)
        * Contents ('ids'/<objects>): NLXCELL:091206

* metaid (class: MetaId, Optional)
* biophysical_properties (class: BiophysicalProperties, Optional)
        * Contents ('ids'/<objects>): 'biophys'

* id (class: NmlId, Required)
        * Contents ('ids'/<objects>): olm

* notes (class: xs:string, Optional)
* properties (class: Property, Optional)
* annotation (class: Annotation, Optional)
* morphology_attr (class: NmlId, Optional)

```

We see the cell already contains `biophysical_properties` or `morphology`.
Because these are components of the cell that are expected to be used, these were added automatically for us when the new component was created.

Let us take a look at the morphology of the cell:
```pycon
>>> cell.morphology.info(show_contents=True)
Morphology -- The collection of  **segment** s which specify the 3D structure of the cell, along with a number of  **segmentGroup** s

Please see the NeuroML standard schema documentation at https://docs.neuroml.org/Userdocs/NeuroMLv2.html for more information.

Valid members for Morphology are:
* segments (class: Segment, Required)
* metaid (class: MetaId, Optional)
* segment_groups (class: SegmentGroup, Optional)
        * Contents ('ids'/<objects>): ['all', 'soma_group', 'axon_group', 'dendrite_group']

* id (class: NmlId, Required)
        * Contents ('ids'/<objects>): morphology

* notes (class: xs:string, Optional)
* properties (class: Property, Optional)
* annotation (class: Annotation, Optional)
```

We see that there are no segments in the cell because we have not added any.
However, there are already a number of "default" segment groups that were automatically added for us: `all`, `soma_group`, `axon_group`, `dendrite_group`.
These groups allow us to keep track of all the segments, and of the segments forming the soma, the axon, and the dendrites of the cell respectively.
Take a look at the {ref}`conventions page <userdocs:conventions:segments>` for more information on these.

We now have an empty cell.
Since we are building a multi-compartmental cell, we now proceed to define the detailed morphology of the cell.
We do this by adding {ref}`segments <schema:segment>` and grouping them in to {ref}`segment groups <schema:segmentgroup>`.
We can add segments using the `add_segment` utility function, as we do for the segments forming the soma.
Here, our soma has two segments.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 123-142
----
```
The utility function takes the dimensions of the segment---it's {ref}`proximal <schema:proximal>` and {ref}`distal <schema:distal>` co-ordinates and the diameter to create a segment of the provided name.
Additionally, since segments need to be contiguous, it makes the first segment the *parent* of the second, to build a chain.
Finally, it places the segment into the specified segment group and the default groups that we also have and adds the segment to the cell's morphology.

Note that by default, the `add_segment` function does not know if the segments are contiguous, i.e., that they form an unbranched branch of the cell.
We could have added segments here that do not line up in a chain, when building different parts of a cell for example.
In this case, we know that the two soma segments must be contiguous, and that they are on the same unbranched branch (i.e. a continuous section without any branching points on it), so we create an unbranched segment group first using the `add_unbranched_segment_group`.

If we were only creating cell morphologies, this would not not matter much.
Even if the two segments were not included in a group of unbranched segments, they would still be connected.
However, for simulation, simulators such as NEURON need to know which parts of the cell form unbranched sections so that they can apply the [cable equation](https://en.wikipedia.org/wiki/Cable_theory#Deriving_the_cable_equation) and break them into smaller segments to simulate the electric current through them.
(See {cite}`Crook2007` for more information on how different simulators simulate cells with detailed morphologies.)

Next, we can call the same functions multiple times to add soma, dendritic, and axonal segments to our cell but this can get quite lengthy.
To easily add unbranched contiguous lists of segments to the cell, we can directly use the `add_unbranched_segments` utility function.
Here we use it to create an axonal segment group, and two dendritic groups each with two segments.
The first point we provide is the proximal (starting) of the dendrite.
The next two points are the distal (ends) of each segment forming the section.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 144-183
----
```
We repeat this process to create more dendritic and axonal sections of contiguous segments.

Finally, we add an extra colour property to the three primary segment groups that can be used when generating morphology graphs:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 185-193
----
```

We have now completed adding the morphological information to our cell.
Next, we proceed to our {ref}`biophysical properties <schema:biophysicalproperties>`, e.g.:
- the {ref}`membrane properties <schema:membraneproperties>`
  - {ref}`spike threshold <schema:spikethresh>`
  - {ref}`initial membrane potential <schema:initmembpotential>`
  - {ref}`channel densities <schema:basechanneldensity>`
  - {ref}`specifc capacitances <schema:specificcapacitance>`
- the {ref}`intracellular properties <schema:intracellularproperties>`
  - {ref}`resistivity <schema:resistivity>`

We use more helpful utility functions to set these values
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 195-198
----
```
For setting channel densities, we have the `add_channel_density` function:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 200-289
----
```
Note that we are not writing our channel files from scratch here.
We are re-using already written NeuroML channel definitions by simply including their NeuroML definition files.

This completes the definition of our cell.
We now run the level one validation, write it to a file while also running a complete (level one and level two) validation using pyNeuroML.
We also generate the morphology plot shown on the top of this page.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 291-294
----
```
The resulting NeuroML file is:
```{literalinclude} ./NML2_examples/olm.cell.nml
----
language: xml
```
We can now already inspect our cell using the NeuroML tools.
We have already generated the morphology plot in our script, but we can also do it using `pynml`:
```{code-block} console
pynml -png olm.cell.png
...
pyNeuroML >>> Writing to: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/source/Userdocs/NML2_examples/olm.cell.png
```
This gives us a figure of the morphology of our cell, similar to the one we've already generated:
```{figure} ../Userdocs/NML2_examples/olm.cell.png
:alt: Figure showing the morphology of the OLM cell generated from the NeuroML definition.
:align: center

Figure showing the morphology of the OLM cell generated from the NeuroML definition.
```
### Declaring the network

We now use our cell in a network.
Similar to our previous example, we are going to only create a network with one cell, and an {ref}`explicit input <schema:explicitinput>` to the cell:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 87-109
----
```
We start in the same way, by creating a new NeuroML document and including our cell file into it.
We then create a {ref}`population <schema:population>` comprising of a single cell.
We create a {ref}`pulse generator <schema:pulsegenerator>` as an {ref}`explicit input <schema:explicitinput>`, which targets our population.
Note that as the schema documentation for `ExplicitInput` notes, any current source (any component that *extends* {ref}`basePointCurrent <schema:basepointcurrent>`) can be used as an `ExplicitInput`.

We add all of these to the {ref}`network <schema:network>` and save (and validate) our network file.
The NeuroML file generated is below:
```{literalinclude} ./NML2_examples/olm_example_net.nml
----
language: xml
```
### The generated NeuroML model

Before we look at simulating the model, we can inspect our model to check for correctness.
All our NeuroML files were validated when they were created already, so we do not need to run this step again.
However, if required, this can be easily done:
```{code-block} console
pynml -validate olm*nml
```
Next, we can visualise our model using the information noted in the {ref}`visualising NeuroML models <userdocs:visualising_models>` page (including the `-v` verbose option for more information on the cell):
```{code-block} console
pynml-summary olm_example_net.nml -v
*******************************************************
* NeuroMLDocument: network
*
*  ComponentType: ['Bezaire_HCNolm_tau', 'Bezaire_Kdrfast_betaq', 'Bezaire_KvAolm_taub', 'Bezaire_Nav_alphah']
*  IonChannel: ['HCNolm', 'Kdrfast', 'KvAolm', 'Nav', 'leak_chan']
*  PulseGenerator: ['pg_olm']
*
*  Cell: olm
*    <Segment|0|Seg0_soma_0>
*      Parent segment: None (root segment)
*      (0.0, 0.0, 0.0), diam 10.0um -> (0.0, 10.0, 0.0), diam 10.0um; seg length: 10.0 um
*      Surface area: 314.1592653589793 um2, volume: 785.3981633974482 um3
*    <Segment|1|Seg1_soma_0>
*      Parent segment: 0
*      None -> (0.0, 20.0, 0.0), diam 10.0um; seg length: 10.0 um
*      Surface area: 314.1592653589793 um2, volume: 785.3981633974482 um3
*    <Segment|2|Seg0_axon_0>
*      Parent segment: 0
*      (0.0, 0.0, 0.0), diam 1.5um -> (0.0, -75.0, 0.0), diam 1.5um; seg length: 75.0 um
*      Surface area: 353.4291735288517 um2, volume: 132.53594007331938 um3
*    <Segment|3|Seg1_axon_0>
*      Parent segment: 2
*      None -> (0.0, -150.0, 0.0), diam 1.5um; seg length: 75.0 um
*      Surface area: 353.4291735288517 um2, volume: 132.53594007331938 um3
*    <Segment|4|Seg0_dend_0>
*      Parent segment: 1
*      (0.0, 20.0, 0.0), diam 3.0um -> (100.0, 120.0, 0.0), diam 3.0um; seg length: 141.4213562373095 um
*      Surface area: 1332.8648814475098 um2, volume: 999.6486610856323 um3
*    <Segment|5|Seg1_dend_0>
*      Parent segment: 4
*      None -> (177.0, 197.0, 0.0), diam 3.0um; seg length: 108.89444430272832 um
*      Surface area: 1026.3059587145826 um2, volume: 769.7294690359369 um3
*    <Segment|6|Seg0_dend_1>
*      Parent segment: 1
*      (0.0, 20.0, 0.0), diam 3.0um -> (-100.0, 120.0, 0.0), diam 3.0um; seg length: 141.4213562373095 um
*      Surface area: 1332.8648814475098 um2, volume: 999.6486610856323 um3
*    <Segment|7|Seg1_dend_1>
*      Parent segment: 6
*      None -> (-177.0, 197.0, 0.0), diam 3.0um; seg length: 108.89444430272832 um
*      Surface area: 1026.3059587145826 um2, volume: 769.7294690359369 um3
*    Total length of 8 segments: 670.6316010800756 um; total area: 6053.518558099847 um2
*
*    SegmentGroup: all, 8 member(s),    0 included group(s);    contains 8 segments in total
*    SegmentGroup: soma_group,  2 member(s),    1 included group(s);   contains 2 segments in total
*    SegmentGroup: axon_group,  2 member(s),    1 included group(s);   contains 2 segments in total
*    SegmentGroup: dendrite_group,      4 member(s),    2 included group(s);    contains 4 segments in total
*    SegmentGroup: soma_0,      2 member(s),    0 included group(s);   contains 2 segments in total
*    SegmentGroup: axon_0,      2 member(s),    0 included group(s);   contains 2 segments in total
*    SegmentGroup: dend_0,      2 member(s),    0 included group(s);   contains 2 segments in total
*    SegmentGroup: dend_1,      2 member(s),    0 included group(s);   contains 2 segments in total
*
*    Channel density: leak_all on all;  conductance of 0.01 mS_per_cm2 through ion chan leak_chan with ion non_specific, erev: -67mV
*      Channel is on <Segment|0|Seg0_soma_0>,   total conductance: 0.1 S_per_m2 x 3.1415926535897934e-10 m2 = 3.1415926535897936e-11 S (31.41592653589794 pS)
*      Channel is on <Segment|1|Seg1_soma_0>,   total conductance: 0.1 S_per_m2 x 3.1415926535897934e-10 m2 = 3.1415926535897936e-11 S (31.41592653589794 pS)
*      Channel is on <Segment|2|Seg0_axon_0>,   total conductance: 0.1 S_per_m2 x 3.534291735288517e-10 m2 = 3.534291735288518e-11 S (35.34291735288518 pS)
*      Channel is on <Segment|3|Seg1_axon_0>,   total conductance: 0.1 S_per_m2 x 3.534291735288517e-10 m2 = 3.534291735288518e-11 S (35.34291735288518 pS)
*      Channel is on <Segment|4|Seg0_dend_0>,   total conductance: 0.1 S_per_m2 x 1.3328648814475097e-09 m2 = 1.3328648814475097e-10 S (133.28648814475096 pS)
*      Channel is on <Segment|5|Seg1_dend_0>,   total conductance: 0.1 S_per_m2 x 1.0263059587145826e-09 m2 = 1.0263059587145826e-10 S (102.63059587145825 pS)
*      Channel is on <Segment|6|Seg0_dend_1>,   total conductance: 0.1 S_per_m2 x 1.3328648814475097e-09 m2 = 1.3328648814475097e-10 S (133.28648814475096 pS)
*      Channel is on <Segment|7|Seg1_dend_1>,   total conductance: 0.1 S_per_m2 x 1.0263059587145826e-09 m2 = 1.0263059587145826e-10 S (102.63059587145825 pS)
*    Channel density: HCNolm_soma on soma_group;        conductance of 0.5 mS_per_cm2 through ion chan HCNolm with ion h, erev: -32.9mV
*      Channel is on <Segment|0|Seg0_soma_0>,   total conductance: 5.0 S_per_m2 x 3.1415926535897934e-10 m2 = 1.5707963267948968e-09 S (1570.796326794897 pS)
*      Channel is on <Segment|1|Seg1_soma_0>,   total conductance: 5.0 S_per_m2 x 3.1415926535897934e-10 m2 = 1.5707963267948968e-09 S (1570.796326794897 pS)
*    Channel density: Kdrfast_soma on soma_group;       conductance of 73.37 mS_per_cm2 through ion chan Kdrfast with ion k, erev: -77mV
*      Channel is on <Segment|0|Seg0_soma_0>,   total conductance: 733.7 S_per_m2 x 3.1415926535897934e-10 m2 = 2.3049865299388314e-07 S (230498.65299388315 pS)
*      Channel is on <Segment|1|Seg1_soma_0>,   total conductance: 733.7 S_per_m2 x 3.1415926535897934e-10 m2 = 2.3049865299388314e-07 S (230498.65299388315 pS)
*    Channel density: Kdrfast_dendrite on dendrite_group;       conductance of 105.8 mS_per_cm2 through ion chan Kdrfast with ion k, erev: -77mV
*      Channel is on <Segment|4|Seg0_dend_0>,   total conductance: 1058.0 S_per_m2 x 1.3328648814475097e-09 m2 = 1.4101710445714652e-06 S (1410171.0445714653 pS)
*      Channel is on <Segment|5|Seg1_dend_0>,   total conductance: 1058.0 S_per_m2 x 1.0263059587145826e-09 m2 = 1.0858317043200284e-06 S (1085831.7043200284 pS)
*      Channel is on <Segment|6|Seg0_dend_1>,   total conductance: 1058.0 S_per_m2 x 1.3328648814475097e-09 m2 = 1.4101710445714652e-06 S (1410171.0445714653 pS)
*      Channel is on <Segment|7|Seg1_dend_1>,   total conductance: 1058.0 S_per_m2 x 1.0263059587145826e-09 m2 = 1.0858317043200284e-06 S (1085831.7043200284 pS)
*    Channel density: Kdrfast_axon on axon_group;       conductance of 117.392 mS_per_cm2 through ion chan Kdrfast with ion k, erev: -77mV
*      Channel is on <Segment|2|Seg0_axon_0>,   total conductance: 1173.92 S_per_m2 x 3.534291735288517e-10 m2 = 4.1489757538898964e-07 S (414897.57538898964 pS)
*      Channel is on <Segment|3|Seg1_axon_0>,   total conductance: 1173.92 S_per_m2 x 3.534291735288517e-10 m2 = 4.1489757538898964e-07 S (414897.57538898964 pS)
*    Channel density: KvAolm_soma on soma_group;        conductance of 4.95 mS_per_cm2 through ion chan KvAolm with ion k, erev: -77mV
*      Channel is on <Segment|0|Seg0_soma_0>,   total conductance: 49.5 S_per_m2 x 3.1415926535897934e-10 m2 = 1.5550883635269477e-08 S (15550.883635269476 pS)
*      Channel is on <Segment|1|Seg1_soma_0>,   total conductance: 49.5 S_per_m2 x 3.1415926535897934e-10 m2 = 1.5550883635269477e-08 S (15550.883635269476 pS)
*    Channel density: KvAolm_dendrite on dendrite_group;        conductance of 2.8 mS_per_cm2 through ion chan KvAolm with ion k, erev: -77mV
*      Channel is on <Segment|4|Seg0_dend_0>,   total conductance: 28.0 S_per_m2 x 1.3328648814475097e-09 m2 = 3.7320216680530273e-08 S (37320.21668053028 pS)
*      Channel is on <Segment|5|Seg1_dend_0>,   total conductance: 28.0 S_per_m2 x 1.0263059587145826e-09 m2 = 2.8736566844008313e-08 S (28736.566844008314 pS)
*      Channel is on <Segment|6|Seg0_dend_1>,   total conductance: 28.0 S_per_m2 x 1.3328648814475097e-09 m2 = 3.7320216680530273e-08 S (37320.21668053028 pS)
*      Channel is on <Segment|7|Seg1_dend_1>,   total conductance: 28.0 S_per_m2 x 1.0263059587145826e-09 m2 = 2.8736566844008313e-08 S (28736.566844008314 pS)
*    Channel density: Nav_soma on soma_group;   conductance of 10.7 mS_per_cm2 through ion chan Nav with ion na, erev: 50mV
*      Channel is on <Segment|0|Seg0_soma_0>,   total conductance: 107.0 S_per_m2 x 3.1415926535897934e-10 m2 = 3.361504139341079e-08 S (33615.04139341079 pS)
*      Channel is on <Segment|1|Seg1_soma_0>,   total conductance: 107.0 S_per_m2 x 3.1415926535897934e-10 m2 = 3.361504139341079e-08 S (33615.04139341079 pS)
*    Channel density: Nav_dendrite on dendrite_group;   conductance of 23.4 mS_per_cm2 through ion chan Nav with ion na, erev: 50mV
*      Channel is on <Segment|4|Seg0_dend_0>,   total conductance: 234.0 S_per_m2 x 1.3328648814475097e-09 m2 = 3.118903822587173e-07 S (311890.3822587173 pS)
*      Channel is on <Segment|5|Seg1_dend_0>,   total conductance: 234.0 S_per_m2 x 1.0263059587145826e-09 m2 = 2.401555943392123e-07 S (240155.59433921232 pS)
*      Channel is on <Segment|6|Seg0_dend_1>,   total conductance: 234.0 S_per_m2 x 1.3328648814475097e-09 m2 = 3.118903822587173e-07 S (311890.3822587173 pS)
*      Channel is on <Segment|7|Seg1_dend_1>,   total conductance: 234.0 S_per_m2 x 1.0263059587145826e-09 m2 = 2.401555943392123e-07 S (240155.59433921232 pS)
*    Channel density: Nav_axon on axon_group;   conductance of 17.12 mS_per_cm2 through ion chan Nav with ion na, erev: 50mV
*      Channel is on <Segment|2|Seg0_axon_0>,   total conductance: 171.20000000000002 S_per_m2 x 3.534291735288517e-10 m2 = 6.050707450813942e-08 S (60507.07450813943 pS)
*      Channel is on <Segment|3|Seg1_axon_0>,   total conductance: 171.20000000000002 S_per_m2 x 3.534291735288517e-10 m2 = 6.050707450813942e-08 S (60507.07450813943 pS)
*
*    Specific capacitance on all: 1.3 uF_per_cm2
*      Capacitance of <Segment|0|Seg0_soma_0>,  total capacitance: 0.013000000000000001 F_per_m2 x 3.1415926535897934e-10 m2 = 4.084070449666732e-12 F (4.084070449666732 pF)
*      Capacitance of <Segment|1|Seg1_soma_0>,  total capacitance: 0.013000000000000001 F_per_m2 x 3.1415926535897934e-10 m2 = 4.084070449666732e-12 F (4.084070449666732 pF)
*      Capacitance of <Segment|2|Seg0_axon_0>,  total capacitance: 0.013000000000000001 F_per_m2 x 3.534291735288517e-10 m2 = 4.594579255875073e-12 F (4.594579255875073 pF)
*      Capacitance of <Segment|3|Seg1_axon_0>,  total capacitance: 0.013000000000000001 F_per_m2 x 3.534291735288517e-10 m2 = 4.594579255875073e-12 F (4.594579255875073 pF)
*      Capacitance of <Segment|4|Seg0_dend_0>,  total capacitance: 0.013000000000000001 F_per_m2 x 1.3328648814475097e-09 m2 = 1.732724345881763e-11 F (17.32724345881763 pF)
*      Capacitance of <Segment|5|Seg1_dend_0>,  total capacitance: 0.013000000000000001 F_per_m2 x 1.0263059587145826e-09 m2 = 1.3341977463289574e-11 F (13.341977463289574 pF)
*      Capacitance of <Segment|6|Seg0_dend_1>,  total capacitance: 0.013000000000000001 F_per_m2 x 1.3328648814475097e-09 m2 = 1.732724345881763e-11 F (17.32724345881763 pF)
*      Capacitance of <Segment|7|Seg1_dend_1>,  total capacitance: 0.013000000000000001 F_per_m2 x 1.0263059587145826e-09 m2 = 1.3341977463289574e-11 F (13.341977463289574 pF)
*
*  Network: single_olm_cell_network
*
*   1 cells in 1 populations
*     Population: pop0 with 1 components of type olm
*       Locations: [(0, 0, 0), ...]
*
*   0 connections in 0 projections
*
*   0 inputs in 0 input lists
*
*   1 explicit inputs (outside of input lists)
*     Explicit Input of type pg_olm to pop0(cell 0), destination: unspecified
*
*******************************************************

```
We can check the connectivity graph of the model:
```{code-block} console
pynml -graph 10 olm_example_net.nml
```
which will give us this figure:
```{figure} ./NML2_examples/single_olm_cell_network.gv.png
:alt: Level 10 network graph generated by pynml
:align: center
:scale: 60 %

Level 10 network graph generated by pynml
```
## Simulating the model

Please note that this example uses the {ref}`NEURON <userdocs:neuron>` simulator to simulate the model.
Please ensure that the `NEURON_HOME` environment variable is correctly set as noted {ref}`here <userdocs:neuron:envvar>`.

Now that we have declared and inspected our network model and all its components, we can proceed to simulate it.
We do this in the `main` function:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 20-68
----
```
Here we first create a `LEMSSimulation` instance and include our network NeuroML file in it.
We must inform LEMS what the target of the simulation is.
In our case, it's the id of our network, `single_olm_cell_network`:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 28-32
----
```
We also want to record some information, so we create an output file first with an `id` of `output0`:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 36
----
```
Now, we can record any quantity that is exposed by NeuroML (any `exposure`).
Here, for example, we add columns for the membrane potentials `v` of the different segments of the {ref}`cell <schema:cell>`.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 37-60
----
```
The path required to point to the `quantity` (exposure) to be recorded needs to be correctly provided.
Here, where we use a {ref}`population list <schema:populationlist>` that includes an {ref}`instance <schema:instance>` of the cell, it is: `population_id/instance_id/cell component type/segment id/exposure`. (See tickets [15](https://github.com/NeuroML/Documentation/issues/15) and [16](https://github.com/NeuroML/Documentation/issues/16))


We then save the LEMS simulation file, and run our simulation with the {ref}`NEURON <userdocs:simulating_models:neuron>` simulator (since the default {ref}`jNeuroML <jneuroml>` simulator can only simulate single compartment cells).

```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 62-66
----
```
## Plotting the recorded variables

To plot the variables that we recorded, we write a simple function that reads the data and uses the `generate_plot` utility function which generates the membrane potential graphs for different segments.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 71-84
----
```
This concludes this example.
Here we have seen how to create, simulate, record, and visualise a multi-compartment neuron.
In the next section, you will find an interactive notebook where you can play with this example.
