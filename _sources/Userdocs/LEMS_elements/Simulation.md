
(lemsschema:page:simulation_)=
# Simulation



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:simulation_)=
## Simulation

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**records**$ {ref}`lemsschema:record_`
**eventRecords**$ {ref}`lemsschema:eventrecord_`
**runs**$ {ref}`lemsschema:run_`
**dataDisplays**$ {ref}`lemsschema:datadisplay_`
**dataWriters**$ {ref}`lemsschema:datawriter_`
**eventWriters**$ {ref}`lemsschema:eventwriter_`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Simulation">
  <xs:sequence>
    <xs:element name="DataDisplay" type="DataDisplay" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Record" type="Record" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="EventRecord" type="EventRecord" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Run" type="Run" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="DataWriter" type="DataWriter" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="EventWriter" type="EventWriter" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="Meta" type="Meta" minOccurs="0" maxOccurs="unbounded"/>
  </xs:sequence>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Simulation>
    <DataDisplay title="title" dataRegion="xmin,xmax,ymin,ymax"/>
</Simulation>
```
```{code-block} xml
<Simulation>
    <Record quantity="quantity" timeScale="timeScale" scale="scale" color="color"/>
</Simulation>
```
```{code-block} xml
<Simulation>
    <DataWriter path="path" fileName="fileName"/>
</Simulation>
```
```{code-block} xml
<Simulation>
    <Record quantity="quantity"/>
</Simulation>
```
```{code-block} xml
<Simulation>
    <Run component="target" variable="t" increment="step" total="length"/>
</Simulation>
```
````
`````
(lemsschema:record_)=
## Record

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**quantity**$ String$ path to the parameter that will contain the path to the quantity to be recorded
**scale**$ String$ path to the element that defines the scale for rendering the quantity dimensionless
**color**$ String$ hex format color suggestion for how the data should be displayed

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Record">
  <xs:attribute name="quantity" type="xs:string" use="required"/>
  <xs:attribute name="timeScale" type="xs:string" use="optional"/>
  <xs:attribute name="scale" type="xs:string" use="optional"/>
  <xs:attribute name="color" type="xs:string" use="optional"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Record quantity="quantity" timeScale="timeScale" scale="scale" color="color"/>
```
```{code-block} xml
<Record quantity="quantity"/>
```
```{code-block} xml
<Record quantity="quantity" timeScale="timeScale" scale="scale" color="color"/>
```
````
`````
(lemsschema:eventrecord_)=
## EventRecord

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**quantity**$ String$ path for the component which will emit spikes to be recorded
**eventPort**$ String$ event port for the component which will emit spikes

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EventRecord">
  <xs:attribute name="quantity" type="xs:string" use="required"/>
  <xs:attribute name="eventPort" type="xs:string" use="required"/>
</xs:complexType>

```
````
`````
(lemsschema:datadisplay_)=
## DataDisplay

<i></i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DataDisplay">
  <xs:attribute name="title" type="xs:string" use="required"/>
  <xs:attribute name="dataRegion" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<DataDisplay title="title" dataRegion="xmin,xmax,ymin,ymax"/>
```
```{code-block} xml
<DataDisplay title="title" dataRegion="xmin,xmax,ymin,ymax"/>
```
````
`````
(lemsschema:datawriter_)=
## DataWriter

<i></i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DataWriter">
  <xs:attribute name="path" type="xs:string" use="required"/>
  <xs:attribute name="fileName" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<DataWriter path="path" fileName="fileName"/>
```
````
`````
(lemsschema:eventwriter_)=
## EventWriter

<i></i>

`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EventWriter">
  <xs:attribute name="path" type="xs:string" use="required"/>
  <xs:attribute name="fileName" type="xs:string" use="required"/>
  <xs:attribute name="format" type="xs:string" use="required"/>
</xs:complexType>

```
````
`````
(lemsschema:run_)=
## Run

<i>The run element provides a way to make a model runnable. It should point to the parameters that set the step size etc. The target parameters have to be dimensionally consistent.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**component**$ String$ name of the component reference that will set the component to be run
**variable**$ String$ 
**increment**$ String$ path to the parameter that sets the step size
**total**$ String$ path to the parameter that sets the total span of the independent variable to be run

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Run">
  <xs:attribute name="component" type="xs:string" use="required"/>
  <xs:attribute name="variable" type="xs:string" use="required"/>
  <xs:attribute name="increment" type="xs:string" use="required"/>
  <xs:attribute name="total" type="xs:string" use="required"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Run component="target" variable="t" increment="step" total="length"/>
```
```{code-block} xml
<Run component="target" variable="t" increment="step" total="length"/>
```
````
`````