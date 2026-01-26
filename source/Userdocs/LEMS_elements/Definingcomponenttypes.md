
(lemsschema:page:defining_component_types_)=
# Defining component types



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
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
**properties**$ {ref}`lemsschema:property_`
**dynamicses**$ {ref}`lemsschema:dynamics_`
**structures**$ {ref}`lemsschema:structure_`
**simulations**$ {ref}`lemsschema:simulation_`
**equilibriums**$ {ref}`lemsschema:equilibrium_`
**procedures**$ {ref}`lemsschema:procedure_`
**geometries**$ {ref}`lemsschema:geometry_`
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ComponentType">
  <xs:sequence>
    <xs:element name="Property" type="Property" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Parameter" type="Parameter" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="DerivedParameter" type="DerivedParameter" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="IndexParameter" type="IndexParameter" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Constant" type="Constant" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Child" type="Child" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Children" type="Children" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Fixed" type="Fixed" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Link" type="Link" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="ComponentReference" type="ComponentReference" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Attachments" type="Attachments" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="EventPort" type="EventPort" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Exposure" type="Exposure" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Requirement" type="Requirement" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="ComponentRequirement" type="ComponentRequirement" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="InstanceRequirement" type="InstanceRequirement" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Path" type="Path" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Text" type="Text" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Dynamics" type="Dynamics" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Structure" type="Structure" minOccurs="0" maxOccurs="1"/>
    <xs:element name="Simulation" type="Simulation" minOccurs="0" maxOccurs="1"/>
  </xs:sequence>
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="extends" type="xs:string" use="optional"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<ComponentType name="Population">
    <ComponentReference name="component" type="Component"/>
    <Parameter name="size" dimension="none"/>
    <Structure>
        <MultiInstantiate number="size" component="component"/>
    </Structure>
</ComponentType>
```
```{code-block} xml
<ComponentType name="EventConnectivity">
    <Link name="source" type="Population"/>
    <Link name="target" type="Population"/>
    <Child name="Connections" type="ConnectionPattern"/>
</ComponentType>
```
```{code-block} xml
<ComponentType name="Network">
    <Children name="populations" type="Population"/>
    <Children name="connectivities" type="EventConnectivity"/>
</ComponentType>
```
```{code-block} xml
<ComponentType name="AllAll" extends="ConnectionPattern">
    <Structure>
        <ForEach instances="../source" as="a">
            <ForEach instances="../target" as="b">
                <EventConnection from="a" to="b"/>
            </ForEach>
        </ForEach>
    </Structure>
</ComponentType>
```
```{code-block} xml
<ComponentType name="ConnectionPattern"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Parameter">
  <xs:complexContent>
    <xs:extension base="NamedDimensionalType"/>
  </xs:complexContent>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Parameter name="size" dimension="none"/>
```
```{code-block} xml
<Parameter name="xmin" dimension="none"/>
```
```{code-block} xml
<Parameter name="xmax" dimension="none"/>
```
```{code-block} xml
<Parameter name="ymin" dimension="none"/>
```
```{code-block} xml
<Parameter name="ymax" dimension="none"/>
```
````
`````
(lemsschema:pathparameter_)=
## PathParameter

<i>A parameter of which the value is a path expression. When a ComponentType declares a PathParameter, a corresponding Component definition should have an attribute with that name whose value is a path expression that evaluates within the instance tree of the built model. This is used, for example, in the definition of a group component class, where the corresponding component specifies a path over the instance tree which selectesthe items that should go in the group.</i>

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Property">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="optional" default="none"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
  <xs:attribute name="defaultValue" type="xs:double" use="optional"/>
</xs:complexType>

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DerivedParameter">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="optional" default="none"/>
  <xs:attribute name="value" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<DerivedParameter name="erev" dimension="voltage" select="//MembranePotential[species=channel/species]/reversal"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Fixed">
  <xs:attribute name="parameter" type="xs:string" use="required"/>
  <xs:attribute name="value" type="PhysicalQuantity" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Fixed parameter="threshold" value="-45mV"/>
```
```{code-block} xml
<Fixed parameter="relativeConductance" value="0"/>
```
```{code-block} xml
<Fixed parameter="relativeConductance" value="1"/>
```
```{code-block} xml
<Fixed parameter="relativeConductance" value="0"/>
```
```{code-block} xml
<Fixed parameter="relativeConductance" value="1"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Requirement">
  <xs:complexContent>
    <xs:extension base="NamedDimensionalType"/>
  </xs:complexContent>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Requirement name="v" dimension="voltage"/>
```
```{code-block} xml
<Requirement name="v" dimension="voltage"/>
```
```{code-block} xml
<Requirement name="v" dimension="voltage"/>
```
```{code-block} xml
<Requirement name="v" dimension="voltage"/>
```
```{code-block} xml
<Requirement name="v" dimension="voltage"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ComponentRequirement">
  <xs:attribute name="name" type="xs:string" use="required"/>
</xs:complexType>

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="InstanceRequirement">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string" use="required"/>
</xs:complexType>

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Exposure">
  <xs:complexContent>
    <xs:extension base="NamedDimensionalType"/>
  </xs:complexContent>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Exposure name="v" dimension="voltage"/>
```
```{code-block} xml
<Exposure name="tsince" dimension="time"/>
```
```{code-block} xml
<Exposure name="r" dimension="per_time"/>
```
```{code-block} xml
<Exposure name="fcond" dimension="none"/>
```
```{code-block} xml
<Exposure name="fcond" dimension="none"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Child">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Child name="Connections" type="ConnectionPattern"/>
```
```{code-block} xml
<Child name="Forward" type="HHRate"/>
```
```{code-block} xml
<Child name="Reverse" type="HHRate"/>
```
```{code-block} xml
<Child name="Forward" type="HHRate"/>
```
```{code-block} xml
<Child name="Reverse" type="HHRate"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Children">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string" use="optional"/>
  <xs:attribute name="min" type="xs:integer" use="optional"/>
  <xs:attribute name="max" type="xs:integer" use="optional"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Children name="populations" type="Population"/>
```
```{code-block} xml
<Children name="connectivities" type="EventConnectivity"/>
```
```{code-block} xml
<Children name="lines" type="Line"/>
```
```{code-block} xml
<Children name="outputColumn" type="OutputColumn"/>
```
```{code-block} xml
<Children name="displays" type="Display"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Link">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Link name="source" type="Population"/>
```
```{code-block} xml
<Link name="target" type="Population"/>
```
```{code-block} xml
<Link name="from" type="KSState"/>
```
```{code-block} xml
<Link name="to" type="KSState"/>
```
```{code-block} xml
<Link name="from" type="KSState"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ComponentReference">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string" use="required"/>
  <xs:attribute name="local" type="xs:string" use="optional"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<ComponentReference name="component" type="Component"/>
```
```{code-block} xml
<ComponentReference name="target" type="Component"/>
```
```{code-block} xml
<ComponentReference name="channel" type="HHChannel"/>
```
```{code-block} xml
<ComponentReference name="component" type="Component"/>
```
```{code-block} xml
<ComponentReference name="synapse" type="Synapse"/>
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

<i>Specifies that instances of components based on this class can containe a named collection of other instances. This provides for containers for operating on groups of instances with path and filter expressions defined in components to operate over the instance tree.</i>

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EventPort">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="direction" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<EventPort name="spikes-in" direction="in"/>
```
```{code-block} xml
<EventPort name="a" direction="out"/>
```
```{code-block} xml
<EventPort name="in" direction="in"/>
```
```{code-block} xml
<EventPort name="out" direction="out"/>
```
```{code-block} xml
<EventPort name="in" direction="in"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Text">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Text name="title"/>
```
```{code-block} xml
<Text name="color"/>
```
```{code-block} xml
<Text name="path"/>
```
```{code-block} xml
<Text name="fileName"/>
```
```{code-block} xml
<Text name="destination"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Path">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Path name="quantity"/>
```
```{code-block} xml
<Path name="quantity"/>
```
```{code-block} xml
<Path name="from"/>
```
```{code-block} xml
<Path name="to"/>
```
```{code-block} xml
<Path name="quantity"/>
```
````
`````
(lemsschema:attachments_)=
## Attachments

<i>Specifies that a component can accept attached components of a particular class. Attached components can be added at build time dependent on other events. For scoping and access purposes they are like child components. The canonical use of attachments is in adding synapses to a cell when a network connection is made.</i>

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Attachments">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Attachments name="synapses" type="Synapse"/>
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IndexParameter">
  <xs:attribute name="name" type="xs:string" use="required"/>
</xs:complexType>

```
````
`````
(lemsschema:about_)=
## About

<i></i>


(lemsschema:meta_)=
## Meta

<i>Meta element to provide arbitrary metadata to LEMS simulations. Note that this is not processed by the LEMS interpreter.</i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Meta">
  <xs:sequence>
    <xs:any minOccurs="0" maxOccurs="unbounded" processContents="lax"/>
  </xs:sequence>
  <xs:anyAttribute processContents="skip"/>
</xs:complexType>

```
````
`````