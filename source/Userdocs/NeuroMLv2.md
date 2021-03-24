(userdocs:neuromlv2)=
# NeuroML v2

```{admonition} Needs review
:class: warning
This page needs review. Please see this issue: https://github.com/NeuroML/Documentation/issues/45
```

The current NeuroML schema is version 2.1, and can be seen [here](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).
The following figure, taken from Cannon et al. 2014 ({cite}`Cannon2014`) shows some of the elements defined in the NeuroML schema version 2.1.

```{figure} ../images/Figure6a.png
:alt: Elements defined in the NeuroML schema, version 2.1.
:align: center
:scale: 60 %

Elements defined in the NeuroML schema, version 2.1.
```
<!-- Sphinx etc. do not support Image maps, so we can't reproduce what's on the NeuroML website -->


You can see the complete definitions of NeuroML 2 entities in the following pages.
You can also search this documentation for specific entities that you may be using in your NeuroML models.

Examples of files using the NeuroML 2 schema are here:

- [A simple cell with morphology & segment groups](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_SimpleMorphology.nml)
- [A cell with biophysical properties (channel densities, passive electrical properties, etc.)](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_FullCell.nml)
- [A simple HH Na+ channel](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_SimpleIonChannel.nml).
- [Some of the simplified spiking neuron models which are supported](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_AbstractCells.nml)
- [Some synapse models (single/double exponential conductances, NMDA-R synapse)](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_SynapseTypes.nml)
- [A network of cells positioned in 3D](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_InstanceBasedNetwork.nml)
- [A full NeuroML network model description with cells, channels, populations and networks](https://github.com/NeuroML/NeuroML2/tree/master/examples/NML2_FullNeuroML.nml)



(userdocs:specification:lemsdefs)=
## Defining dynamics in LEMS

While the valid NeuroML entities are defined in the schema, their underlying structural and mathematical information must also be defined.
For this, NeuroML version 2 makes use of [LEMS (Low Entropy Language Specification)](http://lems.github.io/LEMS).

```{admonition} LEMS
:class: dropdown tip
For an in-depth guide to LEMS, please see the research paper: [LEMS: a language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2](https://www.frontiersin.org/articles/10.3389/fninf.2014.00079/full)
```

LEMS is an XML based language with interpreter originally developed by Robert Cannon for specifying generic models of hybrid dynamical systems.
**ComponentType** (**ComponentClass** was briefly used as a name for these) elements which specify **Parameter**s, **StateVariable**s and their **Dynamics** and **Structure** can be defined as templates for model elements (e.g. HH ion channels, abstract cells, etc.).
**Components** are instances of these with specific values of **Parameters** (e.g. HH squid axon Na+ channel, I&F cell with threshold -60mV, etc.).

```{figure} ../images/lems-neuroml2.png
:alt: Figure showing relationship between LEMS and NeuroML2
:scale: 60 %

This image (from Blundell et al. 2018 ({cite}`Blundell2018`)) shows the usage of LEMS **ComponentTypes** and **Components** in NeuroML.
Elements in NeuroML v2 are **Components** which have a corresponding structural and mathematical definition in LEMS **ComponentTypes**.
```

In the figure, examples are shown of the (truncated) XML representations of: 

- (blue) a network containing two populations of integrate-and-fire cells connected by a single projection between them; 
- (green) a spiking neuron model as described by Izhikevich (2003);
- (yellow) a conductance based synapse with a single exponential decay waveform.

On the right the definition of the structure and dynamics of these elements in the LEMS language is shown.
Each element has a corresponding **ComponentType** definition, describing the parameters (as well as their dimensions, not shown) and the dynamics in terms of the state variables, the time derivative of these, any derived variables, and the behavior when certain conditions are met or (spiking) events are received.
The standard set of **ComponentType** definitions for the core NeuroML2 elements are contained in a curated set of files (below) though users are {ref}`free to define their own ComponentTypes to extend the scope of the language <userdocs:extending>`.

- {ref}`Dimensions/units allowed <schema:neuromlcoredimensions>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/NeuroMLCoreDimensions.xml?view=markup))
- {ref}`Cell models <schema:cells>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Cells.xml?view=markup))
- {ref}`Network elements <schema:networks>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Networks.xml?view=markup))
- {ref}`Ion channels <schema:channels>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Channels.xml?view=markup))
- {ref}`Synapse models <schema:synapses>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Synapses.xml?view=markup))
- {ref}`Mapping of PyNN cells & synapses <schema:pynn>` ([source in LEMS](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/PyNN.xml?view=markup))



Here, for example, the `izhikevichCell` is defined in the [NeuroML schema](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.1.xsd) as a valid NeuroML cell type which may occur either 0 or more times in a NeuroML document:

```{code-block} xml
    <xs:group name="CellTypes">
        <xs:annotation>
            <xs:documentation>Various types of cells which are defined in NeuroML 2. This list will be expanded...</xs:documentation>
        </xs:annotation>
        <xs:sequence>
        ...
            <xs:element name="izhikevichCell" type="IzhikevichCell" minOccurs="0" maxOccurs="unbounded"/>
        ...
        </xs:sequence>
    </xs:group>
```
Correspondingly, its **ComponentType** dynamics are defined in the LEMS file, [Cells.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes/Cells.xml).
(You do not need to read the XML LEMS definitions, you can see this information in a well formatted form {ref}`here in the documentation itself <schema:izhikevichcell>`)

```{code-block} xml
    <ComponentType name="izhikevichCell"
        extends="baseCellMembPot"
        description="Cell based on the 2003 model of Izhikevich, see http://izhikevich.org/publications/spikes.htm">

        <Parameter name="v0" dimension="voltage"/>
        <Parameter name="a" dimension="none"/>
        <Parameter name="b" dimension="none"/>
        <Parameter name="c" dimension="none"/>
        <Parameter name="d" dimension="none"/>
        <Parameter name="thresh" dimension="voltage"/>

        <Constant name="MSEC" dimension="time" value="1ms"/>
        <Constant name="MVOLT" dimension="voltage" value="1mV"/>

        <Attachments name="synapses" type="basePointCurrentDL"/>
        <Exposure name="U" dimension="none"/>

        <Dynamics>
            <StateVariable name="v" dimension="voltage" exposure="v"/>
            <StateVariable name="U" dimension="none" exposure="U"/>

            <DerivedVariable name="ISyn" dimension="none" select="synapses[*]/I" reduce="add" />

            <TimeDerivative variable="v" value="(0.04 * v^2 / MVOLT + 5 * v + (140.0 - U + ISyn) * MVOLT)/MSEC"/>
            <TimeDerivative variable="U" value="a * (b * v / MVOLT - U) / MSEC"/>

            <OnStart>
                <StateAssignment variable="v" value="v0"/>
                <StateAssignment variable="U" value="v0 * b / MVOLT"/>
            </OnStart>

            <OnCondition test="v .gt. thresh">
                <StateAssignment variable="v" value="c * MVOLT"/>
                <StateAssignment variable="U" value="U + d"/>
                <EventOut port="spike"/>
            </OnCondition>
        </Dynamics>
    </ComponentType>
```

We can define **Component**s of the `izhikevichCell` **ComponentType** with the parameters we need.

For example, the `izhikevichCell` neuron model can exhibit different spiking behaviours, so we can define a regular spiking **Component**, and another **Component** that exhibits bursting.
Once these **Component**s are defined in the NeuroML document, we can use **Instance**s of them to create populations and networks, and so on.

Using LEMS to specify the core of NeuroML version 2 has the following significant advantages:

- NeuroML 2 XML files can be used standalone by applications in the same way as NeuroML v1.x, without using LEMS, easing the transition for v1.x compliant applications
- Any NeuroML 2 ComponentType can be extended and will be usable/translatable by any application (e.g. jLEMS) which understands LEMS

The first point above means that a parsing application does not have to natively read the LEMS type definition for, e.g. an izhikevichCell element, it just has to map the NeuroML element parameters onto its own object implementing that entity.
The behaviour should be the same and should be tested against the reference LEMS implementation ([jLEMS](http://github.com/LEMS/jLEMS/)).

The second point above means that if an application does support LEMS, it can automatically parse (and generate code for) a wide range of NeuroML 2 cells, channels and synapses, including any new ComponentType derived from these, without having to natively know anything about channels, cell models, etc.

```{admonition} jnml and pynml handle both LEMS and NeuroML 2.
:class: tip
{ref}`jNeuroML <jneuroML>` and {ref}`pynml <pyneuroml>` handle both LEMS and NeuroML 2.
They bundle jLEMS together with the LEMS definitions for NeuroML 2 ComponentTypes, and can simulate any LEMS model as well as many NeuroML 2 models.
```
