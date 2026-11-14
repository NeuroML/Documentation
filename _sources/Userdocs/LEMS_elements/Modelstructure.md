
(lemsschema:page:model_structure_)=
# Model structure

**Models can be spread over multiple files. The root element in each file is Lems.**

---

Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:lems_)=
## Lems

<i>Root element for any lems content</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**dimensions**$ {ref}`lemsschema:dimension_`
**constants**$ {ref}`lemsschema:constant_`
**units**$ {ref}`lemsschema:unit_`
**assertions**$ {ref}`lemsschema:assertion_`
**componentTypes**$ {ref}`lemsschema:componenttype_`
**components**$ {ref}`lemsschema:component_`
**targets**$ {ref}`lemsschema:target_`

```
````
`````
(lemsschema:target_)=
## Target

<i>A lems file can contain many component definitions. A Target elements specifies that a components should be treated as the entry point for simulation or other processing</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**component**$ String$ Reference to the entry point component
**reportFile**$ String$ Optional attribute specifying file in which to save short report of simulation
**timesFile**$ String$ Optional attribute specifying file in which to save times used in simulation

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Target">
  <xs:attribute name="component" type="xs:string" use="required"/>
  <xs:attribute name="reportFile" type="xs:string" use="optional">
    <xs:annotation>
      <xs:documentation>jLEMS only optional attribute to also write a short report with simulation duration, version, etc.</xs:documentation>
    </xs:annotation>
  </xs:attribute>
  <xs:attribute name="timesFile" type="xs:string" use="optional">
    <xs:annotation>
      <xs:documentation>jLEMS only optional attribute to also write a file containing actual times used in the simulation.</xs:documentation>
    </xs:annotation>
  </xs:attribute>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Target component="sim1"/>
```
```{code-block} xml
<Target component="sim1"/>
```
```{code-block} xml
<Target component="sim1"/>
```
```{code-block} xml
<Target component="sim1"/>
```
```{code-block} xml
<Target component="sim1"/>
```
````
`````
(lemsschema:constant_)=
## Constant

<i>A constant quantity: like a parameter for which the value is supplied in the class definition itself rather than when a component is defined.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ A readable name for the constant.
**symbol**$ String$ The symbol used in expressions to refer to this constant.
**value**$ String$ The value of a constant must be a plain number (no units) giving the SI magnitude of the quantity or an expression involving only plain numbers or other constants.
**dimension**$ String$ 

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Constant">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="optional" default="none"/>
  <xs:attribute name="value" type="PhysicalQuantity" use="required"/>
  <xs:attribute name="description" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Constant name="kte" dimension="voltage" value="25.3mV"/>
```
```{code-block} xml
<Constant name="kte" dimension="voltage" value="25.3mV"/>
```
````
`````
(lemsschema:include_)=
## Include

<i>Include LEMS files in other LEMS files. Files are included where the Include declaration occurs.  The enclosing Lems block is stripped off and the rest of the content included as is</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**file**$ String$ the name or relative path of a file to be included

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Include">
  <xs:attribute name="file" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Include file="SimpleNetwork.xml"/>
```
```{code-block} xml
<Include file="SingleSimulation.xml"/>
```
```{code-block} xml
<Include file="ex2dims.xml"/>
```
```{code-block} xml
<Include file="hhchannel.xml"/>
```
```{code-block} xml
<Include file="hhcell.xml"/>
```
````
`````