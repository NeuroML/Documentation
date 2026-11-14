(userdocs:lemsoverview)=
# Model structure overview

% http://lems.github.io/LEMS/introduction.html

Models are based on user-defined types (the term ComponentType is used in the XML) that contain parameter declarations, reference declarations and specification of what children an instance of a type can have.
Typically they also contain a Dynamics specification which can contain build-time and run-time declarations.
Build-time declarations apply when a simulation is set up, for example to connect cells.
Run-time declarations specify the state variables, equations and events that are involved.

An instance of a ComponentType is a model Component It specifies a particular set of parameters for a given ComponentType. It says nothing about state variables: in a simulation, typically many run-time instances will correspond to a single model component definition, and several model component definitions will use the same type.
A run-time instance holds its own set of state variables as defined by the Type definition and a reference to its component for the parameter values specific to that particular model component.
The update rules come from the type definition.
As such, neither the ComponentType nor the Component is properly a "prototype" for the runtime instance.

(userdocs:lemsoverview:defining_component_types)=
## Defining ComponentTypes

ComponentTypes are declared as, for example:

```{code-block} xml
<ComponentType name="myCell">
   <Parameter name="threshold" dimension="voltage" />
</ComponentType>
```

A Component based on such a type is expressed as:

```{code-block} xml
<Component type="myCell" threshold="dimensional_quantity" />
```

The quoted value for 'threshold' here is a rich quantity with size and dimensions, typically consisting of a numerical value and a unit symbol.
Assignments like this are the only place unit symbols can occur.
Equations and expressions relate rich types, independent of any particular unit system.

An equivalent way of writing the above in shorthand notation (using an example of a string with size and dimension for threshold) is:

```{code-block} xml
<myCell threshold="-30 mV" />
```

A type can contain elements for specifying the following aspects of the structure and parameters of a model component:

- Parameter - dimensional quantities that remain fixed within a model
- Child - a required single sub-component of a given type
- Children - variable number of sub-components of the given type
- ComponentRef - a reference to a top-level component definition.
- Link - a reference to a component definition relative to the referrer
- Attachments - for build-time connections
- EventPort - for run-time discrete event communication
- Exposure - quantities that can be accessed from other components
- Requirement - quantities that must be accessible to the component for it to make sense
- DerivedParameter - like parameters, but derived from some other quantity in the model

The "EventPort" and "Attachments" declarations don't have any corresponding elements in their model component specification.
They only affect how the component can be used when a model is instantiated.
EventPorts specify that a model can send or receive events, and should match up with declarations in its Dynamics specification.
An "Attachments" declaration specifies that a run-time instance can have dynamically generated attachments as, for example, when a new synapse run-time instance is added to a cell for each incoming connection.

(userdocs:lemsoverview:inheritance)=
## Inheritance

A type can extend another type, adding new parameters, or supplying values (SetParam) for inherited parameters.
As well as reducing duplication, the key application of this is with the Child and Children declarations, where a type can specify that it needs a child or children of a particular supertype, but doesn't care about which particular sub-type is used in a model.
This applies, for example, where a cell requires synapses that compute a quantity with dimensions current, but doesn't need access to any other parts of the synapse Dynamics.

(userdocs:lemsoverview:runtime_dynamics)=
## Run-time Dynamics
Run time Dynamics are included within a Dynamics block in a type specification.
They include declaration of:

- state variables
- first order differential equations with respect to time of state variables
- derived quantities - things computed in terms of other local quantities or computed from other run-time instances

Run time Dynamics can be grouped into Regimes, where only one regime is operative at a given time for a particular run-time instance.
Regimes have access to all the variables in the parent instance and can define their own local variables.

Dynamics can also contain event blocks:

- OnStart blocks contain any initialization declarations needed when a run-time state is instantiated
- OnEvent blocks specify what happens when an event is received on a specified port
- OnEntry blocks (only within regimes) specify things that should happen each time the system enters that regime.
- OnCondition blocks have a test condition and specify what should happen when it is met.

Blocks may contain state variable assignments, event sending directives and transition directives to indicate that the system should change from one regime to another.

(userdocs:lemsoverview:buildtime_structure)=
## Build-time Structure
Build-time Structure defines the structure of a multi-component model.
Currently there are:

- MultiInstantiate - for declaring that a component yields multiple run-time instances corresponding to a particular model component. Eg, for defining populations of cells.
- ForEach - for iterating over multiple instances in the run-time structure
- EventConnection - for connecting ports between run-time instances

(userdocs:lemsoverview:other)=
## Other

There are also Run, Show and Record Dynamics for creating type definitions that define simulations and what should be recorded or displayed from such a simulation.

(userdocs:lemsoverview:observations)=
## Observations
The numerous references to "run-time instances" above is problematic, since the structures do not dictate any particular way of building a simulator or running a model.
In particular, there is no requirement that a component or Dynamics declaration should give rise to any particular collection of state variables that could be interpreted as a run-time instance in the state of a simulator.

So, it is convenient to think of eventual state instances, and that is indeed how the reference interpreter works, but the model specification structure should avoid anything that is specific to this picture.

(userdocs:lemsoverview:typespecific_examples)=
## Type specification examples
Examples of type definitions using the various types of child element:

```{code-block} xml
<ComponentType name="synapse">
   <EventPort direction="in" />
</ComponentType>
```
says that instances of components using this type can receive events.
```{code-block} xml
<ComponentType name="HHChannel">
   <Children name="gates" type="HHGate" />
</ComponentType>
```
says that a HHChannel can have gates.
```{code-block} xml
<ComponentType name="HHGate">
   <Child name="Forward" type="HHRate" />
   <Child name="Reverse" type="HHRate" />
</ComponentType>
```
says that a HHGate has two children called Forward and Reverse, each of type HHRate.
```{code-block} xml
<ComponentType name="synapseCell">
   <Attachments name="synapses" type="synapse" />
</ComponentType>
```
says that instances of components based on the synapseCell type can have instances of component based on the synapse type attached to them at build time.
```{code-block} xml
<ComponentType name="Population">
   <ComponentRef name="component" type="Component" />
</ComponentType>
```
says that components based on the Population type need a reference to a component of type Component (ie, anything) (which would then be used as the thing to be repeated in the population, but it doesn't say that here).
```{code-block} xml
<ComponentType name="EventConnectivity">
   <Link name="source" type="Population" />
</ComponentType>
```
says that EventConnectivity components need a relative path to a local component of type Population which will be accessed via the name "source".
The model component declarations corresponding to the channel and gate types would be:

```{code-block} xml
<Component type="HHChanne">
   <Component type="HHGate">
      <Component type="some_hh_gate_type" role="Forward" />
      <Component type="some_hh_gate_type" role="Reverse" />
   </Component>
</Component>
```
or, in the shorthand notation:

```{code-block} xml
<HHChannel>
   <HHGate>
      <Forward type="some_hh_gate_type" />
      <Reverse type="some_hh_gate_type" />
   </HHGate>
</HHChannel>
```
For the population type it would be:


```{code-block} xml
<Component id="myPopulation" type="population" component="myCellModel" />
```
And for the connections:

```{code-block} xml
<Component type="EventConnectivity" source="myPopulation" />
```
