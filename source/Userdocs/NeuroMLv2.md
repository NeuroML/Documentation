(userdocs:neuromlv2)=
# NeuroML v2


The current stable version of NeuroML is v2.1, and can the schema for this be seen [here](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).
The following figure, taken from Cannon et al. 2014 ({cite}`Cannon2014`) shows some of the elements defined in NeuroML version 2 (note: these core elements haven't changed since that publication).

```{figure} ../images/Figure6a.png
:alt: Elements defined in the NeuroML schema, version 2.
:align: center
:scale: 60 %

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

(userdocs:specification:lemsdefs)=
## Defining dynamics in LEMS

While valid NeuroML entities are contained in the schema, their underlying mathematical structure and composition rules must also be defined.
For this, NeuroML version 2 makes use of [LEMS (Low Entropy Language Specification)](http://lems.github.io/LEMS).

```{admonition} LEMS
:class: dropdown tip
For an in-depth guide to LEMS, please see the research paper: [LEMS: a language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2](https://www.frontiersin.org/articles/10.3389/fninf.2014.00079/full). Documentation on the structure of the LEMS language can be found [here](http://lems.github.io/LEMS/elements.html).
```

LEMS is an XML based language originally developed by Robert Cannon for specifying generic models of hybrid dynamical systems. Models defined in LEMS can also be simulated directly through a native interpreter.

- **ComponentType** elements define the behaviour of a specific type of model and specify **Parameters**, **StateVariables**, and their **Dynamics** and **Structure** can be defined as templates for model elements (e.g. HH ion channels, abstract cells, etc.). The notion of a **ComponentType** is thus similar to that of a **class** in object oriented programming.
- **Components** are instances of these types, with specific values of **Parameters** (e.g. HH squid axon Na+ channel, I&F cell with threshold -60mV, etc.). **Components** play the same role as **objects** in object oriented programming.

```{figure} ../images/NeuroML2_LEMS_Overview_web.svg
:alt: Figure showing relationship between LEMS and NeuroML2

This image (from Blundell et al. 2018 ({cite}`Blundell2018`)) shows the usage of LEMS **ComponentTypes** and **Components** in NeuroML.
Elements in NeuroML v2 are **Components** which have a corresponding structural and mathematical definition in LEMS **ComponentTypes**.
```

On the left side of the figure, examples are shown of the (truncated) XML representations of:

- (blue) a {ref}`network <schema:network>` containing two {ref}`populations <schema:population>` of {ref}`integrate-and-fire cells <schema:iafCell>` connected by a single {ref}`projection <schema:projection>` between them;
- (green) a {ref}`spiking neuron model <schema:izhikevichCell>` as described by Izhikevich (2003);
- (yellow) a {ref}`conductance based synapse <schema:expOneSynapse>` with a single exponential decay waveform.

On the right, the definition of the structure and dynamics of these elements in the LEMS language is shown.
Each element has a corresponding **ComponentType** definition, describing the parameters (as well as their dimensions, not shown) and the dynamics in terms of state variables and their derivatives, any derived variables, and the behaviour when certain conditions are met or events are received (for example, the emission of a spike after a given threshold is crossed).

(userdocs:neuromlv2inlems)=
### NeuroML 2 Component Type definitions in LEMS

The standard set of **ComponentType** definitions for the core NeuroML2 elements are contained in a curated set of files (below) though users are {ref}`free to define their own ComponentTypes to extend the scope of the language <userdocs:extending>`.

- {ref}`Dimensions/units allowed <schema:neuromlcoredimensions_>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/NeuroMLCoreDimensions.xml?view=markup))
- {ref}`Cell models <schema:cells_>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Cells.xml?view=markup))
- {ref}`Network elements <schema:networks_>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Networks.xml?view=markup))
- {ref}`Ion channels <schema:channels_>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Channels.xml?view=markup))
- {ref}`Synapse models <schema:synapses_>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Synapses.xml?view=markup))
- {ref}`Mapping of PyNN cells & synapses <schema:pynn_>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/PyNN.xml?view=markup))



Here, for example, the {ref}`izhikevich2007Cell <schema:izhikevich2007Cell>` is defined in the [NeuroML schema](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.1.xsd) as having the following internal attributes:

```{code-block} xml
<xs:complexType name="Izhikevich2007Cell">
    <xs:complexContent>
        <xs:extension base="BaseCellMembPotCap">
            <xs:attribute name="v0" type="Nml2Quantity_voltage" use="required"/>
            <xs:attribute name="k" type="Nml2Quantity_conductancePerVoltage" use="required"/>
            <xs:attribute name="vr" type="Nml2Quantity_voltage" use="required"/>
            <xs:attribute name="vt" type="Nml2Quantity_voltage" use="required"/>
            <xs:attribute name="vpeak" type="Nml2Quantity_voltage" use="required"/>
            <xs:attribute name="a" type="Nml2Quantity_pertime" use="required"/>
            <xs:attribute name="b" type="Nml2Quantity_conductance" use="required"/>
            <xs:attribute name="c" type="Nml2Quantity_voltage" use="required"/>
            <xs:attribute name="d" type="Nml2Quantity_current" use="required"/>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

Correspondingly, its **ComponentType** dynamics are defined in the LEMS file, [Cells.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Cells.xml).
(Note: you do not need to read the XML LEMS definitions, you can see this information in a well formatted form {ref}`here in the documentation itself <schema:izhikevich2007Cell>`)

```{code-block} xml
<ComponentType name="izhikevich2007Cell"
    extends="baseCellMembPotCap"
    description="Cell based on the modified Izhikevich model in Izhikevich 2007, Dynamical systems in neuroscience, MIT Press">

    <Parameter name="v0" dimension="voltage"/>

    <!--
    Defined in baseCellMembPotCap:
    <Parameter name="C" dimension="capacitance"/>
    -->
    <Parameter name="k" dimension="conductance_per_voltage"/>

    <Parameter name="vr" dimension="voltage"/>
    <Parameter name="vt" dimension="voltage"/>
    <Parameter name="vpeak" dimension="voltage"/>

    <Parameter name="a" dimension="per_time"/>
    <Parameter name="b" dimension="conductance"/>
    <Parameter name="c" dimension="voltage"/>
    <Parameter name="d" dimension="current"/>

    <Attachments name="synapses" type="basePointCurrent"/>

    <Exposure name="u" dimension="current"/>

    <Dynamics>

        <StateVariable name="v" dimension="voltage" exposure="v"/>
        <StateVariable name="u" dimension="current" exposure="u"/>

        <DerivedVariable name="iSyn"  dimension="current" exposure="iSyn" select="synapses[*]/i" reduce="add" />

        <DerivedVariable name="iMemb" dimension="current" exposure="iMemb" value="k * (v-vr) * (v-vt) + iSyn - u"/>

        <TimeDerivative variable="v" value="iMemb / C"/>
        <TimeDerivative variable="u" value="a * (b * (v-vr) - u)"/>

        <OnStart>
            <StateAssignment variable="v" value="v0"/>
            <StateAssignment variable="u" value="0"/>
        </OnStart>

        <OnCondition test="v .gt. vpeak">
            <StateAssignment variable="v" value="c"/>
            <StateAssignment variable="u" value="u + d"/>
            <EventOut port="spike"/>
        </OnCondition>

    </Dynamics>

</ComponentType>
```

We can define **Component**s of the {ref}`izhikevich2007Cell <schema:izhikevich2007Cell>` **ComponentType** with the parameters we need. For example, the {ref}`izhikevich2007Cell <schema:izhikevich2007Cell>` neuron model can exhibit different spiking behaviours, so we can define a regular spiking **Component**, or another **Component** that exhibits bursting.

```{code-block} xml
<izhikevich2007Cell id="iz2007RS" v0 = "-60mV" C="100 pF" k = "0.7 nS_per_mV"
                    vr = "-60 mV" vt = "-40 mV" vpeak = "35 mV"
                    a = "0.03 per_ms" b = "-2 nS" c = "-50 mV" d = "100 pA"/>
```

Once these **Component**s are defined in the NeuroML document, we can use **Instance**s of them to create populations and networks, and so on.

```{admonition} You don't have to write in XML...
A quick reminder that while XML files can be edited in a standard text editor, you generally don't have to create/update them by hand. {ref}`This guide <userdocs:getting_started:single_example>` goes through the steps of creating an example using the {ref}`izhikevich2007Cell <schema:izhikevich2007Cell>` model in Python using {ref}`libNeuroML <libNeuroML>` and {ref}`pyNeuroML <pyNeuroML>`
```

Using LEMS to specify the core of NeuroML version 2 has the following significant advantages:

- NeuroML 2 XML files can be used standalone by applications (exported/imported) in the same way as NeuroML v1.x, without reference to the LEMS definitions, easing the transition for v1.x compliant applications
- Any NeuroML 2 **ComponentType** can be extended and will be usable/translatable by any application (e.g. jLEMS) which understands LEMS

The first point above means that a parsing application does not necessarily have to natively read the LEMS type definition for, e.g. an {ref}`izhikevich2007Cell <schema:izhikevich2007Cell>` element: it just has to map the NeuroML element parameters onto its own object model implementing that entity.
Ideally, the behaviour should be the same − which could be ascertained by testing against the reference LEMS interpreter implementation ([jLEMS](http://github.com/LEMS/jLEMS/)).

The second point above means that if an application does support LEMS, it can automatically parse (and generate code for) a wide range of NeuroML 2 cells, channels and synapses, including any new **ComponentType** derived from these, without having to natively know anything about channels, cell models, etc.

```{admonition} jnml and pynml handle both LEMS and NeuroML 2.
:class: tip
{ref}`jNeuroML <jneuroML>` and {ref}`pynml <pyneuroml>` handle both LEMS and NeuroML 2.
They bundle jLEMS together with the LEMS definitions for NeuroML 2 ComponentTypes, and can simulate any LEMS model as well as many NeuroML 2 models.
```
