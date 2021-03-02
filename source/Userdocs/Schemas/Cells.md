
(schema:cells)=
# Cells



Original ComponentType definitions: [Cells.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Cells.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 02/03/21 from [this](https://github.com/NeuroML/NeuroML2/commit/6e4643d0eaa7246982b351a01e28856eeb320500) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:basecell)=

## *baseCell*




extends *{ref}`schema:basestandalone`*



<i>Base type of any cell which can be used in a population.</i>



(schema:basespikingcell)=

## *baseSpikingCell*




extends *{ref}`schema:basecell`*



<i>Base type of any cell which can emit **spike** events.</i>



````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

spike,Direction: out

```
````

(schema:basecellmembpot)=

## *baseCellMembPot*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a membrane potential **v** with voltage units.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

v,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

(schema:basecellmembpotdl)=

## *baseCellMembPotDL*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a dimensioness membrane potential, **V.**.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

V,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

(schema:basechannelpopulation)=

## *baseChannelPopulation*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for any current produced by a population of channels, all of type **ionChannel**.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

ionChannel, {ref}`schema:baseionchannel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:channelpopulation)=

## channelPopulation




extends *{ref}`schema:basechannelpopulation`*



<i>Population of **number** ohmic ion channels. These each produce a conductance **channelg** across a reversal potential **erev,** giving a total current **i.**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`
number,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

vShift = 0mV, {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **channelg** =&nbsp;ionChannel->g
    : **geff** =&nbsp;channelg * number
    : **i** =&nbsp;geff * (erev - v)&emsp;(exposed as **i**)
    





````

(schema:channelpopulationnernst)=

## channelPopulationNernst




extends *{ref}`schema:basechannelpopulation`*



<i>Population of channels with a time varying reversal potential **erev** determined by Nernst equation. Hard coded for Ca only!</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

number,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

R = 8.3144621 J_per_K_per_mol, {ref}`schema:dimensions:idealGasConstantDims`
zCa = 2, Dimensionless
F = 96485.3 C_per_mol, {ref}`schema:dimensions:charge_per_mole`
vShift = 0mV, {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
caConcExt,{ref}`schema:dimensions:concentration`
temperature,{ref}`schema:dimensions:temperature`
*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **singleChannelConductance** =&nbsp;ionChannel->g
    : **totalConductance** =&nbsp;singleChannelConductance * number
    : **erev** =&nbsp;(R * temperature / (zCa * F)) * log(caConcExt / caConc)&emsp;(exposed as **erev**)
    : **i** =&nbsp;totalConductance * (erev - v)&emsp;(exposed as **i**)
    





````

(schema:basechanneldensity)=

## *baseChannelDensity*




<i>Base type for current distributed on an area of a cell.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

ionChannel, {ref}`schema:baseionchannel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

iDensity,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

v,{ref}`schema:dimensions:voltage`

```
````

(schema:basechanneldensitycond)=

## *baseChannelDensityCond*




extends *{ref}`schema:basechanneldensity`*



<i>Base type for distributed conductances on an area of a cell producing a (not necessarily ohmic) current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

condDensity,{ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

gDensity,{ref}`schema:dimensions:conductanceDensity`
*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:variableparameter)=

## variableParameter




<i>Specifies a parameter which can vary its value across a **segmentGroup**.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

parameter,
segmentGroup,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

inhomogeneousValue, {ref}`schema:inhomogeneousvalue`

```
````

(schema:inhomogeneousvalue)=

## inhomogeneousValue




<i>Specifies the value of a  {ref}`schema:variableparameter`.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

inhomogeneousParameter,
value,

````

(schema:channeldensitynonuniform)=

## channelDensityNonUniform




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying ohmic conductance density, which is distributed on a region of the cell. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

variableParameter, {ref}`schema:variableparameter`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

ZERO_CURR_DENS = 0 A_per_m2, {ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

(schema:channeldensitynonuniformnernst)=

## channelDensityNonUniformNernst




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the cell, and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

variableParameter, {ref}`schema:variableparameter`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

ZERO_CURR_DENS = 0 A_per_m2, {ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

(schema:channeldensitynonuniformghk)=

## channelDensityNonUniformGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the cell, and whose current is calculated from the Goldman-Hodgkin-Katz equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

variableParameter, {ref}`schema:variableparameter`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

ZERO_CURR_DENS = 0 A_per_m2, {ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

(schema:channeldensity)=

## channelDensity




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying ohmic conductance density, **gDensity,** which is distributed on an area of the cell with fixed reversal potential **erev** producing a current density **iDensity**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*condDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
erev,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

vShift = 0mV, {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*gDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **channelf** =&nbsp;ionChannel->fopen
    : **gDensity** =&nbsp;condDensity * channelf&emsp;(exposed as **gDensity**)
    : **iDensity** =&nbsp;gDensity * (erev - v)&emsp;(exposed as **iDensity**)
    





````

(schema:channeldensityvshift)=

## channelDensityVShift




extends {ref}`schema:channeldensity`



<i>Same as  {ref}`schema:channeldensity`, but with a **vShift** parameter to change voltage activation of gates. The exact usage of **vShift** in expressions for rates is determined by the individual gates.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*condDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
*erev (from {ref}`schema:channeldensity`)*,{ref}`schema:dimensions:voltage`
vShift,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*gDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:channeldensitynernst)=

## channelDensityNernst




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity** and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*condDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

R = 8.3144621 J_per_K_per_mol, {ref}`schema:dimensions:idealGasConstantDims`
zCa = 2, Dimensionless
F = 96485.3 C_per_mol, {ref}`schema:dimensions:charge_per_mole`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`
*gDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
caConcExt,{ref}`schema:dimensions:concentration`
temperature,{ref}`schema:dimensions:temperature`
*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **channelf** =&nbsp;ionChannel->fopen
    



<i>**Conditional Derived Variables**</i>
    
: IF caConcExt &gt; 0 THEN
: &emsp; **gDensity** = condDensity \* channelf &emsp;(exposed as **gDensity**)
: IF caConcExt &lt;= 0 THEN
: &emsp; **gDensity** = 0 &emsp;(exposed as **gDensity**)
: IF caConcExt &gt; 0 THEN
: &emsp; **erev** = (R \* temperature / (zCa \* F)) \* log(caConcExt / caConc) &emsp;(exposed as **erev**)
: IF caConcExt &lt;= 0 THEN
: &emsp; **erev** = 0 &emsp;(exposed as **erev**)
: IF caConcExt &gt; 0 THEN
: &emsp; **iDensity** = gDensity \* (erev - v) &emsp;(exposed as **iDensity**)
: IF caConcExt &lt;= 0 THEN
: &emsp; **iDensity** = 0 &emsp;(exposed as **iDensity**)


````

(schema:channeldensitynernstca2)=

## channelDensityNernstCa2




extends *{ref}`schema:basechanneldensitycond`*



<i>This component is similar to the original component type **channelDensityNernst** but it is changed in order to have a reversal potential that depends on a second independent Ca++ pool (ca2). See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*condDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

R = 8.3144621 J_per_K_per_mol, {ref}`schema:dimensions:idealGasConstantDims`
zCa = 2, Dimensionless
F = 96485.3 C_per_mol, {ref}`schema:dimensions:charge_per_mole`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`
*gDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

caConc2,{ref}`schema:dimensions:concentration`
caConcExt2,{ref}`schema:dimensions:concentration`
temperature,{ref}`schema:dimensions:temperature`
*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **channelf** =&nbsp;ionChannel->fopen
    



<i>**Conditional Derived Variables**</i>
    
: IF caConcExt2 &gt; 0 THEN
: &emsp; **gDensity** = condDensity \* channelf &emsp;(exposed as **gDensity**)
: IF caConcExt2 &lt;= 0 THEN
: &emsp; **gDensity** = 0 &emsp;(exposed as **gDensity**)
: IF caConcExt2 &gt; 0 THEN
: &emsp; **erev** = (R \* temperature / (zCa \* F)) \* log(caConcExt2 / caConc2) &emsp;(exposed as **erev**)
: IF caConcExt2 &lt;= 0 THEN
: &emsp; **erev** = 0 &emsp;(exposed as **erev**)
: IF caConcExt2 &gt; 0 THEN
: &emsp; **iDensity** = gDensity \* (erev - v) &emsp;(exposed as **iDensity**)
: IF caConcExt2 &lt;= 0 THEN
: &emsp; **iDensity** = 0 &emsp;(exposed as **iDensity**)


````

(schema:channeldensityghk)=

## channelDensityGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity** and whose reversal potential is calculated from the Goldman Hodgkin Katz equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

permeability,{ref}`schema:dimensions:permeability`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

R = 8.3144621 J_per_K_per_mol, {ref}`schema:dimensions:idealGasConstantDims`
zCa = 2, Dimensionless
F = 96485.3 C_per_mol, {ref}`schema:dimensions:charge_per_mole`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
caConcExt,{ref}`schema:dimensions:concentration`
temperature,{ref}`schema:dimensions:temperature`
*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **K** =&nbsp;(zCa * F) / (R * temperature)
    : **expKv** =&nbsp;exp(-1 * K * v)
    : **channelf** =&nbsp;ionChannel->fopen
    



<i>**Conditional Derived Variables**</i>
    
: IF caConcExt &gt; 0 THEN
: &emsp; **iDensity** = -1 \* channelf \* permeability \* zCa \* F \* K \* v \* ( caConc - (caConcExt \* expKv) ) / (1 - expKv) &emsp;(exposed as **iDensity**)
: IF caConcExt &lt;= 0 THEN
: &emsp; **iDensity** = 0 &emsp;(exposed as **iDensity**)


````

(schema:channeldensityghk2)=

## channelDensityGHK2




extends *{ref}`schema:basechanneldensitycond`*



<i>Time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity.** Modified version of Jaffe et al. 1994 (used also in Lawrence et al. 2006). See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*condDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,
ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

VOLT_SCALE = 1 mV, {ref}`schema:dimensions:voltage`
CONC_SCALE = 1 mM, {ref}`schema:dimensions:concentration`
TEMP_SCALE = 1 K, {ref}`schema:dimensions:temperature`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*gDensity (from {ref}`schema:basechanneldensitycond`)*,{ref}`schema:dimensions:conductanceDensity`
*iDensity (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
caConcExt,{ref}`schema:dimensions:concentration`
temperature,{ref}`schema:dimensions:temperature`
*v (from {ref}`schema:basechanneldensity`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **V** =&nbsp;v / VOLT_SCALE
    : **ca_conc_i** =&nbsp;caConc / CONC_SCALE
    : **ca_conc_ext** =&nbsp;caConcExt / CONC_SCALE
    : **T** =&nbsp;temperature / TEMP_SCALE
    : **channelf** =&nbsp;ionChannel->fopen
    : **gDensity** =&nbsp;condDensity * channelf&emsp;(exposed as **gDensity**)
    : **tmp** =&nbsp;(25 * T) / (293.15 * 2)
    



<i>**Conditional Derived Variables**</i>
    
: IF V/tmp = 0. THEN
: &emsp; **pOpen** = tmp \* 1e-3 \* (1 - ((ca_conc_i/ca_conc_ext) \* exp(V/tmp))) \* (1 - (V/tmp)/2) 
: IF V/tmp != 0. THEN
: &emsp; **pOpen** = tmp \* 1e-3 \* (1 - ((ca_conc_i/ca_conc_ext) \* exp(V/tmp))) \* ((V/tmp) / (exp(V/tmp) - 1)) 
: IF ca_conc_ext &gt; 0 THEN
: &emsp; **iDensity** = gDensity \* pOpen &emsp;(exposed as **iDensity**)
: IF ca_conc_ext &lt;= 0 THEN
: &emsp; **iDensity** = 0 &emsp;(exposed as **iDensity**)


````

(schema:pointcellcondbased)=

## pointCellCondBased




extends *{ref}`schema:basecellmembpotcap`*



<i>Simple model of a conductance based cell, with no separate morphology element, just an absolute capacitance **C,** and a set of channel populations.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
thresh,{ref}`schema:dimensions:voltage`
v0,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

populations, {ref}`schema:basechannelpopulation`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless 









<i>**On Start**</i>
: **v** = v0
: **spiking** = 0



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;**spiking** = 1
: &emsp;EVENT OUT on port **spike**

: IF v &lt; thresh THEN
: &emsp;**spiking** = 0





<i>**Derived Variables**</i>
    : **iChannels** =&nbsp;populations[*]->i(reduce method: add)
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;iChannels + iSyn&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb / C
    

````

(schema:pointcellcondbasedca)=

## pointCellCondBasedCa




extends *{ref}`schema:basecellmembpotcap`*



<i>TEMPORARY: Point cell with conductances and Ca concentration  info. Not yet fully tested!!!</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
thresh,{ref}`schema:dimensions:voltage`
v0,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

populations, {ref}`schema:basechannelpopulation`
concentrationModels, {ref}`schema:concentrationmodel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
iCa,{ref}`schema:dimensions:current`
*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless 









<i>**On Start**</i>
: **v** = v0
: **spiking** = 0



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;**spiking** = 1
: &emsp;EVENT OUT on port **spike**

: IF v &lt; thresh THEN
: &emsp;**spiking** = 0





<i>**Derived Variables**</i>
    : **iChannels** =&nbsp;populations[*]->i(reduce method: add)
    : **iCa** =&nbsp;populations[ion='ca']->i(reduce method: add)&emsp;(exposed as **iCa**)
    : **caConc** =&nbsp;concentrationModels[species='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;iChannels + iSyn&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb / C
    

````

(schema:distal)=

## distal




extends {ref}`schema:point3dwithdiam`



<i>Point furthest from the soma in a segment.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*diameter (from {ref}`schema:point3dwithdiam`)*,Dimensionless
*x (from {ref}`schema:point3dwithdiam`)*,Dimensionless
*y (from {ref}`schema:point3dwithdiam`)*,Dimensionless
*z (from {ref}`schema:point3dwithdiam`)*,Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*radius (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`
*xLength (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`
*yLength (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`
*zLength (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`

```
````

(schema:proximal)=

## proximal




extends {ref}`schema:point3dwithdiam`



<i>Point closest to the soma in a segment. Note, if the proximal point is equal to the distal point of the parent segment, proximal can be omitted.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*diameter (from {ref}`schema:point3dwithdiam`)*,Dimensionless
*x (from {ref}`schema:point3dwithdiam`)*,Dimensionless
*y (from {ref}`schema:point3dwithdiam`)*,Dimensionless
*z (from {ref}`schema:point3dwithdiam`)*,Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*radius (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`
*xLength (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`
*yLength (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`
*zLength (from {ref}`schema:point3dwithdiam`)*,{ref}`schema:dimensions:length`

```
````

(schema:parent)=

## parent




<i>Specifies the segment which is this segment's parent.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,
fractionAlong,

````

(schema:segment)=

## segment




<i>A segment defines the smallest unit within a possibly branching structure ( {ref}`schema:morphology`), such as a dendrite or axon. The shape is given by the  {ref}`schema:proximal` and  {ref}`schema:distal` points. If  {ref}`schema:proximal` is missing, the proximal point is assumed to be the  {ref}`schema:distal` point of the parent.  {ref}`schema:parent` specifies the parent segment. The first segment (no  {ref}`schema:parent`) usually represents the soma. NOTE: LEMS does not yet support multicompartmental modelling, so the Dynamics here is only appropriate for single compartment modelling.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

name,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

parent, {ref}`schema:parent`
distal, {ref}`schema:distal`
proximal, {ref}`schema:proximal`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

LEN = 1m, {ref}`schema:dimensions:length`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

length,{ref}`schema:dimensions:length`
radDist,{ref}`schema:dimensions:length`
surfaceArea,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **radDist** =&nbsp;distal->radius&emsp;(exposed as **radDist**)
    : **dx** =&nbsp;distal->xLength
    : **dy** =&nbsp;distal->yLength
    : **dz** =&nbsp;distal->zLength
    : **px** =&nbsp;proximal->xLength
    : **py** =&nbsp;proximal->yLength
    : **pz** =&nbsp;proximal->zLength
    : **length** =&nbsp;sqrt(((dx - px) * (dx - px) + (dy - py) * (dy - py) + (dz - pz) * (dz - pz))/(LEN * LEN)) * LEN&emsp;(exposed as **length**)
    



<i>**Conditional Derived Variables**</i>
    
: IF length = 0 * LEN THEN
: &emsp; **surfaceArea** = 4 \* radDist \* radDist \* 3.14159265 &emsp;(exposed as **surfaceArea**)
: IF length &gt; 0 * LEN THEN
: &emsp; **surfaceArea** = 2 \* radDist \* 3.14159265 \* length &emsp;(exposed as **surfaceArea**)


````

(schema:segmentgroup)=

## segmentGroup




<i>A method to describe a group of  {ref}`schema:segment`s in a  {ref}`schema:morphology`.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

neuroLexId,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

notes, {ref}`schema:notes`
annotation, {ref}`schema:annotation`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

property, {ref}`schema:property`
members, {ref}`schema:member`
paths, {ref}`schema:path`
subTrees, {ref}`schema:subtree`
includes, {ref}`schema:include`
inhomogeneousParameter, {ref}`schema:inhomogeneousparameter`

```
````

(schema:member)=

## member




<i>A single identified  {ref}`schema:segment` which is part of the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,

````

(schema:from)=

## from




<i>Specifies which  {ref}`schema:segment` distal from which to calculate the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,

````

(schema:to)=

## to




<i>Specifies which  {ref}`schema:segment` up to which to calculate the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,

````

(schema:include)=

## include




<i>Include all members of another  {ref}`schema:segmentgroup` in this.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

href,
segmentGroup,

````

(schema:path)=

## path




<i>Include all the segments between those specified by  {ref}`schema:from` and  {ref}`schema:to`, inclusive.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

from, {ref}`schema:from`
to, {ref}`schema:to`

```
````

(schema:subtree)=

## subTree




<i>Include all the segments distal to that specified by  {ref}`schema:from` in the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

from, {ref}`schema:from`

```
````

(schema:inhomogeneousparameter)=

## inhomogeneousParameter




<i>An inhomogeneous parameter specified across the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

variable,
metric,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

proximal, {ref}`schema:proximalproperties`
distal, {ref}`schema:distalproperties`

```
````

(schema:proximalproperties)=

## proximalProperties




<i>What to do at the proximal point when creating an inhomogeneous parameter.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

translationStart,

````

(schema:distalproperties)=

## distalProperties




<i>What to do at the distal point when creating an inhomogeneous parameter.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

normalizationEnd,

````

(schema:morphology)=

## morphology




<i>The collection of  {ref}`schema:segment`s which specify the 3D structure of the cell, along with a number of  {ref}`schema:segmentgroup`s.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

segments, {ref}`schema:segment`
segmentGroups, {ref}`schema:segmentgroup`

```
````

(schema:specificcapacitance)=

## specificCapacitance




<i>Capacitance per unit area.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

value,{ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,

````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

specCap,{ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **specCap** =&nbsp;value&emsp;(exposed as **specCap**)
    





````

(schema:initmembpotential)=

## initMembPotential




<i>Explicitly set initial membrane potential for the cell.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

value,{ref}`schema:dimensions:voltage`

```
````

(schema:spikethresh)=

## spikeThresh




<i>Membrane potential at which to emit a spiking event. Note, usually the spiking event will not be emitted again until the membrane potential has fallen below this value and rises again to cross it in a positive direction.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

value,{ref}`schema:dimensions:voltage`

```
````

(schema:membraneproperties)=

## membraneProperties




<i>Properties specific to the membrane, such as the **populations** of channels, **channelDensities,** **specificCapacitance,** etc.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

initMembPotential, {ref}`schema:initmembpotential`
spikeThresh, {ref}`schema:spikethresh`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

specificCapacitances, {ref}`schema:specificcapacitance`
populations, {ref}`schema:basechannelpopulation`
channelDensities, {ref}`schema:basechanneldensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

iCa,{ref}`schema:dimensions:current`
totChanCurrent,{ref}`schema:dimensions:current`
totSpecCap,{ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

surfaceArea,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;specificCapacitances[*]->specCap(reduce method: add)&emsp;(exposed as **totSpecCap**)
    : **totChanPopCurrent** =&nbsp;populations[*]->i(reduce method: add)
    : **totChanDensCurrentDensity** =&nbsp;channelDensities[*]->iDensity(reduce method: add)
    : **totChanCurrent** =&nbsp;totChanPopCurrent + (totChanDensCurrentDensity * surfaceArea)&emsp;(exposed as **totChanCurrent**)
    : **totChanPopCurrentCa** =&nbsp;populations[ion='ca']->i(reduce method: add)
    : **totChanDensCurrentDensityCa** =&nbsp;channelDensities[ion='ca']->iDensity(reduce method: add)
    : **iCa** =&nbsp;totChanPopCurrentCa + (totChanDensCurrentDensityCa * surfaceArea)&emsp;(exposed as **iCa**)
    





````

(schema:membraneproperties2capools)=

## membraneProperties2CaPools




extends {ref}`schema:membraneproperties`



<i>Variant of membraneProperties with 2 independent Ca pools.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

initMembPotential, {ref}`schema:initmembpotential`
spikeThresh, {ref}`schema:spikethresh`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

specificCapacitances, {ref}`schema:specificcapacitance`
populations, {ref}`schema:basechannelpopulation`
channelDensities, {ref}`schema:basechanneldensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iCa (from {ref}`schema:membraneproperties`)*,{ref}`schema:dimensions:current`
iCa2,{ref}`schema:dimensions:current`
*totChanCurrent (from {ref}`schema:membraneproperties`)*,{ref}`schema:dimensions:current`
*totSpecCap (from {ref}`schema:membraneproperties`)*,{ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

surfaceArea,{ref}`schema:dimensions:area`
*surfaceArea (from {ref}`schema:membraneproperties`)*,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;specificCapacitances[*]->specCap(reduce method: add)&emsp;(exposed as **totSpecCap**)
    : **totChanPopCurrent** =&nbsp;populations[*]->i(reduce method: add)
    : **totChanDensCurrentDensity** =&nbsp;channelDensities[*]->iDensity(reduce method: add)
    : **totChanCurrent** =&nbsp;totChanPopCurrent + (totChanDensCurrentDensity * surfaceArea)&emsp;(exposed as **totChanCurrent**)
    : **totChanPopCurrentCa** =&nbsp;populations[ion='ca']->i(reduce method: add)
    : **totChanDensCurrentDensityCa** =&nbsp;channelDensities[ion='ca']->iDensity(reduce method: add)
    : **iCa** =&nbsp;totChanPopCurrentCa + (totChanDensCurrentDensityCa * surfaceArea)&emsp;(exposed as **iCa**)
    : **totChanPopCurrentCa2** =&nbsp;populations[ion='ca2']->i(reduce method: add)
    : **totChanDensCurrentDensityCa2** =&nbsp;channelDensities[ion='ca2']->iDensity(reduce method: add)
    : **iCa2** =&nbsp;totChanPopCurrentCa2 + (totChanDensCurrentDensityCa2 * surfaceArea)&emsp;(exposed as **iCa2**)
    





````

(schema:biophysicalproperties)=

## biophysicalProperties




<i>The biophysical properties of the  {ref}`schema:cell`, including the  {ref}`schema:membraneproperties` and the  {ref}`schema:intracellularproperties`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

membraneProperties, {ref}`schema:membraneproperties`
intracellularProperties, {ref}`schema:intracellularproperties`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

totSpecCap,{ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;membraneProperties->totSpecCap&emsp;(exposed as **totSpecCap**)
    





````

(schema:biophysicalproperties2capools)=

## biophysicalProperties2CaPools




<i>The biophysical properties of the  {ref}`schema:cell`, including the  {ref}`schema:membraneproperties2capools` and the  {ref}`schema:intracellularproperties2capools` for a cell with two Ca pools.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

membraneProperties2CaPools, {ref}`schema:membraneproperties2capools`
intracellularProperties2CaPools, {ref}`schema:intracellularproperties2capools`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

totSpecCap,{ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;membraneProperties2CaPools->totSpecCap&emsp;(exposed as **totSpecCap**)
    





````

(schema:intracellularproperties)=

## intracellularProperties




<i>Biophysical properties related to the intracellular space within the  {ref}`schema:cell`, such as the  {ref}`schema:resistivity` and the list of ionic  {ref}`schema:species` present. **caConc** and **caConcExt** are explicitly exposed here to facilitate accessing these values from other Components, even though **caConcExt** is clearly not an intracellular property.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

resistivity, {ref}`schema:resistivity`
speciesList, {ref}`schema:species`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
caConcExt,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **caConc** =&nbsp;speciesList[ion='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;speciesList[ion='ca']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt**)
    





````

(schema:intracellularproperties2capools)=

## intracellularProperties2CaPools




extends {ref}`schema:intracellularproperties`



<i>Variant of intracellularProperties with 2 independent Ca pools.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

speciesList, {ref}`schema:species`
resistivity, {ref}`schema:resistivity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*caConc (from {ref}`schema:intracellularproperties`)*,{ref}`schema:dimensions:concentration`
caConc2,{ref}`schema:dimensions:concentration`
*caConcExt (from {ref}`schema:intracellularproperties`)*,{ref}`schema:dimensions:concentration`
caConcExt2,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **caConc2** =&nbsp;speciesList[ion='ca2']->concentration(reduce method: add)&emsp;(exposed as **caConc2**)
    : **caConcExt2** =&nbsp;speciesList[ion='ca2']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt2**)
    : **caConc** =&nbsp;speciesList[ion='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;speciesList[ion='ca']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt**)
    





````

(schema:resistivity)=

## resistivity




<i>The resistivity, or specific axial resistance, of the cytoplasm.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

value,{ref}`schema:dimensions:resistivity`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentGroup,

````

(schema:concentrationmodel)=

## concentrationModel




<i>Base for any model of an **ion** concentration which changes with time. Internal (_concentration) and external (_extConcentration) values for the concentration of the ion are given.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,

````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

concentration,{ref}`schema:dimensions:concentration`
extConcentration,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

initialConcentration,{ref}`schema:dimensions:concentration`
initialExtConcentration,{ref}`schema:dimensions:concentration`
surfaceArea,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration








````

(schema:decayingpoolconcentrationmodel)=

## decayingPoolConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of an intracellular buffering mechanism for **ion** (currently hard Coded to be calcium, due to requirement for **iCa)** which has a baseline level **restingConc** and tends to this value with time course **decayConstant.** The ion is assumed to occupy a shell inside the membrane of thickness **shellThickness.**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

decayConstant,{ref}`schema:dimensions:time`
restingConc,{ref}`schema:dimensions:concentration`
shellThickness,{ref}`schema:dimensions:length`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,

````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

Faraday = 96485.3C_per_mol, {ref}`schema:dimensions:charge_per_mole`
AREA_SCALE = 1m2, {ref}`schema:dimensions:area`
LENGTH_SCALE = 1m, {ref}`schema:dimensions:length`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*concentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*extConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

iCa,{ref}`schema:dimensions:current`
*initialConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*initialExtConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*surfaceArea (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration



<i>**On Conditions**</i>

: IF concentration &lt; 0 THEN
: &emsp;**concentration** = 0





<i>**Derived Variables**</i>
    : **effectiveRadius** =&nbsp;LENGTH_SCALE * sqrt(surfaceArea/(AREA_SCALE * (4 * 3.14159)))
    : **innerRadius** =&nbsp;effectiveRadius - shellThickness
    : **shellVolume** =&nbsp;(4 * (effectiveRadius * effectiveRadius * effectiveRadius) * 3.14159 / 3) - (4 * (innerRadius * innerRadius * innerRadius) * 3.14159 / 3)
    





<i>**Time Derivatives**</i>
    : d **concentration** /dt = iCa / (2 * Faraday * shellVolume) - ((concentration - restingConc) / decayConstant)
    

````

(schema:fixedfactorconcentrationmodel)=

## fixedFactorConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion (currently hard coded to be calcium, due to requirement for **iCa)** which has a baseline level **restingConc** and tends to this value with time course **decayConstant.** A fixed factor **rho** is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

decayConstant,{ref}`schema:dimensions:time`
restingConc,{ref}`schema:dimensions:concentration`
rho,{ref}`schema:dimensions:rho_factor`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,

````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*concentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*extConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

iCa,{ref}`schema:dimensions:current`
*initialConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*initialExtConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
surfaceArea,{ref}`schema:dimensions:area`
*surfaceArea (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration



<i>**On Conditions**</i>

: IF concentration &lt; 0 THEN
: &emsp;**concentration** = 0








<i>**Time Derivatives**</i>
    : d **concentration** /dt = (iCa/surfaceArea) * rho - ((concentration - restingConc) / decayConstant)
    

````

(schema:fixedfactorconcentrationmodeltraub)=

## fixedFactorConcentrationModelTraub




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion (currently hard coded to be calcium, due to requirement for **iCa)** which has a baseline level **restingConc** and tends to this value with time course 1 / **beta.** A fixed factor **phi** is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change. Not recommended for use in models other than Traub et al. 2005!</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

beta,{ref}`schema:dimensions:per_time`
phi,{ref}`schema:dimensions:rho_factor`
restingConc,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

species,

````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*concentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*extConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

iCa,{ref}`schema:dimensions:current`
*initialConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
*initialExtConcentration (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:concentration`
surfaceArea,{ref}`schema:dimensions:area`
*surfaceArea (from {ref}`schema:concentrationmodel`)*,{ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration



<i>**On Conditions**</i>

: IF concentration &lt; 0 THEN
: &emsp;**concentration** = 0








<i>**Time Derivatives**</i>
    : d **concentration** /dt = (iCa/surfaceArea) * 1e-9 * phi - ((concentration - restingConc) * beta)
    

````

(schema:species)=

## species




<i>Description of a chemical species identified by **ion,** which has internal, **concentration,** and external, **extConcentration** values for its concentration.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

initialConcentration,{ref}`schema:dimensions:concentration`
initialExtConcentration,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,
segmentGroup,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

concentrationModel, {ref}`schema:concentrationmodel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

concentration,{ref}`schema:dimensions:concentration`
extConcentration,{ref}`schema:dimensions:concentration`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **concentrationModel**









<i>**Derived Variables**</i>
    : **concentration** =&nbsp;concentrationModel->concentration&emsp;(exposed as **concentration**)
    : **extConcentration** =&nbsp;concentrationModel->extConcentration&emsp;(exposed as **extConcentration**)
    





````

(schema:cell)=

## cell




extends *{ref}`schema:basecellmembpot`*



<i>Cell with  {ref}`schema:segment`s specified in a  {ref}`schema:morphology` element along with details on its  {ref}`schema:biophysicalproperties`. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v** of this cell represents the membrane potential in that isopotential segment.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

neuroLexId,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

morphology, {ref}`schema:morphology`
biophysicalProperties, {ref}`schema:biophysicalproperties`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

caConc,{ref}`schema:dimensions:concentration`
caConcExt,{ref}`schema:dimensions:concentration`
iCa,{ref}`schema:dimensions:current`
iChannels,{ref}`schema:dimensions:current`
iSyn,{ref}`schema:dimensions:current`
spiking,Dimensionless
surfaceArea,{ref}`schema:dimensions:area`
totSpecCap,{ref}`schema:dimensions:specificCapacitance`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless &emsp;(exposed as **spiking**)









<i>**On Start**</i>
: **spiking** = 0
: **v** = initMembPot



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;**spiking** = 1
: &emsp;EVENT OUT on port **spike**

: IF v &lt; thresh THEN
: &emsp;**spiking** = 0





<i>**Derived Variables**</i>
    : **initMembPot** =&nbsp;biophysicalProperties->membraneProperties->initMembPotential->value
    : **thresh** =&nbsp;biophysicalProperties->membraneProperties->spikeThresh->value
    : **surfaceArea** =&nbsp;morphology->segments[*]->surfaceArea(reduce method: add)&emsp;(exposed as **surfaceArea**)
    : **totSpecCap** =&nbsp;biophysicalProperties->totSpecCap&emsp;(exposed as **totSpecCap**)
    : **totCap** =&nbsp;totSpecCap * surfaceArea 
    : **iChannels** =&nbsp;biophysicalProperties->membraneProperties->totChanCurrent&emsp;(exposed as **iChannels**)
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iCa** =&nbsp;biophysicalProperties->membraneProperties->iCa&emsp;(exposed as **iCa**)
    : **caConc** =&nbsp;biophysicalProperties->intracellularProperties->caConc&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;biophysicalProperties->intracellularProperties->caConcExt&emsp;(exposed as **caConcExt**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = (iChannels + iSyn) / totCap
    

````

(schema:cell2capools)=

## cell2CaPools




extends {ref}`schema:cell`



<i>Variant of cell with two independent Ca2+ pools. Cell with  {ref}`schema:segment`s specified in a  {ref}`schema:morphology` element along with details on its  {ref}`schema:biophysicalproperties`. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v** of this cell represents the membrane potential in that isopotential segment.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

neuroLexId,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

biophysicalProperties2CaPools, {ref}`schema:biophysicalproperties2capools`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*caConc (from {ref}`schema:cell`)*,{ref}`schema:dimensions:concentration`
caConc2,{ref}`schema:dimensions:concentration`
*caConcExt (from {ref}`schema:cell`)*,{ref}`schema:dimensions:concentration`
caConcExt2,{ref}`schema:dimensions:concentration`
*iCa (from {ref}`schema:cell`)*,{ref}`schema:dimensions:current`
iCa2,{ref}`schema:dimensions:current`
*iChannels (from {ref}`schema:cell`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:cell`)*,{ref}`schema:dimensions:current`
*spiking (from {ref}`schema:cell`)*,Dimensionless
*surfaceArea (from {ref}`schema:cell`)*,{ref}`schema:dimensions:area`
*totSpecCap (from {ref}`schema:cell`)*,{ref}`schema:dimensions:specificCapacitance`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless &emsp;(exposed as **spiking**)









<i>**On Start**</i>
: **spiking** = 0
: **v** = initMembPot



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;**spiking** = 1
: &emsp;EVENT OUT on port **spike**

: IF v &lt; thresh THEN
: &emsp;**spiking** = 0





<i>**Derived Variables**</i>
    : **initMembPot** =&nbsp;biophysicalProperties2CaPools->membraneProperties2CaPools->initMembPotential->value
    : **thresh** =&nbsp;biophysicalProperties2CaPools->membraneProperties2CaPools->spikeThresh->value
    : **surfaceArea** =&nbsp;morphology->segments[*]->surfaceArea(reduce method: add)&emsp;(exposed as **surfaceArea**)
    : **totSpecCap** =&nbsp;biophysicalProperties2CaPools->totSpecCap&emsp;(exposed as **totSpecCap**)
    : **totCap** =&nbsp;totSpecCap * surfaceArea 
    : **iChannels** =&nbsp;biophysicalProperties2CaPools->membraneProperties2CaPools->totChanCurrent&emsp;(exposed as **iChannels**)
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iCa** =&nbsp;biophysicalProperties2CaPools->membraneProperties2CaPools->iCa&emsp;(exposed as **iCa**)
    : **caConc** =&nbsp;biophysicalProperties2CaPools->intracellularProperties2CaPools->caConc&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;biophysicalProperties2CaPools->intracellularProperties2CaPools->caConcExt&emsp;(exposed as **caConcExt**)
    : **iCa2** =&nbsp;biophysicalProperties2CaPools->membraneProperties2CaPools->iCa2&emsp;(exposed as **iCa2**)
    : **caConc2** =&nbsp;biophysicalProperties2CaPools->intracellularProperties2CaPools->caConc2&emsp;(exposed as **caConc2**)
    : **caConcExt2** =&nbsp;biophysicalProperties2CaPools->intracellularProperties2CaPools->caConcExt2&emsp;(exposed as **caConcExt2**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = (iChannels + iSyn) / totCap
    

````

(schema:basecellmembpotcap)=

## *baseCellMembPotCap*




extends *{ref}`schema:basecellmembpot`*



<i>Any cell with a membrane potential **v** with voltage units and a membrane capacitance **C.** Also defines exposed value **iSyn** for current due to external synapses and **iMemb** for total transmembrane current (usually channel currents plus **iSyn)**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

C,{ref}`schema:dimensions:capacitance`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

iMemb,{ref}`schema:dimensions:current`
iSyn,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

(schema:baseiaf)=

## *baseIaf*




extends *{ref}`schema:basecellmembpot`*



<i>Base ComponentType for an integrate and fire cell which emits a spiking event at membrane potential **thresh** and and resets to **reset**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

reset,{ref}`schema:dimensions:voltage`
thresh,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

(schema:iaftaucell)=

## iafTauCell




extends *{ref}`schema:baseiaf`*



<i>Integrate and fire cell which returns to its leak reversal potential of **leakReversal** with a time constant **tau**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

leakReversal,{ref}`schema:dimensions:voltage`
*reset (from {ref}`schema:baseiaf`)*,{ref}`schema:dimensions:voltage`
tau,{ref}`schema:dimensions:time`
*thresh (from {ref}`schema:baseiaf`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)









<i>**On Start**</i>
: **v** = leakReversal



<i>**On Conditions**</i>

: IF v &gt; thresh THEN
: &emsp;**v** = reset
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **v** /dt = (leakReversal - v) / tau
    

````

(schema:iaftaurefcell)=

## iafTauRefCell




extends {ref}`schema:iaftaucell`



<i>Integrate and fire cell which returns to its leak reversal potential of **leakReversal** with a time course **tau.** It has a refractory period of **refract** after spiking.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*leakReversal (from {ref}`schema:iaftaucell`)*,{ref}`schema:dimensions:voltage`
refract,{ref}`schema:dimensions:time`
*reset (from {ref}`schema:baseiaf`)*,{ref}`schema:dimensions:voltage`
*tau (from {ref}`schema:iaftaucell`)*,{ref}`schema:dimensions:time`
*thresh (from {ref}`schema:baseiaf`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = leakReversal









<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = reset
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + refract THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; thresh THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (leakReversal - v) / tau
````

(schema:baseiafcapcell)=

## *baseIafCapCell*




extends *{ref}`schema:basecellmembpotcap`*



<i>Base Type for all Integrate and Fire cells with a capacitance **C,** threshold **thresh** and reset membrane potential **reset**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
reset,{ref}`schema:dimensions:voltage`
thresh,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

(schema:iafcell)=

## iafCell




extends *{ref}`schema:baseiafcapcell`*



<i>Integrate and fire cell with capacitance **C,** **leakConductance** and **leakReversal**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
leakConductance,{ref}`schema:dimensions:conductance`
leakReversal,{ref}`schema:dimensions:voltage`
*reset (from {ref}`schema:baseiafcapcell`)*,{ref}`schema:dimensions:voltage`
*thresh (from {ref}`schema:baseiafcapcell`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)









<i>**On Start**</i>
: **v** = leakReversal



<i>**On Conditions**</i>

: IF v &gt; thresh THEN
: &emsp;**v** = reset
: &emsp;EVENT OUT on port **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;leakConductance * (leakReversal - v) + iSyn&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb / C
    

````

(schema:iafrefcell)=

## iafRefCell




extends {ref}`schema:iafcell`



<i>Integrate and fire cell  with capacitance **C,** **leakConductance,** **leakReversal** and refractory period **refract**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
*leakConductance (from {ref}`schema:iafcell`)*,{ref}`schema:dimensions:conductance`
*leakReversal (from {ref}`schema:iafcell`)*,{ref}`schema:dimensions:voltage`
refract,{ref}`schema:dimensions:time`
*reset (from {ref}`schema:baseiafcapcell`)*,{ref}`schema:dimensions:voltage`
*thresh (from {ref}`schema:baseiafcapcell`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = leakReversal





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;leakConductance * (leakReversal - v) + iSyn&emsp;(exposed as **iMemb**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = reset
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + refract THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; thresh THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = iMemb / C
````

(schema:izhikevichcell)=

## izhikevichCell




extends *{ref}`schema:basecellmembpot`*



<i>Cell based on the 2003 model of Izhikevich, see http://izhikevich.org/publications/spikes.htm.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

a,Dimensionless
b,Dimensionless
c,Dimensionless
d,Dimensionless
thresh,{ref}`schema:dimensions:voltage`
v0,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MSEC = 1ms, {ref}`schema:dimensions:time`
MVOLT = 1mV, {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

U,Dimensionless
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrentdl`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **U**: Dimensionless &emsp;(exposed as **U**)









<i>**On Start**</i>
: **v** = v0
: **U** = v0 * b / MVOLT



<i>**On Conditions**</i>

: IF v &gt; thresh THEN
: &emsp;**v** = c * MVOLT
: &emsp;**U** = U + d
: &emsp;EVENT OUT on port **spike**





<i>**Derived Variables**</i>
    : **ISyn** =&nbsp;synapses[*]->I(reduce method: add)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = (0.04 * v^2 / MVOLT + 5 * v + (140.0 - U + ISyn) * MVOLT)/MSEC
    : d **U** /dt = a * (b * v / MVOLT - U) / MSEC
    

````

(schema:izhikevich2007cell)=

## izhikevich2007Cell




extends *{ref}`schema:basecellmembpotcap`*



<i>Cell based on the modified Izhikevich model in Izhikevich 2007, Dynamical systems in neuroscience, MIT Press.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
a,{ref}`schema:dimensions:per_time`
b,{ref}`schema:dimensions:conductance`
c,{ref}`schema:dimensions:voltage`
d,{ref}`schema:dimensions:current`
k,{ref}`schema:dimensions:conductance_per_voltage`
v0,{ref}`schema:dimensions:voltage`
vpeak,{ref}`schema:dimensions:voltage`
vr,{ref}`schema:dimensions:voltage`
vt,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
u,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **u**: {ref}`schema:dimensions:current` &emsp;(exposed as **u**)









<i>**On Start**</i>
: **v** = v0
: **u** = 0



<i>**On Conditions**</i>

: IF v &gt; vpeak THEN
: &emsp;**v** = c
: &emsp;**u** = u + d
: &emsp;EVENT OUT on port **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;k * (v-vr) * (v-vt) + iSyn - u&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb / C
    : d **u** /dt = a * (b * (v-vr) - u)
    

````

(schema:adexiafcell)=

## adExIaFCell




extends *{ref}`schema:basecellmembpotcap`*



<i>Model based on Brette R and Gerstner W (2005) Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity. J Neurophysiol 94:3637-3642.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
EL,{ref}`schema:dimensions:voltage`
VT,{ref}`schema:dimensions:voltage`
a,{ref}`schema:dimensions:conductance`
b,{ref}`schema:dimensions:current`
delT,{ref}`schema:dimensions:voltage`
gL,{ref}`schema:dimensions:conductance`
refract,{ref}`schema:dimensions:time`
reset,{ref}`schema:dimensions:voltage`
tauw,{ref}`schema:dimensions:time`
thresh,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iMemb (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*iSyn (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`
w,{ref}`schema:dimensions:current`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **w**: {ref}`schema:dimensions:current` &emsp;(exposed as **w**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = EL
: **w** = 0





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;-1 * gL * (v - EL) + gL * delT * exp((v - VT) / delT) - w + iSyn&emsp;(exposed as **iMemb**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = reset
: &emsp; **w** = w + b
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + refract THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**
: <i>**Time derivatives**</i>
: &emsp; d **w** /dt = (a * (v - EL) - w) / tauw

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; thresh THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = iMemb / C
: &emsp; d **w** /dt = (a * (v - EL) - w) / tauw
````

(schema:fitzhughnagumocell)=

## fitzHughNagumoCell




extends *{ref}`schema:basecellmembpotdl`*



<i>Simple dimensionless model of spiking cell from FitzHugh and Nagumo. Superseded by **fitzHughNagumo1969Cell** (See https://github.com/NeuroML/NeuroML2/issues/42).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

I,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SEC = 1s, {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*V (from {ref}`schema:basecellmembpotdl`)*,Dimensionless
W,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **V**: Dimensionless &emsp;(exposed as **V**)
: **W**: Dimensionless &emsp;(exposed as **W**)










<i>**Time Derivatives**</i>
    : d **V** /dt = ( (V - ((V^3) / 3)) - W + I) / SEC
    : d **W** /dt = (0.08 * (V + 0.7 - 0.8 * W)) / SEC
    

````

(schema:pinskyrinzelca3cell)=

## pinskyRinzelCA3Cell




extends *{ref}`schema:basecellmembpot`*



<i>Reduced CA3 cell model from Pinsky and Rinzel 1994. See https://github.com/OpenSourceBrain/PinskyRinzelModel.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

alphac,Dimensionless
betac,Dimensionless
cm,{ref}`schema:dimensions:specificCapacitance`
eCa,{ref}`schema:dimensions:voltage`
eK,{ref}`schema:dimensions:voltage`
eL,{ref}`schema:dimensions:voltage`
eNa,{ref}`schema:dimensions:voltage`
gAmpa,{ref}`schema:dimensions:conductanceDensity`
gCa,{ref}`schema:dimensions:conductanceDensity`
gKC,{ref}`schema:dimensions:conductanceDensity`
gKahp,{ref}`schema:dimensions:conductanceDensity`
gKdr,{ref}`schema:dimensions:conductanceDensity`
gLd,{ref}`schema:dimensions:conductanceDensity`
gLs,{ref}`schema:dimensions:conductanceDensity`
gNa,{ref}`schema:dimensions:conductanceDensity`
gNmda,{ref}`schema:dimensions:conductanceDensity`
gc,{ref}`schema:dimensions:conductanceDensity`
iDend,{ref}`schema:dimensions:currentDensity`
iSoma,{ref}`schema:dimensions:currentDensity`
pp,Dimensionless
qd0,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MSEC = 1 ms, {ref}`schema:dimensions:time`
MVOLT = 1 mV, {ref}`schema:dimensions:voltage`
UAMP_PER_CM2 = 1 uA_per_cm2, {ref}`schema:dimensions:currentDensity`
Smax = 125.0, Dimensionless
Vsyn = 60.0 mV, {ref}`schema:dimensions:voltage`
betaqd = 0.001, Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

Cad,Dimensionless
ICad,{ref}`schema:dimensions:currentDensity`
Si,Dimensionless
Vd,{ref}`schema:dimensions:voltage`
Vs,{ref}`schema:dimensions:voltage`
Wi,Dimensionless
cd,Dimensionless
hs,Dimensionless
ns,Dimensionless
qd,Dimensionless
sd,Dimensionless
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **Vs**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **Vs**)
: **Vd**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **Vd**)
: **Cad**: Dimensionless &emsp;(exposed as **Cad**)
: **hs**: Dimensionless &emsp;(exposed as **hs**)
: **ns**: Dimensionless &emsp;(exposed as **ns**)
: **sd**: Dimensionless &emsp;(exposed as **sd**)
: **cd**: Dimensionless &emsp;(exposed as **cd**)
: **qd**: Dimensionless &emsp;(exposed as **qd**)
: **Si**: Dimensionless &emsp;(exposed as **Si**)
: **Wi**: Dimensionless &emsp;(exposed as **Wi**)
: **Sisat**: Dimensionless 









<i>**On Start**</i>
: **Vs** = eL
: **Vd** = eL
: **qd** = qd0





<i>**Derived Variables**</i>
    : **v** =&nbsp;Vs&emsp;(exposed as **v**)
    : **ICad** =&nbsp;gCa*sd*sd*(Vd-eCa)&emsp;(exposed as **ICad**)
    : **alphams_Vs** =&nbsp;0.32*(-46.9-Vs/MVOLT)/(exp((-46.9-Vs/MVOLT)/4.0)-1.0)
    : **betams_Vs** =&nbsp;0.28*(Vs/MVOLT+19.9)/(exp((Vs/MVOLT+19.9)/5.0)-1.0)
    : **Minfs_Vs** =&nbsp;alphams_Vs/(alphams_Vs+betams_Vs)
    : **alphans_Vs** =&nbsp;0.016*(-24.9-Vs/MVOLT)/(exp((-24.9-Vs/MVOLT)/5.0)-1.0)
    : **betans_Vs** =&nbsp;0.25*exp(-1.0-0.025*Vs/MVOLT)
    : **alphahs_Vs** =&nbsp;0.128*exp((-43.0-Vs/MVOLT)/18.0)
    : **betahs_Vs** =&nbsp;4.0/(1.0+exp((-20.0-Vs/MVOLT)/5.0))
    : **alphasd_Vd** =&nbsp;1.6/(1.0+exp(-0.072*(Vd/MVOLT-5.0)))
    : **betasd_Vd** =&nbsp;0.02*(Vd/MVOLT+8.9)/(exp((Vd/MVOLT+8.9)/5.0)-1.0)
    : **Iampa** =&nbsp;gAmpa*Wi*(Vd-Vsyn)
    : **Inmda** =&nbsp;gNmda*Sisat*(Vd-Vsyn)/(1.0+0.28*exp(-0.062*(Vd/MVOLT-60.0)))
    : **Isyn** =&nbsp;Iampa+Inmda
    



<i>**Conditional Derived Variables**</i>
    
: IF 0.00002*Cad &gt; 0.01 THEN
: &emsp; **alphaqd** = 0.01 
: OTHERWISE
: &emsp; **alphaqd** = 0.00002\*Cad 
: IF Cad/250 &gt; 1 THEN
: &emsp; **chid** = 1 
: OTHERWISE
: &emsp; **chid** = Cad/250 
: IF Vd &lt; -10*MVOLT THEN
: &emsp; **alphacd_Vd** = exp((Vd/MVOLT+50.0)/11-(Vd/MVOLT+53.5)/27)/18.975 
: OTHERWISE
: &emsp; **alphacd_Vd** = 2.0\*exp((-53.5-Vd/MVOLT)/27.0) 
: IF Vd &lt; -10*MVOLT THEN
: &emsp; **betacd_Vd** = (2.0\*exp((-53.5-Vd/MVOLT)/27.0)-alphacd_Vd) 
: OTHERWISE
: &emsp; **betacd_Vd** = 0 
: IF Si &gt; Smax THEN
: &emsp; **Sisat** = Smax 
: OTHERWISE
: &emsp; **Sisat** = Si 


<i>**Time Derivatives**</i>
    : d **Vs** /dt = (-gLs*(Vs-eL)-gNa*(Minfs_Vs^2)*hs*(Vs-eNa)-gKdr*ns*(Vs-eK)+(gc/pp)*(Vd-Vs)+iSoma/pp) / cm
    : d **Vd** /dt = (iDend/(1.0-pp)-Isyn/(1.0-pp)-gLd*(Vd-eL)-ICad-gKahp*qd*(Vd-eK)-gKC*cd*chid*(Vd-eK)+(gc*(Vs-Vd))/(1.0-pp)) / cm
    : d **Cad** /dt = (-0.13*ICad/UAMP_PER_CM2-0.075*Cad) / MSEC
    : d **hs** /dt = (alphahs_Vs-(alphahs_Vs+betahs_Vs)*hs) / MSEC
    : d **ns** /dt = (alphans_Vs-(alphans_Vs+betans_Vs)*ns) / MSEC
    : d **sd** /dt = (alphasd_Vd-(alphasd_Vd+betasd_Vd)*sd) / MSEC
    : d **cd** /dt = (alphacd_Vd-(alphacd_Vd+betacd_Vd)*cd) / MSEC
    : d **qd** /dt = (alphaqd-(alphaqd+betaqd)*qd) / MSEC
    : d **Si** /dt = -Si/150.0
    : d **Wi** /dt = -Wi/2.0
    

````
