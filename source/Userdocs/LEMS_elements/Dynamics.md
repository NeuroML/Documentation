
(lemsschema:page:dynamics_)=
# Dynamics



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:dynamics_)=
## Dynamics

<i>Specifies the dynamical behavior of components build from this ComponentType. Note that all variables in a Dynamics definition are private. If other components need access to them, then the definition should explicitly link them to an Exposure defined in the component class</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**supers**$ {ref}`lemsschema:super_`
**derivedVariables**$ {ref}`lemsschema:derivedvariable_`
**conditionalDerivedVariables**$ {ref}`lemsschema:conditionalderivedvariable_`
**stateVariables**$ {ref}`lemsschema:statevariable_`
**timeDerivatives**$ {ref}`lemsschema:timederivative_`
**kineticSchemes**$ {ref}`lemsschema:kineticscheme_`
**onStarts**$ {ref}`lemsschema:onstart_`
**onEvents**$ {ref}`lemsschema:onevent_`
**onConditions**$ {ref}`lemsschema:oncondition_`
**stateScalarFields**$ {ref}`lemsschema:statescalarfield_`
**derivedScalarFields**$ {ref}`lemsschema:derivedscalarfield_`
**derivedPunctateFields**$ {ref}`lemsschema:derivedpunctatefield_`
**regimes**$ {ref}`lemsschema:regime_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Dynamics">
  <xs:sequence>
    <xs:element name="StateVariable" type="StateVariable" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="DerivedVariable" type="DerivedVariable" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="ConditionalDerivedVariable" type="ConditionalDerivedVariable" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="TimeDerivative" type="TimeDerivative" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="OnStart" type="OnStart" minOccurs="0" maxOccurs="1"/>
    <xs:element name="OnEvent" type="OnEvent" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="OnCondition" type="OnCondition" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Regime" type="Regime" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="KineticScheme" type="KineticScheme" minOccurs="0" maxOccurs="1"/>
  </xs:sequence>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Dynamics>
    <StateVariable name="t" dimension="time"/>
</Dynamics>
```
```{code-block} xml
<Dynamics>
    <StateVariable name="x" dimension="none"/>
    <DerivedVariable name="ex" dimension="none" value="exp(x)"/>
    <DerivedVariable name="q" dimension="none" value="ex / (1 + ex)"/>
    <DerivedVariable name="rf" dimension="per_time" select="Forward/r"/>
    <DerivedVariable name="rr" dimension="per_time" select="Reverse/r"/>
    <TimeDerivative variable="x" value="(1 + ex)^2 / ex * (rf * (1 - q) - rr * q)"/>
    <DerivedVariable name="fcond" dimension="none" exposure="fcond" value="q^power"/>
</Dynamics>
```
```{code-block} xml
<Dynamics>
    <StateVariable name="q" dimension="none"/>
    <DerivedVariable dimension="per_time" name="rf" select="Forward/r"/>
    <DerivedVariable dimension="per_time" name="rr" select="Reverse/r"/>
    <TimeDerivative variable="q" value="rf * (1 - q) - rr * q"/>
    <DerivedVariable name="fcond" dimension="none" exposure="fcond" value="q^power"/>
</Dynamics>
```
```{code-block} xml
<Dynamics>
    <OnStart>
        <StateAssignment variable="v" value="v0"/>
    </OnStart>
    <DerivedVariable name="totcurrent" dimension="current" select="populations[*]/current" reduce="add"/>
    <StateVariable name="v" exposure="v" dimension="voltage"/>
    <TimeDerivative variable="v" value="(totcurrent + injection) / capacitance"/>
</Dynamics>
```
```{code-block} xml
<Dynamics>
    <StateVariable name="v" exposure="v" dimension="voltage"/>
    <TimeDerivative variable="v" value="leakConductance * (leakReversal - v) / capacitance"/>
    <OnEvent port="spikes-in">
        <StateAssignment variable="v" value="v + deltaV"/>
    </OnEvent>
</Dynamics>
```
````
`````
(lemsschema:statevariable_)=
## StateVariable

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the state variable
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**exposure**$ String$ If this variable is to be accessed from outside, it should be linked to an Exposure that is defined in the ComponentType.
**description**$ String$ An optional description of the state variable

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="StateVariable">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="optional" default="none"/>
  <xs:attribute name="exposure" type="xs:string" use="optional"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<StateVariable name="t" dimension="time"/>
```
```{code-block} xml
<StateVariable name="v" exposure="v" dimension="voltage"/>
```
```{code-block} xml
<StateVariable name="tsince" exposure="tsince" dimension="time"/>
```
```{code-block} xml
<StateVariable name="tlast" dimension="time"/>
```
```{code-block} xml
<StateVariable name="q" dimension="none"/>
```
````
`````
(lemsschema:stateassignment_)=
## StateAssignment

<i>Has 'variable' and 'value' fields</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**variable**$ String$ The name of the variable
**value**$ String$ A string defining the value of the element

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="StateAssignment">
  <xs:attribute name="variable" type="xs:string" use="required"/>
  <xs:attribute name="value" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<StateAssignment variable="v" value="v + deltaV"/>
```
```{code-block} xml
<StateAssignment variable="tsince" value="0"/>
```
```{code-block} xml
<StateAssignment variable="tlast" value="t"/>
```
```{code-block} xml
<StateAssignment variable="v" value="v0"/>
```
```{code-block} xml
<StateAssignment variable="geff" value="0"/>
```
````
`````
(lemsschema:timederivative_)=
## TimeDerivative

<i>First order differential equations, functions of StateVariables and Parameters, for how StateVariables change with time. Has a variable and a value. The value is the rate of change of the variable.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**variable**$ String$ The name of the variable
**value**$ String$ A string defining the value of the element

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="TimeDerivative">
  <xs:attribute name="variable" type="xs:string" use="required"/>
  <xs:attribute name="value" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<TimeDerivative variable="v" value="leakConductance * (leakReversal - v) / capacitance"/>
```
```{code-block} xml
<TimeDerivative variable="tsince" value="1"/>
```
```{code-block} xml
<TimeDerivative variable="q" value="rf * (1 - q) - rr * q"/>
```
```{code-block} xml
<TimeDerivative variable="x" value="(1 + ex)^2 / ex * (rf * (1 - q) - rr * q)"/>
```
```{code-block} xml
<TimeDerivative variable="v" value="(totcurrent + injection) / capacitance"/>
```
````
`````
(lemsschema:derivedvariable_)=
## DerivedVariable

<i>A quantity that depends algebraically on other quantities in the model. The 'value' field can be set to a mathematical expression, or the 'select' field to a path expression. If the path expression produces multiple matches, then the 'reduce' field says how these are reduced to a single value by taking the sum or product.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the derived variable
**select**$ String$ A path to the variable that supplies the value. Note that to select a variable from another component, the variable must be marked as an Exposure. Exactly one of 'select' and 'value' is required
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the derived variable
**reduce**$ String$ Either 'add' or 'multiply'. This applies if there are multiple matches to the path or if 'required' is false. In the latter case, for multiply mode, multiplicative expressions in this variable behave as if the term was absent. Additive expressions generate an error. Conversely, if set to 'add' then additive expressions behave as if it was not there and multiplicative ones generateand error.
**exposure**$ String$ 
**required**$ boolean$ Set to true if it OK for this variable to be absent. See 'reduce' for what happens in this case
**value**$ String$ A string defining the value of the element

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DerivedVariable">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="optional" default="none"/>
  <xs:attribute name="exposure" type="xs:string" use="optional"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
  <xs:attribute name="select" type="xs:string" use="optional"/>
  <xs:attribute name="value" type="xs:string" use="optional"/>
  <xs:attribute name="reduce" type="xs:string" use="optional"/>
  <xs:attribute name="required" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<DerivedVariable name="tsince" dimension="time" exposure="tsince" value="t - tlast"/>
```
```{code-block} xml
<DerivedVariable name="r" dimension="per_time" exposure="r" value="rate * exp((v - midpoint)/scale)"/>
```
```{code-block} xml
<DerivedVariable name="r" dimension="per_time" exposure="r" value="rate / (1 + exp( -(v - midpoint)/scale))"/>
```
```{code-block} xml
<DerivedVariable name="x" dimension="none" value="(v - midpoint) / scale"/>
```
```{code-block} xml
<DerivedVariable name="r" dimension="per_time" exposure="r" value="rate * x / (1 - exp(-x))"/>
```
````
`````
(lemsschema:onstart_)=
## OnStart

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**stateAssignments**$ {ref}`lemsschema:stateassignment_`
**eventOuts**$ {ref}`lemsschema:eventout_`
**transitions**$ {ref}`lemsschema:transition_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="OnStart">
  <xs:sequence>
    <xs:element name="StateAssignment" type="StateAssignment" minOccurs="1" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<OnStart>
    <StateAssignment variable="v" value="v0"/>
</OnStart>
```
```{code-block} xml
<OnStart>
    <StateAssignment variable="geff" value="0"/>
</OnStart>
```
```{code-block} xml
<OnStart>
    <StateAssignment variable="v" value="v0"/>
</OnStart>
```
```{code-block} xml
<OnStart>
    <StateAssignment variable="v" value="v0"/>
</OnStart>
```
```{code-block} xml
<OnStart>
    <StateAssignment variable="v" value="v0"/>
</OnStart>
```
````
`````
(lemsschema:oncondition_)=
## OnCondition

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**stateAssignments**$ {ref}`lemsschema:stateassignment_`
**eventOuts**$ {ref}`lemsschema:eventout_`
**transitions**$ {ref}`lemsschema:transition_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="OnCondition">
  <xs:sequence>
    <xs:element name="StateAssignment" type="StateAssignment" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="EventOut" type="EventOut" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Transition" type="Transition" minOccurs="0" maxOccurs="1"/>
  </xs:sequence>
  <xs:attribute name="test" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<OnCondition test="tsince .gt. period">
    <StateAssignment variable="tsince" value="0"/>
    <EventOut port="a"/>
</OnCondition>
```
```{code-block} xml
<OnCondition test="t - tlast .gt. period">
    <StateAssignment variable="tlast" value="t"/>
    <EventOut port="a"/>
</OnCondition>
```
```{code-block} xml
<OnCondition test="v .gt. threshold">
    <EventOut port="out"/>
    <Transition regime="refr"/>
</OnCondition>
```
```{code-block} xml
<OnCondition test="t .gt. tin + refractoryPeriod">
    <Transition regime="int"/>
</OnCondition>
```
```{code-block} xml
<OnCondition test="tsince .gt. period">
    <StateAssignment variable="tsince" value="0"/>
    <EventOut port="a"/>
</OnCondition>
```
````
`````
(lemsschema:onevent_)=
## OnEvent

<i>Event handler block</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**port**$ String$ the port to listen on

```
````

````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**stateAssignments**$ {ref}`lemsschema:stateassignment_`
**eventOuts**$ {ref}`lemsschema:eventout_`
**transitions**$ {ref}`lemsschema:transition_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="OnEvent">
  <xs:sequence>
    <xs:element name="StateAssignment" type="StateAssignment" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="EventOut" type="EventOut" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute name="port" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<OnEvent port="spikes-in">
    <StateAssignment variable="v" value="v + deltaV"/>
</OnEvent>
```
```{code-block} xml
<OnEvent port="in">
    <StateAssignment variable="geff" value="geff + deltaG"/>
</OnEvent>
```
```{code-block} xml
<OnEvent port="in">
    <StateAssignment variable="v" value="v + deltaV"/>
</OnEvent>
```
```{code-block} xml
<OnEvent port="spikes-in">
    <StateAssignment variable="v" value="v + deltaV"/>
</OnEvent>
```
````
`````
(lemsschema:eventout_)=
## EventOut

<i></i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EventOut">
  <xs:attribute name="port" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<EventOut port="a"/>
```
```{code-block} xml
<EventOut port="a"/>
```
```{code-block} xml
<EventOut port="out"/>
```
```{code-block} xml
<EventOut port="a"/>
```
```{code-block} xml
<EventOut port="a"/>
```
````
`````
(lemsschema:kineticscheme_)=
## KineticScheme

<i>Allows the specification of systems that can be in one of a small number of states at any time with probabilistic transitions between states. This includes continuous time Markov processes as are used for stochastic models of ion channels. A kinetic scheme does not itself introduce any new elements or state variables. It is rather a way of connecting quantities in existing components by saying that quantities in the edge elements should be interpreted as transition rates among quantities in the node elements.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of kinetic scheme
**nodes**$ String$ Source of notes for scheme
**edges**$ String$ The element that provides the transitions for the scheme
**stateVariable**$ String$ Name of state variable in state elements
**edgeSource**$ String$ The name of the attribute in the rate element that defines the source of the transition
**edgeTarget**$ String$ Attribute that defines the target
**forwardRate**$ String$ Name of forward rate exposure
**reverseRate**$ String$ Name of reverse rate exposure

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="KineticScheme">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="nodes" type="xs:string" use="required"/>
  <xs:attribute name="stateVariable" type="xs:string" use="required"/>
  <xs:attribute name="edges" type="xs:string" use="required"/>
  <xs:attribute name="edgeSource" type="xs:string" use="required"/>
  <xs:attribute name="edgeTarget" type="xs:string" use="required"/>
  <xs:attribute name="forwardRate" type="xs:string" use="required"/>
  <xs:attribute name="reverseRate" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<KineticScheme name="ks" nodes="states" stateVariable="occupancy" edges="transitions" edgeSource="from" edgeTarget="to" forwardRate="rf" reverseRate="rr"/>
```
```{code-block} xml
<KineticScheme name="ks" nodes="states" stateVariable="occupancy" edges="transitions" edgeSource="from" edgeTarget="to" forwardRate="rf" reverseRate="rr" dependency="v" step="deltaV"/>
```
````
`````
(lemsschema:regime_)=
## Regime

<i>Allows the dynamics of a ComponentType to be expressed via a finite state machine. Each regime has its internal dynamics, and conditions on which transitions between regimes occur are specified using the OnCondition element</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name of the regime
**initial**$ String$ 'True' if this is the initial regime of the system

```
````

````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**derivedVariables**$ {ref}`lemsschema:derivedvariable_`
**stateVariables**$ {ref}`lemsschema:statevariable_`
**timeDerivatives**$ {ref}`lemsschema:timederivative_`
**onStarts**$ {ref}`lemsschema:onstart_`
**onEntrys**$ {ref}`lemsschema:onentry_`
**onEvents**$ {ref}`lemsschema:onevent_`
**onConditions**$ {ref}`lemsschema:oncondition_`
**requiredVars**$ {ref}`lemsschema:requiredvar_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Regime">
  <xs:sequence>
    <xs:element name="TimeDerivative" type="TimeDerivative" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="OnEntry" type="OnEntry" minOccurs="0" maxOccurs="1"/>
    <xs:element name="OnCondition" type="OnCondition" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="initial" type="TrueOrFalse" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Regime name="int" initial="true">
    <TimeDerivative variable="v" value="(current + gleak * (vleak - v)) / capacitance"/>
    <OnCondition test="v .gt. threshold">
        <EventOut port="out"/>
        <Transition regime="refr"/>
    </OnCondition>
    <OnEvent port="in">
        <StateAssignment variable="v" value="v + deltaV"/>
    </OnEvent>
</Regime>
```
```{code-block} xml
<Regime name="refr">
    <OnEntry>
        <StateAssignment variable="tin" value="t"/>
        <StateAssignment variable="v" value="vreset"/>
    </OnEntry>
    <OnCondition test="t .gt. tin + refractoryPeriod">
        <Transition regime="int"/>
    </OnCondition>
</Regime>
```
````
`````
(lemsschema:onentry_)=
## OnEntry

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**stateAssignments**$ {ref}`lemsschema:stateassignment_`
**eventOuts**$ {ref}`lemsschema:eventout_`
**transitions**$ {ref}`lemsschema:transition_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="OnEntry">
  <xs:sequence>
    <xs:element name="StateAssignment" type="StateAssignment" minOccurs="1" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<OnEntry>
    <StateAssignment variable="tin" value="t"/>
    <StateAssignment variable="v" value="vreset"/>
</OnEntry>
```
````
`````
(lemsschema:transition_)=
## Transition

<i></i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Transition">
  <xs:attribute name="regime" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Transition regime="int"/>
```
```{code-block} xml
<Transition regime="refr"/>
```
````
`````
(lemsschema:super_)=
## Super

<i></i>


(lemsschema:conditionalderivedvariable_)=
## ConditionalDerivedVariable

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 
**dimension**$ String$ 
**exposure**$ String$ 

```
````

````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**cases**$ {ref}`lemsschema:case_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ConditionalDerivedVariable">
  <xs:sequence>
    <xs:element name="Case" type="Case" minOccurs="1" maxOccurs="unbounded"/>
  </xs:sequence>
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="optional" default="none"/>
  <xs:attribute name="exposure" type="xs:string" use="optional"/>
</xs:complexType>

```
````
`````
(lemsschema:case_)=
## Case

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**value**$ String$ A string defining the value of the element

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Case">
  <xs:attribute name="condition" type="xs:string" use="optional"/>
  <xs:attribute name="value" type="xs:string" use="required"/>
</xs:complexType>

```
````
`````
(lemsschema:equilibrium_)=
## Equilibrium

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**derivedVariables**$ {ref}`lemsschema:derivedvariable_`

```
````
`````
(lemsschema:statescalarfield_)=
## StateScalarField

<i></i>


(lemsschema:derivedscalarfield_)=
## DerivedScalarField

<i></i>


(lemsschema:derivedpunctatefield_)=
## DerivedPunctateField

<i></i>

