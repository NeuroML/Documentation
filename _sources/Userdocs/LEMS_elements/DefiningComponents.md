
(lemsschema:page:defining_components_)=
# Defining Components



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:component_)=
## Component

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**id**$ String$ 
**name**$ String$ Name by which the component was declared - this shouldn't be accessible.
**declaredType**$ String$ Name by which the component was declared - this shouldn't be accessible.
**type**$ String$ 
**eXtends**$ String$ 

```
````

````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**insertions**$ {ref}`lemsschema:insertion_`
**components**$ {ref}`lemsschema:component_`
**abouts**$ {ref}`lemsschema:about_`
**metas**$ {ref}`lemsschema:meta_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Component">
  <xs:sequence>
    <xs:any minOccurs="0" maxOccurs="unbounded" processContents="lax"/>
  </xs:sequence>
  <xs:anyAttribute processContents="skip"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Component id="ctb" type="iaf1" threshold="-30 mV" refractoryPeriod="2 ms" capacitance="1uF"/>
```
```{code-block} xml
<Component id="celltype_c" type="iaf3" leakConductance="3 pS" refractoryPeriod="3 ms" threshold="45 mV" leakReversal="-50 mV" deltaV="5mV" capacitance="1uF"/>
```
```{code-block} xml
<Component id="gen1" type="spikeGenerator" period="30ms"/>
```
```{code-block} xml
<Component id="gen2" type="spikeGenerator2" period="32ms"/>
```
```{code-block} xml
<Component id="iaf3cpt" type="iaf3" leakReversal="-50mV" deltaV="50mV" threshold="-30mV" leakConductance="50pS" refractoryPeriod="4ms" capacitance="1pF"/>
```
````
`````