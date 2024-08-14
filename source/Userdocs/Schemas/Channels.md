
(schema:channels_)=
# Channels

**Defines voltage ( and concentration ) gated ion channel models. Ion channels will generally extend  {ref}`schema:baseionchannel`. The most commonly used voltage dependent gate will extend  {ref}`schema:basegate`.**

---


Original ComponentType definitions: [Channels.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Channels.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basevoltagedeprate)=

## *baseVoltageDepRate*




<i>Base ComponentType for voltage dependent rate. Produces a time varying rate **r** which depends on **v.**.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:basevoltageconcdeprate)=

## *baseVoltageConcDepRate*




extends *{ref}`schema:basevoltagedeprate`*



<i>Base ComponentType for voltage and concentration dependent rate. Produces a time varying rate **r** which depends on **v** and **caConc.**.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:basehhrate)=

## *baseHHRate*




extends *{ref}`schema:basevoltagedeprate`*



<i>Base ComponentType for rate which follow one of the typical forms for rate equations in the standard HH formalism, using the parameters **rate,** **midpoint** and **scale**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  ${ref}`schema:dimensions:voltage`
**rate**$  ${ref}`schema:dimensions:per_time`
**scale**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHRate">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="Nml2Quantity_pertime" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:hhexprate)=

## HHExpRate




extends *{ref}`schema:basehhrate`*



<i>Exponential form for rate equation ( Q: Should these be renamed hhExpRate, etc? ).</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:per_time`
**scale**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **r** =&nbsp;rate * exp((v - midpoint)/scale)&emsp;(exposed as **r**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHRate">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="Nml2Quantity_pertime" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:hhsigmoidrate)=

## HHSigmoidRate




extends *{ref}`schema:basehhrate`*



<i>Sigmoidal form for rate equation.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:per_time`
**scale**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **r** =&nbsp;rate / (1 + exp(0 - (v - midpoint)/scale))&emsp;(exposed as **r**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHRate">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="Nml2Quantity_pertime" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:hhexplinearrate)=

## HHExpLinearRate




extends *{ref}`schema:basehhrate`*



<i>Exponential linear form for rate equation. Linear for large positive **v,** exponentially decays for large negative **v.**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:per_time`
**scale**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **x** =&nbsp;(v - midpoint) / scale
    



<i>**Conditional Derived Variables**</i>
    
: IF x != 0 THEN
: &emsp; **r** = rate \* x / (1 - exp(0 - x)) &emsp;(exposed as **r**)
: IF x = 0 THEN
: &emsp; **r** = rate &emsp;(exposed as **r**)


````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHRate">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="Nml2Quantity_pertime" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:basevoltagedepvariable)=

## *baseVoltageDepVariable*




<i>Base ComponentType for voltage dependent variable **x,** which depends on **v.** Can be used for inf/steady state of rate variable.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:basevoltageconcdepvariable)=

## *baseVoltageConcDepVariable*




extends *{ref}`schema:basevoltagedepvariable`*



<i>Base ComponentType for voltage and calcium concentration dependent variable **x,** which depends on **v** and **caConc.**.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:basehhvariable)=

## *baseHHVariable*




extends *{ref}`schema:basevoltagedepvariable`*



<i>Base ComponentType for voltage dependent dimensionless variable which follow one of the typical forms for variable equations in the standard HH formalism, using the parameters **rate,** **midpoint,** **scale**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  ${ref}`schema:dimensions:voltage`
**rate**$  $Dimensionless
**scale**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHVariable">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="xs:float" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:hhexpvariable)=

## HHExpVariable




extends *{ref}`schema:basehhvariable`*



<i>Exponential form for variable equation.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhvariable`)* $Dimensionless
**scale**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **x** =&nbsp;rate * exp((v - midpoint)/scale)&emsp;(exposed as **x**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHVariable">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="xs:float" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:hhsigmoidvariable)=

## HHSigmoidVariable




extends *{ref}`schema:basehhvariable`*



<i>Sigmoidal form for variable equation.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhvariable`)* $Dimensionless
**scale**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **x** =&nbsp;rate / (1 + exp(0 - (v - midpoint)/scale))&emsp;(exposed as **x**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHVariable">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="xs:float" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:hhexplinearvariable)=

## HHExpLinearVariable




extends *{ref}`schema:basehhvariable`*



<i>Exponential linear form for variable equation. Linear for large positive **v,** exponentially decays for large negative **v.**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhvariable`)* $Dimensionless
**scale**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **a** =&nbsp;(v - midpoint) / scale
    : **x** =&nbsp;rate * a / (1 - exp(0 - a))&emsp;(exposed as **x**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HHVariable">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="type" type="NmlId" use="required"/>
      <xs:attribute name="rate" type="xs:float" use="optional"/>
      <xs:attribute name="midpoint" type="Nml2Quantity_voltage" use="optional"/>
      <xs:attribute name="scale" type="Nml2Quantity_voltage" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:basevoltagedeptime)=

## *baseVoltageDepTime*




<i>Base ComponentType for voltage dependent ComponentType producing value **t** with dimension time ( e.g. for time course of rate variable ). Note: time course would not normally be fit to exp/sigmoid etc.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**t**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:basevoltageconcdeptime)=

## *baseVoltageConcDepTime*




extends *{ref}`schema:basevoltagedeptime`*



<i>Base type for voltage and calcium concentration dependent ComponentType producing value **t** with dimension time ( e.g. for time course of rate variable ).</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**t**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**v**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:fixedtimecourse)=

## fixedTimeCourse




extends *{ref}`schema:basevoltagedeptime`*



<i>Time course of a fixed magnitude **tau** which can be used for the time course in  {ref}`schema:gatehhtauinf`,  {ref}`schema:gatehhratestau` or  {ref}`schema:gatehhratestauinf`.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**t**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **t** =&nbsp;tau&emsp;(exposed as **t**)
    





````
`````

(schema:baseq10settings)=

## *baseQ10Settings*




<i>Base ComponentType for a scaling to apply to gating variable time course, usually temperature dependent.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**q10**$  $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  ${ref}`schema:dimensions:temperature`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Q10Settings">
  <xs:attribute name="type" type="NmlId" use="required"/>
  <xs:attribute name="fixedQ10" type="Nml2Quantity_none" use="optional"/>
  <xs:attribute name="q10Factor" type="Nml2Quantity_none" use="optional"/>
  <xs:attribute name="experimentalTemp" type="Nml2Quantity_temperature" use="optional"/>
</xs:complexType>

```
````
`````

(schema:q10fixed)=

## q10Fixed




extends *{ref}`schema:baseq10settings`*



<i>A fixed value, **fixedQ10,** for the scaling of the time course of the gating variable.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fixedQ10**$  $Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**q10**$  *(from {ref}`schema:baseq10settings`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  *(from {ref}`schema:baseq10settings`)* ${ref}`schema:dimensions:temperature`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **q10** =&nbsp;fixedQ10&emsp;(exposed as **q10**)
    





````
`````

(schema:q10exptemp)=

## q10ExpTemp




extends *{ref}`schema:baseq10settings`*



<i>A value for the Q10 scaling which varies as a standard function of the difference between the current temperature, **temperature,** and the temperature at which the gating variable equations were determined, **experimentalTemp**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**experimentalTemp**$  ${ref}`schema:dimensions:temperature`
**q10Factor**$  $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**TENDEGREES** = 10K$  $ {ref}`schema:dimensions:temperature`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**q10**$  *(from {ref}`schema:baseq10settings`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  *(from {ref}`schema:baseq10settings`)* ${ref}`schema:dimensions:temperature`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **q10** =&nbsp;q10Factor^((temperature - experimentalTemp)/TENDEGREES)&emsp;(exposed as **q10**)
    





````
`````

(schema:baseconductancescaling)=

## *baseConductanceScaling*




<i>Base ComponentType for a scaling to apply to a gate's conductance, e.g. temperature dependent scaling.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**factor**$  $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  ${ref}`schema:dimensions:temperature`

```
````
`````

(schema:q10conductancescaling)=

## q10ConductanceScaling




extends *{ref}`schema:baseconductancescaling`*



<i>A value for the conductance scaling which varies as a standard function of the difference between the current temperature, **temperature,** and the temperature at which the conductance was originally determined, **experimentalTemp**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**experimentalTemp**$  ${ref}`schema:dimensions:temperature`
**q10Factor**$  $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**TENDEGREES** = 10K$  $ {ref}`schema:dimensions:temperature`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**factor**$  *(from {ref}`schema:baseconductancescaling`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  *(from {ref}`schema:baseconductancescaling`)* ${ref}`schema:dimensions:temperature`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **factor** =&nbsp;q10Factor^((temperature - experimentalTemp)/TENDEGREES)&emsp;(exposed as **factor**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Q10ConductanceScaling">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="q10Factor" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="experimentalTemp" type="Nml2Quantity_temperature" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Q10ConductanceScaling" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Q10ConductanceScaling
from neuroml.utils import component_factory

variable = component_factory(
    Q10ConductanceScaling,
    q10_factor: 'a Nml2Quantity_none (required)' = None,
    experimental_temp: 'a Nml2Quantity_temperature (required)' = None,
)
```
````
`````

(schema:baseconductancescalingcadependent)=

## *baseConductanceScalingCaDependent*




extends *{ref}`schema:baseconductancescaling`*



<i>Base ComponentType for a scaling to apply to a gate's conductance which depends on Ca concentration. Usually a generic expression of **caConc** ( so no standard, non-base form here ).</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**factor**$  *(from {ref}`schema:baseconductancescaling`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**temperature**$  *(from {ref}`schema:baseconductancescaling`)* ${ref}`schema:dimensions:temperature`

```
````
`````

(schema:basegate)=

## *baseGate*




<i>Base ComponentType for a voltage and/or concentration dependent gate.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  $Dimensionless
**q**$  $Dimensionless

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHUndetermined">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="forwardRate" type="HHRate" minOccurs="0"/>
        <xs:element name="reverseRate" type="HHRate" minOccurs="0"/>
        <xs:element name="timeCourse" type="HHTime" minOccurs="0"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="0"/>
        <xs:element name="subGate" type="GateFractionalSubgate" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
      <xs:attribute name="type" type="gateTypes" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:gate)=

## gate




extends *{ref}`schema:basegate`*



<i>Conveniently named baseGate.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHUndetermined">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="forwardRate" type="HHRate" minOccurs="0"/>
        <xs:element name="reverseRate" type="HHRate" minOccurs="0"/>
        <xs:element name="timeCourse" type="HHTime" minOccurs="0"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="0"/>
        <xs:element name="subGate" type="GateFractionalSubgate" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
      <xs:attribute name="type" type="gateTypes" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHUndetermined" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHUndetermined
from neuroml.utils import component_factory

variable = component_factory(
    GateHHUndetermined,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    type: 'a gateTypes (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    forward_rate: 'a HHRate (optional)' = None,
    reverse_rate: 'a HHRate (optional)' = None,
    time_course: 'a HHTime (optional)' = None,
    steady_state: 'a HHVariable (optional)' = None,
    sub_gates: 'list of GateFractionalSubgate(s) (optional)' = None,
)
```
````
`````

(schema:gatehhrates)=

## gateHHrates




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**alpha**$  ${ref}`schema:dimensions:per_time`
**beta**$  ${ref}`schema:dimensions:per_time`
**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**inf**$  $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **q**: Dimensionless &emsp;(exposed as **q**)









<i>**On Start**</i>
: **q** = inf





<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **alpha** =&nbsp;forwardRate->r&emsp;(exposed as **alpha**)
    : **beta** =&nbsp;reverseRate->r&emsp;(exposed as **beta**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    : **inf** =&nbsp;alpha/(alpha+beta)&emsp;(exposed as **inf**)
    : **tau** =&nbsp;1/((alpha+beta) * rateScale)&emsp;(exposed as **tau**)
    





<i>**Time Derivatives**</i>
    : d **q** /dt = (inf - q) / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHRates">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="forwardRate" type="HHRate" minOccurs="1"/>
        <xs:element name="reverseRate" type="HHRate" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHRates" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHRates
from neuroml.utils import component_factory

variable = component_factory(
    GateHHRates,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    forward_rate: 'a HHRate (required)' = None,
    reverse_rate: 'a HHRate (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<gateHHrates id="m" instances="3">
    <forwardRate type="HHExpLinearRate" rate="1per_ms" midpoint="-40mV" scale="10mV"/>
    <reverseRate type="HHExpRate" rate="4per_ms" midpoint="-65mV" scale="-18mV"/>
</gateHHrates>
```
```{code-block} xml
<gateHHrates id="h" instances="1">
    <forwardRate type="HHExpRate" rate="0.07per_ms" midpoint="-65mV" scale="-20mV"/>
    <reverseRate type="HHSigmoidRate" rate="1per_ms" midpoint="-35mV" scale="10mV"/>
</gateHHrates>
```
```{code-block} xml
<gateHHrates id="m" instances="3">
    <forwardRate type="HHExpLinearRate" rate="1per_ms" midpoint="-40mV" scale="10mV"/>
    <reverseRate type="HHExpRate" rate="4per_ms" midpoint="-65mV" scale="-18mV"/>
</gateHHrates>
```
````
`````

(schema:gatehhtauinf)=

## gateHHtauInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**inf**$  $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **q**: Dimensionless &emsp;(exposed as **q**)









<i>**On Start**</i>
: **q** = inf





<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    : **inf** =&nbsp;steadyState->x&emsp;(exposed as **inf**)
    : **tauUnscaled** =&nbsp;timeCourse->t
    : **tau** =&nbsp;tauUnscaled / rateScale&emsp;(exposed as **tau**)
    





<i>**Time Derivatives**</i>
    : d **q** /dt = (inf - q) / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHTauInf">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="timeCourse" type="HHTime" minOccurs="1"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHTauInf" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHTauInf
from neuroml.utils import component_factory

variable = component_factory(
    GateHHTauInf,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    time_course: 'a HHTime (required)' = None,
    steady_state: 'a HHVariable (required)' = None,
)
```
````
`````

(schema:gatehhinstantaneous)=

## gateHHInstantaneous




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism but is instantaneous, so tau = 0 and gate follows exactly inf value.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SEC** = 1 s$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**inf**$  $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **inf** =&nbsp;steadyState->x&emsp;(exposed as **inf**)
    : **tau** =&nbsp;0 * SEC&emsp;(exposed as **tau**)
    : **q** =&nbsp;inf&emsp;(exposed as **q**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHInstantaneous">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHInstantaneous" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHInstantaneous
from neuroml.utils import component_factory

variable = component_factory(
    GateHHInstantaneous,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    steady_state: 'a HHVariable (required)' = None,
)
```
````
`````

(schema:gatehhratestau)=

## gateHHratesTau




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`
**timeCourse**$  $ {ref}`schema:basevoltagedeptime`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**alpha**$  ${ref}`schema:dimensions:per_time`
**beta**$  ${ref}`schema:dimensions:per_time`
**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**inf**$  $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **q**: Dimensionless &emsp;(exposed as **q**)









<i>**On Start**</i>
: **q** = inf





<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **alpha** =&nbsp;forwardRate->r&emsp;(exposed as **alpha**)
    : **beta** =&nbsp;reverseRate->r&emsp;(exposed as **beta**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    : **inf** =&nbsp;alpha/(alpha+beta)&emsp;(exposed as **inf**)
    : **tauUnscaled** =&nbsp;timeCourse->t
    : **tau** =&nbsp;tauUnscaled / rateScale&emsp;(exposed as **tau**)
    





<i>**Time Derivatives**</i>
    : d **q** /dt = (inf - q) / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHRatesTau">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="forwardRate" type="HHRate" minOccurs="1"/>
        <xs:element name="reverseRate" type="HHRate" minOccurs="1"/>
        <xs:element name="timeCourse" type="HHTime" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHRatesTau" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHRatesTau
from neuroml.utils import component_factory

variable = component_factory(
    GateHHRatesTau,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    forward_rate: 'a HHRate (required)' = None,
    reverse_rate: 'a HHRate (required)' = None,
    time_course: 'a HHTime (required)' = None,
)
```
````
`````

(schema:gatehhratesinf)=

## gateHHratesInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**alpha**$  ${ref}`schema:dimensions:per_time`
**beta**$  ${ref}`schema:dimensions:per_time`
**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**inf**$  $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **q**: Dimensionless &emsp;(exposed as **q**)









<i>**On Start**</i>
: **q** = inf





<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **alpha** =&nbsp;forwardRate->r&emsp;(exposed as **alpha**)
    : **beta** =&nbsp;reverseRate->r&emsp;(exposed as **beta**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    : **inf** =&nbsp;steadyState->x&emsp;(exposed as **inf**)
    : **tau** =&nbsp;1/((alpha+beta) * rateScale)&emsp;(exposed as **tau**)
    





<i>**Time Derivatives**</i>
    : d **q** /dt = (inf - q) / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHRatesInf">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="forwardRate" type="HHRate" minOccurs="1"/>
        <xs:element name="reverseRate" type="HHRate" minOccurs="1"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHRatesInf" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHRatesInf
from neuroml.utils import component_factory

variable = component_factory(
    GateHHRatesInf,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    forward_rate: 'a HHRate (required)' = None,
    reverse_rate: 'a HHRate (required)' = None,
    steady_state: 'a HHVariable (required)' = None,
)
```
````
`````

(schema:gatehhratestauinf)=

## gateHHratesTauInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`
**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**alpha**$  ${ref}`schema:dimensions:per_time`
**beta**$  ${ref}`schema:dimensions:per_time`
**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**inf**$  $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **q**: Dimensionless &emsp;(exposed as **q**)









<i>**On Start**</i>
: **q** = inf





<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **alpha** =&nbsp;forwardRate->r&emsp;(exposed as **alpha**)
    : **beta** =&nbsp;reverseRate->r&emsp;(exposed as **beta**)
    : **inf** =&nbsp;steadyState->x&emsp;(exposed as **inf**)
    : **tauUnscaled** =&nbsp;timeCourse->t
    : **tau** =&nbsp;tauUnscaled / rateScale&emsp;(exposed as **tau**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    





<i>**Time Derivatives**</i>
    : d **q** /dt = (inf - q) / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateHHRatesTauInf">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="forwardRate" type="HHRate" minOccurs="1"/>
        <xs:element name="reverseRate" type="HHRate" minOccurs="1"/>
        <xs:element name="timeCourse" type="HHTime" minOccurs="1"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHRatesTauInf" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateHHRatesTauInf
from neuroml.utils import component_factory

variable = component_factory(
    GateHHRatesTauInf,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    forward_rate: 'a HHRate (required)' = None,
    reverse_rate: 'a HHRate (required)' = None,
    time_course: 'a HHTime (required)' = None,
    steady_state: 'a HHVariable (required)' = None,
)
```
````
`````

(schema:gatefractional)=

## gateFractional




extends {ref}`schema:gate`



<i>Gate composed of subgates contributing with fractional conductance.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`
**subGate**$  $ {ref}`schema:subgate`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **q** =&nbsp;subGate[*]->qfrac(reduce method: add)&emsp;(exposed as **q**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateFractional">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="subGate" type="GateFractionalSubgate" minOccurs="1" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateFractional" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateFractional
from neuroml.utils import component_factory

variable = component_factory(
    GateFractional,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    sub_gates: 'list of GateFractionalSubgate(s) (required)' = None,
)
```
````
`````

(schema:subgate)=

## subGate




<i>Gate composed of subgates contributing with fractional conductance.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fractionalConductance**$  $Dimensionless

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**inf**$  $Dimensionless
**q**$  $Dimensionless
**qfrac**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rateScale**$  $Dimensionless

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **q**: Dimensionless &emsp;(exposed as **q**)









<i>**On Start**</i>
: **q** = inf





<i>**Derived Variables**</i>
    : **inf** =&nbsp;steadyState->x&emsp;(exposed as **inf**)
    : **tauUnscaled** =&nbsp;timeCourse->t
    : **tau** =&nbsp;tauUnscaled / rateScale&emsp;(exposed as **tau**)
    : **qfrac** =&nbsp;q * fractionalConductance&emsp;(exposed as **qfrac**)
    





<i>**Time Derivatives**</i>
    : d **q** /dt = (inf - q) / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateFractionalSubgate">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="steadyState" type="HHVariable" minOccurs="1"/>
        <xs:element name="timeCourse" type="HHTime" minOccurs="1"/>
      </xs:all>
      <xs:attribute name="fractionalConductance" type="Nml2Quantity_none" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateFractionalSubgate" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateFractionalSubgate
from neuroml.utils import component_factory

variable = component_factory(
    GateFractionalSubgate,
    id: 'a NmlId (required)' = None,
    fractional_conductance: 'a Nml2Quantity_none (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    steady_state: 'a HHVariable (required)' = None,
    time_course: 'a HHTime (required)' = None,
)
```
````
`````

(schema:baseionchannel)=

## *baseIonChannel*




<i>Base for all ion channel ComponentTypes.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**neuroLexId**$ 

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**annotation**$  $ {ref}`schema:annotation`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  $Dimensionless
**g**$  ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:ionchannelpassive)=

## ionChannelPassive




extends {ref}`schema:ionchannel`



<i>Simple passive ion channel where the constant conductance through the channel is equal to **conductance**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**species**$ 

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **fopen** =&nbsp;1&emsp;(exposed as **fopen**)
    : **g** =&nbsp;conductance&emsp;(exposed as **g**)
    





````
`````

(schema:ionchannelhh)=

## ionChannelHH




extends *{ref}`schema:baseionchannel`*



<i>Note  {ref}`schema:ionchannel` and  {ref}`schema:ionchannelhh` are currently functionally identical. This is needed since many existing examples use ionChannel, some use ionChannelHH. NeuroML v2beta4 should remove one of these, probably ionChannelHH.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**species**$ 

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**conductanceScaling**$  $ {ref}`schema:baseconductancescaling`
**gates**$  $ {ref}`schema:gate`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **conductanceScale** =&nbsp;conductanceScaling[*]->factor(reduce method: multiply)
    : **fopen0** =&nbsp;gates[*]->fcond(reduce method: multiply)
    : **fopen** =&nbsp;conductanceScale * fopen0&emsp;(exposed as **fopen**)
    : **g** =&nbsp;conductance * fopen&emsp;(exposed as **g**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IonChannelHH">
  <xs:complexContent>
    <xs:extension base="IonChannel"/>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannelHH" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IonChannelHH
from neuroml.utils import component_factory

variable = component_factory(
    IonChannelHH,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    q10_conductance_scalings: 'list of Q10ConductanceScaling(s) (optional)' = None,
    species: 'a NmlId (optional)' = None,
    type: 'a channelTypes (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (optional)' = None,
    gates: 'list of GateHHUndetermined(s) (optional)' = None,
    gate_hh_rates: 'list of GateHHRates(s) (optional)' = None,
    gate_h_hrates_taus: 'list of GateHHRatesTau(s) (optional)' = None,
    gate_hh_tau_infs: 'list of GateHHTauInf(s) (optional)' = None,
    gate_h_hrates_infs: 'list of GateHHRatesInf(s) (optional)' = None,
    gate_h_hrates_tau_infs: 'list of GateHHRatesTauInf(s) (optional)' = None,
    gate_hh_instantaneouses: 'list of GateHHInstantaneous(s) (optional)' = None,
    gate_fractionals: 'list of GateFractional(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<ionChannelHH id="pas" conductance="10pS"/>
```
```{code-block} xml
<ionChannelHH id="HH_Na" conductance="10pS" species="na">  
        
    </ionChannelHH>
```
```{code-block} xml
<ionChannelHH id="NaConductance" conductance="10pS" species="na">
    <gateHHrates id="m" instances="3">
        <forwardRate type="HHExpLinearRate" rate="1per_ms" midpoint="-40mV" scale="10mV"/>
        <reverseRate type="HHExpRate" rate="4per_ms" midpoint="-65mV" scale="-18mV"/>
    </gateHHrates>
    <gateHHrates id="h" instances="1">
        <forwardRate type="HHExpRate" rate="0.07per_ms" midpoint="-65mV" scale="-20mV"/>
        <reverseRate type="HHSigmoidRate" rate="1per_ms" midpoint="-35mV" scale="10mV"/>
    </gateHHrates>
</ionChannelHH>
```
````
`````

(schema:ionchannel)=

## ionChannel




extends {ref}`schema:ionchannelhh`



<i>Note  {ref}`schema:ionchannel` and  {ref}`schema:ionchannelhh` are currently functionally identical. This is needed since many existing examples use ionChannel, some use ionChannelHH. NeuroML v2beta4 should remove one of these, probably ionChannelHH.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **conductanceScale** =&nbsp;conductanceScaling[*]->factor(reduce method: multiply)
    : **fopen0** =&nbsp;gates[*]->fcond(reduce method: multiply)
    : **fopen** =&nbsp;conductanceScale * fopen0&emsp;(exposed as **fopen**)
    : **g** =&nbsp;conductance * fopen&emsp;(exposed as **g**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IonChannel">
  <xs:complexContent>
    <xs:extension base="IonChannelScalable">
      <xs:choice>
        <xs:element name="gate" type="GateHHUndetermined" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateHHrates" type="GateHHRates" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateHHratesTau" type="GateHHRatesTau" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateHHtauInf" type="GateHHTauInf" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateHHratesInf" type="GateHHRatesInf" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateHHratesTauInf" type="GateHHRatesTauInf" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateHHInstantaneous" type="GateHHInstantaneous" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="gateFractional" type="GateFractional" minOccurs="0" maxOccurs="unbounded"/>
      </xs:choice>
      <xs:attribute name="species" type="NmlId" use="optional"/>
      <xs:attribute name="type" type="channelTypes" use="optional"/>
      <xs:attribute name="conductance" type="Nml2Quantity_conductance" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannel" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IonChannel
from neuroml.utils import component_factory

variable = component_factory(
    IonChannel,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    q10_conductance_scalings: 'list of Q10ConductanceScaling(s) (optional)' = None,
    species: 'a NmlId (optional)' = None,
    type: 'a channelTypes (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (optional)' = None,
    gates: 'list of GateHHUndetermined(s) (optional)' = None,
    gate_hh_rates: 'list of GateHHRates(s) (optional)' = None,
    gate_h_hrates_taus: 'list of GateHHRatesTau(s) (optional)' = None,
    gate_hh_tau_infs: 'list of GateHHTauInf(s) (optional)' = None,
    gate_h_hrates_infs: 'list of GateHHRatesInf(s) (optional)' = None,
    gate_h_hrates_tau_infs: 'list of GateHHRatesTauInf(s) (optional)' = None,
    gate_hh_instantaneouses: 'list of GateHHInstantaneous(s) (optional)' = None,
    gate_fractionals: 'list of GateFractional(s) (optional)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:ionchannelvshift)=

## ionChannelVShift




extends {ref}`schema:ionchannel`



<i>Same as  {ref}`schema:ionchannel`, but with a **vShift** parameter to change voltage activation of gates. The exact usage of **vShift** in expressions for rates is determined by the individual gates.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`
**vShift**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**species**$ 

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IonChannelVShift">
  <xs:complexContent>
    <xs:extension base="IonChannel">
      <xs:attribute name="vShift" type="Nml2Quantity_voltage" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannelVShift" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IonChannelVShift
from neuroml.utils import component_factory

variable = component_factory(
    IonChannelVShift,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    q10_conductance_scalings: 'list of Q10ConductanceScaling(s) (optional)' = None,
    species: 'a NmlId (optional)' = None,
    type: 'a channelTypes (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (optional)' = None,
    gates: 'list of GateHHUndetermined(s) (optional)' = None,
    gate_hh_rates: 'list of GateHHRates(s) (optional)' = None,
    gate_h_hrates_taus: 'list of GateHHRatesTau(s) (optional)' = None,
    gate_hh_tau_infs: 'list of GateHHTauInf(s) (optional)' = None,
    gate_h_hrates_infs: 'list of GateHHRatesInf(s) (optional)' = None,
    gate_h_hrates_tau_infs: 'list of GateHHRatesTauInf(s) (optional)' = None,
    gate_hh_instantaneouses: 'list of GateHHInstantaneous(s) (optional)' = None,
    gate_fractionals: 'list of GateFractional(s) (optional)' = None,
    v_shift: 'a Nml2Quantity_voltage (required)' = None,
)
```
````
`````

(schema:ksstate)=

## KSState




<i>One of the states in which a  {ref}`schema:gateks` can be. The rates of transitions between these states are given by  {ref}`schema:kstransition`s.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**relativeConductance**$  $Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**occupancy**$  $Dimensionless
**q**$  $Dimensionless

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **occupancy**: Dimensionless &emsp;(exposed as **occupancy**)







<i>**Derived Variables**</i>
    : **q** =&nbsp;relativeConductance * occupancy&emsp;(exposed as **q**)
    





````
`````

(schema:closedstate)=

## closedState




extends {ref}`schema:ksstate`



<i>A  {ref}`schema:ksstate` with **relativeConductance** of 0.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**relativeConductance**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**occupancy**$  *(from {ref}`schema:ksstate`)* $Dimensionless
**q**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ClosedState">
  <xs:complexContent>
    <xs:extension base="Base">
      </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ClosedState" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ClosedState
from neuroml.utils import component_factory

variable = component_factory(
    ClosedState,
    id: 'a NmlId (required)' = None,
)
```
````
`````

(schema:openstate)=

## openState




extends {ref}`schema:ksstate`



<i>A  {ref}`schema:ksstate` with **relativeConductance** of 1.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**relativeConductance**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**occupancy**$  *(from {ref}`schema:ksstate`)* $Dimensionless
**q**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="OpenState">
  <xs:complexContent>
    <xs:extension base="Base">
      </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=OpenState" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import OpenState
from neuroml.utils import component_factory

variable = component_factory(
    OpenState,
    id: 'a NmlId (required)' = None,
)
```
````
`````

(schema:ionchannelks)=

## ionChannelKS




extends *{ref}`schema:baseionchannel`*



<i>A kinetic scheme based ion channel with multiple  {ref}`schema:gateks`s, each of which consists of multiple  {ref}`schema:ksstate`s and  {ref}`schema:kstransition`s giving the rates of transition between them.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**species**$ 

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**conductanceScaling**$  $ {ref}`schema:baseconductancescaling`
**gates**$  $ {ref}`schema:gateks`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **fopen** =&nbsp;gates[*]->fcond(reduce method: multiply)&emsp;(exposed as **fopen**)
    : **g** =&nbsp;fopen * conductance&emsp;(exposed as **g**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IonChannelKS">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="gateKS" type="GateKS" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="species" type="NmlId" use="optional"/>
      <xs:attribute name="conductance" type="Nml2Quantity_conductance" use="optional"/>
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannelKS" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IonChannelKS
from neuroml.utils import component_factory

variable = component_factory(
    IonChannelKS,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    species: 'a NmlId (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gate_kses: 'list of GateKS(s) (optional)' = None,
)
```
````
`````

(schema:kstransition)=

## KSTransition




<i>Specified the forward and reverse rates of transition between two  {ref}`schema:ksstate`s in a  {ref}`schema:gateks`.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  ${ref}`schema:dimensions:per_time`
**rr**$  ${ref}`schema:dimensions:per_time`

```
````
`````

(schema:forwardtransition)=

## forwardTransition




extends {ref}`schema:kstransition`



<i>A forward only  {ref}`schema:kstransition` for a  {ref}`schema:gateks` which specifies a **rate** ( type  {ref}`schema:basehhrate` ) which follows one of the standard Hodgkin Huxley forms ( e.g.  {ref}`schema:hhexprate`,  {ref}`schema:hhsigmoidrate`,  {ref}`schema:hhexplinearrate`.</i>


`````{tab-set}
````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SEC** = 1s$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rate**$  $ {ref}`schema:basehhrate`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **rf0** =&nbsp;rate->r
    : **rf** =&nbsp;rf0&emsp;(exposed as **rf**)
    : **rr** =&nbsp;0/SEC&emsp;(exposed as **rr**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ForwardTransition">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:any processContents="skip" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="from" type="NmlId" use="required"/>
      <xs:attribute name="to" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ForwardTransition" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ForwardTransition
from neuroml.utils import component_factory

variable = component_factory(
    ForwardTransition,
    id: 'a NmlId (required)' = None,
    from_: 'a NmlId (required)' = None,
    to: 'a NmlId (required)' = None,
    anytypeobjs_=None,
)
```
````
`````

(schema:reversetransition)=

## reverseTransition




extends {ref}`schema:kstransition`



<i>A reverse only  {ref}`schema:kstransition` for a  {ref}`schema:gateks` which specifies a **rate** ( type  {ref}`schema:basehhrate` ) which follows one of the standard Hodgkin Huxley forms ( e.g.  {ref}`schema:hhexprate`,  {ref}`schema:hhsigmoidrate`,  {ref}`schema:hhexplinearrate`.</i>


`````{tab-set}
````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SEC** = 1s$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rate**$  $ {ref}`schema:basehhrate`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **rr0** =&nbsp;rate->r
    : **rr** =&nbsp;rr0&emsp;(exposed as **rr**)
    : **rf** =&nbsp;0/SEC&emsp;(exposed as **rf**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ReverseTransition">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:any processContents="skip" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="from" type="NmlId" use="required"/>
      <xs:attribute name="to" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ReverseTransition" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ReverseTransition
from neuroml.utils import component_factory

variable = component_factory(
    ReverseTransition,
    id: 'a NmlId (required)' = None,
    from_: 'a NmlId (required)' = None,
    to: 'a NmlId (required)' = None,
    anytypeobjs_=None,
)
```
````
`````

(schema:vhalftransition)=

## vHalfTransition




extends {ref}`schema:kstransition`



<i>Transition which specifies both the forward and reverse rates of transition.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gamma**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`
**tauMin**$  ${ref}`schema:dimensions:time`
**vHalf**$  ${ref}`schema:dimensions:voltage`
**z**$  $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**kte** = 25.3mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **rf0** =&nbsp;exp(z * gamma * (v - vHalf) / kte) / tau
    : **rr0** =&nbsp;exp(-z * (1 - gamma) * (v - vHalf) / kte) / tau
    : **rf** =&nbsp;1 / (1/rf0 + tauMin)&emsp;(exposed as **rf**)
    : **rr** =&nbsp;1 / (1/rr0 + tauMin)&emsp;(exposed as **rr**)
    





````
`````

(schema:tauinftransition)=

## tauInfTransition




extends {ref}`schema:kstransition`



<i>KS Transition specified in terms of time constant  {ref}`schema:tau` and steady state  {ref}`schema:inf`.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **tau** =&nbsp;timeCourse->t
    : **inf** =&nbsp;steadyState->x
    : **rf** =&nbsp;inf/tau&emsp;(exposed as **rf**)
    : **rr** =&nbsp;(1-inf)/tau&emsp;(exposed as **rr**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="TauInfTransition">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:all>
        <xs:element name="steadyState" type="HHVariable"/>
        <xs:element name="timeCourse" type="HHTime"/>
      </xs:all>
      <xs:attribute name="from" type="NmlId" use="required"/>
      <xs:attribute name="to" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=TauInfTransition" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import TauInfTransition
from neuroml.utils import component_factory

variable = component_factory(
    TauInfTransition,
    id: 'a NmlId (required)' = None,
    from_: 'a NmlId (required)' = None,
    to: 'a NmlId (required)' = None,
    steady_state: 'a HHVariable (required)' = None,
    time_course: 'a HHTime (required)' = None,
)
```
````
`````

(schema:gateks)=

## gateKS




extends *{ref}`schema:basegate`*



<i>A gate which consists of multiple  {ref}`schema:ksstate`s and  {ref}`schema:kstransition`s giving the rates of transition between them.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**states**$  $ {ref}`schema:ksstate`
**transitions**$  $ {ref}`schema:kstransition`
**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **q** =&nbsp;states[*]->q(reduce method: add)&emsp;(exposed as **q**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GateKS">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="q10Settings" type="Q10Settings" minOccurs="0"/>
        <xs:element name="closedState" type="ClosedState" minOccurs="1" maxOccurs="unbounded"/>
        <xs:element name="openState" type="OpenState" minOccurs="1" maxOccurs="unbounded"/>
        <xs:choice minOccurs="1" maxOccurs="unbounded">
          <xs:group ref="ForwardReverseTransition"/>
          <xs:element name="tauInfTransition" type="TauInfTransition"/>
        </xs:choice>
      </xs:sequence>
      <xs:attribute name="instances" type="PositiveInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateKS" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GateKS
from neuroml.utils import component_factory

variable = component_factory(
    GateKS,
    id: 'a NmlId (required)' = None,
    instances: 'a PositiveInteger (required)' = None,
    notes: 'a string (optional)' = None,
    q10_settings: 'a Q10Settings (optional)' = None,
    closed_states: 'list of ClosedState(s) (required)' = None,
    open_states: 'list of OpenState(s) (required)' = None,
    forward_transition: 'list of ForwardTransition(s) (required)' = None,
    reverse_transition: 'list of ReverseTransition(s) (required)' = None,
    tau_inf_transition: 'list of TauInfTransition(s) (required)' = None,
)
```
````
`````
