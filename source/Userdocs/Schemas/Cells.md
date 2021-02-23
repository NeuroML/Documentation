
(schema:cells)=
# Cells



Original ComponentType definitions: [Cells.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Cells.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:basecell)=

## *baseCell*




extends *{ref}`schema:basestandalone`*



<i>Base type of any cell which can be used in a population.</i>



(schema:basespikingcell)=

## *baseSpikingCell*




extends *{ref}`schema:basecell`*



<i>Base type of any cell which can emit _spike events.</i>



(schema:basecellmembpot)=

## *baseCellMembPot*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a membrane potential _v with voltage units.</i>



(schema:basecellmembpotdl)=

## *baseCellMembPotDL*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a dimensioness membrane potential, _V.</i>



(schema:basechannelpopulation)=

## *baseChannelPopulation*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for any current produced by a population of channels, all of type _ionChannel.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

ionChannel, {ref}`schema:baseionchannel`

```
````

(schema:channelpopulation)=

## channelPopulation




extends *{ref}`schema:basechannelpopulation`*



<i>Population of _number ohmic ion channels. These each produce a conductance _channelg across a reversal potential _erev, giving a total current _i.</i>



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

(schema:channelpopulationnernst)=

## channelPopulationNernst




extends *{ref}`schema:basechannelpopulation`*



<i>Population of channels with a time varying reversal potential _erev determined by Nernst equation. Hard coded for Ca only!.</i>



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

(schema:variableparameter)=

## variableParameter




<i>Specifies a parameter which can vary its value across a _segmentGroup.</i>



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




<i>Specifies the value of a _variableParameter_.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

inhomogeneousParameter,
value,

````

(schema:channeldensitynonuniform)=

## channelDensityNonUniform




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying ohmic conductance density, which is distributed on a region of the cell. The conductance density of the channel is not uniform, but is set using the _variableParameter_. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



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

(schema:channeldensitynonuniformnernst)=

## channelDensityNonUniformNernst




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the cell, and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the _variableParameter_. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



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

(schema:channeldensitynonuniformghk)=

## channelDensityNonUniformGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the cell, and whose current is calculated from the Goldman-Hodgkin-Katz equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the _variableParameter_. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



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

(schema:channeldensity)=

## channelDensity




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying ohmic conductance density, _gDensity, which is distributed on an area of the cell with fixed reversal potential _erev producing a current density _iDensity.</i>



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

(schema:channeldensityvshift)=

## channelDensityVShift




extends {ref}`schema:channeldensity`



<i>Same as _channelDensity_, but with a _vShift parameter to change voltage activation of gates. The exact usage of _vShift in expressions for rates is determined by the individual gates.</i>



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

(schema:channeldensitynernst)=

## channelDensityNernst




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying conductance density, _gDensity, which is distributed on an area of the cell, producing a current density _iDensity and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>



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

(schema:channeldensitynernstca2)=

## channelDensityNernstCa2




extends *{ref}`schema:basechanneldensitycond`*



<i>This component is similar to the original component type _ channelDensityNernst _ but it is changed in order to have a reversal potential that depends on a second independent Ca++ pool (ca2). See https://github.com/OpenSourceBrain/ghk-nernst.</i>



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

(schema:channeldensityghk)=

## channelDensityGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, _gDensity, which is distributed on an area of the cell, producing a current density _iDensity and whose reversal potential is calculated from the Goldman Hodgkin Katz equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>



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

(schema:channeldensityghk2)=

## channelDensityGHK2




extends *{ref}`schema:basechanneldensitycond`*



<i>Time varying conductance density, _gDensity, which is distributed on an area of the cell, producing a current density _iDensity. Modified version of Jaffe et al. 1994 (used also in Lawrence et al. 2006). See https://github.com/OpenSourceBrain/ghk-nernst.</i>



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

(schema:pointcellcondbased)=

## pointCellCondBased




extends *{ref}`schema:basecellmembpotcap`*



<i>Simple model of a conductance based cell, with no separate morphology element, just an absolute capacitance _C, and a set of channel populations.</i>



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

(schema:pointcellcondbasedca)=

## pointCellCondBasedCa




extends *{ref}`schema:basecellmembpotcap`*



<i>TEMPORARY: Point cell with conductances and Ca concentration  info. Not yet fully tested!!!.</i>



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




<i>A segment defines the smallest unit within a possibly branching structure (_morphology_), such as a dendrite or axon. The shape is given by the _proximal_ and _distal_ points. If _proximal_ is missing, the proximal point is assumed to be the _distal_ point of the parent. _parent_ specifies the parent segment. The first segment (no _parent_) usually represents the soma. NOTE: LEMS does not yet support multicompartmental modelling, so the Dynamics here is only appropriate for single compartment modelling. .</i>



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

(schema:segmentgroup)=

## segmentGroup




<i>A method to describe a group of _segment_s in a _morphology_.</i>



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




<i>A single identified _segment_ which is part of the _segmentGroup_.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,

````

(schema:from)=

## from




<i>Specifies which _segment_ distal from which to calculate the _segmentGroup_.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,

````

(schema:to)=

## to




<i>Specifies which _segment_ up to which to calculate the _segmentGroup_.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segment,

````

(schema:include)=

## include




<i>Include all members of another _segmentGroup_ in this.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

href,
segmentGroup,

````

(schema:path)=

## path




<i>Include all the segments between those specified by _from_ and _to_, inclusive.</i>



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




<i>Include all the segments distal to that specified by _from_ in the _segmentGroup_.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

from, {ref}`schema:from`

```
````

(schema:inhomogeneousparameter)=

## inhomogeneousParameter




<i>An inhomogeneous parameter specified across the _segmentGroup_.</i>



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




<i>The collection of _segment_s which specify the 3D structure of the cell, along with a number of _segmentGroup_s.</i>



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




<i>Properties specific to the membrane, such as the _populations of channels, _channelDensities, _specificCapacitance, etc.</i>



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

(schema:biophysicalproperties)=

## biophysicalProperties




<i>The biophysical properties of the _cell_, including the _membraneProperties_ and the _intracellularProperties_.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

membraneProperties, {ref}`schema:membraneproperties`
intracellularProperties, {ref}`schema:intracellularproperties`

```
````

(schema:biophysicalproperties2capools)=

## biophysicalProperties2CaPools




<i>The biophysical properties of the _cell_, including the _membraneProperties2CaPools_ and the _intracellularProperties2CaPools_ for a cell with two Ca pools.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

membraneProperties2CaPools, {ref}`schema:membraneproperties2capools`
intracellularProperties2CaPools, {ref}`schema:intracellularproperties2capools`

```
````

(schema:intracellularproperties)=

## intracellularProperties




<i>Biophysical properties related to the intracellular space within the _cell_, such as the _resistivity_ and the list of ionic _species_ present. _caConc and _caConcExt are explicitly exposed here to facilitate accessing these values from other Components, even though _caConcExt is clearly not an intracellular property.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

resistivity, {ref}`schema:resistivity`
speciesList, {ref}`schema:species`

```
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




<i>Base for any model of an _ion concentration which changes with time. Internal (_concentration) and external (_extConcentration) values for the concentration of the ion are given.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

ion,

````

(schema:decayingpoolconcentrationmodel)=

## decayingPoolConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of an intracellular buffering mechanism for _ion (currently hard Coded to be calcium, due to requirement for _iCa) which has a baseline level _restingConc and tends to this value with time course _decayConstant. The ion is assumed to occupy a shell inside the membrane of thickness _shellThickness.</i>



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

(schema:fixedfactorconcentrationmodel)=

## fixedFactorConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion (currently hard coded to be calcium, due to requirement for _iCa) which has a baseline level _restingConc and tends to this value with time course _decayConstant. A fixed factor _rho is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change.</i>



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

(schema:fixedfactorconcentrationmodeltraub)=

## fixedFactorConcentrationModelTraub




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion (currently hard coded to be calcium, due to requirement for _iCa) which has a baseline level _restingConc and tends to this value with time course 1 / _beta. A fixed factor _phi is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change. Not recommended for use in models other than Traub et al. 2005!.</i>



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

(schema:species)=

## species




<i>Description of a chemical species identified by _ion, which has internal, _concentration, and external, _extConcentration values for its concentration.</i>



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

(schema:cell)=

## cell




extends *{ref}`schema:basecellmembpot`*



<i>Cell with _segment_s specified in a _morphology_ element along with details on its _biophysicalProperties_. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and _v of this cell represents the membrane potential in that isopotential segment.</i>



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

(schema:cell2capools)=

## cell2CaPools




extends {ref}`schema:cell`



<i>Variant of cell with two independent Ca2+ pools. Cell with _segment_s specified in a _morphology_ element along with details on its _biophysicalProperties_. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and _v of this cell represents the membrane potential in that isopotential segment.</i>



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

(schema:basecellmembpotcap)=

## *baseCellMembPotCap*




extends *{ref}`schema:basecellmembpot`*



<i>Any cell with a membrane potential _v with voltage units and a membrane capacitance _C. Also defines exposed value _iSyn for current due to external synapses and _iMemb for total transmembrane current (usually channel currents plus _iSyn).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

C,{ref}`schema:dimensions:capacitance`

```
````

(schema:baseiaf)=

## *baseIaf*




extends *{ref}`schema:basecellmembpot`*



<i>Base ComponentType for an integrate and fire cell which emits a spiking event at membrane potential _thresh and and resets to _reset.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

reset,{ref}`schema:dimensions:voltage`
thresh,{ref}`schema:dimensions:voltage`

```
````

(schema:iaftaucell)=

## iafTauCell




extends *{ref}`schema:baseiaf`*



<i>Integrate and fire cell which returns to its leak reversal potential of _leakReversal with a time constant _tau.</i>



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

(schema:iaftaurefcell)=

## iafTauRefCell




extends {ref}`schema:iaftaucell`



<i>Integrate and fire cell which returns to its leak reversal potential of _leakReversal with a time course _tau. It has a refractory period of _refract after spiking.</i>



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

(schema:baseiafcapcell)=

## *baseIafCapCell*




extends *{ref}`schema:basecellmembpotcap`*



<i>Base Type for all Integrate and Fire cells with a capacitance _C, threshold _thresh and reset membrane potential _reset.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*C (from {ref}`schema:basecellmembpotcap`)*,{ref}`schema:dimensions:capacitance`
reset,{ref}`schema:dimensions:voltage`
thresh,{ref}`schema:dimensions:voltage`

```
````

(schema:iafcell)=

## iafCell




extends *{ref}`schema:baseiafcapcell`*



<i>Integrate and fire cell with capacitance _C, _leakConductance and _leakReversal.</i>



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

(schema:iafrefcell)=

## iafRefCell




extends {ref}`schema:iafcell`



<i>Integrate and fire cell  with capacitance _C, _leakConductance, _leakReversal and refractory period _refract.</i>



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

(schema:fitzhughnagumocell)=

## fitzHughNagumoCell




extends *{ref}`schema:basecellmembpotdl`*



<i>Simple dimensionless model of spiking cell from FitzHugh and Nagumo. Superseded by _fitzHughNagumo1969Cell (See https://github.com/NeuroML/NeuroML2/issues/42).</i>



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

(schema:synapses)=
# Synapses



Original ComponentType definitions: [Synapses.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Synapses.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:basesynapse)=

## *baseSynapse*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all synapses, i.e. ComponentTypes which produce a current (dimension current) and change Dynamics in response to an incoming event. .</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseSynapse.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000009)


(schema:basevoltagedepsynapse)=

## *baseVoltageDepSynapse*




extends *{ref}`schema:basesynapse`*



<i>Base type for synapses with a dependence on membrane potential.</i>



(schema:basesynapsedl)=

## *baseSynapseDL*




extends *{ref}`schema:basevoltagedeppointcurrentdl`*



<i>Base type for all synapses, i.e. ComponentTypes which produce a dimensionless current and change Dynamics in response to an incoming event. .</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseSynapseDL.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000009)


(schema:basecurrentbasedsynapse)=

## *baseCurrentBasedSynapse*




extends *{ref}`schema:basesynapse`*



<i>Synapse model which produces a synaptic current.</i>



(schema:alphacurrentsynapse)=

## alphaCurrentSynapse




extends *{ref}`schema:basecurrentbasedsynapse`*



<i>Alpha current synapse: rise time and decay time are both _tau.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

ibase,{ref}`schema:dimensions:current`
tau,{ref}`schema:dimensions:time`

```
````

(schema:baseconductancebasedsynapse)=

## *baseConductanceBasedSynapse*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Synapse model which exposes a conductance _g in addition to producing a current. Not necessarily ohmic!! .</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseConductanceBasedSynapse.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000027)


````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`
gbase,{ref}`schema:dimensions:conductance`

```
````

(schema:baseconductancebasedsynapsetwo)=

## *baseConductanceBasedSynapseTwo*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Synapse model suited for a sum of two expTwoSynapses which exposes a conductance _g in addition to producing a current. Not necessarily ohmic!! .</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseConductanceBasedSynapseTwo.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000027)


````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

erev,{ref}`schema:dimensions:voltage`
gbase1,{ref}`schema:dimensions:conductance`
gbase2,{ref}`schema:dimensions:conductance`

```
````

(schema:exponesynapse)=

## expOneSynapse




extends *{ref}`schema:baseconductancebasedsynapse`*



<i>Ohmic synapse model whose conductance rises instantaneously by (_gbase * _weight) on receiving an event, and which decays exponentially to zero with time course _tauDecay.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*erev (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:voltage`
*gbase (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
tauDecay,{ref}`schema:dimensions:time`

```
````

(schema:alphasynapse)=

## alphaSynapse




extends *{ref}`schema:baseconductancebasedsynapse`*



<i>Ohmic synapse model where rise time and decay time are both _tau. Max conductance reached during this time (assuming zero conductance before) is _gbase * _weight.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*erev (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:voltage`
*gbase (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
tau,{ref}`schema:dimensions:time`

```
````

(schema:exptwosynapse)=

## expTwoSynapse




extends *{ref}`schema:baseconductancebasedsynapse`*



<i>Ohmic synapse model whose conductance waveform on receiving an event has a rise time of _tauRise and a decay time of _tauDecay. Max conductance reached during this time (assuming zero conductance before) is _gbase * _weight.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*erev (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:voltage`
*gbase (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
tauDecay,{ref}`schema:dimensions:time`
tauRise,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

peakTime,{ref}`schema:dimensions:time`
waveformFactor,Dimensionless

```
````

(schema:expthreesynapse)=

## expThreeSynapse




extends *{ref}`schema:baseconductancebasedsynapsetwo`*



<i>Ohmic synapse similar to expTwoSynapse but consisting of two components that can differ in decay times and max conductances but share the same rise time.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*erev (from {ref}`schema:baseconductancebasedsynapsetwo`)*,{ref}`schema:dimensions:voltage`
*gbase1 (from {ref}`schema:baseconductancebasedsynapsetwo`)*,{ref}`schema:dimensions:conductance`
*gbase2 (from {ref}`schema:baseconductancebasedsynapsetwo`)*,{ref}`schema:dimensions:conductance`
tauDecay1,{ref}`schema:dimensions:time`
tauDecay2,{ref}`schema:dimensions:time`
tauRise,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

peakTime1,{ref}`schema:dimensions:time`
peakTime2,{ref}`schema:dimensions:time`
waveformFactor1,Dimensionless
waveformFactor2,Dimensionless

```
````

(schema:baseblockmechanism)=

## *baseBlockMechanism*




<i>Base of any ComponentType which produces a varying scaling (or blockage) of synaptic strength of magnitude _scaling.</i>



(schema:voltageconcdepblockmechanism)=

## voltageConcDepBlockMechanism




extends *{ref}`schema:baseblockmechanism`*



<i>Synaptic blocking mechanism which varys with membrane potential across the synapse, e.g. in NMDA receptor mediated synapses.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

blockConcentration,{ref}`schema:dimensions:concentration`
scalingConc,{ref}`schema:dimensions:concentration`
scalingVolt,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

species,

````

(schema:baseplasticitymechanism)=

## *basePlasticityMechanism*




<i>Base plasticity mechanism.</i>



(schema:tsodyksmarkramdepmechanism)=

## tsodyksMarkramDepMechanism




extends *{ref}`schema:baseplasticitymechanism`*



<i>Depression-only Tsodyks-Markram model, as in Tsodyks and Markram 1997.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

initReleaseProb,Dimensionless
tauRec,{ref}`schema:dimensions:time`

```
````

(schema:tsodyksmarkramdepfacmechanism)=

## tsodyksMarkramDepFacMechanism




extends *{ref}`schema:baseplasticitymechanism`*



<i>Full Tsodyks-Markram STP model with both depression and facilitation, as in Tsodyks, Pawelzik and Markram 1998.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

initReleaseProb,Dimensionless
tauFac,{ref}`schema:dimensions:time`
tauRec,{ref}`schema:dimensions:time`

```
````

(schema:blockingplasticsynapse)=

## blockingPlasticSynapse




extends {ref}`schema:exptwosynapse`



<i>Biexponential synapse that allows for     optional block and plasticity     mechanisms, which can be expressed as     child elements.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*erev (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:voltage`
*gbase (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*tauDecay (from {ref}`schema:exptwosynapse`)*,{ref}`schema:dimensions:time`
*tauRise (from {ref}`schema:exptwosynapse`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*peakTime (from {ref}`schema:exptwosynapse`)*,{ref}`schema:dimensions:time`
*waveformFactor (from {ref}`schema:exptwosynapse`)*,Dimensionless

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

plasticityMechanisms, {ref}`schema:baseplasticitymechanism`
blockMechanisms, {ref}`schema:baseblockmechanism`

```
````

(schema:doublesynapse)=

## doubleSynapse




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Synapse consisting of two independent synaptic mechanisms (e.g. AMPA-R and NMDA-R), which can be easily colocated in connections.</i>



````{tabbed} Paths
```{csv-table}
:width: 100%

synapse1Path,
synapse2Path,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse1, {ref}`schema:basesynapse`
synapse2, {ref}`schema:basesynapse`

```
````

(schema:stdpsynapse)=

## stdpSynapse




extends {ref}`schema:exptwosynapse`



<i>Spike timing dependent plasticity mechanism,  NOTE: EXAMPLE NOT YET WORKING!!!! .</i>


[Bioportal entry for Computational Neuroscience Ontology related to stdpSynapse.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000034)


````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*erev (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:voltage`
*gbase (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*tauDecay (from {ref}`schema:exptwosynapse`)*,{ref}`schema:dimensions:time`
*tauRise (from {ref}`schema:exptwosynapse`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*peakTime (from {ref}`schema:exptwosynapse`)*,{ref}`schema:dimensions:time`
*waveformFactor (from {ref}`schema:exptwosynapse`)*,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

tsinceRate = 1, Dimensionless
longTime = 1000s, {ref}`schema:dimensions:time`

```
````

(schema:gapjunction)=

## gapJunction




extends *{ref}`schema:basesynapse`*



<i>Gap junction/single electrical connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

conductance,{ref}`schema:dimensions:conductance`

```
````

(schema:basegradedsynapse)=

## *baseGradedSynapse*




extends *{ref}`schema:basesynapse`*



<i>Base type for graded synapses.</i>



(schema:silentsynapse)=

## silentSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Dummy synapse which emits no current. Used as presynaptic endpoint for analog synaptic connection.</i>



(schema:lineargradedsynapse)=

## linearGradedSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Behaves just like a one way gap junction.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

conductance,{ref}`schema:dimensions:conductance`

```
````

(schema:gradedsynapse)=

## gradedSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Graded/analog synapse. Based on synapse in Methods of http://www.nature.com/neuro/journal/v7/n12/abs/nn1352.html.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

Vth,{ref}`schema:dimensions:voltage`
conductance,{ref}`schema:dimensions:conductance`
delta,{ref}`schema:dimensions:voltage`
erev,{ref}`schema:dimensions:voltage`
k,{ref}`schema:dimensions:per_time`

```
````

(schema:channels)=
# Channels



Original ComponentType definitions: [Channels.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Channels.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:basevoltagedeprate)=

## *baseVoltageDepRate*




<i>Base ComponentType for voltage dependent rate. Produces a time varying rate _r which depends on _v.</i>



(schema:basevoltageconcdeprate)=

## *baseVoltageConcDepRate*




extends *{ref}`schema:basevoltagedeprate`*



<i>Base ComponentType for voltage and concentration dependent rate. Produces a time varying rate _r which depends on _v and _caConc.</i>



(schema:basehhrate)=

## *baseHHRate*




extends *{ref}`schema:basevoltagedeprate`*



<i>Base ComponentType for rate which follow one of the typical forms for rate equations in the standard HH formalism, using the parameters _rate, _midpoint and _scale.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

midpoint,{ref}`schema:dimensions:voltage`
rate,{ref}`schema:dimensions:per_time`
scale,{ref}`schema:dimensions:voltage`

```
````

(schema:hhexprate)=

## HHExpRate




extends *{ref}`schema:basehhrate`*



<i>Exponential form for rate equation (Q: Should these be renamed hhExpRate, etc?).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*midpoint (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:voltage`
*rate (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:per_time`
*scale (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:hhsigmoidrate)=

## HHSigmoidRate




extends *{ref}`schema:basehhrate`*



<i>Sigmoidal form for rate equation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*midpoint (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:voltage`
*rate (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:per_time`
*scale (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:hhexplinearrate)=

## HHExpLinearRate




extends *{ref}`schema:basehhrate`*



<i>Exponential linear form for rate equation. Linear for large positive _v, exponentially decays for large negative _v.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*midpoint (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:voltage`
*rate (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:per_time`
*scale (from {ref}`schema:basehhrate`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:basevoltagedepvariable)=

## *baseVoltageDepVariable*




<i>Base ComponentType for voltage dependent variable  _x, which depends on _v. Can be used for inf/steady state of rate variable.</i>



(schema:basevoltageconcdepvariable)=

## *baseVoltageConcDepVariable*




extends *{ref}`schema:basevoltagedepvariable`*



<i>Base ComponentType for voltage and calcium concentration dependent variable _x, which depends on _v and _caConc.</i>



(schema:basehhvariable)=

## *baseHHVariable*




extends *{ref}`schema:basevoltagedepvariable`*



<i>Base ComponentType for voltage dependent dimensionless variable which follow one of the typical forms for variable equations in the standard HH formalism, using the parameters _rate, _midpoint, _scale.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

midpoint,{ref}`schema:dimensions:voltage`
rate,Dimensionless
scale,{ref}`schema:dimensions:voltage`

```
````

(schema:hhexpvariable)=

## HHExpVariable




extends *{ref}`schema:basehhvariable`*



<i>Exponential form for variable equation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*midpoint (from {ref}`schema:basehhvariable`)*,{ref}`schema:dimensions:voltage`
*rate (from {ref}`schema:basehhvariable`)*,Dimensionless
*scale (from {ref}`schema:basehhvariable`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:hhsigmoidvariable)=

## HHSigmoidVariable




extends *{ref}`schema:basehhvariable`*



<i>Sigmoidal form for variable equation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*midpoint (from {ref}`schema:basehhvariable`)*,{ref}`schema:dimensions:voltage`
*rate (from {ref}`schema:basehhvariable`)*,Dimensionless
*scale (from {ref}`schema:basehhvariable`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:hhexplinearvariable)=

## HHExpLinearVariable




extends *{ref}`schema:basehhvariable`*



<i>Exponential linear form for variable equation. Linear for large positive _v, exponentially decays for large negative _v.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*midpoint (from {ref}`schema:basehhvariable`)*,{ref}`schema:dimensions:voltage`
*rate (from {ref}`schema:basehhvariable`)*,Dimensionless
*scale (from {ref}`schema:basehhvariable`)*,{ref}`schema:dimensions:voltage`

```
````

(schema:basevoltagedeptime)=

## *baseVoltageDepTime*




<i>Base ComponentType for voltage dependent ComponentType producing value _t with dimension time (e.g. for time course of rate variable). Note: time course would not normally be fit to exp/sigmoid etc.</i>



(schema:basevoltageconcdeptime)=

## *baseVoltageConcDepTime*




extends *{ref}`schema:basevoltagedeptime`*



<i>Base type for voltage and calcium concentration dependent ComponentType producing value _t with dimension time (e.g. for time course of rate variable).</i>



(schema:fixedtimecourse)=

## fixedTimeCourse




extends *{ref}`schema:basevoltagedeptime`*



<i>Time course of a fixed magnitude _tau which can be used for the time course in _gateHH_.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

tau,{ref}`schema:dimensions:time`

```
````

(schema:baseq10settings)=

## *baseQ10Settings*




<i>Base ComponentType for a scaling to apply to gating variable time course, usually temperature dependent.</i>



(schema:q10fixed)=

## q10Fixed




extends *{ref}`schema:baseq10settings`*



<i>A fixed value, _fixedQ10, for the scaling of the time course of the gating variable.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

fixedQ10,Dimensionless

```
````

(schema:q10exptemp)=

## q10ExpTemp




extends *{ref}`schema:baseq10settings`*



<i>A value for the Q10 scaling which varies as a standard function of the difference between the current temperature, _temperature, and the temperature at which the gating variable equations were determined, _experimentalTemp.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

experimentalTemp,{ref}`schema:dimensions:temperature`
q10Factor,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

TENDEGREES = 10K, {ref}`schema:dimensions:temperature`

```
````

(schema:baseconductancescaling)=

## *baseConductanceScaling*




<i>Base ComponentType for a scaling to apply to a gate's conductance, e.g. temperature dependent scaling.</i>



(schema:q10conductancescaling)=

## q10ConductanceScaling




extends *{ref}`schema:baseconductancescaling`*



<i>A value for the conductance scaling which varies as a standard function of the difference between the current temperature, _temperature, and the temperature at which the conductance was originally determined, _experimentalTemp.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

experimentalTemp,{ref}`schema:dimensions:temperature`
q10Factor,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

TENDEGREES = 10K, {ref}`schema:dimensions:temperature`

```
````

(schema:baseconductancescalingcadependent)=

## *baseConductanceScalingCaDependent*




extends *{ref}`schema:baseconductancescaling`*



<i>Base ComponentType for a scaling to apply to a gate's conductance which depends on Ca concentration. Usually a generic expression of _caConc (so no standard, non-base form here).</i>



(schema:basegate)=

## *baseGate*




<i>Base ComponentType for a voltage and/or concentration dependent gate.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

instances,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

notes, {ref}`schema:notes`

```
````

(schema:gate)=

## gate




extends *{ref}`schema:basegate`*



<i>Conveniently named baseGate.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

(schema:gatehhrates)=

## gateHHrates




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

forwardRate, {ref}`schema:basevoltagedeprate`
reverseRate, {ref}`schema:basevoltagedeprate`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

q10Settings, {ref}`schema:baseq10settings`

```
````

(schema:gatehhtauinf)=

## gateHHtauInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

timeCourse, {ref}`schema:basevoltagedeptime`
steadyState, {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

q10Settings, {ref}`schema:baseq10settings`

```
````

(schema:gatehhinstantaneous)=

## gateHHInstantaneous




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism but is instantaneous, so tau = 0 and gate follows exactly inf value.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

steadyState, {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SEC = 1 s, {ref}`schema:dimensions:time`

```
````

(schema:gatehhratestau)=

## gateHHratesTau




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

forwardRate, {ref}`schema:basevoltagedeprate`
reverseRate, {ref}`schema:basevoltagedeprate`
timeCourse, {ref}`schema:basevoltagedeptime`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

q10Settings, {ref}`schema:baseq10settings`

```
````

(schema:gatehhratesinf)=

## gateHHratesInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

forwardRate, {ref}`schema:basevoltagedeprate`
reverseRate, {ref}`schema:basevoltagedeprate`
steadyState, {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

q10Settings, {ref}`schema:baseq10settings`

```
````

(schema:gatehhratestauinf)=

## gateHHratesTauInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

forwardRate, {ref}`schema:basevoltagedeprate`
reverseRate, {ref}`schema:basevoltagedeprate`
timeCourse, {ref}`schema:basevoltagedeptime`
steadyState, {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

q10Settings, {ref}`schema:baseq10settings`

```
````

(schema:gatefractional)=

## gateFractional




extends {ref}`schema:gate`



<i>Gate composed of subgates contributing with fractional conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

q10Settings, {ref}`schema:baseq10settings`
subGate, {ref}`schema:subgate`

```
````

(schema:subgate)=

## subGate




<i>Gate composed of subgates contributing with fractional conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

fractionalConductance,Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

notes, {ref}`schema:notes`
timeCourse, {ref}`schema:basevoltagedeptime`
steadyState, {ref}`schema:basevoltagedepvariable`

```
````

(schema:baseionchannel)=

## *baseIonChannel*




<i>Base for all ion channel ComponentTypes.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

conductance,{ref}`schema:dimensions:conductance`

```
````

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

(schema:ionchannelpassive)=

## ionChannelPassive




extends {ref}`schema:ionchannel`



<i>Simple passive ion channel where the constant conductance through the channel is equal to _conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*conductance (from {ref}`schema:baseionchannel`)*,{ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

species,

````

(schema:ionchannelhh)=

## ionChannelHH




extends *{ref}`schema:baseionchannel`*



<i>Note _ionChannel_ and _ionChannelHH_ are currently functionally identical. This is needed since many existing examples use ionChannel, some use ionChannelHH. NeuroML v2beta4 should remove one of these, probably ionChannelHH.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*conductance (from {ref}`schema:baseionchannel`)*,{ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

species,

````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

conductanceScaling, {ref}`schema:baseconductancescaling`
gates, {ref}`schema:gate`

```
````

(schema:ionchannel)=

## ionChannel




extends {ref}`schema:ionchannelhh`



<i>Note _ionChannel_ and _ionChannelHH_ are currently functionally identical. This is needed since many existing examples use ionChannel, some use ionChannelHH. NeuroML v2beta4 should remove one of these, probably ionChannelHH.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*conductance (from {ref}`schema:baseionchannel`)*,{ref}`schema:dimensions:conductance`

```
````

(schema:ionchannelvshift)=

## ionChannelVShift




extends {ref}`schema:ionchannel`



<i>Same as _ionChannel_, but with a _vShift parameter to change voltage activation of gates. The exact usage of _vShift in expressions for rates is determined by the individual gates.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*conductance (from {ref}`schema:baseionchannel`)*,{ref}`schema:dimensions:conductance`
vShift,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

species,

````

(schema:ksstate)=

## KSState




<i>One of the states in which a _gateKS_ can be. The rates of transitions between these states are given by _KSTransition_s.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

relativeConductance,Dimensionless

```
````

(schema:closedstate)=

## closedState




extends {ref}`schema:ksstate`



<i>A _KSState_ with _relativeConductance of 0.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*relativeConductance (from {ref}`schema:ksstate`)*,Dimensionless

```
````

(schema:openstate)=

## openState




extends {ref}`schema:ksstate`



<i>A _KSState_ with _relativeConductance of 1.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*relativeConductance (from {ref}`schema:ksstate`)*,Dimensionless

```
````

(schema:ionchannelks)=

## ionChannelKS




extends *{ref}`schema:baseionchannel`*



<i>A kinetic scheme based ion channel with multiple _gateKS_s, each of which consists of multiple _KSState_s and _KSTransition_s giving the rates of transition between them.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*conductance (from {ref}`schema:baseionchannel`)*,{ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

species,

````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

conductanceScaling, {ref}`schema:baseconductancescaling`
gates, {ref}`schema:gateks`

```
````

(schema:kstransition)=

## KSTransition




<i>Specified the forward and reverse rates of transition between two _KSState_s in a _gateKS_.</i>



(schema:forwardtransition)=

## forwardTransition




extends {ref}`schema:kstransition`



<i>A forward only _KSTransition_ for a _gateKS_ which specifies a _rate (type _baseHHRate_) which follows one of the standard Hodgkin Huxley forms (e.g. _HHExpRate_, _HHSigmoidRate_, _HHExpLinearRate_.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rate, {ref}`schema:basehhrate`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SEC = 1s, {ref}`schema:dimensions:time`

```
````

(schema:reversetransition)=

## reverseTransition




extends {ref}`schema:kstransition`



<i>A reverse only _KSTransition_ for a _gateKS_ which specifies a _rate (type _baseHHRate_) which follows one of the standard Hodgkin Huxley forms (e.g. _HHExpRate_, _HHSigmoidRate_, _HHExpLinearRate_.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rate, {ref}`schema:basehhrate`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SEC = 1s, {ref}`schema:dimensions:time`

```
````

(schema:vhalftransition)=

## vHalfTransition




extends {ref}`schema:kstransition`



<i>Transition which specifies both the forward and reverse rates of transition.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

gamma,Dimensionless
tau,{ref}`schema:dimensions:time`
tauMin,{ref}`schema:dimensions:time`
vHalf,{ref}`schema:dimensions:voltage`
z,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

kte = 25.3mV, {ref}`schema:dimensions:voltage`

```
````

(schema:tauinftransition)=

## tauInfTransition




extends {ref}`schema:kstransition`



<i>KS Transition specified in terms of time constant _tau_ and steady state _inf_.</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

timeCourse, {ref}`schema:basevoltagedeptime`
steadyState, {ref}`schema:basevoltagedepvariable`

```
````

(schema:gateks)=

## gateKS




extends *{ref}`schema:basegate`*



<i>A gate which consists of multiple _KSState_s and _KSTransition_s giving the rates of transition between them.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*instances (from {ref}`schema:basegate`)*,Dimensionless

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

states, {ref}`schema:ksstate`
transitions, {ref}`schema:kstransition`
q10Settings, {ref}`schema:baseq10settings`

```
````

(schema:inputs)=
# Inputs



Original ComponentType definitions: [Inputs.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Inputs.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:basepointcurrent)=

## *basePointCurrent*




extends *{ref}`schema:basestandalone`*



<i>Base type for all ComponentTypes which produce a current _i (with dimension current).</i>



(schema:basevoltagedeppointcurrent)=

## *baseVoltageDepPointCurrent*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all ComponentTypes which produce a current _i (with dimension current) and require a membrane potential _v exposed on the parent Component.</i>



(schema:basevoltagedeppointcurrentspiking)=

## *baseVoltageDepPointCurrentSpiking*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for all ComponentTypes which produce a current _i, require a membrane potential _v exposed on the parent and emit spikes (on a port _spike). The exposed variable _tsince can be used for plotting the time since the Component has spiked last.</i>



(schema:basepointcurrentdl)=

## *basePointCurrentDL*




<i>Base type for all ComponentTypes which produce a dimensionless current _I. There will eventually be dimensionless equivalents of all the core current producing ComponentTypes such as _pulseGenerator_, _sineGenerator_ and _rampGenerator_.</i>



(schema:basevoltagedeppointcurrentdl)=

## *baseVoltageDepPointCurrentDL*




extends *{ref}`schema:basepointcurrentdl`*



<i>Base type for all ComponentTypes which produce a dimensionless current _I and require a dimensionless membrane potential _V exposed on the parent Component.</i>



(schema:basespikesource)=

## *baseSpikeSource*




<i>Base for any ComponentType whose main purpose is to emit spikes (on a port _spike). The exposed variable _tsince can be used for plotting the time since the Component has spiked last.</i>



(schema:spikegenerator)=

## spikeGenerator




extends *{ref}`schema:basespikesource`*



<i>Simple generator of spikes at a regular interval set by _period.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

period,{ref}`schema:dimensions:time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SMALL_TIME = 1e-9ms, {ref}`schema:dimensions:time`

```
````

(schema:spikegeneratorrandom)=

## spikeGeneratorRandom




extends *{ref}`schema:basespikesource`*



<i>Generator of spikes with a random interspike interval of at least _minISI and at most _maxISI.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

maxISI,{ref}`schema:dimensions:time`
minISI,{ref}`schema:dimensions:time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MSEC = 1ms, {ref}`schema:dimensions:time`

```
````

(schema:spikegeneratorpoisson)=

## spikeGeneratorPoisson




extends *{ref}`schema:basespikesource`*



<i>Generator of spikes whose ISI is distributed according to an exponential pdf with scale 1/_averageRate.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

averageRate,{ref}`schema:dimensions:per_time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SMALL_TIME = 1e-9ms, {ref}`schema:dimensions:time`

```
````

(schema:spikegeneratorrefpoisson)=

## spikeGeneratorRefPoisson




extends {ref}`schema:spikegeneratorpoisson`



<i>Generator of spikes whose ISI distribution is the maximum entropy distribution over [_minimumISI, +infinity) with mean 1/_averageRate.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*averageRate (from {ref}`schema:spikegeneratorpoisson`)*,{ref}`schema:dimensions:per_time`
minimumISI,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

averageIsi,{ref}`schema:dimensions:time`

```
````

(schema:poissonfiringsynapse)=

## poissonFiringSynapse




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Poisson spike generator connected to single synapse providing an input current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

averageRate,{ref}`schema:dimensions:per_time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

averageIsi,{ref}`schema:dimensions:time`

```
````

````{tabbed} Paths
```{csv-table}
:width: 100%

spikeTarget,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SMALL_TIME = 1e-9ms, {ref}`schema:dimensions:time`

```
````

(schema:transientpoissonfiringsynapse)=

## transientPoissonFiringSynapse




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Poisson spike generator with delay and duration connected to single synapse providing an input current.                        Similar to ComponentType poissonFiringSynapse.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

averageRate,{ref}`schema:dimensions:per_time`
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

averageIsi,{ref}`schema:dimensions:time`

```
````

````{tabbed} Paths
```{csv-table}
:width: 100%

spikeTarget,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

SMALL_TIME = 1e-9ms, {ref}`schema:dimensions:time`
LONG_TIME = 1e9hour, {ref}`schema:dimensions:time`

```
````

(schema:timedsynapticinput)=

## timedSynapticInput




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Spike array connected to a single synapse, producing current triggered by each spike in the array.</i>



````{tabbed} Paths
```{csv-table}
:width: 100%

spikeTarget,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

spikes, {ref}`schema:spike`

```
````

(schema:pulsegenerator)=

## pulseGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a constant current pulse of a certain _amplitude for a specified _duration after a _delay. Scaled by _weight, if set.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

amplitude,{ref}`schema:dimensions:current`
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`

```
````

(schema:compoundinput)=

## compoundInput




extends *{ref}`schema:basepointcurrent`*



<i>Generates a current which is the sum of all its child _basePointCurrent_ elements.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

currents, {ref}`schema:basepointcurrent`

```
````

(schema:compoundinputdl)=

## compoundInputDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Generates a current which is the sum of all its child _basePointCurrentDL_ elements.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

currents, {ref}`schema:basepointcurrentdl`

```
````

(schema:pulsegeneratordl)=

## pulseGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of _pulseGenerator_. Generates a constant current pulse of a certain _amplitude for a specified _duration after a _delay.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

amplitude,Dimensionless
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`

```
````

(schema:sinegenerator)=

## sineGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a sinusoidally varying current after a time _delay, for a fixed _duration. The _period and maximum _amplitude of the current can be set as well as the _phase at which to start.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

amplitude,{ref}`schema:dimensions:current`
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`
period,{ref}`schema:dimensions:time`
phase,Dimensionless

```
````

(schema:sinegeneratordl)=

## sineGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Generates a sinusoidally varying current after a time _delay, for a fixed _duration. The _period and maximum _amplitude of the current can be set as well as the _phase at which to start.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

amplitude,Dimensionless
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`
period,{ref}`schema:dimensions:time`
phase,Dimensionless

```
````

(schema:rampgenerator)=

## rampGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a ramping current after a time _delay, for a fixed _duration. During this time the current steadily changes from _startAmplitude to _finishAmplitude.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

baselineAmplitude,{ref}`schema:dimensions:current`
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`
finishAmplitude,{ref}`schema:dimensions:current`
startAmplitude,{ref}`schema:dimensions:current`

```
````

(schema:rampgeneratordl)=

## rampGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Generates a ramping current after a time _delay, for a fixed _duration. During this time the dimensionless current steadily changes from _startAmplitude to _finishAmplitude.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

baselineAmplitude,Dimensionless
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`
finishAmplitude,Dimensionless
startAmplitude,Dimensionless

```
````

(schema:voltageclamp)=

## voltageClamp




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Voltage clamp. Applies a variable current _i to try to keep parent at _targetVoltage. Not yet fully tested!!! Consider using voltageClampTriple!!.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`
simpleSeriesResistance,{ref}`schema:dimensions:resistance`
targetVoltage,{ref}`schema:dimensions:voltage`

```
````

(schema:voltageclamptriple)=

## voltageClampTriple




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Voltage clamp with 3 clamp levels. Applies a variable current _i (through _simpleSeriesResistance) to try to keep parent cell at _conditioningVoltage until time _delay, _testingVoltage until _delay + _duration, and _returnVoltage afterwards. Only enabled if _active = 1. .</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

active,Dimensionless
conditioningVoltage,{ref}`schema:dimensions:voltage`
delay,{ref}`schema:dimensions:time`
duration,{ref}`schema:dimensions:time`
returnVoltage,{ref}`schema:dimensions:voltage`
simpleSeriesResistance,{ref}`schema:dimensions:resistance`
testingVoltage,{ref}`schema:dimensions:voltage`

```
````

(schema:spikearray)=

## spikeArray




extends *{ref}`schema:basespikesource`*



<i>Set of spike ComponentTypes, each emitting one spike at a certain time. Can be used to feed a predetermined spike train into a cell.</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

spikes, {ref}`schema:spike`

```
````

(schema:spike)=

## spike




extends *{ref}`schema:basespikesource`*



<i>Emits a single spike at the specified time.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

time,{ref}`schema:dimensions:time`

```
````

(schema:networks)=
# Networks



Original ComponentType definitions: [Networks.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Networks.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:network)=

## network




extends *{ref}`schema:basestandalone`*



<i>Network containing _population_s, _projection_s and lists of _explicitConnection_s (either directly between components of the populations or via synapses).</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

regions, {ref}`schema:region`
populations, {ref}`schema:basepopulation`
projections, {ref}`schema:projection`
synapticConnections, {ref}`schema:explicitconnection`
electricalProjection, {ref}`schema:electricalprojection`
continuousProjection, {ref}`schema:continuousprojection`
explicitInputs, {ref}`schema:explicitinput`
inputs, {ref}`schema:inputlist`

```
````

(schema:networkwithtemperature)=

## networkWithTemperature




extends {ref}`schema:network`



<i>Network containing _population_s, _projection_s and lists of _explicitConnection_s (either directly between components of the populations or via synapses), and an explicit temperature.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

temperature,{ref}`schema:dimensions:temperature`

```
````

(schema:basepopulation)=

## *basePopulation*




extends *{ref}`schema:basestandalone`*



<i>A population of cells (anything which extends _baseCell_).</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

component, {ref}`schema:basecell`

```
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

```
````

(schema:population)=

## population




extends *{ref}`schema:basepopulation`*



<i>A population of components, with just one parameter for the _size.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

size,Dimensionless

```
````

(schema:populationlist)=

## populationList




extends *{ref}`schema:basepopulation`*



<i>An explicit list of the cells in the population. .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

size,

````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

instances, {ref}`schema:instance`

```
````

(schema:instance)=

## instance




<i>Specifies a single instance of a component in a population (placed at _location_).</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

location, {ref}`schema:location`

```
````

(schema:location)=

## location




<i>Specifies location of a single _instance_ of a component in a population.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

x,Dimensionless
y,Dimensionless
z,Dimensionless

```
````

(schema:region)=

## region




<i>Initial attempt to specify 3D region for placing cells. Work in progress...</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rectangularExtent, {ref}`schema:rectangularextent`

```
````

(schema:rectangularextent)=

## rectangularExtent




<i>For defining a 3D rectangular box.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

xLength,Dimensionless
xStart,Dimensionless
yLength,Dimensionless
yStart,Dimensionless
zLength,Dimensionless
zStart,Dimensionless

```
````

(schema:projection)=

## projection




<i>Projection from one population, _presynapticPopulation to another, _postsynapticPopulation, through _synapse. Contains lists of _connection_ or _connectionWD_ elements.</i>



````{tabbed} Paths
```{csv-table}
:width: 100%

presynapticPopulation,
postsynapticPopulation,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

connections, {ref}`schema:connection`
connectionsWD, {ref}`schema:connectionwd`

```
````

(schema:explicitconnection)=

## explicitConnection




<i>Explicit event connection between components.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

targetPort,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

from,
to,

````

(schema:connection)=

## connection




<i>Event connection directly between named components, which gets processed via a new instance of a _synapse component which is created on the target component. Normally contained inside a _projection_ element.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,
preFractionAlong,
postFractionAlong,
preSegmentId,
postSegmentId,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCellId,
postCellId,

````

(schema:synapticconnection)=

## synapticConnection




extends {ref}`schema:explicitconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a _synapse component which is created on the target component.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

from,
to,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

(schema:synapticconnectionwd)=

## synapticConnectionWD




extends {ref}`schema:synapticconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a _synapse component which is created on the target component, includes setting of _weight and _delay for the synaptic connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

delay,{ref}`schema:dimensions:time`
weight,Dimensionless

```
````

````{tabbed} Paths
```{csv-table}
:width: 100%

from,
to,

````

(schema:connectionwd)=

## connectionWD




extends {ref}`schema:connection`



<i>Event connection between named components, which gets processed via a new instance of a synapse component which is created on the target component, includes setting of _weight and _delay for the synaptic connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

delay,{ref}`schema:dimensions:time`
weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,
preFractionAlong,
postFractionAlong,
preSegmentId,
postSegmentId,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCellId,
postCellId,

````

(schema:electricalconnection)=

## electricalConnection




<i>To enable connections between populations through gap junctions.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:gapjunction`

```
````

(schema:electricalconnectioninstance)=

## electricalConnectionInstance




<i>To enable connections between populations through gap junctions. Populations need to be of type _populationList_ and contain _instance_ and _location_ elements.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:gapjunction`

```
````

(schema:electricalconnectioninstancew)=

## electricalConnectionInstanceW




extends {ref}`schema:electricalconnectioninstance`



<i>To enable connections between populations through gap junctions. Populations need to be of type _populationList_ and contain _instance_ and _location_ elements. Includes setting of _weight for the connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

(schema:electricalprojection)=

## electricalProjection




<i>A projection between _presynapticPopulation to another _postsynapticPopulation through gap junctions.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

presynapticPopulation, {ref}`schema:population`
postsynapticPopulation, {ref}`schema:population`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

connections, {ref}`schema:electricalconnection`
connectionInstances, {ref}`schema:electricalconnectioninstance`

```
````

(schema:continuousconnection)=

## continuousConnection




<i>An instance of a connection in a _continuousProjection_ between _presynapticPopulation to another _postsynapticPopulation through a _preComponent at the start and _postComponent at the end. Can be used for analog synapses.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

preComponent, {ref}`schema:basegradedsynapse`
postComponent, {ref}`schema:basegradedsynapse`

```
````

(schema:continuousconnectioninstance)=

## continuousConnectionInstance




<i>An instance of a connection in a _continuousProjection_ between _presynapticPopulation to another _postsynapticPopulation through a _preComponent at the start and _postComponent at the end. Populations need to be of type _populationList_ and contain _instance_ and _location_ elements. Can be used for analog synapses.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

preComponent, {ref}`schema:basegradedsynapse`
postComponent, {ref}`schema:basegradedsynapse`

```
````

(schema:continuousconnectioninstancew)=

## continuousConnectionInstanceW




extends {ref}`schema:continuousconnectioninstance`



<i>An instance of a connection in a _continuousProjection_ between _presynapticPopulation to another _postsynapticPopulation through a _preComponent at the start and _postComponent at the end. Populations need to be of type _populationList_ and contain _instance_ and _location_ elements. Can be used for analog synapses. Includes setting of _weight for the connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

(schema:continuousprojection)=

## continuousProjection




<i>A projection between _presynapticPopulation and _postsynapticPopulation through components _preComponent at the start and _postComponent at the end of a _continuousConnection_ or _continuousConnectionInstance_. Can be used for analog synapses.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

presynapticPopulation, {ref}`schema:population`
postsynapticPopulation, {ref}`schema:population`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

connections, {ref}`schema:continuousconnection`
connectionInstances, {ref}`schema:continuousconnectioninstance`

```
````

(schema:explicitinput)=

## explicitInput




<i>An explicit input (anything which extends _basePointCurrent_) to a target cell in a population.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,
sourcePort,
targetPort,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

target,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

input, {ref}`schema:basepointcurrent`

```
````

(schema:inputlist)=

## inputList




<i>An explicit list of inputs. Not yet stable...</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

population,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

component, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

inputs, {ref}`schema:input`

```
````

(schema:input)=

## input




<i>Specifies input lists.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentId,
fractionAlong,
destination,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

target,

````

(schema:inputw)=

## inputW




extends {ref}`schema:input`



<i>Specifies input lists. Can set _weight to scale individual inputs.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

target,

````

(schema:pynn)=
# PyNN



Original ComponentType definitions: [PyNN.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//PyNN.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:basepynncell)=

## *basePyNNCell*




extends *{ref}`schema:basecellmembpot`*



<i>Base type of any PyNN standard cell model. Note: membrane potential _v has dimensions voltage, but all other parameters are dimensionless. This is to facilitate translation to and from PyNN scripts in Python, where these parameters have implicit units, see http://neuralensemble.org/trac/PyNN/wiki/StandardModels.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

cm,Dimensionless
i_offset,Dimensionless
tau_syn_E,Dimensionless
tau_syn_I,Dimensionless
v_init,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MSEC = 1ms, {ref}`schema:dimensions:time`
MVOLT = 1mV, {ref}`schema:dimensions:voltage`
NFARAD = 1nF, {ref}`schema:dimensions:capacitance`

```
````

(schema:basepynniafcell)=

## *basePyNNIaFCell*




extends *{ref}`schema:basepynncell`*



<i>Base type of any PyNN standard integrate and fire model.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
tau_m,Dimensionless
tau_refrac,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
v_reset,Dimensionless
v_rest,Dimensionless
v_thresh,Dimensionless

```
````

(schema:basepynniafcondcell)=

## *basePyNNIaFCondCell*




extends *{ref}`schema:basepynniafcell`*



<i>Base type of conductance based PyNN IaF cell models.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
e_rev_E,Dimensionless
e_rev_I,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

(schema:if_curr_alpha)=

## IF_curr_alpha




extends *{ref}`schema:basepynniafcell`*



<i>Leaky integrate and fire model with fixed threshold and alpha-function-shaped post-synaptic current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

(schema:if_curr_exp)=

## IF_curr_exp




extends *{ref}`schema:basepynniafcell`*



<i>Leaky integrate and fire model with fixed threshold and decaying-exponential post-synaptic current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

(schema:if_cond_alpha)=

## IF_cond_alpha




extends *{ref}`schema:basepynniafcondcell`*



<i>Leaky integrate and fire model with fixed threshold and alpha-function-shaped post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
*e_rev_E (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*e_rev_I (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

(schema:if_cond_exp)=

## IF_cond_exp




extends *{ref}`schema:basepynniafcondcell`*



<i>Leaky integrate and fire model with fixed threshold and exponentially-decaying post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
*e_rev_E (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*e_rev_I (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

(schema:eif_cond_exp_isfa_ista)=

## EIF_cond_exp_isfa_ista




extends *{ref}`schema:basepynniafcondcell`*



<i>Adaptive exponential integrate and fire neuron according to Brette R and Gerstner W (2005) with exponentially-decaying post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

a,Dimensionless
b,Dimensionless
*cm (from {ref}`schema:basepynncell`)*,Dimensionless
delta_T,Dimensionless
*e_rev_E (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*e_rev_I (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
tau_w,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
v_spike,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

eif_threshold,Dimensionless

```
````

(schema:eif_cond_alpha_isfa_ista)=

## EIF_cond_alpha_isfa_ista




extends *{ref}`schema:basepynniafcondcell`*



<i>Adaptive exponential integrate and fire neuron according to Brette R and Gerstner W (2005) with alpha-function-shaped post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

a,Dimensionless
b,Dimensionless
*cm (from {ref}`schema:basepynncell`)*,Dimensionless
delta_T,Dimensionless
*e_rev_E (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*e_rev_I (from {ref}`schema:basepynniafcondcell`)*,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_m (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_refrac (from {ref}`schema:basepynniafcell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
tau_w,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
*v_reset (from {ref}`schema:basepynniafcell`)*,Dimensionless
*v_rest (from {ref}`schema:basepynniafcell`)*,Dimensionless
v_spike,Dimensionless
*v_thresh (from {ref}`schema:basepynniafcell`)*,Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

eif_threshold,Dimensionless

```
````

(schema:hh_cond_exp)=

## HH_cond_exp




extends *{ref}`schema:basepynncell`*



<i>Single-compartment Hodgkin-Huxley-type neuron with transient sodium and delayed-rectifier potassium currents using the ion channel models from Traub.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*cm (from {ref}`schema:basepynncell`)*,Dimensionless
e_rev_E,Dimensionless
e_rev_I,Dimensionless
e_rev_K,Dimensionless
e_rev_Na,Dimensionless
e_rev_leak,Dimensionless
g_leak,Dimensionless
gbar_K,Dimensionless
gbar_Na,Dimensionless
*i_offset (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_E (from {ref}`schema:basepynncell`)*,Dimensionless
*tau_syn_I (from {ref}`schema:basepynncell`)*,Dimensionless
*v_init (from {ref}`schema:basepynncell`)*,Dimensionless
v_offset,Dimensionless

```
````

(schema:basepynnsynapse)=

## *basePynnSynapse*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Base type for all PyNN synapses. Note, the current _I produced is dimensionless, but it requires a membrane potential _v with dimension voltage.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

tau_syn,Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MSEC = 1ms, {ref}`schema:dimensions:time`
MVOLT = 1mV, {ref}`schema:dimensions:voltage`
NAMP = 1nA, {ref}`schema:dimensions:current`

```
````

(schema:expcondsynapse)=

## expCondSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Conductance based synapse with instantaneous rise and single exponential decay (with time constant tau_syn).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

e_rev,Dimensionless
*tau_syn (from {ref}`schema:basepynnsynapse`)*,Dimensionless

```
````

(schema:expcurrsynapse)=

## expCurrSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Current based synapse with instantaneous rise and single exponential decay (with time constant tau_syn).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*tau_syn (from {ref}`schema:basepynnsynapse`)*,Dimensionless

```
````

(schema:alphacondsynapse)=

## alphaCondSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Alpha synapse: rise time and decay time are both tau_syn. Conductance based synapse.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

e_rev,Dimensionless
*tau_syn (from {ref}`schema:basepynnsynapse`)*,Dimensionless

```
````

(schema:alphacurrsynapse)=

## alphaCurrSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Alpha synapse: rise time and decay time are both tau_syn. Current based synapse.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

*tau_syn (from {ref}`schema:basepynnsynapse`)*,Dimensionless

```
````

(schema:spikesourcepoisson)=

## SpikeSourcePoisson




extends *{ref}`schema:basespikesource`*



<i>Spike source, generating spikes according to a Poisson process.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

duration,{ref}`schema:dimensions:time`
rate,{ref}`schema:dimensions:per_time`
start,{ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

end,{ref}`schema:dimensions:time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

LONG_TIME = 1e9hour, {ref}`schema:dimensions:time`
SMALL_TIME = 1e-9ms, {ref}`schema:dimensions:time`

```
````

(schema:neuromlcoredimensions)=
# NeuroMLCoreDimensions



Original ComponentType definitions: [NeuroMLCoreDimensions.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//NeuroMLCoreDimensions.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

## Dimensions

(schema:dimensions:area)=
### area

```{panels}
Dimensions
^^^
L{superscript}`2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:cm2`

- Defined unit: {ref}`schema:units:m2`

- Defined unit: {ref}`schema:units:um2`

```

(schema:dimensions:capacitance)=
### capacitance

```{panels}
Dimensions
^^^
M{superscript}`-1` L{superscript}`-2` T{superscript}`4` I{superscript}`2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:F`

- Defined unit: {ref}`schema:units:nF`

- Defined unit: {ref}`schema:units:pF`

- Defined unit: {ref}`schema:units:uF`

```

(schema:dimensions:charge)=
### charge

```{panels}
Dimensions
^^^
T{superscript}`1` I{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:C`

```

(schema:dimensions:charge_per_mole)=
### charge\_per\_mole

```{panels}
Dimensions
^^^
T{superscript}`1` I{superscript}`1` N{superscript}`-1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:C_per_mol`

- Defined unit: {ref}`schema:units:nA_ms_per_amol`

```

(schema:dimensions:concentration)=
### concentration

```{panels}
Dimensions
^^^
L{superscript}`-3` N{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:M`

- Defined unit: {ref}`schema:units:mM`

- Defined unit: {ref}`schema:units:mol_per_cm3`

- Defined unit: {ref}`schema:units:mol_per_m3`

```

(schema:dimensions:conductance)=
### conductance

```{panels}
Dimensions
^^^
M{superscript}`-1` L{superscript}`-2` T{superscript}`3` I{superscript}`2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:S`

- Defined unit: {ref}`schema:units:mS`

- Defined unit: {ref}`schema:units:nS`

- Defined unit: {ref}`schema:units:pS`

- Defined unit: {ref}`schema:units:uS`

```

(schema:dimensions:conductanceDensity)=
### conductanceDensity

```{panels}
Dimensions
^^^
M{superscript}`-1` L{superscript}`-4` T{superscript}`3` I{superscript}`2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:S_per_cm2`

- Defined unit: {ref}`schema:units:S_per_m2`

- Defined unit: {ref}`schema:units:mS_per_cm2`

```

(schema:dimensions:conductance_per_voltage)=
### conductance\_per\_voltage

```{panels}
Dimensions
^^^
M{superscript}`-2` L{superscript}`-4` T{superscript}`6` I{superscript}`3` 
---
Units
^^^

- Defined unit: {ref}`schema:units:S_per_V`

- Defined unit: {ref}`schema:units:nS_per_mV`

```

(schema:dimensions:current)=
### current

```{panels}
Dimensions
^^^
I{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:A`

- Defined unit: {ref}`schema:units:nA`

- Defined unit: {ref}`schema:units:pA`

- Defined unit: {ref}`schema:units:uA`

```

(schema:dimensions:currentDensity)=
### currentDensity

```{panels}
Dimensions
^^^
L{superscript}`-2` I{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:A_per_m2`

- Defined unit: {ref}`schema:units:mA_per_cm2`

- Defined unit: {ref}`schema:units:uA_per_cm2`

```

(schema:dimensions:idealGasConstantDims)=
### idealGasConstantDims

```{panels}
Dimensions
^^^
M{superscript}`1` L{superscript}`2` T{superscript}`-2` K{superscript}`-1` N{superscript}`-1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:J_per_K_per_mol`

```

(schema:dimensions:length)=
### length

```{panels}
Dimensions
^^^
L{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:cm`

- Defined unit: {ref}`schema:units:m__`

- Defined unit: {ref}`schema:units:um`

```

(schema:dimensions:per_time)=
### per\_time

```{panels}
Dimensions
^^^
T{superscript}`-1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:Hz`

- Defined unit: {ref}`schema:units:per_hour`

- Defined unit: {ref}`schema:units:per_min`

- Defined unit: {ref}`schema:units:per_ms`

- Defined unit: {ref}`schema:units:per_s`

```

(schema:dimensions:per_voltage)=
### per\_voltage

```{panels}
Dimensions
^^^
M{superscript}`-1` L{superscript}`-2` T{superscript}`3` I{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:per_V`

- Defined unit: {ref}`schema:units:per_mV`

```

(schema:dimensions:permeability)=
### permeability

```{panels}
Dimensions
^^^
L{superscript}`1` T{superscript}`-1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:cm_per_ms`

- Defined unit: {ref}`schema:units:cm_per_s`

- Defined unit: {ref}`schema:units:m_per_s`

- Defined unit: {ref}`schema:units:um_per_ms`

```

(schema:dimensions:resistance)=
### resistance

```{panels}
Dimensions
^^^
M{superscript}`1` L{superscript}`2` T{superscript}`-3` I{superscript}`-2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:Mohm`

- Defined unit: {ref}`schema:units:kohm`

- Defined unit: {ref}`schema:units:ohm`

```

(schema:dimensions:resistivity)=
### resistivity

```{panels}
Dimensions
^^^
M{superscript}`2` L{superscript}`2` T{superscript}`-3` I{superscript}`-2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:kohm_cm`

- Defined unit: {ref}`schema:units:ohm_cm`

- Defined unit: {ref}`schema:units:ohm_m`

```

(schema:dimensions:rho_factor)=
### rho\_factor

```{panels}
Dimensions
^^^
L{superscript}`-1` T{superscript}`-1` I{superscript}`-1` N{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:mol_per_cm_per_uA_per_ms`

- Defined unit: {ref}`schema:units:mol_per_m_per_A_per_s`

```

(schema:dimensions:specificCapacitance)=
### specificCapacitance

```{panels}
Dimensions
^^^
M{superscript}`-1` L{superscript}`-4` T{superscript}`4` I{superscript}`2` 
---
Units
^^^

- Defined unit: {ref}`schema:units:F_per_m2`

- Defined unit: {ref}`schema:units:uF_per_cm2`

```

(schema:dimensions:substance)=
### substance

```{panels}
Dimensions
^^^
N{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:mol`

```

(schema:dimensions:temperature)=
### temperature

```{panels}
Dimensions
^^^
K{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:K`

- Defined unit: {ref}`schema:units:degC`

```

(schema:dimensions:time)=
### time

```{panels}
Dimensions
^^^
T{superscript}`1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:hour`

- Defined unit: {ref}`schema:units:min`

- Defined unit: {ref}`schema:units:ms__`

- Defined unit: {ref}`schema:units:s__`

```

(schema:dimensions:voltage)=
### voltage

```{panels}
Dimensions
^^^
M{superscript}`1` L{superscript}`2` T{superscript}`-3` I{superscript}`-1` 
---
Units
^^^

- Defined unit: {ref}`schema:units:V`

- Defined unit: {ref}`schema:units:mV`

```

(schema:dimensions:volume)=
### volume

```{panels}
Dimensions
^^^
L{superscript}`3` 
---
Units
^^^

- Defined unit: {ref}`schema:units:cm3`

- Defined unit: {ref}`schema:units:litre`

- Defined unit: {ref}`schema:units:m3`

- Defined unit: {ref}`schema:units:um3`

```





## Units

(schema:units:A)=
### A

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: 0



----
Conversions
^^^

- 1 A = 1.0E+9 {ref}`schema:units:nA`
- 1 A = 1.0E+12 {ref}`schema:units:pA`
- 1 A = 1.0E+6 {ref}`schema:units:uA`

```

(schema:units:A_per_m2)=
### A_per_m2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:currentDensity`
- Power of 10: 0



----
Conversions
^^^

- 1 A_per_m2 = 0.1 {ref}`schema:units:mA_per_cm2`
- 1 A_per_m2 = 1.0E+2 {ref}`schema:units:uA_per_cm2`

```

(schema:units:C)=
### C

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:charge`
- Power of 10: 0



```

(schema:units:C_per_mol)=
### C_per_mol

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:charge_per_mole`
- Power of 10: 0



----
Conversions
^^^

- 1 C_per_mol = 0.000001 {ref}`schema:units:nA_ms_per_amol`

```

(schema:units:F)=
### F

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: 0



----
Conversions
^^^

- 1 F = 1.0E+9 {ref}`schema:units:nF`
- 1 F = 1.0E+12 {ref}`schema:units:pF`
- 1 F = 1.0E+6 {ref}`schema:units:uF`

```

(schema:units:F_per_m2)=
### F_per_m2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:specificCapacitance`
- Power of 10: 0



----
Conversions
^^^

- 1 F_per_m2 = 1.0E+2 {ref}`schema:units:uF_per_cm2`

```

(schema:units:Hz)=
### Hz

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0



----
Conversions
^^^

- 1 Hz = 3.6E+3 {ref}`schema:units:per_hour`
- 1 Hz = 60 {ref}`schema:units:per_min`
- 1 Hz = 0.001 {ref}`schema:units:per_ms`
- 1 Hz = 1 {ref}`schema:units:per_s`

```

(schema:units:J_per_K_per_mol)=
### J_per_K_per_mol

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:idealGasConstantDims`
- Power of 10: 0



```

(schema:units:K)=
### K

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:temperature`
- Power of 10: 0



----
Conversions
^^^

- 1 K = 0.0036 {ref}`schema:units:degC`

```

(schema:units:M)=
### M

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 3



----
Conversions
^^^

- 1 M = 1.0E+3 {ref}`schema:units:mM`
- 1 M = 0.001 {ref}`schema:units:mol_per_cm3`
- 1 M = 1.0E+3 {ref}`schema:units:mol_per_m3`

```

(schema:units:Mohm)=
### Mohm

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:resistance`
- Power of 10: 6



----
Conversions
^^^

- 1 Mohm = 1.0E+3 {ref}`schema:units:kohm`
- 1 Mohm = 1.0E+6 {ref}`schema:units:ohm`

```

(schema:units:S)=
### S

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: 0



----
Conversions
^^^

- 1 S = 1.0E+3 {ref}`schema:units:mS`
- 1 S = 1.0E+9 {ref}`schema:units:nS`
- 1 S = 1.0E+12 {ref}`schema:units:pS`
- 1 S = 1.0E+6 {ref}`schema:units:uS`

```

(schema:units:S_per_V)=
### S_per_V

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance_per_voltage`
- Power of 10: 0



----
Conversions
^^^

- 1 S_per_V = 1.0E+6 {ref}`schema:units:nS_per_mV`

```

(schema:units:S_per_cm2)=
### S_per_cm2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: 4



----
Conversions
^^^

- 1 S_per_cm2 = 1.0E+4 {ref}`schema:units:S_per_m2`
- 1 S_per_cm2 = 1.0E+3 {ref}`schema:units:mS_per_cm2`

```

(schema:units:S_per_m2)=
### S_per_m2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: 0



----
Conversions
^^^

- 1 S_per_m2 = 0.0001 {ref}`schema:units:S_per_cm2`
- 1 S_per_m2 = 0.1 {ref}`schema:units:mS_per_cm2`

```

(schema:units:V)=
### V

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:voltage`
- Power of 10: 0



----
Conversions
^^^

- 1 V = 1.0E+3 {ref}`schema:units:mV`

```

(schema:units:cm)=
### cm

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:length`
- Power of 10: -2



----
Conversions
^^^

- 1 cm = 0.010 {ref}`schema:units:m__`
- 1 cm = 1.0E+4 {ref}`schema:units:um`

```

(schema:units:cm2)=
### cm2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:area`
- Power of 10: -4



----
Conversions
^^^

- 1 cm2 = 0.00010 {ref}`schema:units:m2`
- 1 cm2 = 1.0E+8 {ref}`schema:units:um2`

```

(schema:units:cm3)=
### cm3

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: -6



----
Conversions
^^^

- 1 cm3 = 0.0010 {ref}`schema:units:litre`
- 1 cm3 = 0.0000010 {ref}`schema:units:m3`
- 1 cm3 = 1.0E+12 {ref}`schema:units:um3`

```

(schema:units:cm_per_ms)=
### cm_per_ms

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: 1



----
Conversions
^^^

- 1 cm_per_ms = 1.0E+3 {ref}`schema:units:cm_per_s`
- 1 cm_per_ms = 10 {ref}`schema:units:m_per_s`
- 1 cm_per_ms = 1.0E+4 {ref}`schema:units:um_per_ms`

```

(schema:units:cm_per_s)=
### cm_per_s

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: -2



----
Conversions
^^^

- 1 cm_per_s = 0.0010 {ref}`schema:units:cm_per_ms`
- 1 cm_per_s = 0.010 {ref}`schema:units:m_per_s`
- 1 cm_per_s = 1E+1 {ref}`schema:units:um_per_ms`

```

(schema:units:degC)=
### degC

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:temperature`
- Power of 10: 0
- Offset: 273.15



----
Conversions
^^^

- 1 degC = 2.7E+2 {ref}`schema:units:K`

```

(schema:units:hour)=
### hour

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: 0


- Scale: 3600.0


----
Conversions
^^^

- 1 hour = 60 {ref}`schema:units:min`
- 1 hour = 3.6E+6 {ref}`schema:units:ms__`
- 1 hour = 3.6E+3 {ref}`schema:units:s__`

```

(schema:units:kohm)=
### kohm

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:resistance`
- Power of 10: 3



----
Conversions
^^^

- 1 kohm = 0.001 {ref}`schema:units:Mohm`
- 1 kohm = 1.0E+3 {ref}`schema:units:ohm`

```

(schema:units:kohm_cm)=
### kohm_cm

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:resistivity`
- Power of 10: 1



----
Conversions
^^^

- 1 kohm_cm = 1.0E+3 {ref}`schema:units:ohm_cm`
- 1 kohm_cm = 10 {ref}`schema:units:ohm_m`

```

(schema:units:litre)=
### litre

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: -3



----
Conversions
^^^

- 1 litre = 1.0E+3 {ref}`schema:units:cm3`
- 1 litre = 0.0010 {ref}`schema:units:m3`
- 1 litre = 1.0E+15 {ref}`schema:units:um3`

```

(schema:units:m__)=
### m

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:length`
- Power of 10: 0



----
Conversions
^^^

- 1 m = 1.0E+2 {ref}`schema:units:cm`
- 1 m = 1.0E+6 {ref}`schema:units:um`

```

(schema:units:m2)=
### m2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:area`
- Power of 10: 0



----
Conversions
^^^

- 1 m2 = 1.0E+4 {ref}`schema:units:cm2`
- 1 m2 = 1.0E+12 {ref}`schema:units:um2`

```

(schema:units:m3)=
### m3

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: 0



----
Conversions
^^^

- 1 m3 = 1.0E+6 {ref}`schema:units:cm3`
- 1 m3 = 1.0E+3 {ref}`schema:units:litre`
- 1 m3 = 1.0E+18 {ref}`schema:units:um3`

```

(schema:units:mA_per_cm2)=
### mA_per_cm2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:currentDensity`
- Power of 10: 1



----
Conversions
^^^

- 1 mA_per_cm2 = 10 {ref}`schema:units:A_per_m2`
- 1 mA_per_cm2 = 1.0E+3 {ref}`schema:units:uA_per_cm2`

```

(schema:units:mM)=
### mM

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 0



----
Conversions
^^^

- 1 mM = 0.001 {ref}`schema:units:M`
- 1 mM = 0.000001 {ref}`schema:units:mol_per_cm3`
- 1 mM = 1 {ref}`schema:units:mol_per_m3`

```

(schema:units:mS)=
### mS

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -3



----
Conversions
^^^

- 1 mS = 0.0010 {ref}`schema:units:S`
- 1 mS = 1.0E+6 {ref}`schema:units:nS`
- 1 mS = 1.0E+9 {ref}`schema:units:pS`
- 1 mS = 1.0E+3 {ref}`schema:units:uS`

```

(schema:units:mS_per_cm2)=
### mS_per_cm2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductanceDensity`
- Power of 10: 1



----
Conversions
^^^

- 1 mS_per_cm2 = 0.001 {ref}`schema:units:S_per_cm2`
- 1 mS_per_cm2 = 10 {ref}`schema:units:S_per_m2`

```

(schema:units:mV)=
### mV

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:voltage`
- Power of 10: -3



----
Conversions
^^^

- 1 mV = 0.0010 {ref}`schema:units:V`

```

(schema:units:m_per_s)=
### m_per_s

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: 0



----
Conversions
^^^

- 1 m_per_s = 0.1 {ref}`schema:units:cm_per_ms`
- 1 m_per_s = 1.0E+2 {ref}`schema:units:cm_per_s`
- 1 m_per_s = 1.0E+3 {ref}`schema:units:um_per_ms`

```

(schema:units:min)=
### min

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: 0


- Scale: 60.0


----
Conversions
^^^

- 1 min = 0.017 {ref}`schema:units:hour`
- 1 min = 6.0E+4 {ref}`schema:units:ms__`
- 1 min = 60 {ref}`schema:units:s__`

```

(schema:units:mol)=
### mol

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:substance`
- Power of 10: 0



```

(schema:units:mol_per_cm3)=
### mol_per_cm3

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 6



----
Conversions
^^^

- 1 mol_per_cm3 = 1.0E+3 {ref}`schema:units:M`
- 1 mol_per_cm3 = 1.0E+6 {ref}`schema:units:mM`
- 1 mol_per_cm3 = 1.0E+6 {ref}`schema:units:mol_per_m3`

```

(schema:units:mol_per_cm_per_uA_per_ms)=
### mol_per_cm_per_uA_per_ms

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:rho_factor`
- Power of 10: 11



----
Conversions
^^^

- 1 mol_per_cm_per_uA_per_ms = 1.0E+11 {ref}`schema:units:mol_per_m_per_A_per_s`

```

(schema:units:mol_per_m3)=
### mol_per_m3

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:concentration`
- Power of 10: 0



----
Conversions
^^^

- 1 mol_per_m3 = 0.001 {ref}`schema:units:M`
- 1 mol_per_m3 = 1 {ref}`schema:units:mM`
- 1 mol_per_m3 = 0.000001 {ref}`schema:units:mol_per_cm3`

```

(schema:units:mol_per_m_per_A_per_s)=
### mol_per_m_per_A_per_s

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:rho_factor`
- Power of 10: 0



----
Conversions
^^^

- 1 mol_per_m_per_A_per_s = 1E-11 {ref}`schema:units:mol_per_cm_per_uA_per_ms`

```

(schema:units:ms__)=
### ms

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: -3



----
Conversions
^^^

- 1 ms = 2.8E-7 {ref}`schema:units:hour`
- 1 ms = 0.000017 {ref}`schema:units:min`
- 1 ms = 0.0010 {ref}`schema:units:s__`

```

(schema:units:nA)=
### nA

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: -9



----
Conversions
^^^

- 1 nA = 1.0E-9 {ref}`schema:units:A`
- 1 nA = 1.0E+3 {ref}`schema:units:pA`
- 1 nA = 0.0010 {ref}`schema:units:uA`

```

(schema:units:nA_ms_per_amol)=
### nA_ms_per_amol

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:charge_per_mole`
- Power of 10: 6



----
Conversions
^^^

- 1 nA_ms_per_amol = 1.0E+6 {ref}`schema:units:C_per_mol`

```

(schema:units:nF)=
### nF

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: -9



----
Conversions
^^^

- 1 nF = 1.0E-9 {ref}`schema:units:F`
- 1 nF = 1.0E+3 {ref}`schema:units:pF`
- 1 nF = 0.0010 {ref}`schema:units:uF`

```

(schema:units:nS)=
### nS

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -9



----
Conversions
^^^

- 1 nS = 1.0E-9 {ref}`schema:units:S`
- 1 nS = 0.0000010 {ref}`schema:units:mS`
- 1 nS = 1.0E+3 {ref}`schema:units:pS`
- 1 nS = 0.0010 {ref}`schema:units:uS`

```

(schema:units:nS_per_mV)=
### nS_per_mV

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance_per_voltage`
- Power of 10: -6



----
Conversions
^^^

- 1 nS_per_mV = 0.0000010 {ref}`schema:units:S_per_V`

```

(schema:units:ohm)=
### ohm

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:resistance`
- Power of 10: 0



----
Conversions
^^^

- 1 ohm = 0.000001 {ref}`schema:units:Mohm`
- 1 ohm = 0.001 {ref}`schema:units:kohm`

```

(schema:units:ohm_cm)=
### ohm_cm

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:resistivity`
- Power of 10: -2



----
Conversions
^^^

- 1 ohm_cm = 0.0010 {ref}`schema:units:kohm_cm`
- 1 ohm_cm = 0.010 {ref}`schema:units:ohm_m`

```

(schema:units:ohm_m)=
### ohm_m

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:resistivity`
- Power of 10: 0



----
Conversions
^^^

- 1 ohm_m = 0.1 {ref}`schema:units:kohm_cm`
- 1 ohm_m = 1.0E+2 {ref}`schema:units:ohm_cm`

```

(schema:units:pA)=
### pA

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: -12



----
Conversions
^^^

- 1 pA = 1.0E-12 {ref}`schema:units:A`
- 1 pA = 0.0010 {ref}`schema:units:nA`
- 1 pA = 0.0000010 {ref}`schema:units:uA`

```

(schema:units:pF)=
### pF

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: -12



----
Conversions
^^^

- 1 pF = 1.0E-12 {ref}`schema:units:F`
- 1 pF = 0.0010 {ref}`schema:units:nF`
- 1 pF = 0.0000010 {ref}`schema:units:uF`

```

(schema:units:pS)=
### pS

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -12



----
Conversions
^^^

- 1 pS = 1.0E-12 {ref}`schema:units:S`
- 1 pS = 1.0E-9 {ref}`schema:units:mS`
- 1 pS = 0.0010 {ref}`schema:units:nS`
- 1 pS = 0.0000010 {ref}`schema:units:uS`

```

(schema:units:per_V)=
### per_V

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_voltage`
- Power of 10: 0



----
Conversions
^^^

- 1 per_V = 0.001 {ref}`schema:units:per_mV`

```

(schema:units:per_hour)=
### per_hour

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0


- Scale: 0.00027777777778


----
Conversions
^^^

- 1 per_hour = 0.00028 {ref}`schema:units:Hz`
- 1 per_hour = 0.017 {ref}`schema:units:per_min`
- 1 per_hour = 2.8E-7 {ref}`schema:units:per_ms`
- 1 per_hour = 0.00028 {ref}`schema:units:per_s`

```

(schema:units:per_mV)=
### per_mV

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_voltage`
- Power of 10: 3



----
Conversions
^^^

- 1 per_mV = 1.0E+3 {ref}`schema:units:per_V`

```

(schema:units:per_min)=
### per_min

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0


- Scale: 0.01666666667


----
Conversions
^^^

- 1 per_min = 0.017 {ref}`schema:units:Hz`
- 1 per_min = 60 {ref}`schema:units:per_hour`
- 1 per_min = 0.000017 {ref}`schema:units:per_ms`
- 1 per_min = 0.017 {ref}`schema:units:per_s`

```

(schema:units:per_ms)=
### per_ms

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 3



----
Conversions
^^^

- 1 per_ms = 1.0E+3 {ref}`schema:units:Hz`
- 1 per_ms = 3.6E+6 {ref}`schema:units:per_hour`
- 1 per_ms = 6.0E+4 {ref}`schema:units:per_min`
- 1 per_ms = 1.0E+3 {ref}`schema:units:per_s`

```

(schema:units:per_s)=
### per_s

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:per_time`
- Power of 10: 0



----
Conversions
^^^

- 1 per_s = 1 {ref}`schema:units:Hz`
- 1 per_s = 3.6E+3 {ref}`schema:units:per_hour`
- 1 per_s = 60 {ref}`schema:units:per_min`
- 1 per_s = 0.001 {ref}`schema:units:per_ms`

```

(schema:units:s__)=
### s

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:time`
- Power of 10: 0



----
Conversions
^^^

- 1 s = 0.00028 {ref}`schema:units:hour`
- 1 s = 0.017 {ref}`schema:units:min`
- 1 s = 1.0E+3 {ref}`schema:units:ms__`

```

(schema:units:uA)=
### uA

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:current`
- Power of 10: -6



----
Conversions
^^^

- 1 uA = 0.0000010 {ref}`schema:units:A`
- 1 uA = 1.0E+3 {ref}`schema:units:nA`
- 1 uA = 1.0E+6 {ref}`schema:units:pA`

```

(schema:units:uA_per_cm2)=
### uA_per_cm2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:currentDensity`
- Power of 10: -2



----
Conversions
^^^

- 1 uA_per_cm2 = 0.010 {ref}`schema:units:A_per_m2`
- 1 uA_per_cm2 = 0.0010 {ref}`schema:units:mA_per_cm2`

```

(schema:units:uF)=
### uF

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:capacitance`
- Power of 10: -6



----
Conversions
^^^

- 1 uF = 0.0000010 {ref}`schema:units:F`
- 1 uF = 1.0E+3 {ref}`schema:units:nF`
- 1 uF = 1.0E+6 {ref}`schema:units:pF`

```

(schema:units:uF_per_cm2)=
### uF_per_cm2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:specificCapacitance`
- Power of 10: -2



----
Conversions
^^^

- 1 uF_per_cm2 = 0.010 {ref}`schema:units:F_per_m2`

```

(schema:units:uS)=
### uS

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:conductance`
- Power of 10: -6



----
Conversions
^^^

- 1 uS = 0.0000010 {ref}`schema:units:S`
- 1 uS = 0.0010 {ref}`schema:units:mS`
- 1 uS = 1.0E+3 {ref}`schema:units:nS`
- 1 uS = 1.0E+6 {ref}`schema:units:pS`

```

(schema:units:um)=
### um

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:length`
- Power of 10: -6



----
Conversions
^^^

- 1 um = 0.00010 {ref}`schema:units:cm`
- 1 um = 0.0000010 {ref}`schema:units:m__`

```

(schema:units:um2)=
### um2

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:area`
- Power of 10: -12



----
Conversions
^^^

- 1 um2 = 1.0E-8 {ref}`schema:units:cm2`
- 1 um2 = 1.0E-12 {ref}`schema:units:m2`

```

(schema:units:um3)=
### um3

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:volume`
- Power of 10: -18



----
Conversions
^^^

- 1 um3 = 1.0E-12 {ref}`schema:units:cm3`
- 1 um3 = 1.0E-15 {ref}`schema:units:litre`
- 1 um3 = 1.0E-18 {ref}`schema:units:m3`

```

(schema:units:um_per_ms)=
### um_per_ms

```{panels}
Summary
^^^
- Dimension: {ref}`schema:dimensions:permeability`
- Power of 10: -3



----
Conversions
^^^

- 1 um_per_ms = 0.00010 {ref}`schema:units:cm_per_ms`
- 1 um_per_ms = 0.1 {ref}`schema:units:cm_per_s`
- 1 um_per_ms = 0.0010 {ref}`schema:units:m_per_s`

```



(schema:neuromlcorecomptypes)=
# NeuroMLCoreCompTypes



Original ComponentType definitions: [NeuroMLCoreCompTypes.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//NeuroMLCoreCompTypes.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

(schema:notes)=

## notes




<i>Human readable notes on a Component.</i>



(schema:annotation)=

## annotation




<i>Annotation...</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:RDF, {ref}`schema:rdf_rdf`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

property, {ref}`schema:property`

```
````

(schema:property)=

## property




<i>Property in Annotation...</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

tag,
value,

````

(schema:basestandalone)=

## *baseStandalone*




<i>Base type of any component which will require notes, annotation, etc.</i>



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

```
````

(schema:rdf_rdf)=

## rdf_RDF




<i>Work in progress...</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

xmlns:rdf,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:Description, {ref}`schema:rdf_description`

```
````

(schema:rdf_description)=

## rdf_Description




<i>Work in progress...</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

rdf:about,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

bqbiol:encodes, {ref}`schema:bqbiol_encodes`
bqbiol:hasPart, {ref}`schema:bqbiol_haspart`
bqbiol:hasProperty, {ref}`schema:bqbiol_hasproperty`
bqbiol:hasVersion, {ref}`schema:bqbiol_hasversion`
bqbiol:is, {ref}`schema:bqbiol_is`
bqbiol:isDescribedBy, {ref}`schema:bqbiol_isdescribedby`
bqbiol:isEncodedBy, {ref}`schema:bqbiol_isencodedby`
bqbiol:isHomologTo, {ref}`schema:bqbiol_ishomologto`
bqbiol:isPartOf, {ref}`schema:bqbiol_ispartof`
bqbiol:isPropertyOf, {ref}`schema:bqbiol_ispropertyof`
bqbiol:isVersionOf, {ref}`schema:bqbiol_isversionof`
bqbiol:occursIn, {ref}`schema:bqbiol_occursin`
bqbiol:hasTaxon, {ref}`schema:bqbiol_hastaxon`
bqmodel:is, {ref}`schema:bqmodel_is`
bqmodel:isDescribedBy, {ref}`schema:bqmodel_isdescribedby`
bqmodel:isDerivedFrom, {ref}`schema:bqmodel_isderivedfrom`

```
````

(schema:basebqbiol)=

## *baseBqbiol*




<i>Work in progress...</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:Bag, {ref}`schema:rdf_bag`

```
````

(schema:bqbiol_encodes)=

## bqbiol_encodes




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_haspart)=

## bqbiol_hasPart




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_hasproperty)=

## bqbiol_hasProperty




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_hasversion)=

## bqbiol_hasVersion




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_is)=

## bqbiol_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_isdescribedby)=

## bqbiol_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_isencodedby)=

## bqbiol_isEncodedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_ishomologto)=

## bqbiol_isHomologTo




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_ispartof)=

## bqbiol_isPartOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_ispropertyof)=

## bqbiol_isPropertyOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_isversionof)=

## bqbiol_isVersionOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

xmlns:bqbiol,

````

(schema:bqbiol_occursin)=

## bqbiol_occursIn




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_hastaxon)=

## bqbiol_hasTaxon




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqmodel_is)=

## bqmodel_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqmodel_isdescribedby)=

## bqmodel_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

xmlns:bqmodel,

````

(schema:bqmodel_isderivedfrom)=

## bqmodel_isDerivedFrom




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:rdf_bag)=

## rdf_Bag




<i>Work in progress...</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:li, {ref}`schema:rdf:li`

```
````

(schema:rdf_li)=

## rdf_li




<i>Annotation...</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

rdf:resource,

````

(schema:point3dwithdiam)=

## point3DWithDiam




<i>Base type for ComponentTypes which specify an ( _x, _y, _z ) coordinate along with a _diameter. Note: no dimension used in the attributes for these coordinates! These are assumed to have dimension micrometer (10^-6 m). This is due to micrometers being the default option for the majority of neuronal morphology formats, and dimensions are omitted here to facilitate reading and writing of morphologies in NeuroML.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

diameter,Dimensionless
x,Dimensionless
y,Dimensionless
z,Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

radius,{ref}`schema:dimensions:length`
xLength,{ref}`schema:dimensions:length`
yLength,{ref}`schema:dimensions:length`
zLength,{ref}`schema:dimensions:length`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MICRON = 1um, {ref}`schema:dimensions:length`

```
````
