
(lemsschema:page:defining_component_types_)=
# Defining component types



Generated on 22/08/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:componenttype_)=
## ComponentType

<i>Root element for defining LEMS Component Types.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name of the component type. This can be uses as an XML element name in the shorthand form whendefining components.
**eXtends**$ String$ The component type that this type inherits field definitions for, if any

```
````

````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**parameters**$ {ref}`lemsschema:parameter_`
**indexParameters**$ {ref}`lemsschema:indexparameter_`
**derivedParameters**$ {ref}`lemsschema:derivedparameter_`
**pathParameters**$ {ref}`lemsschema:pathparameter_`
**requirements**$ {ref}`lemsschema:requirement_`
**componentRequirements**$ {ref}`lemsschema:componentrequirement_`
**instanceRequirements**$ {ref}`lemsschema:instancerequirement_`
**exposures**$ {ref}`lemsschema:exposure_`
**childs**$ {ref}`lemsschema:child_`
**childrens**$ {ref}`lemsschema:children_`
**links**$ {ref}`lemsschema:link_`
**componentReferences**$ {ref}`lemsschema:componentreference_`
**componentTypeReferences**$ {ref}`lemsschema:componenttypereference_`
**locations**$ {ref}`lemsschema:location_`
**propertys**$ {ref}`lemsschema:property_`
**dynamicses**$ {ref}`lemsschema:dynamics_`
**structures**$ {ref}`lemsschema:structure_`
**simulations**$ {ref}`lemsschema:simulation_`
**equilibriums**$ {ref}`lemsschema:equilibrium_`
**procedures**$ {ref}`lemsschema:procedure_`
**geometrys**$ {ref}`lemsschema:geometry_`
**fixeds**$ {ref}`lemsschema:fixed_`
**constants**$ {ref}`lemsschema:constant_`
**attachmentses**$ {ref}`lemsschema:attachments_`
**eventPorts**$ {ref}`lemsschema:eventport_`
**paths**$ {ref}`lemsschema:path_`
**texts**$ {ref}`lemsschema:text_`
**collections**$ {ref}`lemsschema:collection_`
**pairCollections**$ {ref}`lemsschema:paircollection_`
**abouts**$ {ref}`lemsschema:about_`
**metas**$ {ref}`lemsschema:meta_`

```
````
`````
(lemsschema:parameter_)=
## Parameter

<i>A quantity, defined by name and dimension, that must be supplied when a Component of the enclosing ComponentType is defined</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name of the parameter. This is the name of the attribute to be used when the parameter is supplied in a component definition
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the parameter

```
````
`````
(lemsschema:pathparameter_)=
## PathParameter

<i>A parameter of which the value is a path expression. When a ComponentType declares a PathParameter, a corresponding Component definition should have an attibute with that name whose value is a path expression that evaluates within the instance tree of the built model. This is used, for example, in the definition of a group component class, where the coresponding component specifies a path over the instance tree which selectesthe items that should go in the group.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the parameter

```
````
`````
(lemsschema:property_)=
## Property

<i>An property on an instance of a component. Unlike a Parameter, a Property can very from instance to instance. It should be set with an Assign element within the build specification.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 
**dimension**$ String$ 
**defaultValue**$ String$ The defaultValue for the property must be a plain number (no units) giving the SI magnitude of the quantity.

```
````
`````
(lemsschema:derivedparameter_)=
## DerivedParameter

<i>A parameter that is a function of the Component's Parameters, which does not change with time. Its value can be supplied either with the 'value' attribute that evaluates within the scope of the definition, or with the 'select' attribute which gives a path to 'primary' version of the parameter. For example,  setting select='//MembranePotential[species=channel/species]/reversal' within the appropriate context allows  a channel's reversal potential to taken from a single global setting according to its permeant ion, rather than explicitly supplied locally.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name of the derived parameter
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the derived parameter
**select**$ String$ Path to the parameter that supplies the value. Exactly one of 'select' and 'value' is required.
**value**$ String$ A string defining the value of the element

```
````
`````
(lemsschema:fixed_)=
## Fixed

<i>Fixes the value of a parameter in the parent class, so that it does not have to be supplied separately in component definitions.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**parameter**$ String$ 
**value**$ String$ 

```
````
`````
(lemsschema:requirement_)=
## Requirement

<i>A Requirement gives the name and dimension of a quantity (parameter or variable) that should be accessible within the scope of a model component. This is only applicable for elements that can be included as children of other elements, where the scope comprises its own parameters and those in the scope of its enclosing element. Once a requirement has been declared, then the quantity can be used within the Dynamics definition of the component. It is the responsibility of an implementation to check that the component is only used in a context in which the requirement is met. A typical example is in defining membrand bound components which require access to the membrane potential  but where the variable that holds the potential itself is defined in the top level component.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ name
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the requirement

```
````
`````
(lemsschema:componentrequirement_)=
## ComponentRequirement

<i>The name of a component or component reference that must exist in the component hierarchy</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ name

```
````
`````
(lemsschema:instancerequirement_)=
## InstanceRequirement

<i>An instance that must be supplied at build time. Expressions can contain references to quantities in the instance</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ name

```
````
`````
(lemsschema:exposure_)=
## Exposure

<i>A quantity that is made available to other components in the simulation. Note that all variables in a Dynamics definition are private. If other components need access to them, then the definition should explicitly link them to an exposure defined in the component class</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the exposure element
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the element

```
````
`````
(lemsschema:child_)=
## Child

<i>Specifies that a component can have a child of a particular type. The name supplied here can be used in path expressions to access the component. This is useful, for example, where a component can have multiple children of the same type but with different roles, such as the forward and reverse transition rates in a channel.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the child
**type**$ String$ Reference to a component class, the value should be the name of the target class.
**description**$ String$ An optional description of the child

```
````
`````
(lemsschema:children_)=
## Children

<i>Specifies that a component can have children of a particular class. The class may refer to an extendedtype, in which case components of any class that extends the specified target class should be valid as child components</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the children
**type**$ String$ The class of component allowed as children.

```
````
`````
(lemsschema:link_)=
## Link

<i>Like a ComponentRef, but resolved relative to the enclosing object so the target must already be in the model. One or the other should be deprecated. The Link element has the same properties as ComponentRef. The Link element just establishes a connection with the target component, but leaves it in its existing place in the hierarchy. Variables in the target component can be accessed via the name of the link element.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ A name for the ComponentReference
**type**$ String$ The type of the target Component
**description**$ String$ An optional description of the ComponentReference

```
````
`````
(lemsschema:componentreference_)=
## ComponentReference

<i>A reference to another component. The target component can be accessed with path expressions in the same way as a child component, but can be defined independently</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ A name for the ComponentReference
**type**$ String$ The type of the target Component
**description**$ String$ An optional description of the ComponentReference

```
````
`````
(lemsschema:componenttypereference_)=
## ComponentTypeReference

<i>This is used in conjunction with PathParameter elements to specify the target class of selections defined within components operating over the instance tree.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 

```
````
`````
(lemsschema:collection_)=
## Collection

<i>Specifies that instances of components based on this class can containe a named collection of other instances. This provides for containers for oprating on groups of instances with path and filter expressions defined in components to operate over the instance tree.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 

```
````
`````
(lemsschema:paircollection_)=
## PairCollection

<i>Defines a named collection of paris of instances, similar to the Collection element.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 

```
````
`````
(lemsschema:eventport_)=
## EventPort

<i>A port on a component that can send or receive events, depending on the direction specified</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ Name of the EventPort
**direction**$ String$ 'IN' or 'OUT'
**description**$ String$ An optional description of the EventPort

```
````
`````
(lemsschema:text_)=
## Text

<i>Holds textual information that does not change the model but is needed for other purposes such as labelling graphs.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The textual content
**description**$ String$ An optional description of the element

```
````
`````
(lemsschema:path_)=
## Path

<i>Duplicates some functionality of PathParameter - the two should be merged.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ 

```
````
`````
(lemsschema:attachments_)=
## Attachments

<i>Specifies that a component can accept attached components of a particular class. Attached components can be added at build time dependent on other events. For scoping and access purposes they are like child components. The cannonical use of attachments is in adding synapses to a cell when a network connection is made.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ A name for the Attachments
**type**$ String$ The type of the Attachments

```
````
`````
(lemsschema:insertion_)=
## Insertion

<i></i>


(lemsschema:integerparameter_)=
## IntegerParameter

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name of the parameter. This is the name of the attribute to be used when the parameter is supplied in a component definition
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the parameter

```
````
`````
(lemsschema:indexparameter_)=
## IndexParameter

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name of the parameter. This is the name of the attribute to be used when the parameter is supplied in a component definition
**dimension**$ String$ The dimension, or 'none'. This should be the name of an already defined dimension element
**description**$ String$ An optional description of the parameter

```
````
`````
(lemsschema:about_)=
## About

<i></i>


(lemsschema:meta_)=
## Meta

<i>Meta element to provide arbitrary metadata to LEMS simulations. Note that this is not processed by the LEMS interpreter.</i>

