
(lemsschema:page:dynamics_)=
# Dynamics



Generated on 02/05/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:dynamics_)=
## Dynamics

<i>Specifies the dynamical behavior of components build from this ComponentType.</i>

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

**name**$ String$ 
**dimension**$ String$ 
**exposure**$ String$ If this variable is to be accessed from outside, it should be linked to an Exposure that is defined in the ComponentType.

```
````
`````
(lemsschema:stateassignment_)=
## StateAssignment

<i>Has 'variable' and 'value' fields</i>


(lemsschema:timederivative_)=
## TimeDerivative

<i>Has a variable and a value. The value is the rate of change of the variable.</i>


(lemsschema:derivedvariable_)=
## DerivedVariable

<i>A quantity that depends algebraically on other quantities in the model. The 'value' field can be set to a mathematical expression, or the select field to a path expression. If the path expression produces multiple matches, then the 'reduce' field says how these are reduced to a single value by taking the sum or product.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 
**select**$ String$ 
**dimension**$ String$ 
**reduce**$ String$ Either 'add' or 'multiply'. This applies if ther are multiple matches to the path or if 'required' is false. In the latter case, for multiply mode, multiplicative expressions in this variable behave as if the term was absent. Additive expressions generate an error. Conversely, if set to 'add' then additive expressions behave as if it was not there and multiplicative ones generateand error.
**exposure**$ String$ 
**required**$ boolean$ Set to true if it OK for this variable to be absent. See 'reduce' for what happens in this case

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
`````
(lemsschema:eventout_)=
## EventOut

<i></i>


(lemsschema:kineticscheme_)=
## KineticScheme

<i>A kinetic scheme does not itself introduce any new elements or state variables. It is rather a way of connecting quantities in existing components by saying that quantities in the edge elements should be interpreted as transition rates among quantities in the node elements.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 
**nodes**$ String$ Source of notes for scheme
**edges**$ String$ The element that provides the transitions for the scheme
**stateVariable**$ String$ Name of state variable in state elements
**edgeSource**$ String$ The name of the attribute in the rate element that defines the source of the transition
**edgeTarget**$ String$ Attribute tha defines the target
**forwardRate**$ String$ Name of forward rate exposure
**reverseRate**$ String$ Name of reverse rate exposure

```
````
`````
(lemsschema:regime_)=
## Regime

<i></i>

`````{tab-set}
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
`````
(lemsschema:transition_)=
## Transition

<i></i>


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
`````
(lemsschema:case_)=
## Case

<i></i>


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

