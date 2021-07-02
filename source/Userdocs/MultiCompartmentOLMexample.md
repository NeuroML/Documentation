(userdocs:getting_started:multi_compartment_example)=
# Simulating a multi compartment OLM neuron

In this section we will model and simulate a multi-compartment Oriens-lacunosum moleculare (OLM) interneuron cell from the rodent hippocampal CA1 network model developed by Bezaire et al. ({cite}`Bezaire2016`).
The complete network model can be seen [here on GitHub](https://github.com/mbezaire/ca1), and [here on Open Source Brain](https://www.opensourcebrain.org/projects/nc_ca1).

```{figure} ../Userdocs/NML2_examples/olm_example_sim_seg0_soma0-v.png
:alt: Membrane potential for neuron recorded from the simulation at the soma
:align: center

Membrane potential of the simulated OLM cell at the soma.
```
This plot, saved as `olm_example_sim_seg0_soma0-v.png` is generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
----
```

As we will see, we repeat the same operations in the script while adding segments and ion-channels to our model, so we also write some helper functions to make it easier for ourselves:

```{literalinclude} ./NML2_examples/CellBuilder.py
----
language: python
----
```
These helper functions will be included in the Python NeuroML libraries in their next release.
Currently, we *import* them into our Python script at the top:

```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 12
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
lines: 113-306
----
```
Let us walk through this function:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 118-120
----
```
First, we create a new NeuroML document that we will use to save this cell.
Then, we proceed to create a new cell using the {ref}`Cell NeuroML component type <schema:cell>`, and define the name of the file we will use to store the cell in NeuroML.
To create the cell, we use the `create_cell` utility function:

```{literalinclude} ./NML2_examples/CellBuilder.py
----
language: python
lines: 24,47-72
----
```
We now know that a {ref}`Cell <schema:cell>` component has two children: {ref}`morphology <schema:morphology>`, and {ref}`biophysical properties <schema:biophysicalproperties>`.
The function simply creates the new {ref}`Cell <schema:cell>` component for us and initialises the {ref}`morphology <schema:morphology>` and {ref}`biophysical properties <schema:biophysicalproperties>`.
Additionally, it creates some default {ref}`segment groups <schema:segmentgroup>` for us that we use to organise our our segments in later.

We now have an empty cell.
Since we are building a multi-compartmental cell, we now proceed to define the detailed morphology of the cell.
We do this by adding {ref}`segments <schema:segment>` and grouping them in to {ref}`segment groups <schema:segmentgroup>` which are both children elements of the {ref}`morphology <schema:morphology>` of the cell.
This is done using the `add_segment` utility function as required:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 124-128
----
```
The utility function takes the dimensions of the segment---it's {ref}`proximal <schema:proximal>` and {ref}`distal <schema:distal>` co-ordinates and the diameter to create a segment of the provided name.
Additionally, since segments need to be contiguous, it adds the segment to a *parent* segment.
Finally, it places the segment into the specified segment group and the default groups that we also have and adds the segment to the cell's morphology.
```{literalinclude} ./NML2_examples/CellBuilder.py
----
language: python
lines: 74,103-144,152-158
----
```

We call the same function multiple times to add soma, dendritic, and axonal segments to our cell.
Note how the segments connect to each other to form the contiguous cell morphology.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 122-185
----
```

Next, we add extra information to our segments and organise them so that they can be correctly exported to the NEURON format for simulation later.

```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 189-205
----
```

We have now completed adding the morphological information to our cell.
Next, we proceed to our {ref}`biophysical properties <schema:biophysicalproperties>`, which are split into two:
- the {ref}`membrane properties <schema:membraneproperties>`
- the {ref}`intracellular properties <schema:intracellularproperties>`

We also use a few simple helper functions defined  in the `CellBuilder.py` module to add these to our cell:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 207-303
----
```
This completes the definition of our cell.
We write it to a NeuroML file, and validate it.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 304
----
```
The resulting NeuroML file is:
```{literalinclude} ./NML2_examples/olm.cell.nml
----
language: xml
```
We can now already inspect our cell using the NeuroML tools:
```{code-block} console

pynml -png olm.cell.png
...
pyNeuroML >>> Writing to: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/source/Userdocs/NML2_examples/olm.cell.png
```
This gives us a figure of the morphology of our cell:
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
lines: 85-110
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

Now that we have declared and inspected our network model and all its components, we can proceed to simulate it.
We do this in the `main` function:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 18-66
----
```
Here we first create a `LEMSSimulation` instance and include our network NeuroML file in it.
We must inform LEMS what the target of the simulation is.
In our case, it's the id of our network, `single_olm_cell_network`:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 25-30
----
```
We also want to record some information, so we create an output file first with an `id` of `output0`:
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 33
----
```
Now, we can record any quantity that is exposed by NeuroML (any `exposure`).
Here, for example, we add columns for the membrane potentials `v` of the different segments of the {ref}`cell <schema:cell>`.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 35-58
----
```
The path required to point to the `quantity` (exposure) to be recorded needs to be correctly provided.
Here, where we use a {ref}`population list <schema:populationlist>` that includes an {ref}`instance <schema:instance>` of the cell, it is: `population_id/instance_id/cell component type/segment id/exposure`. (See tickets [15](https://github.com/NeuroML/Documentation/issues/15) and [16](https://github.com/NeuroML/Documentation/issues/16))


We then save the LEMS simulation file, and run our simulation with the {ref}`NEURON <userdocs:simulating_models:neuron>` simulator (since the default {ref}`jNeuroML <jneuroml>` simulator can only simulate single compartment cells).

```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 62-64
----
```
## Plotting the recorded variables

To plot the variables that we recorded, we write a simple function that reads the data and uses the `generate_plot` utility function which generates the membrane potential graphs for different segments.
```{literalinclude} ./NML2_examples/olm-example.py
----
language: python
lines: 69-82
----
```
This concludes this example.
Here we have seen how to create, simulate, record, and visualise a multi-compartment neuron.
In the next section, you will find an interactive notebook where you can play with this example.
