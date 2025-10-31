(userdocs:lems)=
# LEMS: Low Entropy Model Specification


% from http://lems.github.io/LEMS/index.html

A language for specifying hierarchical models based on fundamental physical relationships

```{admonition} LEMS
:class: dropdown tip
For an in-depth guide to LEMS, please see the research paper: [LEMS: a language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2](https://www.frontiersin.org/articles/10.3389/fninf.2014.00079/full). Documentation on the structure of the LEMS language can be found {ref}`here <userdocs:lemsschema>`.
```

LEMS is being developed to provide a compact, minimally redundant, human-readable, human-writable, declarative way of expressing models of biological systems.

It differs from other systems such as CellML or SBML in its requirement to be human writable and the inclusion of basic physical concepts such as dimensionality and physical nesting as part of the language.
The main goal is to enable model developers to write declarative models in LEMS in much the same way as software developers write software applications in computer languages such as in C, Java or Python.
The examples shown here use XML for expressing models as text, but LEMS is not primarily an XML language. Rather it defines a set of structures for representing models. The reference implementation also supports a more concise indentation-based format for representing models.

There are two independent implementations of LEMS: jLEMS, written in Java and pyLEMS written in Python.
Both are hosted on the github.com/LEMS.


(userdocs:lems:capabilities)=
## Capabilities
You can define ComponentTypes (e.g. a "HH channel" or "a bi-exponential synapse") which express the general properties of a particular type of thing that goes in a model.
This includes saying what parameters they have, what child elements they are allowed, and how they behave (the equations).

You can then define Components based on these types by supplying values for the parameters and adding any child elements that are required, so, for example, a bi-exponential synapse model with rise time 1ms and decay 5ms would be a component.

ComponentTypes can extend other ComponentTypes to add extra parameters, fix certain values, and otherwise modify their behavior.
Components can extend other Components to reuse specified parameter values.
There is also a loose notion of abstract types, so a component can accept children with a particular lineage without needing to know exactly what type they are.
This can be used, for example, to define cells that accept synaptic connections provided they have a particular signature.

Each ComponentType can have a Dynamics element that specifies how it behaves: what the state variables are, the equations that govern them, and what happens when events are sent or received.
The interpreter takes a model consisting of type and component elements referenced from a network, builds an instance from them and runs it.

For those familiar with object oriented languages, the ComponentType/Component distinction is close to the normal Class/Instance distinction.
When the model is run, the same pattern applies again, with the Components acting as class definitions, with their "instances" actually containing the state variables in the running mode.


(userdocs:lems:background)=
## Background

The March 2010 NeuroML meeting ([minutes](https://docs.neuroml.org/_static/files/NeuroMLWorkshop2010.pdf)) identified a need to extend the capability within NeuroML for expressing a range of models of synapses.
It was decided that the hitherto adopted approach of defining parameterized building blocks to construct models by combining blocks and setting parameters was unlikely to be flexible enough to cope with the needs for synapse models.
This is not obvious a-priori, since, for example, the pre NeuroML 2.0 ion channel building blocks are fully adequate to describe the dynamics of a wide range existing channel models.
But there appears to be no such commonality in models used for synapses, where the mechanisms used range from highly detailed biochemical models to much more abstract ones.

This work also has antecedents in Catacomb 3, which was essentially a GUI for a component definition system and model builder using a type system similar to that proposed here.
Much of the XML processing code used in the interpreter was taken from PSICS which itself currently uses the "building block" approach to model specification.
The need for user-defined types has been considered with respect to future PSICS development, and this proposal also reflects potential requirements for PSICS.

(userdocs:lems:example)=
## Example

Here is the XML for a simple integrate-and-fire cell definition:

```{code-block} xml
 <ComponentType name="refractiaf">
     <Parameter name="threshold" dimension="voltage"/>
     <Parameter name="refractoryPeriod" dimension="time"/>
     <Parameter name="capacitance" dimension="capacitance"/>
     <Parameter name="vleak" dimension="voltage"/>
     <Parameter name="gleak" dimension="conductance"/>

     <Parameter name="current" dimension="current"/>
     <Parameter name="vreset" dimension="voltage"/>
     <Parameter name="deltaV" dimension="voltage"/>
     <Parameter name="v0" dimension="voltage"/>

     <EventPort name="out" direction="out"/>
     <EventPort name="in" direction="in"/>

     <Exposure name="v" dimension="voltage"/>

     <Dynamics>
         <StateVariable name="v" exposure="v" dimension="voltage" />   
         <StateVariable name="tin" dimension="time"/>
         <OnStart>
             <StateAssignment variable="v" value="v0"/>
         </OnStart>

         <Regime name="refr">
             <OnEntry>
                 <StateAssignment variable="tin" value="t" />
                 <StateAssignment variable="v" value="vreset" />
             </OnEntry>
             <OnCondition test="t .gt. tin + refractoryPeriod">
                 <Transition regime="int" />
             </OnCondition>
         </Regime>

         <Regime name="int" initial="true">
             <TimeDerivative variable="v" value="(current + gleak * (vleak - v)) / capacitance" />
             <OnCondition test="v .gt. threshold">
                 <EventOut port="out" />
                 <Transition regime="refr" />
             </OnCondition>

         </Regime>
     </Dynamics>

 </ComponentType>
```

Once this definition is available, a particular model using this structure can be specified with the following XML:

```{code-block} xml
<refractiaf threshold="-40mV" refractoryPeriod="5ms" capacitance="1nF" vleak="-80mV" gleak="100pS" vreset="-70mV" v0="-70mV" deltaV="10mV" />
```

More complex models will have nested components and other types of parameters, but the basic principle of separating out the equations and parameters for reusable model components, such that the equations are only stated once, remains the same.
