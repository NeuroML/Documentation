
(lemsschema:page:structure_)=
# Structure



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:structure_)=
## Structure

<i>By default, each Component in a model gives rise to a single instance of its state variables when the model is executed. The state variables are then governed by the dynamics definition in the associated ComponentType. Elements in the Structure declaration  can be used to change this behavior, for example to make multiple instances of the state variables, or to instantiate a different component. A typical application for the latter would be a Component that defines a population of cells. The population Component might define the number of cells it contains but would refer to a Component defined elsewhere for the actual cell model to use.</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Structure">
  <xs:sequence>
    <xs:element name="ChildInstance" type="ChildInstance" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="MultiInstantiate" type="MultiInstantiate" minOccurs="0" maxOccurs="1"/>
    <xs:element name="ForEach" type="ForEach" minOccurs="0" maxOccurs="1"/>
    <xs:element name="With" type="With" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Tunnel" type="Tunnel" minOccurs="0" maxOccurs="1"/>
    <xs:element name="EventConnection" type="EventConnection" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Structure>
    <MultiInstantiate number="size" component="component"/>
</Structure>
```
```{code-block} xml
<Structure>
    <ForEach instances="../source" as="a">
        <ForEach instances="../target" as="b">
            <EventConnection from="a" to="b"/>
        </ForEach>
    </ForEach>
</Structure>
```
```{code-block} xml
<Structure>
    <ChildInstance component="channel"/>
</Structure>
```
```{code-block} xml
<Structure>
    <With instance="from" as="a"/>
    <With instance="to" as="b"/>
    <EventConnection from="a" to="b" receiver="synapse" receiverContainer="destination" sourcePort="sourcePort" targetPort="targetPort"/>
</Structure>
```
```{code-block} xml
<Structure>
    <MultiInstantiate number="size" component="component"/>
</Structure>
```
````
`````
(lemsschema:buildelement_)=
## BuildElement

<i>Base class for elements that can be used in Structures</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:multiinstantiate_)=
## MultiInstantiate

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="MultiInstantiate">
  <xs:attribute name="component" type="xs:string" use="required"/>
  <xs:attribute name="number" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<MultiInstantiate number="size" component="component"/>
```
```{code-block} xml
<MultiInstantiate number="size" component="component"/>
```
```{code-block} xml
<MultiInstantiate number="size" component="component"/>
```
```{code-block} xml
<MultiInstantiate number="size" component="component"/>
```
````
`````
(lemsschema:coinstantiate_)=
## CoInstantiate

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:assign_)=
## Assign

<i></i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Assign">
  <xs:attribute name="property" type="xs:string" use="required"/>
  <xs:attribute name="value" type="xs:string" use="required"/>
</xs:complexType>

```
````
`````
(lemsschema:choose_)=
## Choose

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:childinstance_)=
## ChildInstance

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChildInstance">
  <xs:attribute name="component" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<ChildInstance component="channel"/>
```
```{code-block} xml
<ChildInstance component="channel"/>
```
```{code-block} xml
<ChildInstance component="channel"/>
```
```{code-block} xml
<ChildInstance component="channel"/>
```
````
`````
(lemsschema:foreach_)=
## ForEach

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ForEach">
  <xs:sequence>
    <xs:element name="MultiInstantiate" type="MultiInstantiate" minOccurs="0" maxOccurs="1"/>
  </xs:sequence>
  <xs:attribute name="instances" type="xs:string" use="required"/>
  <xs:attribute name="as" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<ForEach instances="../source" as="a">
    <ForEach instances="../target" as="b">
        <EventConnection from="a" to="b"/>
    </ForEach>
</ForEach>
```
```{code-block} xml
<ForEach instances="../target" as="b">
    <EventConnection from="a" to="b"/>
</ForEach>
```
```{code-block} xml
<ForEach instances="../source" as="a">
    <ForEach instances="../target" as="b">
        <EventConnection from="a" to="b"/>
    </ForEach>
</ForEach>
```
```{code-block} xml
<ForEach instances="../target" as="b">
    <EventConnection from="a" to="b"/>
</ForEach>
```
```{code-block} xml
<ForEach instances="../source" as="a">
    <ForEach instances="../target" as="b">
        <EventConnection from="a" to="b"/>
    </ForEach>
</ForEach>
```
````
`````
(lemsschema:eventconnection_)=
## EventConnection

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EventConnection">
  <xs:sequence>
    <xs:element name="Assign" type="Assign" minOccurs="0" maxOccurs="1"/>
  </xs:sequence>
  <xs:attribute name="from" type="xs:string" use="required"/>
  <xs:attribute name="to" type="xs:string" use="required"/>
  <xs:attribute name="sourcePort" type="xs:string" use="optional"/>
  <xs:attribute name="targetPort" type="xs:string" use="optional"/>
  <xs:attribute name="receiver" type="xs:string" use="optional"/>
  <xs:attribute name="receiverContainer" type="xs:string" use="optional"/>
  <xs:attribute name="delay" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<EventConnection from="a" to="b"/>
```
```{code-block} xml
<EventConnection from="a" to="b" receiver="synapse" receiverContainer="destination" sourcePort="sourcePort" targetPort="targetPort"/>
```
```{code-block} xml
<EventConnection from="a" to="b"/>
```
```{code-block} xml
<EventConnection from="a" to="b"/>
```
````
`````
(lemsschema:tunnel_)=
## Tunnel

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Tunnel">
  <xs:sequence>
    <xs:element name="Assign" type="Assign" minOccurs="0" maxOccurs="1"/>
  </xs:sequence>
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="endA" type="xs:string" use="required"/>
  <xs:attribute name="endB" type="xs:string" use="required"/>
  <xs:attribute name="componentA" type="xs:string" use="required"/>
  <xs:attribute name="componentB" type="xs:string" use="required"/>
</xs:complexType>

```
````
`````
(lemsschema:pairseventconnection_)=
## PairsEventConnection

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:pairfilter_)=
## PairFilter

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:includepair_)=
## IncludePair

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:with_)=
## With

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="With">
  <xs:attribute name="instance" type="xs:string" use="optional"/>
  <xs:attribute name="list" type="xs:string" use="optional"/>
  <xs:attribute name="index" type="xs:string" use="optional"/>
  <xs:attribute name="as" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<With instance="from" as="a"/>
```
```{code-block} xml
<With instance="to" as="b"/>
```
````
`````
(lemsschema:if_)=
## If

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:apply_)=
## Apply

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:gather_)=
## Gather

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:gatherpairs_)=
## GatherPairs

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````