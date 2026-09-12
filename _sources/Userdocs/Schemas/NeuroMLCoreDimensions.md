
(schema:neuromlcoredimensions_)=
# NeuroMLCoreDimensions




Original ComponentType definitions: [NeuroMLCoreDimensions.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//NeuroMLCoreDimensions.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:dimensions:*)=
## Dimensions

(schema:dimensions:area)=
### area

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:cm2`

- Defined unit: {ref}`schema:units:m2`

- Defined unit: {ref}`schema:units:um2`

````



`````

(schema:dimensions:capacitance)=
### capacitance

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`-1` L{superscript}`-2` T{superscript}`4` I{superscript}`2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:F`

- Defined unit: {ref}`schema:units:nF`

- Defined unit: {ref}`schema:units:pF`

- Defined unit: {ref}`schema:units:uF`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_capacitance">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(F|uF|nF|pF)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:charge)=
### charge

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
T{superscript}`1` I{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:C`

- Defined unit: {ref}`schema:units:e`

````



`````

(schema:dimensions:charge_per_mole)=
### charge\_per\_mole

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
T{superscript}`1` I{superscript}`1` N{superscript}`-1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:C_per_mol`

- Defined unit: {ref}`schema:units:nA_ms_per_amol`

- Defined unit: {ref}`schema:units:pC_per_umol`

````



`````

(schema:dimensions:concentration)=
### concentration

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`-3` N{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:M`

- Defined unit: {ref}`schema:units:mM`

- Defined unit: {ref}`schema:units:mol_per_cm3`

- Defined unit: {ref}`schema:units:mol_per_m3`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_concentration">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(mol_per_m3|mol_per_cm3|M|mM)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:conductance)=
### conductance

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`-1` L{superscript}`-2` T{superscript}`3` I{superscript}`2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:S`

- Defined unit: {ref}`schema:units:mS`

- Defined unit: {ref}`schema:units:nS`

- Defined unit: {ref}`schema:units:pS`

- Defined unit: {ref}`schema:units:uS`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_conductance">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(S|mS|uS|nS|pS)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:conductanceDensity)=
### conductanceDensity

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`-1` L{superscript}`-4` T{superscript}`3` I{superscript}`2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:S_per_cm2`

- Defined unit: {ref}`schema:units:S_per_m2`

- Defined unit: {ref}`schema:units:mS_per_cm2`

- Defined unit: {ref}`schema:units:uS_per_cm2`

````



`````

(schema:dimensions:conductance_per_voltage)=
### conductance\_per\_voltage

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`-2` L{superscript}`-4` T{superscript}`6` I{superscript}`3` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:S_per_V`

- Defined unit: {ref}`schema:units:nS_per_mV`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_conductancePerVoltage">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(S_per_V|nS_per_mV)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:current)=
### current

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
I{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:A`

- Defined unit: {ref}`schema:units:nA`

- Defined unit: {ref}`schema:units:pA`

- Defined unit: {ref}`schema:units:uA`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_current">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(A|uA|nA|pA)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:currentDensity)=
### currentDensity

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`-2` I{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:A_per_m2`

- Defined unit: {ref}`schema:units:mA_per_cm2`

- Defined unit: {ref}`schema:units:uA_per_cm2`

````



`````

(schema:dimensions:idealGasConstantDims)=
### idealGasConstantDims

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`1` L{superscript}`2` T{superscript}`-2` K{superscript}`-1` N{superscript}`-1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:J_per_K_per_mol`

- Defined unit: {ref}`schema:units:fJ_per_K_per_umol`

````



`````

(schema:dimensions:length)=
### length

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:cm`

- Defined unit: {ref}`schema:units:m__`

- Defined unit: {ref}`schema:units:um`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_length">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(m|cm|um)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:per_time)=
### per\_time

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
T{superscript}`-1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:Hz`

- Defined unit: {ref}`schema:units:per_hour`

- Defined unit: {ref}`schema:units:per_min`

- Defined unit: {ref}`schema:units:per_ms`

- Defined unit: {ref}`schema:units:per_s`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_pertime">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(per_s|per_ms|Hz)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:per_voltage)=
### per\_voltage

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`-1` L{superscript}`-2` T{superscript}`3` I{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:per_V`

- Defined unit: {ref}`schema:units:per_mV`

````



`````

(schema:dimensions:permeability)=
### permeability

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`1` T{superscript}`-1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:cm_per_ms`

- Defined unit: {ref}`schema:units:cm_per_s`

- Defined unit: {ref}`schema:units:m_per_s`

- Defined unit: {ref}`schema:units:um_per_ms`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_permeability">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(m_per_s|um_per_ms|cm_per_s|cm_per_ms)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:resistance)=
### resistance

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`1` L{superscript}`2` T{superscript}`-3` I{superscript}`-2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:Mohm`

- Defined unit: {ref}`schema:units:kohm`

- Defined unit: {ref}`schema:units:ohm`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_resistance">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(ohm|kohm|Mohm)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:resistivity)=
### resistivity

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`2` L{superscript}`2` T{superscript}`-3` I{superscript}`-2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:kohm_cm`

- Defined unit: {ref}`schema:units:ohm_cm`

- Defined unit: {ref}`schema:units:ohm_m`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:complexType name="Resistivity">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="value" type="Nml2Quantity_resistivity" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

`````

(schema:dimensions:rho_factor)=
### rho\_factor

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`-1` T{superscript}`-1` I{superscript}`-1` N{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:mol_per_cm_per_uA_per_ms`

- Defined unit: {ref}`schema:units:mol_per_m_per_A_per_s`

- Defined unit: {ref}`schema:units:umol_per_cm_per_nA_per_ms`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_rhoFactor">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(mol_per_m_per_A_per_s|mol_per_cm_per_uA_per_ms)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:specificCapacitance)=
### specificCapacitance

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`-1` L{superscript}`-4` T{superscript}`4` I{superscript}`2` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:F_per_m2`

- Defined unit: {ref}`schema:units:uF_per_cm2`

````



`````

(schema:dimensions:substance)=
### substance

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
N{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:mol`

````



`````

(schema:dimensions:temperature)=
### temperature

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
K{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:K`

- Defined unit: {ref}`schema:units:degC`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_temperature">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(degC)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:time)=
### time

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
T{superscript}`1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:hour`

- Defined unit: {ref}`schema:units:min`

- Defined unit: {ref}`schema:units:ms__`

- Defined unit: {ref}`schema:units:s__`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_time">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(s|ms)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:voltage)=
### voltage

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
M{superscript}`1` L{superscript}`2` T{superscript}`-3` I{superscript}`-1` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:V`

- Defined unit: {ref}`schema:units:mV`

````


````{grid-item-card} Schema
:columns: 12
```{code-block} xml
<xs:simpleType name="Nml2Quantity_voltage">
  <xs:restriction base="xs:string">
    <xs:pattern value="-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(V|mV)"/>
  </xs:restriction>
</xs:simpleType>

```
````

`````

(schema:dimensions:volume)=
### volume

`````{grid}
:gutter: 2


````{grid-item-card} Dimensions
:columns: 6
L{superscript}`3` 
````

````{grid-item-card} Units
:columns: 6

- Defined unit: {ref}`schema:units:cm3`

- Defined unit: {ref}`schema:units:litre`

- Defined unit: {ref}`schema:units:m3`

- Defined unit: {ref}`schema:units:um3`

````



`````



## Units

(schema:units:A)=
### A

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 A = 1.00e+09 {ref}`schema:units:nA`
- 1 A = 1.00e+12 {ref}`schema:units:pA`
- 1 A = 1.00e+06 {ref}`schema:units:uA`

```
````

(schema:units:A_per_m2)=
### A_per_m2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:currentDensity`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 A_per_m2 = 0.1 {ref}`schema:units:mA_per_cm2`
- 1 A_per_m2 = 100 {ref}`schema:units:uA_per_cm2`

```
````

(schema:units:C)=
### C

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:charge`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 C = 6.24e+18 {ref}`schema:units:e`

```
````

(schema:units:C_per_mol)=
### C_per_mol

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:charge_per_mole`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 C_per_mol = 1e-06 {ref}`schema:units:nA_ms_per_amol`
- 1 C_per_mol = 1.00e+06 {ref}`schema:units:pC_per_umol`

```
````

(schema:units:F)=
### F

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 F = 1.00e+09 {ref}`schema:units:nF`
- 1 F = 1.00e+12 {ref}`schema:units:pF`
- 1 F = 1.00e+06 {ref}`schema:units:uF`

```
````

(schema:units:F_per_m2)=
### F_per_m2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:specificCapacitance`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 F_per_m2 = 100 {ref}`schema:units:uF_per_cm2`

```
````

(schema:units:Hz)=
### Hz

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 Hz = 3600 {ref}`schema:units:per_hour`
- 1 Hz = 60 {ref}`schema:units:per_min`
- 1 Hz = 0.001 {ref}`schema:units:per_ms`
- 1 Hz = 1 {ref}`schema:units:per_s`

```
````

(schema:units:J_per_K_per_mol)=
### J_per_K_per_mol

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:idealGasConstantDims`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 J_per_K_per_mol = 1.00e+09 {ref}`schema:units:fJ_per_K_per_umol`

```
````

(schema:units:K)=
### K

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:temperature`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 K = -272.15 {ref}`schema:units:degC`

```
````

(schema:units:M)=
### M

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 3



```

```{grid-item-card} Conversions

- 1 M = 1000 {ref}`schema:units:mM`
- 1 M = 0.001 {ref}`schema:units:mol_per_cm3`
- 1 M = 1000 {ref}`schema:units:mol_per_m3`

```
````

(schema:units:Mohm)=
### Mohm

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:resistance`
- Power of 10: 6



```

```{grid-item-card} Conversions

- 1 Mohm = 1000 {ref}`schema:units:kohm`
- 1 Mohm = 1.00e+06 {ref}`schema:units:ohm`

```
````

(schema:units:S)=
### S

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 S = 1000 {ref}`schema:units:mS`
- 1 S = 1.00e+09 {ref}`schema:units:nS`
- 1 S = 1.00e+12 {ref}`schema:units:pS`
- 1 S = 1.00e+06 {ref}`schema:units:uS`

```
````

(schema:units:S_per_V)=
### S_per_V

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance_per_voltage`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 S_per_V = 1.00e+06 {ref}`schema:units:nS_per_mV`

```
````

(schema:units:S_per_cm2)=
### S_per_cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: 4



```

```{grid-item-card} Conversions

- 1 S_per_cm2 = 10000 {ref}`schema:units:S_per_m2`
- 1 S_per_cm2 = 1000 {ref}`schema:units:mS_per_cm2`
- 1 S_per_cm2 = 1.00e+06 {ref}`schema:units:uS_per_cm2`

```
````

(schema:units:S_per_m2)=
### S_per_m2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 S_per_m2 = 0.0001 {ref}`schema:units:S_per_cm2`
- 1 S_per_m2 = 0.1 {ref}`schema:units:mS_per_cm2`
- 1 S_per_m2 = 100 {ref}`schema:units:uS_per_cm2`

```
````

(schema:units:V)=
### V

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:voltage`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 V = 1000 {ref}`schema:units:mV`

```
````

(schema:units:cm)=
### cm

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:length`
- Power of 10: -2



```

```{grid-item-card} Conversions

- 1 cm = 0.01 {ref}`schema:units:m__`
- 1 cm = 10000 {ref}`schema:units:um`

```
````

(schema:units:cm2)=
### cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:area`
- Power of 10: -4



```

```{grid-item-card} Conversions

- 1 cm2 = 0.0001 {ref}`schema:units:m2`
- 1 cm2 = 1.00e+08 {ref}`schema:units:um2`

```
````

(schema:units:cm3)=
### cm3

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 cm3 = 0.001 {ref}`schema:units:litre`
- 1 cm3 = 1e-06 {ref}`schema:units:m3`
- 1 cm3 = 1.00e+12 {ref}`schema:units:um3`

```
````

(schema:units:cm_per_ms)=
### cm_per_ms

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: 1



```

```{grid-item-card} Conversions

- 1 cm_per_ms = 1000 {ref}`schema:units:cm_per_s`
- 1 cm_per_ms = 10 {ref}`schema:units:m_per_s`
- 1 cm_per_ms = 10000 {ref}`schema:units:um_per_ms`

```
````

(schema:units:cm_per_s)=
### cm_per_s

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: -2



```

```{grid-item-card} Conversions

- 1 cm_per_s = 0.001 {ref}`schema:units:cm_per_ms`
- 1 cm_per_s = 0.01 {ref}`schema:units:m_per_s`
- 1 cm_per_s = 10 {ref}`schema:units:um_per_ms`

```
````

(schema:units:degC)=
### degC

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:temperature`
- Power of 10: 0
- Offset: 273.15



```

```{grid-item-card} Conversions

- 1 degC = 274.15 {ref}`schema:units:K`

```
````

(schema:units:e)=
### e

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:charge`
- Power of 10: 0


- Scale: 1.602176634e-19


```

```{grid-item-card} Conversions

- 1 e = 1.6022e-19 {ref}`schema:units:C`

```
````

(schema:units:fJ_per_K_per_umol)=
### fJ_per_K_per_umol

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:idealGasConstantDims`
- Power of 10: -9



```

```{grid-item-card} Conversions

- 1 fJ_per_K_per_umol = 1e-09 {ref}`schema:units:J_per_K_per_mol`

```
````

(schema:units:hour)=
### hour

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: 0


- Scale: 3600.0


```

```{grid-item-card} Conversions

- 1 hour = 60 {ref}`schema:units:min`
- 1 hour = 3.60e+06 {ref}`schema:units:ms__`
- 1 hour = 3600 {ref}`schema:units:s__`

```
````

(schema:units:kohm)=
### kohm

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:resistance`
- Power of 10: 3



```

```{grid-item-card} Conversions

- 1 kohm = 0.001 {ref}`schema:units:Mohm`
- 1 kohm = 1000 {ref}`schema:units:ohm`

```
````

(schema:units:kohm_cm)=
### kohm_cm

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:resistivity`
- Power of 10: 1



```

```{grid-item-card} Conversions

- 1 kohm_cm = 1000 {ref}`schema:units:ohm_cm`
- 1 kohm_cm = 10 {ref}`schema:units:ohm_m`

```
````

(schema:units:litre)=
### litre

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: -3



```

```{grid-item-card} Conversions

- 1 litre = 1000 {ref}`schema:units:cm3`
- 1 litre = 0.001 {ref}`schema:units:m3`
- 1 litre = 1.00e+15 {ref}`schema:units:um3`

```
````

(schema:units:m__)=
### m

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:length`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 m = 100 {ref}`schema:units:cm`
- 1 m = 1.00e+06 {ref}`schema:units:um`

```
````

(schema:units:m2)=
### m2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:area`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 m2 = 10000 {ref}`schema:units:cm2`
- 1 m2 = 1.00e+12 {ref}`schema:units:um2`

```
````

(schema:units:m3)=
### m3

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 m3 = 1.00e+06 {ref}`schema:units:cm3`
- 1 m3 = 1000 {ref}`schema:units:litre`
- 1 m3 = 1.00e+18 {ref}`schema:units:um3`

```
````

(schema:units:mA_per_cm2)=
### mA_per_cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:currentDensity`
- Power of 10: 1



```

```{grid-item-card} Conversions

- 1 mA_per_cm2 = 10 {ref}`schema:units:A_per_m2`
- 1 mA_per_cm2 = 1000 {ref}`schema:units:uA_per_cm2`

```
````

(schema:units:mM)=
### mM

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 mM = 0.001 {ref}`schema:units:M`
- 1 mM = 1e-06 {ref}`schema:units:mol_per_cm3`
- 1 mM = 1 {ref}`schema:units:mol_per_m3`

```
````

(schema:units:mS)=
### mS

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -3



```

```{grid-item-card} Conversions

- 1 mS = 0.001 {ref}`schema:units:S`
- 1 mS = 1.00e+06 {ref}`schema:units:nS`
- 1 mS = 1.00e+09 {ref}`schema:units:pS`
- 1 mS = 1000 {ref}`schema:units:uS`

```
````

(schema:units:mS_per_cm2)=
### mS_per_cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: 1



```

```{grid-item-card} Conversions

- 1 mS_per_cm2 = 0.001 {ref}`schema:units:S_per_cm2`
- 1 mS_per_cm2 = 10 {ref}`schema:units:S_per_m2`
- 1 mS_per_cm2 = 1000 {ref}`schema:units:uS_per_cm2`

```
````

(schema:units:mV)=
### mV

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:voltage`
- Power of 10: -3



```

```{grid-item-card} Conversions

- 1 mV = 0.001 {ref}`schema:units:V`

```
````

(schema:units:m_per_s)=
### m_per_s

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 m_per_s = 0.1 {ref}`schema:units:cm_per_ms`
- 1 m_per_s = 100 {ref}`schema:units:cm_per_s`
- 1 m_per_s = 1000 {ref}`schema:units:um_per_ms`

```
````

(schema:units:min)=
### min

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: 0


- Scale: 60.0


```

```{grid-item-card} Conversions

- 1 min = 0.016667 {ref}`schema:units:hour`
- 1 min = 6.00e+04 {ref}`schema:units:ms__`
- 1 min = 60 {ref}`schema:units:s__`

```
````

(schema:units:mol)=
### mol

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:substance`
- Power of 10: 0



```
````

(schema:units:mol_per_cm3)=
### mol_per_cm3

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 6



```

```{grid-item-card} Conversions

- 1 mol_per_cm3 = 1000 {ref}`schema:units:M`
- 1 mol_per_cm3 = 1.00e+06 {ref}`schema:units:mM`
- 1 mol_per_cm3 = 1.00e+06 {ref}`schema:units:mol_per_m3`

```
````

(schema:units:mol_per_cm_per_uA_per_ms)=
### mol_per_cm_per_uA_per_ms

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:rho_factor`
- Power of 10: 11



```

```{grid-item-card} Conversions

- 1 mol_per_cm_per_uA_per_ms = 1.00e+11 {ref}`schema:units:mol_per_m_per_A_per_s`
- 1 mol_per_cm_per_uA_per_ms = 1000 {ref}`schema:units:umol_per_cm_per_nA_per_ms`

```
````

(schema:units:mol_per_m3)=
### mol_per_m3

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 mol_per_m3 = 0.001 {ref}`schema:units:M`
- 1 mol_per_m3 = 1 {ref}`schema:units:mM`
- 1 mol_per_m3 = 1e-06 {ref}`schema:units:mol_per_cm3`

```
````

(schema:units:mol_per_m_per_A_per_s)=
### mol_per_m_per_A_per_s

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:rho_factor`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 mol_per_m_per_A_per_s = 1e-11 {ref}`schema:units:mol_per_cm_per_uA_per_ms`
- 1 mol_per_m_per_A_per_s = 1e-08 {ref}`schema:units:umol_per_cm_per_nA_per_ms`

```
````

(schema:units:ms__)=
### ms

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: -3



```

```{grid-item-card} Conversions

- 1 ms = 2.7778e-07 {ref}`schema:units:hour`
- 1 ms = 1.6667e-05 {ref}`schema:units:min`
- 1 ms = 0.001 {ref}`schema:units:s__`

```
````

(schema:units:nA)=
### nA

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: -9



```

```{grid-item-card} Conversions

- 1 nA = 1e-09 {ref}`schema:units:A`
- 1 nA = 1000 {ref}`schema:units:pA`
- 1 nA = 0.001 {ref}`schema:units:uA`

```
````

(schema:units:nA_ms_per_amol)=
### nA_ms_per_amol

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:charge_per_mole`
- Power of 10: 6



```

```{grid-item-card} Conversions

- 1 nA_ms_per_amol = 1.00e+06 {ref}`schema:units:C_per_mol`
- 1 nA_ms_per_amol = 1.00e+12 {ref}`schema:units:pC_per_umol`

```
````

(schema:units:nF)=
### nF

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: -9



```

```{grid-item-card} Conversions

- 1 nF = 1e-09 {ref}`schema:units:F`
- 1 nF = 1000 {ref}`schema:units:pF`
- 1 nF = 0.001 {ref}`schema:units:uF`

```
````

(schema:units:nS)=
### nS

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -9



```

```{grid-item-card} Conversions

- 1 nS = 1e-09 {ref}`schema:units:S`
- 1 nS = 1e-06 {ref}`schema:units:mS`
- 1 nS = 1000 {ref}`schema:units:pS`
- 1 nS = 0.001 {ref}`schema:units:uS`

```
````

(schema:units:nS_per_mV)=
### nS_per_mV

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance_per_voltage`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 nS_per_mV = 1e-06 {ref}`schema:units:S_per_V`

```
````

(schema:units:ohm)=
### ohm

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:resistance`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 ohm = 1e-06 {ref}`schema:units:Mohm`
- 1 ohm = 0.001 {ref}`schema:units:kohm`

```
````

(schema:units:ohm_cm)=
### ohm_cm

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:resistivity`
- Power of 10: -2



```

```{grid-item-card} Conversions

- 1 ohm_cm = 0.001 {ref}`schema:units:kohm_cm`
- 1 ohm_cm = 0.01 {ref}`schema:units:ohm_m`

```
````

(schema:units:ohm_m)=
### ohm_m

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:resistivity`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 ohm_m = 0.1 {ref}`schema:units:kohm_cm`
- 1 ohm_m = 100 {ref}`schema:units:ohm_cm`

```
````

(schema:units:pA)=
### pA

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: -12



```

```{grid-item-card} Conversions

- 1 pA = 1e-12 {ref}`schema:units:A`
- 1 pA = 0.001 {ref}`schema:units:nA`
- 1 pA = 1e-06 {ref}`schema:units:uA`

```
````

(schema:units:pC_per_umol)=
### pC_per_umol

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:charge_per_mole`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 pC_per_umol = 1e-06 {ref}`schema:units:C_per_mol`
- 1 pC_per_umol = 1e-12 {ref}`schema:units:nA_ms_per_amol`

```
````

(schema:units:pF)=
### pF

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: -12



```

```{grid-item-card} Conversions

- 1 pF = 1e-12 {ref}`schema:units:F`
- 1 pF = 0.001 {ref}`schema:units:nF`
- 1 pF = 1e-06 {ref}`schema:units:uF`

```
````

(schema:units:pS)=
### pS

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -12



```

```{grid-item-card} Conversions

- 1 pS = 1e-12 {ref}`schema:units:S`
- 1 pS = 1e-09 {ref}`schema:units:mS`
- 1 pS = 0.001 {ref}`schema:units:nS`
- 1 pS = 1e-06 {ref}`schema:units:uS`

```
````

(schema:units:per_V)=
### per_V

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_voltage`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 per_V = 0.001 {ref}`schema:units:per_mV`

```
````

(schema:units:per_hour)=
### per_hour

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0


- Scale: 0.00027777777778


```

```{grid-item-card} Conversions

- 1 per_hour = 0.00027778 {ref}`schema:units:Hz`
- 1 per_hour = 0.016667 {ref}`schema:units:per_min`
- 1 per_hour = 2.7778e-07 {ref}`schema:units:per_ms`
- 1 per_hour = 0.00027778 {ref}`schema:units:per_s`

```
````

(schema:units:per_mV)=
### per_mV

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_voltage`
- Power of 10: 3



```

```{grid-item-card} Conversions

- 1 per_mV = 1000 {ref}`schema:units:per_V`

```
````

(schema:units:per_min)=
### per_min

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0


- Scale: 0.01666666667


```

```{grid-item-card} Conversions

- 1 per_min = 0.016667 {ref}`schema:units:Hz`
- 1 per_min = 60 {ref}`schema:units:per_hour`
- 1 per_min = 1.6667e-05 {ref}`schema:units:per_ms`
- 1 per_min = 0.016667 {ref}`schema:units:per_s`

```
````

(schema:units:per_ms)=
### per_ms

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 3



```

```{grid-item-card} Conversions

- 1 per_ms = 1000 {ref}`schema:units:Hz`
- 1 per_ms = 3.60e+06 {ref}`schema:units:per_hour`
- 1 per_ms = 6.00e+04 {ref}`schema:units:per_min`
- 1 per_ms = 1000 {ref}`schema:units:per_s`

```
````

(schema:units:per_s)=
### per_s

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 per_s = 1 {ref}`schema:units:Hz`
- 1 per_s = 3600 {ref}`schema:units:per_hour`
- 1 per_s = 60 {ref}`schema:units:per_min`
- 1 per_s = 0.001 {ref}`schema:units:per_ms`

```
````

(schema:units:s__)=
### s

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: 0



```

```{grid-item-card} Conversions

- 1 s = 0.00027778 {ref}`schema:units:hour`
- 1 s = 0.016667 {ref}`schema:units:min`
- 1 s = 1000 {ref}`schema:units:ms__`

```
````

(schema:units:uA)=
### uA

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 uA = 1e-06 {ref}`schema:units:A`
- 1 uA = 1000 {ref}`schema:units:nA`
- 1 uA = 1.00e+06 {ref}`schema:units:pA`

```
````

(schema:units:uA_per_cm2)=
### uA_per_cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:currentDensity`
- Power of 10: -2



```

```{grid-item-card} Conversions

- 1 uA_per_cm2 = 0.01 {ref}`schema:units:A_per_m2`
- 1 uA_per_cm2 = 0.001 {ref}`schema:units:mA_per_cm2`

```
````

(schema:units:uF)=
### uF

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 uF = 1e-06 {ref}`schema:units:F`
- 1 uF = 1000 {ref}`schema:units:nF`
- 1 uF = 1.00e+06 {ref}`schema:units:pF`

```
````

(schema:units:uF_per_cm2)=
### uF_per_cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:specificCapacitance`
- Power of 10: -2



```

```{grid-item-card} Conversions

- 1 uF_per_cm2 = 0.01 {ref}`schema:units:F_per_m2`

```
````

(schema:units:uS)=
### uS

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 uS = 1e-06 {ref}`schema:units:S`
- 1 uS = 0.001 {ref}`schema:units:mS`
- 1 uS = 1000 {ref}`schema:units:nS`
- 1 uS = 1.00e+06 {ref}`schema:units:pS`

```
````

(schema:units:uS_per_cm2)=
### uS_per_cm2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: -2



```

```{grid-item-card} Conversions

- 1 uS_per_cm2 = 1e-06 {ref}`schema:units:S_per_cm2`
- 1 uS_per_cm2 = 0.01 {ref}`schema:units:S_per_m2`
- 1 uS_per_cm2 = 0.001 {ref}`schema:units:mS_per_cm2`

```
````

(schema:units:um)=
### um

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:length`
- Power of 10: -6



```

```{grid-item-card} Conversions

- 1 um = 0.0001 {ref}`schema:units:cm`
- 1 um = 1e-06 {ref}`schema:units:m__`

```
````

(schema:units:um2)=
### um2

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:area`
- Power of 10: -12



```

```{grid-item-card} Conversions

- 1 um2 = 1e-08 {ref}`schema:units:cm2`
- 1 um2 = 1e-12 {ref}`schema:units:m2`

```
````

(schema:units:um3)=
### um3

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: -18



```

```{grid-item-card} Conversions

- 1 um3 = 1e-12 {ref}`schema:units:cm3`
- 1 um3 = 1e-15 {ref}`schema:units:litre`
- 1 um3 = 1e-18 {ref}`schema:units:m3`

```
````

(schema:units:um_per_ms)=
### um_per_ms

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: -3



```

```{grid-item-card} Conversions

- 1 um_per_ms = 0.0001 {ref}`schema:units:cm_per_ms`
- 1 um_per_ms = 0.1 {ref}`schema:units:cm_per_s`
- 1 um_per_ms = 0.001 {ref}`schema:units:m_per_s`

```
````

(schema:units:umol_per_cm_per_nA_per_ms)=
### umol_per_cm_per_nA_per_ms

````{grid}
:gutter: 2

```{grid-item-card} Summary
- Dimension: {ref}`schema:dimensions:rho_factor`
- Power of 10: 8



```

```{grid-item-card} Conversions

- 1 umol_per_cm_per_nA_per_ms = 0.001 {ref}`schema:units:mol_per_cm_per_uA_per_ms`
- 1 umol_per_cm_per_nA_per_ms = 1.00e+08 {ref}`schema:units:mol_per_m_per_A_per_s`

```
````


