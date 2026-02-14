
(lemsschema:page:units_and_dimensions_)=
# Units and dimensions



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:dimension_)=
## Dimension

<i>A Dimenson element associated a name with a particular combination of  the standards SI base dimensions, mass, length, time, current, temperature and amount if substance (moles). Fractional dimensions are not currently supported.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name to be used when referring to this dimension from variable declaration or units
**m**$ int$ Mass
**l**$ int$ Length
**t**$ int$ Time
**i**$ int$ Current
**k**$ int$ Temperature
**n**$ int$ Amount of substance
**j**$ int$ Luminous intensity

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Dimension">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="m" type="xs:integer" use="optional" default="0"/>
  <xs:attribute name="l" type="xs:integer" use="optional" default="0"/>
  <xs:attribute name="t" type="xs:integer" use="optional" default="0"/>
  <xs:attribute name="i" type="xs:integer" use="optional" default="0"/>
  <xs:attribute name="k" type="xs:integer" use="optional" default="0"/>
  <xs:attribute name="n" type="xs:integer" use="optional" default="0"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Dimension name="voltage" m="1" l="2" t="-3" i="-1"/>
```
```{code-block} xml
<Dimension name="time" t="1"/>
```
```{code-block} xml
<Dimension name="conductance" m="-1" l="-2" t="3" i="2"/>
```
```{code-block} xml
<Dimension name="capacitance" m="-1" l="-2" t="4" i="2"/>
```
```{code-block} xml
<Dimension name="current" i="1"/>
```
````
`````
(lemsschema:unit_)=
## Unit

<i>A Unit associates a symbol with a dimension and a power of ten. For non-metric units a scale can be provided, as in '1 inch = 0.0254 m'. In this case there is a degeneracy between the power and the scale which is best resolved by not using the two together. The offset parameter is available for units which are not zero-offset, such as fahrenheit.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ As with constants, units are only referred to within expressions using their symbols, so the name is just for readability.
**symbol**$ String$ The symbol is used to refer to this unit inside compound expressions coutaining a number and a unit symbol. Such expressions can only occur on the right hand side of assignments statements.
**dimension**$ String$ Reference to the dimension for this unit
**power**$ int$ Power of ten
**scale**$ double$ Scale, only to be used for scales which are not powers of ten
**offset**$ double$ Offset for non zero-offset units

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Unit">
  <xs:attribute name="symbol" type="xs:string" use="required"/>
  <xs:attribute name="dimension" type="xs:string" use="required"/>
  <xs:attribute name="power" type="xs:integer" use="optional" default="0">
    <xs:annotation>
      <xs:documentation>Some have asked whether fractional dimensions should be allowed. Disallowing it until needed...</xs:documentation>
    </xs:annotation>
  </xs:attribute>
  <xs:attribute name="scale" type="xs:float" use="optional" default="1"/>
  <xs:attribute name="offset" type="xs:float" use="optional" default="0"/>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<Unit symbol="mV" dimension="voltage" power="-3"/>
```
```{code-block} xml
<Unit symbol="ms" dimension="time" power="-3"/>
```
```{code-block} xml
<Unit symbol="pS" dimension="conductance" power="-12"/>
```
```{code-block} xml
<Unit symbol="nS" dimension="conductance" power="-9"/>
```
```{code-block} xml
<Unit symbol="uF" dimension="capacitance" power="-6"/>
```
````
`````
(lemsschema:assertion_)=
## Assertion

<i>Assertions are not strictly part of the model, but can be included in a file as a consistency check.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**dimension**$ String$ The name of a dimension
**matches**$ String$ An expression involving dimensions. The dimensionality of the expression should match the dimensionality of the dimension reference.

```
````
`````