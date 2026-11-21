(userdocs:getting_started_neuroml)=
# Getting started with NeuroML

The best way to understand NeuroML is to work through NeuroML examples to see how they are constructed and what they can do.
We present below a set of step-by-step guides to illustrate how models are written and simulated using NeuroML.

<table>
<tr>
<td><a href="https://docs.neuroml.org/Userdocs/NML2_examples/SingleNeuron.html"><img src="../_images/example-single-izhikevich2007cell-sim-v.png" height=150 title="Guide 1"/></a>&nbsp;&nbsp;</td>
<td><a href="https://docs.neuroml.org/Userdocs/IzhikevichNetworkExample.html"><img src="../_images/example_izhikevich2007network_sim-spikes.png" height=150 title="Guide 2"/></a>&nbsp;&nbsp;</td>
<td><a href="https://docs.neuroml.org/Userdocs/SingleCompartmentHHExample.html"><img src="../_images/HH_single_compartment_example_sim-v.png" height=150 title="Guide 3"/></a>&nbsp;&nbsp;</td>
<td><a href="https://docs.neuroml.org/Userdocs/MultiCompartmentOLMexample.html"><img src="../_images/olm.cell.xy.png" height=150 title="Guide 4"/></a>&nbsp;&nbsp;</td>
</tr>
</table>


| Link to guide    | Description | Model life cycle stages |
| :------ | ----------- | ----------------------- |
| | **Introductory guides** ||
| {ref}`Guide 1 <userdocs:getting_started:single_example>` | Create and simulate a simple regular spiking Izhikevich neuron in NeuroML | Create, Validate, Simulate |
| {ref}`Guide 2 <userdocs:gettingstarted:izhikevichnetwork>`| Create a network of two synaptically connected populations of Izhikevich neurons  | Create, Validate, Visualise, Simulate |
| {ref}`Guide 3 <userdocs:getting_started:single_compartment_example>`| Build and simulate a single compartment Hodgkin-Huxley neuron | Create, Validate, Visualise, Simulate |
| {ref}`Guide 4 <userdocs:getting_started:multi_compartment_example>`| Create and simulate a multi compartment hippocampal OLM neuron | Create, Validate, Visualise, Simulate |
| | **Advanced guides** ||
| [Guide 5](https://docs.neuroml.org/Userdocs/NML2_examples/NeuroML-DB.html) | Create novel NeuroML models from components on NeuroML-DB | Reuse, Create, Validate, Simulate |
| {ref}`Guide 6 <userdocs:optimising>` | Optimise/fit NeuroML models to experimental data | Create, Validate, Simulate, Fit |
| {ref}`Guide 7 <userdocs:extending>`| Extend NeuroML by creating a novel model type in LEMS  | Create, Simulate |
| | **Step by step walkthroughs** ||
| {ref}`Guide 8 <userdocs:creating_models:converting_conductance>`| Guide to converting cell models to NeuroML and sharing them on Open Source Brain | Create, Validate, Simulate, Share |
| {ref}`Guide 9 <userdocs:walkthroughs:rayetal2020>`| Conversion of Ray et al 2020 {cite}`Ray2020` to NeuroML | Create, Validate, Visualise, Simulate, Extend using LEMS |


You do not need to install any software on your computers to run many of the examples above.
These examples are followed by a [Jupyter notebook](https://jupyter.org/index.html) for you to experiment with inside your browser ({ref}`more info <userdocs:usage:jupyterbooks>`).
