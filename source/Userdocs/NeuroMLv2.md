(userdocs:neuromlv2)=
# NeuroML v2

The current stable version of NeuroML is v2.3, and the XSD Schema for this can be found [here](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
The following figure, taken from Cannon et al. 2014 ({cite}`Cannon2014`) shows some of the core elements defined in NeuroML version 2 (note: these key elements haven't changed since that publication).

```{figure} ../images/Figure6a.png
:alt: Elements defined in the NeuroML schema, version 2.
:align: center

Elements defined in the NeuroML schema, version 2.
```
<!-- Sphinx etc. do not support Image maps, so we can't reproduce what's on the NeuroML website -->


You can see the complete definitions of NeuroML 2 entities in the following pages.
You can also search this documentation for specific entities that you may be using in your NeuroML models.

Examples of files using the NeuroML 2 schema, and some of the elements they use are:

| Example file | NeuroML elements used |
| --- | --- |
| [A simple cell with a morphology & segments arranged into groups](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_SimpleMorphology.nml) | {ref}`<cell> <schema:cell>`, {ref}`<morphology> <schema:morphology>`, {ref}`<segment> <schema:segment>`, {ref}`<segmentGroup> <schema:segmentGroup>` |
| [A cell specifying biophysical properties (channel densities, passive electrical properties, etc.)](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_FullCell.nml) | {ref}`<membraneProperties> <schema:membraneProperties>`, {ref}`<intracellularProperties> <schema:intracellularProperties>`, {ref}`<channelDensity> <schema:channelDensity>` |
| [A simple HH Na+ channel](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_SimpleIonChannel.nml) | {ref}`<ionChannelHH> <schema:ionChannelHH>`, {ref}`<gateHHrates> <schema:gateHHrates>`, {ref}`<HHExpLinearRate> <schema:HHExpLinearRate>` |
| [Some of the simplified spiking neuron models which are supported](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_AbstractCells.nml) | {ref}`<iafCell> <schema:iafCell>`, {ref}`<izhikevich2007Cell> <schema:izhikevich2007Cell>`, {ref}`<adExIaFCell> <schema:adExIaFCell>`, {ref}`<fitzHughNagumoCell> <schema:fitzHughNagumoCell>` |
| [Synapse models ](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_SynapseTypes.nml) | {ref}`<alphaSynapse> <schema:alphaSynapse>`, {ref}`<expTwoSynapse> <schema:expTwoSynapse>`, {ref}`<blockingPlasticSynapse> <schema:blockingPlasticSynapse>`, {ref}`<doubleSynapse> <schema:doubleSynapse>` |
| [A network of cells positioned in 3D and synaptically connected ](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_InstanceBasedNetwork.nml) | {ref}`<network> <schema:network>`, {ref}`<population> <schema:population>`, {ref}`<projection> <schema:projection>`, {ref}`<connection> <schema:connection>`, {ref}`<inputList> <schema:inputList>`  |


NeuroML files containing the XML representation of the model can be {ref}`validated <userdocs:validating_models>` to ensure all of the correct tags/attributes are present.

**But** how do we know how the model is actually meant to use the specified attributes in an element? The schema only says that `leakReversal`, `thresh`, etc. are allowed attributes on `iafCell`, but how are these used to calculate the membrane potential? The answer lies in another, lower-level language, called LEMS (Low Entropy Model Specification).

While valid NeuroML entities are contained in the schema, their underlying mathematical structure and composition rules must also be defined.
For this, NeuroML version 2 makes use of {ref}`LEMS <userdocs:lems>`.

