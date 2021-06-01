
(schema:cells)=
# Cells



Original ComponentType definitions: [Cells.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Cells.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 01/06/21 from [this](https://github.com/NeuroML/NeuroML2/commit/f186fdc0c7e7d6ad7fcab3b5f31639244541c2b6) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:basecell)=

## *baseCell*




extends *{ref}`schema:basestandalone`*



<i>Base type of any cell ( e.g. point neuron like  {ref}`schema:izhikevich2007cell`, or a morphologically detailed  {ref}`schema:cell` with  {ref}`schema:segment`s ) which can be used in a  {ref}`schema:population`.</i>



````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import BaseCell

variable = BaseCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, extensiontype_=None, **kwargs_)
```



````

(schema:basespikingcell)=

## *baseSpikingCell*




extends *{ref}`schema:basecell`*



<i>Base type of any cell which can emit **spike** events.</i>



````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event$Direction: out

```
````

(schema:basecellmembpot)=

## *baseCellMembPot*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a membrane potential **v** with units of voltage ( as opposed to a dimensionless membrane potential used in  {ref}`schema:basecellmembpotdl` ).</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

(schema:basecellmembpotdl)=

## *baseCellMembPotDL*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a dimensioness membrane potential, **V** ( as opposed to a membrane potential units of voltage,  {ref}`schema:basecellmembpot` ).</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**V**$ Membrane potential $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

(schema:basechannelpopulation)=

## *baseChannelPopulation*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for any current produced by a population of channels, all of which are of type **ionChannel**.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**ionChannel**$  $ {ref}`schema:baseionchannel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:channelpopulation)=

## channelPopulation




extends *{ref}`schema:basechannelpopulation`*



<i>Population of a **number** of ohmic ion channels. These each produce a conductance **channelg** across a reversal potential **erev,** giving a total current **i.** Note that active membrane currents are more frequently specified as a density over an area of the  {ref}`schema:cell` using  {ref}`schema:channeldensity`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`
**number**$ The number of channels present. This will be multiplied by the time varying conductance of the individual ion channel (which extends _baseIonChannel_) to produce the total conductance $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**vShift** = 0mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelPopulation" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelPopulation

variable = ChannelPopulation(neuro_lex_id=None, id=None, ion_channel=None, number=None, erev=None, segment_groups='all', segments=None, ion=None, variable_parameters=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<channelPopulation xmlns:xi="http://www.w3.org/2001/XInclude" id="naChansDend" ionChannel="NaConductance" segment="2" number="120000" erev="50mV" ion="na"/>
```

````

(schema:channelpopulationnernst)=

## channelPopulationNernst




extends *{ref}`schema:basechannelpopulation`*



<i>Population of a **number** of channels with a time varying reversal potential **erev** determined by Nernst equation. Note: hard coded for Ca only!</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**number**$ The number of channels present. This will be multiplied by the time varying conductance of the individual ion channel (which extends _baseIonChannel_) to produce the total conductance $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$  $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$  $ Dimensionless
**F** = 96485.3 C_per_mol$  $ {ref}`schema:dimensions:charge_per_mole`
**vShift** = 0mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced, calculated from _caConcExt and _caConc ${ref}`schema:dimensions:voltage`
**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$ The internal Ca2+ concentration, as calculated/exposed by the parent Component ${ref}`schema:dimensions:concentration`
**caConcExt**$ The external Ca2+ concentration, as calculated/exposed by the parent Component ${ref}`schema:dimensions:concentration`
**temperature**$ The temperature to use in the calculation of _erev. Note this is generally exposed by a _networkWithTemperature_. ${ref}`schema:dimensions:temperature`
**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

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




<i>Base type for a current of density **iDensity** distributed on an area of a  {ref}`schema:cell`, flowing through the specified **ionChannel.** Instances of this ( normally  {ref}`schema:channeldensity` ) are specified in the  {ref}`schema:membraneproperties` of the  {ref}`schema:cell`.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**ionChannel**$  $ {ref}`schema:baseionchannel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  ${ref}`schema:dimensions:voltage`

```
````

(schema:basechanneldensitycond)=

## *baseChannelDensityCond*




extends *{ref}`schema:basechanneldensity`*



<i>Base type for distributed conductances on an area of a cell producing a ( not necessarily ohmic ) current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:variableparameter)=

## variableParameter




<i>Specifies a **parameter** ( e.g. condDensity ) which can vary its value across a **segmentGroup.** The value is calculated from **value** attribute of the  {ref}`schema:inhomogeneousvalue` subelement. This element is normally a child of  {ref}`schema:channeldensitynonuniform`,  {ref}`schema:channeldensitynonuniformnernst` or  {ref}`schema:channeldensitynonuniformghk` and is used to calculate the value of the conductance, etc. which will vary on different parts of the cell. The **segmentGroup** specified here needs to define an  {ref}`schema:inhomogeneousparameter` ( referenced from **inhomogeneousParameter** in the  {ref}`schema:inhomogeneousvalue` ), which calculates a **variable** ( e.g. p ) varying across the cell ( e.g. based on the path length from soma ), which is then used in the **value** attribute of the  {ref}`schema:inhomogeneousvalue` ( so for example condDensity = f( p ) ).</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**parameter**$ 
**segmentGroup**$ 

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**inhomogeneousValue**$  $ {ref}`schema:inhomogeneousvalue`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=VariableParameter" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import VariableParameter

variable = VariableParameter(parameter=None, segment_groups=None, inhomogeneous_value=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<variableParameter parameter="condDensity" segmentGroup="dendrite_group">
                        <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>  
                    </variableParameter>
```

````

(schema:inhomogeneousvalue)=

## inhomogeneousValue




<i>Specifies the **value** of an **inhomogeneousParameter.** For usage see  {ref}`schema:variableparameter`.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**inhomogeneousParameter**$ 
**value**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InhomogeneousValue" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import InhomogeneousValue

variable = InhomogeneousValue(inhomogeneous_parameters=None, value=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>
```

````

(schema:channeldensitynonuniform)=

## channelDensityNonUniform




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying ohmic conductance density, which is distributed on a region of the **cell.** The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**variableParameter**$  $ {ref}`schema:variableparameter`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**ZERO_CURR_DENS** = 0 A_per_m2$  $ {ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNonUniform" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityNonUniform

variable = ChannelDensityNonUniform(neuro_lex_id=None, id=None, ion_channel=None, erev=None, ion=None, variable_parameters=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<channelDensityNonUniform id="nonuniform_na_chans" ionChannel="NaConductance" erev="50mV" ion="na">
                    <variableParameter parameter="condDensity" segmentGroup="dendrite_group">
                        <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>  
                    </variableParameter>
                </channelDensityNonUniform>
```

````

(schema:channeldensitynonuniformnernst)=

## channelDensityNonUniformNernst




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the **cell,** and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**variableParameter**$  $ {ref}`schema:variableparameter`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**ZERO_CURR_DENS** = 0 A_per_m2$  $ {ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNonUniformNernst" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityNonUniformNernst

variable = ChannelDensityNonUniformNernst(neuro_lex_id=None, id=None, ion_channel=None, ion=None, variable_parameters=None, **kwargs_)
```



````

(schema:channeldensitynonuniformghk)=

## channelDensityNonUniformGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the **cell,** and whose current is calculated from the Goldman-Hodgkin-Katz equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**variableParameter**$  $ {ref}`schema:variableparameter`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**ZERO_CURR_DENS** = 0 A_per_m2$  $ {ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNonUniformGHK" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityNonUniformGHK

variable = ChannelDensityNonUniformGHK(neuro_lex_id=None, id=None, ion_channel=None, ion=None, variable_parameters=None, **kwargs_)
```



````

(schema:channeldensity)=

## channelDensity




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying ohmic conductance density, **gDensity,** which is distributed on an area of the **cell** ( specified in  {ref}`schema:membraneproperties` ) with fixed reversal potential **erev** producing a current density **iDensity**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensity is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**vShift** = 0mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensity" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensity

variable = ChannelDensity(neuro_lex_id=None, id=None, ion_channel=None, cond_density=None, erev=None, segment_groups='all', segments=None, ion=None, variable_parameters=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<channelDensity id="leak" ionChannel="passiveChan" condDensity="3.0 S_per_m2" erev="-54.3mV" ion="non_specific"/>
```
```{code-block} xml
<channelDensity id="naChans" ionChannel="naChan" condDensity="120.0 mS_per_cm2" erev="50.0 mV" ion="na"/>
```
```{code-block} xml
<channelDensity id="kChans" ionChannel="kChan" condDensity="360 S_per_m2" erev="-77mV" ion="k"/>
```

````

(schema:channeldensityvshift)=

## channelDensityVShift




extends {ref}`schema:channeldensity`



<i>Same as  {ref}`schema:channeldensity`, but with a **vShift** parameter to change voltage activation of gates. The exact usage of **vShift** in expressions for rates is determined by the individual gates.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**erev**$ The reversal potential of the current produced *(from {ref}`schema:channeldensity`)* ${ref}`schema:dimensions:voltage`
**vShift**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensity is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityVShift" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityVShift

variable = ChannelDensityVShift(neuro_lex_id=None, id=None, ion_channel=None, cond_density=None, erev=None, segment_groups='all', segments=None, ion=None, variable_parameters=None, v_shift=None, **kwargs_)
```



````

(schema:channeldensitynernst)=

## channelDensityNernst




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying conductance density, **gDensity,** which is distributed on an area of the **cell,** producing a current density **iDensity** and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityNernst is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$  $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$  $ Dimensionless
**F** = 96485.3 C_per_mol$  $ {ref}`schema:dimensions:charge_per_mole`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced, calculated from caConcExt and caConc ${ref}`schema:dimensions:voltage`
**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  ${ref}`schema:dimensions:concentration`
**temperature**$  ${ref}`schema:dimensions:temperature`
**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNernst" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityNernst

variable = ChannelDensityNernst(neuro_lex_id=None, id=None, ion_channel=None, cond_density=None, segment_groups='all', segments=None, ion=None, variable_parameters=None, extensiontype_=None, **kwargs_)
```



````

(schema:channeldensitynernstca2)=

## channelDensityNernstCa2




extends *{ref}`schema:basechanneldensitycond`*



<i>This component is similar to the original component type  {ref}`schema:channeldensitynernst` but it is changed in order to have a reversal potential that depends on a second independent Ca++ pool ( ca2 ). See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityNernstCa2 is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$  $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$  $ Dimensionless
**F** = 96485.3 C_per_mol$  $ {ref}`schema:dimensions:charge_per_mole`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`
**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc2**$  ${ref}`schema:dimensions:concentration`
**caConcExt2**$  ${ref}`schema:dimensions:concentration`
**temperature**$  ${ref}`schema:dimensions:temperature`
**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNernstCa2" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityNernstCa2

variable = ChannelDensityNernstCa2(neuro_lex_id=None, id=None, ion_channel=None, cond_density=None, segment_groups='all', segments=None, ion=None, variable_parameters=None, **kwargs_)
```



````

(schema:channeldensityghk)=

## channelDensityGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity** and whose reversal potential is calculated from the Goldman Hodgkin Katz equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**permeability**$  ${ref}`schema:dimensions:permeability`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityGHK is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$  $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$  $ Dimensionless
**F** = 96485.3 C_per_mol$  $ {ref}`schema:dimensions:charge_per_mole`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  ${ref}`schema:dimensions:concentration`
**temperature**$  ${ref}`schema:dimensions:temperature`
**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityGHK" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityGHK

variable = ChannelDensityGHK(neuro_lex_id=None, id=None, ion_channel=None, permeability=None, segment_groups='all', segments=None, ion=None, **kwargs_)
```



````

(schema:channeldensityghk2)=

## channelDensityGHK2




extends *{ref}`schema:basechanneldensitycond`*



<i>Time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity.** Modified version of Jaffe et al. 1994 ( used also in Lawrence et al. 2006 ). See https://github.com/OpenSourceBrain/ghk-nernst.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityGHK2 is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**VOLT_SCALE** = 1 mV$  $ {ref}`schema:dimensions:voltage`
**CONC_SCALE** = 1 mM$  $ {ref}`schema:dimensions:concentration`
**TEMP_SCALE** = 1 K$  $ {ref}`schema:dimensions:temperature`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  ${ref}`schema:dimensions:concentration`
**temperature**$  ${ref}`schema:dimensions:temperature`
**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityGHK2" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ChannelDensityGHK2

variable = ChannelDensityGHK2(neuro_lex_id=None, id=None, ion_channel=None, cond_density=None, segment_groups='all', segments=None, ion=None, **kwargs_)
```



````

(schema:pointcellcondbased)=

## pointCellCondBased




extends *{ref}`schema:basecellmembpotcap`*



<i>Simple model of a conductance based cell, with no separate  {ref}`schema:morphology` element, just an absolute capacitance **C,** and a set of channel **populations.** Note: use of  {ref}`schema:cell` is generally preferable ( and more widely supported ), even for a single compartment cell.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**thresh**$ The voltage threshold above which the cell is considered to be _spiking ${ref}`schema:dimensions:voltage`
**v0**$ The initial membrane potential of the cell ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**populations**$  $ {ref}`schema:basechannelpopulation`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless 









<i>**On Start**</i>
: **v** = v0
: **spiking** = 0



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;&emsp;&emsp;**spiking** = 1
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**

: IF v &lt; thresh THEN
: &emsp;&emsp;&emsp;**spiking** = 0





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



<i>TEMPORARY: Point cell with conductances and Ca concentration info. Not yet fully tested!!! TODO: Remove in favour of  {ref}`schema:cell`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**thresh**$ The voltage threshold above which the cell is considered to be _spiking ${ref}`schema:dimensions:voltage`
**v0**$ The initial membrane potential of the cell ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**populations**$  $ {ref}`schema:basechannelpopulation`
**concentrationModels**$  $ {ref}`schema:concentrationmodel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**iCa**$  ${ref}`schema:dimensions:current`
**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless 









<i>**On Start**</i>
: **v** = v0
: **spiking** = 0



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;&emsp;&emsp;**spiking** = 1
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**

: IF v &lt; thresh THEN
: &emsp;&emsp;&emsp;**spiking** = 0





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



<i>Point on a  {ref}`schema:segment` furthest from the soma. Should always be present in the description of a  {ref}`schema:segment`, unlike  {ref}`schema:proximal`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**diameter**$ Diameter of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless
**x**$ x coordinate of the point. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless
**y**$ y coordinate of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless
**z**$ z coordinate of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**radius**$ A dimensional quantity given by half the _diameter. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
**xLength**$ A version of _x with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
**yLength**$ A version of _y with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
**zLength**$ A version of _z with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`

```
````

````{tabbed} Usage



*XML examples*
```{code-block} xml
<distal x="10" y="0" z="0" diameter="10"/>
```
```{code-block} xml
<distal x="20" y="0" z="0" diameter="3"/>
```
```{code-block} xml
<distal x="30" y="0" z="0" diameter="1"/>
```

````

(schema:proximal)=

## proximal




extends {ref}`schema:point3dwithdiam`



<i>Point on a  {ref}`schema:segment` closest to the soma. Note, the proximal point can be omitted, and in this case is defined as being the point **fractionAlong** between the proximal and  {ref}`schema:distal` point of the  {ref}`schema:parent`, i.e. if **fractionAlong** = 1 ( as it is by default ) it will be the **distal** on the parent, or if **fractionAlong** = 0, it will be the proximal point. If between 0 and 1, it is the linear interpolation between the two points.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**diameter**$ Diameter of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless
**x**$ x coordinate of the point. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless
**y**$ y coordinate of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless
**z**$ z coordinate of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. *(from {ref}`schema:point3dwithdiam`)* $Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**radius**$ A dimensional quantity given by half the _diameter. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
**xLength**$ A version of _x with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
**yLength**$ A version of _y with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
**zLength**$ A version of _z with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`

```
````

````{tabbed} Usage



*XML examples*
```{code-block} xml
<proximal x="0" y="0" z="0" diameter="10"/>
```
```{code-block} xml
<proximal x="10" y="0" z="0" diameter="3"/>
```
```{code-block} xml
<proximal translationStart="0"/>
```

````

(schema:parent)=

## parent




<i>Specifies the id of the **segment** which is this segment's parent.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ The id of the parent segment
**fractionAlong**$ The fraction along the the parent segment at which this segment is attached. For usage see _proximal_

````

````{tabbed} Usage



*XML examples*
```{code-block} xml
<parent segment="0"/>
```
```{code-block} xml
<parent segment="1"/>
```
```{code-block} xml
<parent segment="0"/>
```

````

(schema:segment)=

## segment




<i>A segment defines the smallest unit within a possibly branching structure (  {ref}`schema:morphology` ), such as a dendrite or axon. Its **id** should be a nonnegative integer ( usually soma/root = 0 ). Its end points are given by the  {ref}`schema:proximal` and  {ref}`schema:distal` points. The  {ref}`schema:proximal` point can be omitted, usually because it is the same as a point on the  {ref}`schema:parent` segment, see  {ref}`schema:proximal` for details.  {ref}`schema:parent` specifies the parent segment. The first segment of a  {ref}`schema:cell` ( with no  {ref}`schema:parent` ) usually represents the soma. The shape is normally a cylinder ( radii of the  {ref}`schema:proximal` and  {ref}`schema:distal` equal, but positions different ) or a conical frustum ( radii and positions different ). If the x, y, x positions of the  {ref}`schema:proximal` and  {ref}`schema:distal` are equal, the segment can be interpreted as a sphere, and in this case the radii of these points must be equal. NOTE: LEMS does not yet support multicompartmental modelling, so the Dynamics here is only appropriate for single compartment modelling.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**name**$ An optional name for the segment. Convenient for providing a suitable variable name for generated code, e.g. soma, dend0

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**parent**$  $ {ref}`schema:parent`
**distal**$  $ {ref}`schema:distal`
**proximal**$  $ {ref}`schema:proximal`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**LEN** = 1m$  $ {ref}`schema:dimensions:length`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**length**$  ${ref}`schema:dimensions:length`
**radDist**$  ${ref}`schema:dimensions:length`
**surfaceArea**$  ${ref}`schema:dimensions:area`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Segment" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Segment

variable = Segment(neuro_lex_id=None, id=None, name=None, parent=None, proximal=None, distal=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<segment id="1" name="MainDendrite1">
                <parent segment="0"/>
                
                <proximal x="10" y="0" z="0" diameter="3"/> 
                <distal x="20" y="0" z="0" diameter="3"/>
            </segment>
```
```{code-block} xml
<segment id="0" name="Soma">    
                
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="10" y="0" z="0" diameter="10"/>
            </segment>
```
```{code-block} xml
<segment id="2" name="MainDendrite2">
                <parent segment="1"/>
                
                <distal x="30" y="0" z="0" diameter="1"/>
            </segment>
```

````

(schema:segmentgroup)=

## segmentGroup




<i>A method to describe a group of  {ref}`schema:segment`s in a  {ref}`schema:morphology`, e.g. soma_group, dendrite_group, axon_group. While a name is useful to describe the group, the **neuroLexId** attribute can be used to explicitly specify the meaning of the group, e.g. sao1044911821 for 'Neuronal Cell Body', sao1211023249 for 'Dendrite'. The  {ref}`schema:segment`s in this group can be specified as: a list of individual  {ref}`schema:member` segments; a  {ref}`schema:path`, all of the segments along which should be included; a  {ref}`schema:subtree` of the  {ref}`schema:cell` to include; other segmentGroups to  {ref}`schema:include` ( so all segments from those get included here ). An  {ref}`schema:inhomogeneousparameter` can be defined on the region of the cell specified by this group ( see  {ref}`schema:variableparameter` for usage ).</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**neuroLexId**$ An id string for pointing to an entry in the NeuroLex ontology. Use of this attribute is a shorthand for a full         RDF based reference to the MIRIAM Resource urn:miriam:neurolex, with an bqbiol:is qualifier.

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**annotation**$  $ {ref}`schema:annotation`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`
**members**$  $ {ref}`schema:member`
**paths**$  $ {ref}`schema:path`
**subTrees**$  $ {ref}`schema:subtree`
**includes**$  $ {ref}`schema:include`
**inhomogeneousParameter**$  $ {ref}`schema:inhomogeneousparameter`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SegmentGroup" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SegmentGroup

variable = SegmentGroup(neuro_lex_id=None, id=None, notes=None, properties=None, annotation=None, members=None, includes=None, paths=None, sub_trees=None, inhomogeneous_parameters=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<segmentGroup id="dendrite_group" neuroLexId="sao1211023249">
                <member segment="1"/>
                <member segment="2"/>
                
                <inhomogeneousParameter id="dendrite_group_x1" variable="p" metric="Path Length from root"/>
 
                <inhomogeneousParameter id="dendrite_group_x2" variable="r" metric="Path Length from root">
                        <proximal translationStart="0"/>
                        <distal normalizationEnd="1"/>
                </inhomogeneousParameter>
                
            </segmentGroup>
```
```{code-block} xml
<segmentGroup id="soma_group" neuroLexId="sao1044911821">    
                <member segment="0"/>
            </segmentGroup>
```
```{code-block} xml
<segmentGroup id="dendSec2" neuroLexId="sao864921383">   
                <property tag="numberInternalDivisions" value="9"/>
                <member segment="2"/>
                <member segment="3"/>
            </segmentGroup>
```

````

(schema:member)=

## member




<i>A single identified **segment** which is part of the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Member" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Member

variable = Member(segments=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<member segment="0"/>
```
```{code-block} xml
<member segment="1"/>
```
```{code-block} xml
<member segment="2"/>
```

````

(schema:from)=

## from




<i>In a  {ref}`schema:path` or  {ref}`schema:subtree`, specifies which **segment** ( inclusive ) from which to calculate the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ 

````

````{tabbed} Usage



*XML examples*
```{code-block} xml
<from segment="1"/>
```
```{code-block} xml
<from segment="1"/>
```

````

(schema:to)=

## to




<i>In a  {ref}`schema:path`, specifies which **segment** ( inclusive ) up to which to calculate the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ 

````

````{tabbed} Usage



*XML examples*
```{code-block} xml
<to segment="2"/>
```

````

(schema:include)=

## include




<i>Include all members of another  {ref}`schema:segmentgroup` in this group.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**href**$ TODO: fix this!!! This is needed here, since include is used to include external nml files!!
**segmentGroup**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Include" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Include

variable = Include(segment_groups=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<include href="NML2_SimpleIonChannel.nml"/>
```
```{code-block} xml
<include href="NML2_SingleCompHHCell.nml"/>
```
```{code-block} xml
<include segmentGroup="soma"/>
```

````

(schema:path)=

## path




<i>Include all the  {ref}`schema:segment`s between those specified by  {ref}`schema:from` and  {ref}`schema:to`, inclusive.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**from**$  $ {ref}`schema:from`
**to**$  $ {ref}`schema:to`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Path" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Path

variable = Path(from_=None, to=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<path>
                    <from segment="1"/>
                    <to segment="2"/>
                </path>
```

````

(schema:subtree)=

## subTree




<i>Include all the  {ref}`schema:segment`s distal to that specified by  {ref}`schema:from` in the  {ref}`schema:segmentgroup`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**from**$  $ {ref}`schema:from`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SubTree" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SubTree

variable = SubTree(from_=None, to=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<subTree>
                    <from segment="1"/>
                </subTree>
```

````

(schema:inhomogeneousparameter)=

## inhomogeneousParameter




<i>An inhomogeneous parameter specified across the  {ref}`schema:segmentgroup` ( see  {ref}`schema:variableparameter` for usage ).</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**variable**$ 
**metric**$ 

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**proximal**$  $ {ref}`schema:proximalproperties`
**distal**$  $ {ref}`schema:distalproperties`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InhomogeneousParameter" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import InhomogeneousParameter

variable = InhomogeneousParameter(neuro_lex_id=None, id=None, variable=None, metric=None, proximal=None, distal=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<inhomogeneousParameter id="dendrite_group_x2" variable="r" metric="Path Length from root">
                        <proximal translationStart="0"/>
                        <distal normalizationEnd="1"/>
                </inhomogeneousParameter>
```
```{code-block} xml
<inhomogeneousParameter id="dendrite_group_x1" variable="p" metric="Path Length from root"/>
```

````

(schema:proximalproperties)=

## proximalProperties




<i>What to do at the proximal point when creating an inhomogeneous parameter.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**translationStart**$ 

````

(schema:distalproperties)=

## distalProperties




<i>What to do at the distal point when creating an inhomogeneous parameter.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**normalizationEnd**$ 

````

(schema:morphology)=

## morphology




<i>The collection of  {ref}`schema:segment`s which specify the 3D structure of the cell, along with a number of  {ref}`schema:segmentgroup`s.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**segments**$  $ {ref}`schema:segment`
**segmentGroups**$  $ {ref}`schema:segmentgroup`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Morphology" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Morphology

variable = Morphology(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, segments=None, segment_groups=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<morphology id="SimpleCell_Morphology">
            
            <segment id="0" name="Soma">    
                
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="10" y="0" z="0" diameter="10"/>
            </segment>
            <segment id="1" name="MainDendrite1">
                <parent segment="0"/>
                
                <proximal x="10" y="0" z="0" diameter="3"/> 
                <distal x="20" y="0" z="0" diameter="3"/>
            </segment>
            <segment id="2" name="MainDendrite2">
                <parent segment="1"/>
                
                <distal x="30" y="0" z="0" diameter="1"/>
            </segment>
            
            <segmentGroup id="soma_group" neuroLexId="sao1044911821">    
                <member segment="0"/>
            </segmentGroup>
            <segmentGroup id="dendrite_group" neuroLexId="sao1211023249">
                <member segment="1"/>
                <member segment="2"/>
                
                <inhomogeneousParameter id="dendrite_group_x1" variable="p" metric="Path Length from root"/>
 
                <inhomogeneousParameter id="dendrite_group_x2" variable="r" metric="Path Length from root">
                        <proximal translationStart="0"/>
                        <distal normalizationEnd="1"/>
                </inhomogeneousParameter>
                
            </segmentGroup>
        </morphology>
```
```{code-block} xml
<morphology id="MultiCompCell_morphology">
            <segment id="0" name="Soma">
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="0" y="10" z="0" diameter="10"/>
            </segment>
            <segment id="1" name="Dendrite1">
                <parent segment="0"/>
                <proximal x="0" y="10" z="0" diameter="3"/>
                <distal x="0" y="20" z="0" diameter="3"/>
            </segment>
            <segment id="2" name="Dendrite2a">
                <parent segment="1"/>
                <proximal x="0" y="20" z="0" diameter="3"/>
                <distal x="0" y="30" z="0" diameter="2.5"/>
            </segment>
            
            <segment id="3" name="Dendrite2b">
                <parent segment="2"/>
                <distal x="0" y="50" z="0" diameter="1.5"/>
            </segment>
            
            
            <segmentGroup id="soma" neuroLexId="sao864921383">    <!--
                This group contains an unbranched set of segments, and all of the segmentGroups marked with
                neuroLexId = sao864921383 form a non-overlapping set of all of the segments. 
                These segmentGroups correspond to the 'cables' of NeuroML v1.8.1. -->
                <member segment="0"/>
            </segmentGroup>
            
            <segmentGroup id="dendSec1" neuroLexId="sao864921383">   
                <member segment="1"/>
            </segmentGroup>
            
            <segmentGroup id="dendSec2" neuroLexId="sao864921383">   
                <property tag="numberInternalDivisions" value="9"/>
                <member segment="2"/>
                <member segment="3"/>
            </segmentGroup>
            
            <segmentGroup id="soma_group"> 
                <include segmentGroup="soma"/>
            </segmentGroup>
           <segmentGroup id="dendrite_group">  
                <include segmentGroup="dendSec1"/>
                <include segmentGroup="dendSec2"/>
            </segmentGroup>
        </morphology>
```
```{code-block} xml
<morphology id="SimpleCell_Morphology">
            
            <segment id="0" name="Soma">    
                
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="10" y="0" z="0" diameter="10"/>
            </segment>
            <segment id="1" name="MainDendrite1">
                <parent segment="0"/>
                
                <proximal x="10" y="0" z="0" diameter="3"/> 
                <distal x="20" y="0" z="0" diameter="3"/>
            </segment>
            <segment id="2" name="MainDendrite2">
                <parent segment="1"/>
                
                <distal x="30" y="0" z="0" diameter="1"/>
            </segment>
            <segment id="3" name="Spine">
                
                <parent segment="2" fractionAlong="0.5"/>
                <proximal x="25" y="0" z="0" diameter="0.2"/>
                <distal x="25" y="1" z="0" diameter="0.2"/>
            </segment>
            
            <segmentGroup id="soma_group" neuroLexId="sao1044911821">    
                <member segment="0"/>
            </segmentGroup>
            <segmentGroup id="thick_dendrites">
                <member segment="1"/>
                <member segment="2"/>
            </segmentGroup>
            
            <segmentGroup id="spines" neuroLexId="sao1145756102"> 
                <member segment="3"/>
            </segmentGroup>
            <segmentGroup id="dendrite_group" neuroLexId="sao1211023249">     
                <include segmentGroup="thick_dendrites"/>
                <include segmentGroup="spines"/>
                
            </segmentGroup>
            <segmentGroup id="middle">            
                <path>
                    <from segment="1"/>
                    <to segment="2"/>
                </path>
            </segmentGroup>
            <segmentGroup id="tip">              
                <subTree>
                    <from segment="1"/>
                </subTree>
            </segmentGroup>
            
        </morphology>
```

````

(schema:specificcapacitance)=

## specificCapacitance




<i>Capacitance per unit area.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**specCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **specCap** =&nbsp;value&emsp;(exposed as **specCap**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpecificCapacitance" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpecificCapacitance

variable = SpecificCapacitance(value=None, segment_groups='all', segments=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
```
```{code-block} xml
<specificCapacitance value="1.0 uF_per_cm2"/>
```
```{code-block} xml
<specificCapacitance xmlns:xi="http://www.w3.org/2001/XInclude" segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
```

````

(schema:initmembpotential)=

## initMembPotential




<i>Explicitly set initial membrane potential for the cell.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InitMembPotential" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import InitMembPotential

variable = InitMembPotential(value=None, segment_groups='all', segments=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<initMembPotential value="-65mV"/>
```
```{code-block} xml
<initMembPotential value="-65mV"/>
```

````

(schema:spikethresh)=

## spikeThresh




<i>Membrane potential at which to emit a spiking event. Note, usually the spiking event will not be emitted again until the membrane potential has fallen below this value and rises again to cross it in a positive direction.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeThresh" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeThresh

variable = SpikeThresh(value=None, segment_groups='all', segments=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<spikeThresh value="-20mV"/>
```
```{code-block} xml
<spikeThresh value="-20mV"/>
```

````

(schema:membraneproperties)=

## membraneProperties




<i>Properties specific to the membrane, such as the **populations** of channels, **channelDensities,** **specificCapacitance,** etc.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**initMembPotential**$  $ {ref}`schema:initmembpotential`
**spikeThresh**$  $ {ref}`schema:spikethresh`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**specificCapacitances**$  $ {ref}`schema:specificcapacitance`
**populations**$  $ {ref}`schema:basechannelpopulation`
**channelDensities**$  $ {ref}`schema:basechanneldensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iCa**$  ${ref}`schema:dimensions:current`
**totChanCurrent**$  ${ref}`schema:dimensions:current`
**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**surfaceArea**$  ${ref}`schema:dimensions:area`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=MembraneProperties" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import MembraneProperties

variable = MembraneProperties(channel_populations=None, channel_densities=None, channel_density_v_shifts=None, channel_density_nernsts=None, channel_density_ghks=None, channel_density_ghk2s=None, channel_density_non_uniforms=None, channel_density_non_uniform_nernsts=None, channel_density_non_uniform_ghks=None, spike_threshes=None, specific_capacitances=None, init_memb_potentials=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<membraneProperties>
                <channelDensityNonUniform id="nonuniform_na_chans" ionChannel="NaConductance" erev="50mV" ion="na">
                    <variableParameter parameter="condDensity" segmentGroup="dendrite_group">
                        <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>  
                    </variableParameter>
                </channelDensityNonUniform>
                <specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
            </membraneProperties>
```
```{code-block} xml
<membraneProperties>
                        
                <channelDensity id="leak" ionChannel="passiveChan" condDensity="3.0 S_per_m2" erev="-54.3mV" ion="non_specific"/>
                <channelDensity id="naChans" ionChannel="naChan" condDensity="120.0 mS_per_cm2" erev="50.0 mV" ion="na"/>
                <channelDensity id="kChans" ionChannel="kChan" condDensity="360 S_per_m2" erev="-77mV" ion="k"/>
                <spikeThresh value="-20mV"/>
                <specificCapacitance value="1.0 uF_per_cm2"/>
                <initMembPotential value="-65mV"/>
            </membraneProperties>
```
```{code-block} xml
<membraneProperties xmlns:xi="http://www.w3.org/2001/XInclude"> 
                <channelPopulation id="naChansDend" ionChannel="NaConductance" segment="2" number="120000" erev="50mV" ion="na"/>   
                <channelDensity id="pasChans" ionChannel="pas" condDensity="3.0 S_per_m2" erev="-70mV" ion="non_specific"/> 
                <channelDensity id="naChansSoma" ionChannel="NaConductance" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" erev="50mV" ion="na"/>
                <specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
                <specificCapacitance segmentGroup="dendrite_group" value="2.0 uF_per_cm2"/>
            </membraneProperties>
```

````

(schema:membraneproperties2capools)=

## membraneProperties2CaPools




extends {ref}`schema:membraneproperties`



<i>Variant of membraneProperties with 2 independent Ca pools.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**initMembPotential**$  $ {ref}`schema:initmembpotential`
**spikeThresh**$  $ {ref}`schema:spikethresh`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**specificCapacitances**$  $ {ref}`schema:specificcapacitance`
**populations**$  $ {ref}`schema:basechannelpopulation`
**channelDensities**$  $ {ref}`schema:basechanneldensity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iCa**$  *(from {ref}`schema:membraneproperties`)* ${ref}`schema:dimensions:current`
**iCa2**$  ${ref}`schema:dimensions:current`
**totChanCurrent**$  *(from {ref}`schema:membraneproperties`)* ${ref}`schema:dimensions:current`
**totSpecCap**$  *(from {ref}`schema:membraneproperties`)* ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**surfaceArea**$  ${ref}`schema:dimensions:area`
**surfaceArea**$  *(from {ref}`schema:membraneproperties`)* ${ref}`schema:dimensions:area`

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=MembraneProperties2CaPools" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import MembraneProperties2CaPools

variable = MembraneProperties2CaPools(channel_populations=None, channel_densities=None, channel_density_v_shifts=None, channel_density_nernsts=None, channel_density_ghks=None, channel_density_ghk2s=None, channel_density_non_uniforms=None, channel_density_non_uniform_nernsts=None, channel_density_non_uniform_ghks=None, spike_threshes=None, specific_capacitances=None, init_memb_potentials=None, channel_density_nernst_ca2s=None, **kwargs_)
```



````

(schema:biophysicalproperties)=

## biophysicalProperties




<i>The biophysical properties of the  {ref}`schema:cell`, including the  {ref}`schema:membraneproperties` and the  {ref}`schema:intracellularproperties`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**membraneProperties**$  $ {ref}`schema:membraneproperties`
**intracellularProperties**$  $ {ref}`schema:intracellularproperties`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;membraneProperties->totSpecCap&emsp;(exposed as **totSpecCap**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BiophysicalProperties" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import BiophysicalProperties

variable = BiophysicalProperties(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, membrane_properties=None, intracellular_properties=None, extracellular_properties=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<biophysicalProperties id="biophys">
            <membraneProperties>
                <channelDensityNonUniform id="nonuniform_na_chans" ionChannel="NaConductance" erev="50mV" ion="na">
                    <variableParameter parameter="condDensity" segmentGroup="dendrite_group">
                        <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>  
                    </variableParameter>
                </channelDensityNonUniform>
                <specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
            </membraneProperties>
            <intracellularProperties>
                <resistivity value="0.1 kohm_cm"/>  
            </intracellularProperties>
        </biophysicalProperties>
```
```{code-block} xml
<biophysicalProperties id="bioPhys1">
            
            <membraneProperties>
                        
                <channelDensity id="leak" ionChannel="passiveChan" condDensity="3.0 S_per_m2" erev="-54.3mV" ion="non_specific"/>
                <channelDensity id="naChans" ionChannel="naChan" condDensity="120.0 mS_per_cm2" erev="50.0 mV" ion="na"/>
                <channelDensity id="kChans" ionChannel="kChan" condDensity="360 S_per_m2" erev="-77mV" ion="k"/>
                <spikeThresh value="-20mV"/>
                <specificCapacitance value="1.0 uF_per_cm2"/>
                <initMembPotential value="-65mV"/>
            </membraneProperties>
            <intracellularProperties>
                <resistivity value="100 kohm_cm"/>   
            </intracellularProperties>
        </biophysicalProperties>
```
```{code-block} xml
<biophysicalProperties xmlns:xi="http://www.w3.org/2001/XInclude" id="bio_cell">
            <membraneProperties> 
                <channelPopulation id="naChansDend" ionChannel="NaConductance" segment="2" number="120000" erev="50mV" ion="na"/>   
                <channelDensity id="pasChans" ionChannel="pas" condDensity="3.0 S_per_m2" erev="-70mV" ion="non_specific"/> 
                <channelDensity id="naChansSoma" ionChannel="NaConductance" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" erev="50mV" ion="na"/>
                <specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
                <specificCapacitance segmentGroup="dendrite_group" value="2.0 uF_per_cm2"/>
            </membraneProperties>
            <intracellularProperties>
                <resistivity value="0.1 kohm_cm"/>  
            </intracellularProperties>
        </biophysicalProperties>
```

````

(schema:biophysicalproperties2capools)=

## biophysicalProperties2CaPools




<i>The biophysical properties of the  {ref}`schema:cell`, including the  {ref}`schema:membraneproperties2capools` and the  {ref}`schema:intracellularproperties2capools` for a cell with two Ca pools.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**membraneProperties2CaPools**$  $ {ref}`schema:membraneproperties2capools`
**intracellularProperties2CaPools**$  $ {ref}`schema:intracellularproperties2capools`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;membraneProperties2CaPools->totSpecCap&emsp;(exposed as **totSpecCap**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BiophysicalProperties2CaPools" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import BiophysicalProperties2CaPools

variable = BiophysicalProperties2CaPools(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, membrane_properties2_ca_pools=None, intracellular_properties2_ca_pools=None, extracellular_properties=None, **kwargs_)
```



````

(schema:intracellularproperties)=

## intracellularProperties




<i>Biophysical properties related to the intracellular space within the  {ref}`schema:cell`, such as the  {ref}`schema:resistivity` and the list of ionic  {ref}`schema:species` present. **caConc** and **caConcExt** are explicitly exposed here to facilitate accessing these values from other Components, even though **caConcExt** is clearly not an intracellular property.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**resistivity**$  $ {ref}`schema:resistivity`
**speciesList**$  $ {ref}`schema:species`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **caConc** =&nbsp;speciesList[ion='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;speciesList[ion='ca']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IntracellularProperties" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IntracellularProperties

variable = IntracellularProperties(species=None, resistivities=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<intracellularProperties>
                <resistivity value="0.1 kohm_cm"/>  
            </intracellularProperties>
```
```{code-block} xml
<intracellularProperties>
                <resistivity value="100 kohm_cm"/>   
            </intracellularProperties>
```
```{code-block} xml
<intracellularProperties xmlns:xi="http://www.w3.org/2001/XInclude">
                <resistivity value="0.1 kohm_cm"/>  
            </intracellularProperties>
```

````

(schema:intracellularproperties2capools)=

## intracellularProperties2CaPools




extends {ref}`schema:intracellularproperties`



<i>Variant of intracellularProperties with 2 independent Ca pools.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**speciesList**$  $ {ref}`schema:species`
**resistivity**$  $ {ref}`schema:resistivity`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  *(from {ref}`schema:intracellularproperties`)* ${ref}`schema:dimensions:concentration`
**caConc2**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  *(from {ref}`schema:intracellularproperties`)* ${ref}`schema:dimensions:concentration`
**caConcExt2**$  ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **caConc2** =&nbsp;speciesList[ion='ca2']->concentration(reduce method: add)&emsp;(exposed as **caConc2**)
    : **caConcExt2** =&nbsp;speciesList[ion='ca2']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt2**)
    : **caConc** =&nbsp;speciesList[ion='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;speciesList[ion='ca']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IntracellularProperties2CaPools" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IntracellularProperties2CaPools

variable = IntracellularProperties2CaPools(species=None, resistivities=None, **kwargs_)
```



````

(schema:resistivity)=

## resistivity




<i>The resistivity, or specific axial resistance, of the cytoplasm.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:resistivity`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Resistivity" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Resistivity

variable = Resistivity(value=None, segment_groups='all', segments=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<resistivity value="0.1 kohm_cm"/>
```
```{code-block} xml
<resistivity value="100 kohm_cm"/>
```
```{code-block} xml
<resistivity xmlns:xi="http://www.w3.org/2001/XInclude" value="0.1 kohm_cm"/>
```

````

(schema:concentrationmodel)=

## concentrationModel




<i>Base for any model of an **ion** concentration which changes with time. Internal ( **concentration** ) and external ( **extConcentration** ) values for the concentration of the ion are given.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  ${ref}`schema:dimensions:concentration`
**extConcentration**$  ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**initialConcentration**$  ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  ${ref}`schema:dimensions:concentration`
**surfaceArea**$  ${ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration








````

(schema:decayingpoolconcentrationmodel)=

## decayingPoolConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of an intracellular buffering mechanism for **ion** ( currently hard Coded to be calcium, due to requirement for **iCa** ) which has a baseline level **restingConc** and tends to this value with time course **decayConstant.** The ion is assumed to occupy a shell inside the membrane of thickness **shellThickness.**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**decayConstant**$  ${ref}`schema:dimensions:time`
**restingConc**$  ${ref}`schema:dimensions:concentration`
**shellThickness**$  ${ref}`schema:dimensions:length`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 

````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**Faraday** = 96485.3C_per_mol$  $ {ref}`schema:dimensions:charge_per_mole`
**AREA_SCALE** = 1m2$  $ {ref}`schema:dimensions:area`
**LENGTH_SCALE** = 1m$  $ {ref}`schema:dimensions:length`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**extConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iCa**$  ${ref}`schema:dimensions:current`
**initialConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**surfaceArea**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration



<i>**On Conditions**</i>

: IF concentration &lt; 0 THEN
: &emsp;&emsp;&emsp;**concentration** = 0





<i>**Derived Variables**</i>
    : **effectiveRadius** =&nbsp;LENGTH_SCALE * sqrt(surfaceArea/(AREA_SCALE * (4 * 3.14159)))
    : **innerRadius** =&nbsp;effectiveRadius - shellThickness
    : **shellVolume** =&nbsp;(4 * (effectiveRadius * effectiveRadius * effectiveRadius) * 3.14159 / 3) - (4 * (innerRadius * innerRadius * innerRadius) * 3.14159 / 3)
    





<i>**Time Derivatives**</i>
    : d **concentration** /dt = iCa / (2 * Faraday * shellVolume) - ((concentration - restingConc) / decayConstant)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=DecayingPoolConcentrationModel" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import DecayingPoolConcentrationModel

variable = DecayingPoolConcentrationModel(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, ion=None, resting_conc=None, decay_constant=None, shell_thickness=None, extensiontype_=None, **kwargs_)
```



````

(schema:fixedfactorconcentrationmodel)=

## fixedFactorConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion ( currently hard coded to be calcium, due to requirement for **iCa** ) which has a baseline level **restingConc** and tends to this value with time course **decayConstant.** A fixed factor **rho** is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**decayConstant**$  ${ref}`schema:dimensions:time`
**restingConc**$  ${ref}`schema:dimensions:concentration`
**rho**$  ${ref}`schema:dimensions:rho_factor`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**extConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iCa**$  ${ref}`schema:dimensions:current`
**initialConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**surfaceArea**$  ${ref}`schema:dimensions:area`
**surfaceArea**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration



<i>**On Conditions**</i>

: IF concentration &lt; 0 THEN
: &emsp;&emsp;&emsp;**concentration** = 0








<i>**Time Derivatives**</i>
    : d **concentration** /dt = (iCa/surfaceArea) * rho - ((concentration - restingConc) / decayConstant)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=FixedFactorConcentrationModel" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import FixedFactorConcentrationModel

variable = FixedFactorConcentrationModel(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, ion=None, resting_conc=None, decay_constant=None, rho=None, **kwargs_)
```



````

(schema:fixedfactorconcentrationmodeltraub)=

## fixedFactorConcentrationModelTraub




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion ( currently hard coded to be calcium, due to requirement for **iCa** ) which has a baseline level **restingConc** and tends to this value with time course 1 / **beta.** A fixed factor **phi** is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change. Not recommended for use in models other than Traub et al. 2005!</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**beta**$  ${ref}`schema:dimensions:per_time`
**phi**$  ${ref}`schema:dimensions:rho_factor`
**restingConc**$  ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**species**$ 

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**extConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iCa**$  ${ref}`schema:dimensions:current`
**initialConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**surfaceArea**$  ${ref}`schema:dimensions:area`
**surfaceArea**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:area`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration



<i>**On Conditions**</i>

: IF concentration &lt; 0 THEN
: &emsp;&emsp;&emsp;**concentration** = 0








<i>**Time Derivatives**</i>
    : d **concentration** /dt = (iCa/surfaceArea) * 1e-9 * phi - ((concentration - restingConc) * beta)
    

````

(schema:species)=

## species




<i>Description of a chemical species identified by **ion,** which has internal, **concentration,** and external, **extConcentration** values for its concentration.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**initialConcentration**$  ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 
**segmentGroup**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**concentrationModel**$  $ {ref}`schema:concentrationmodel`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  ${ref}`schema:dimensions:concentration`
**extConcentration**$  ${ref}`schema:dimensions:concentration`

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **concentrationModel**









<i>**Derived Variables**</i>
    : **concentration** =&nbsp;concentrationModel->concentration&emsp;(exposed as **concentration**)
    : **extConcentration** =&nbsp;concentrationModel->extConcentration&emsp;(exposed as **extConcentration**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Species" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Species

variable = Species(value=None, segment_groups='all', segments=None, id=None, concentration_model=None, ion=None, initial_concentration=None, initial_ext_concentration=None, **kwargs_)
```



````

(schema:cell)=

## cell




extends *{ref}`schema:basecellmembpot`*



<i>Cell with  {ref}`schema:segment`s specified in a  {ref}`schema:morphology` element along with details on its  {ref}`schema:biophysicalproperties`. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v** of this cell represents the membrane potential in that isopotential segment.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**neuroLexId**$ 

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**morphology**$  $ {ref}`schema:morphology`
**biophysicalProperties**$  $ {ref}`schema:biophysicalproperties`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  ${ref}`schema:dimensions:concentration`
**iCa**$  ${ref}`schema:dimensions:current`
**iChannels**$  ${ref}`schema:dimensions:current`
**iSyn**$  ${ref}`schema:dimensions:current`
**spiking**$  $Dimensionless
**surfaceArea**$  ${ref}`schema:dimensions:area`
**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless &emsp;(exposed as **spiking**)









<i>**On Start**</i>
: **spiking** = 0
: **v** = initMembPot



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;&emsp;&emsp;**spiking** = 1
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**

: IF v &lt; thresh THEN
: &emsp;&emsp;&emsp;**spiking** = 0





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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Cell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Cell

variable = Cell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, morphology_attr=None, biophysical_properties_attr=None, morphology=None, biophysical_properties=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<cell id="SimpleCell">
        <morphology id="SimpleCell_Morphology">
            
            <segment id="0" name="Soma">    
                
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="10" y="0" z="0" diameter="10"/>
            </segment>
            <segment id="1" name="MainDendrite1">
                <parent segment="0"/>
                
                <proximal x="10" y="0" z="0" diameter="3"/> 
                <distal x="20" y="0" z="0" diameter="3"/>
            </segment>
            <segment id="2" name="MainDendrite2">
                <parent segment="1"/>
                
                <distal x="30" y="0" z="0" diameter="1"/>
            </segment>
            
            <segmentGroup id="soma_group" neuroLexId="sao1044911821">    
                <member segment="0"/>
            </segmentGroup>
            <segmentGroup id="dendrite_group" neuroLexId="sao1211023249">
                <member segment="1"/>
                <member segment="2"/>
                
                <inhomogeneousParameter id="dendrite_group_x1" variable="p" metric="Path Length from root"/>
 
                <inhomogeneousParameter id="dendrite_group_x2" variable="r" metric="Path Length from root">
                        <proximal translationStart="0"/>
                        <distal normalizationEnd="1"/>
                </inhomogeneousParameter>
                
            </segmentGroup>
        </morphology>
        
        <biophysicalProperties id="biophys">
            <membraneProperties>
                <channelDensityNonUniform id="nonuniform_na_chans" ionChannel="NaConductance" erev="50mV" ion="na">
                    <variableParameter parameter="condDensity" segmentGroup="dendrite_group">
                        <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>  
                    </variableParameter>
                </channelDensityNonUniform>
                <specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
            </membraneProperties>
            <intracellularProperties>
                <resistivity value="0.1 kohm_cm"/>  
            </intracellularProperties>
        </biophysicalProperties>
    </cell>
```
```{code-block} xml
<cell id="MultiCompCell">
        <notes>Multicompartmental cell</notes>
        <morphology id="MultiCompCell_morphology">
            <segment id="0" name="Soma">
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="0" y="10" z="0" diameter="10"/>
            </segment>
            <segment id="1" name="Dendrite1">
                <parent segment="0"/>
                <proximal x="0" y="10" z="0" diameter="3"/>
                <distal x="0" y="20" z="0" diameter="3"/>
            </segment>
            <segment id="2" name="Dendrite2a">
                <parent segment="1"/>
                <proximal x="0" y="20" z="0" diameter="3"/>
                <distal x="0" y="30" z="0" diameter="2.5"/>
            </segment>
            
            <segment id="3" name="Dendrite2b">
                <parent segment="2"/>
                <distal x="0" y="50" z="0" diameter="1.5"/>
            </segment>
            
            
            <segmentGroup id="soma" neuroLexId="sao864921383">    <!--
                This group contains an unbranched set of segments, and all of the segmentGroups marked with
                neuroLexId = sao864921383 form a non-overlapping set of all of the segments. 
                These segmentGroups correspond to the 'cables' of NeuroML v1.8.1. -->
                <member segment="0"/>
            </segmentGroup>
            
            <segmentGroup id="dendSec1" neuroLexId="sao864921383">   
                <member segment="1"/>
            </segmentGroup>
            
            <segmentGroup id="dendSec2" neuroLexId="sao864921383">   
                <property tag="numberInternalDivisions" value="9"/>
                <member segment="2"/>
                <member segment="3"/>
            </segmentGroup>
            
            <segmentGroup id="soma_group"> 
                <include segmentGroup="soma"/>
            </segmentGroup>
           <segmentGroup id="dendrite_group">  
                <include segmentGroup="dendSec1"/>
                <include segmentGroup="dendSec2"/>
            </segmentGroup>
        </morphology>
        <biophysicalProperties id="bioPhys1">
            
            <membraneProperties>
                        
                <channelDensity id="leak" ionChannel="passiveChan" condDensity="3.0 S_per_m2" erev="-54.3mV" ion="non_specific"/>
                <channelDensity id="naChans" ionChannel="naChan" condDensity="120.0 mS_per_cm2" erev="50.0 mV" ion="na"/>
                <channelDensity id="kChans" ionChannel="kChan" condDensity="360 S_per_m2" erev="-77mV" ion="k"/>
                <spikeThresh value="-20mV"/>
                <specificCapacitance value="1.0 uF_per_cm2"/>
                <initMembPotential value="-65mV"/>
            </membraneProperties>
            <intracellularProperties>
                <resistivity value="100 kohm_cm"/>   
            </intracellularProperties>
        </biophysicalProperties>
    </cell>
```
```{code-block} xml
<cell id="SimpleCell">
        <morphology id="SimpleCell_Morphology">
            
            <segment id="0" name="Soma">    
                
                <proximal x="0" y="0" z="0" diameter="10"/>
                <distal x="10" y="0" z="0" diameter="10"/>
            </segment>
            <segment id="1" name="MainDendrite1">
                <parent segment="0"/>
                
                <proximal x="10" y="0" z="0" diameter="3"/> 
                <distal x="20" y="0" z="0" diameter="3"/>
            </segment>
            <segment id="2" name="MainDendrite2">
                <parent segment="1"/>
                
                <distal x="30" y="0" z="0" diameter="1"/>
            </segment>
            <segment id="3" name="Spine">
                
                <parent segment="2" fractionAlong="0.5"/>
                <proximal x="25" y="0" z="0" diameter="0.2"/>
                <distal x="25" y="1" z="0" diameter="0.2"/>
            </segment>
            
            <segmentGroup id="soma_group" neuroLexId="sao1044911821">    
                <member segment="0"/>
            </segmentGroup>
            <segmentGroup id="thick_dendrites">
                <member segment="1"/>
                <member segment="2"/>
            </segmentGroup>
            
            <segmentGroup id="spines" neuroLexId="sao1145756102"> 
                <member segment="3"/>
            </segmentGroup>
            <segmentGroup id="dendrite_group" neuroLexId="sao1211023249">     
                <include segmentGroup="thick_dendrites"/>
                <include segmentGroup="spines"/>
                
            </segmentGroup>
            <segmentGroup id="middle">            
                <path>
                    <from segment="1"/>
                    <to segment="2"/>
                </path>
            </segmentGroup>
            <segmentGroup id="tip">              
                <subTree>
                    <from segment="1"/>
                </subTree>
            </segmentGroup>
            
        </morphology>
    </cell>
```

````

(schema:cell2capools)=

## cell2CaPools




extends {ref}`schema:cell`



<i>Variant of cell with two independent Ca2+ pools. Cell with  {ref}`schema:segment`s specified in a  {ref}`schema:morphology` element along with details on its  {ref}`schema:biophysicalproperties`. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v** of this cell represents the membrane potential in that isopotential segment.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**neuroLexId**$ 

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**biophysicalProperties2CaPools**$  $ {ref}`schema:biophysicalproperties2capools`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:concentration`
**caConc2**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:concentration`
**caConcExt2**$  ${ref}`schema:dimensions:concentration`
**iCa**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:current`
**iCa2**$  ${ref}`schema:dimensions:current`
**iChannels**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:current`
**iSyn**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:current`
**spiking**$  *(from {ref}`schema:cell`)* $Dimensionless
**surfaceArea**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:area`
**totSpecCap**$  *(from {ref}`schema:cell`)* ${ref}`schema:dimensions:specificCapacitance`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **spiking**: Dimensionless &emsp;(exposed as **spiking**)









<i>**On Start**</i>
: **spiking** = 0
: **v** = initMembPot



<i>**On Conditions**</i>

: IF v &gt; thresh AND spiking &lt; 0.5 THEN
: &emsp;&emsp;&emsp;**spiking** = 1
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**

: IF v &lt; thresh THEN
: &emsp;&emsp;&emsp;**spiking** = 0





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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Cell2CaPools" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Cell2CaPools

variable = Cell2CaPools(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, morphology_attr=None, biophysical_properties_attr=None, morphology=None, biophysical_properties=None, biophysical_properties2_ca_pools=None, **kwargs_)
```



````

(schema:basecellmembpotcap)=

## *baseCellMembPotCap*




extends *{ref}`schema:basecellmembpot`*



<i>Any cell with a membrane potential **v** with voltage units and a membrane capacitance **C.** Also defines exposed value **iSyn** for current due to external synapses and **iMemb** for total transmembrane current ( usually channel currents plus **iSyn** ).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane ${ref}`schema:dimensions:capacitance`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseCellMembPotCap" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import BaseCellMembPotCap

variable = BaseCellMembPotCap(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, C=None, extensiontype_=None, **kwargs_)
```



````

(schema:baseiaf)=

## *baseIaf*




extends *{ref}`schema:basecellmembpot`*



<i>Base ComponentType for an integrate and fire cell which emits a spiking event at membrane potential **thresh** and and resets to **reset**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**reset**$ The value the membrane potential is reset to on spiking ${ref}`schema:dimensions:voltage`
**thresh**$ The membrane potential at which to emit a spiking event and reset voltage ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

(schema:iaftaucell)=

## iafTauCell




extends *{ref}`schema:baseiaf`*



<i>Integrate and fire cell which returns to its leak reversal potential of **leakReversal** with a time constant **tau**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**leakReversal**$  ${ref}`schema:dimensions:voltage`
**reset**$ The value the membrane potential is reset to on spiking *(from {ref}`schema:baseiaf`)* ${ref}`schema:dimensions:voltage`
**tau**$  ${ref}`schema:dimensions:time`
**thresh**$ The membrane potential at which to emit a spiking event and reset voltage *(from {ref}`schema:baseiaf`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)









<i>**On Start**</i>
: **v** = leakReversal



<i>**On Conditions**</i>

: IF v &gt; thresh THEN
: &emsp;&emsp;&emsp;**v** = reset
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **v** /dt = (leakReversal - v) / tau
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafTauCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IafTauCell

variable = IafTauCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, leak_reversal=None, thresh=None, reset=None, tau=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<iafTauCell id="iafTau" leakReversal="-50mV" thresh="-55mV" reset="-70mV" tau="30ms"/>
```

````

(schema:iaftaurefcell)=

## iafTauRefCell




extends {ref}`schema:iaftaucell`



<i>Integrate and fire cell which returns to its leak reversal potential of **leakReversal** with a time course **tau.** It has a refractory period of **refract** after spiking.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**leakReversal**$  *(from {ref}`schema:iaftaucell`)* ${ref}`schema:dimensions:voltage`
**refract**$  ${ref}`schema:dimensions:time`
**reset**$ The value the membrane potential is reset to on spiking *(from {ref}`schema:baseiaf`)* ${ref}`schema:dimensions:voltage`
**tau**$  *(from {ref}`schema:iaftaucell`)* ${ref}`schema:dimensions:time`
**thresh**$ The membrane potential at which to emit a spiking event and reset voltage *(from {ref}`schema:baseiaf`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = leakReversal









<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = reset
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + refract THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; thresh THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (leakReversal - v) / tau
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafTauRefCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IafTauRefCell

variable = IafTauRefCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, leak_reversal=None, thresh=None, reset=None, tau=None, refract=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<iafTauRefCell id="iafTauRef" leakReversal="-50mV" thresh="-55mV" reset="-70mV" tau="30ms" refract="5ms"/>
```

````

(schema:baseiafcapcell)=

## *baseIafCapCell*




extends *{ref}`schema:basecellmembpotcap`*



<i>Base Type for all Integrate and Fire cells with a capacitance **C,** threshold **thresh** and reset membrane potential **reset**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**reset**$  ${ref}`schema:dimensions:voltage`
**thresh**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

(schema:iafcell)=

## iafCell




extends *{ref}`schema:baseiafcapcell`*



<i>Integrate and fire cell with capacitance **C,** **leakConductance** and **leakReversal**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**leakConductance**$  ${ref}`schema:dimensions:conductance`
**leakReversal**$  ${ref}`schema:dimensions:voltage`
**reset**$  *(from {ref}`schema:baseiafcapcell`)* ${ref}`schema:dimensions:voltage`
**thresh**$  *(from {ref}`schema:baseiafcapcell`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)









<i>**On Start**</i>
: **v** = leakReversal



<i>**On Conditions**</i>

: IF v &gt; thresh THEN
: &emsp;&emsp;&emsp;**v** = reset
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;leakConductance * (leakReversal - v) + iSyn&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb / C
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IafCell

variable = IafCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, leak_reversal=None, thresh=None, reset=None, C=None, leak_conductance=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<iafCell id="iaf" leakReversal="-50mV" thresh="-55mV" reset="-70mV" C="0.2nF" leakConductance="0.01uS"/>
```
```{code-block} xml
<iafCell id="iaf" leakConductance="0.2nS" leakReversal="-70mV" thresh="-55mV" reset="-70mV" C="3.2pF"/>
```
```{code-block} xml
<iafCell id="iaf" leakConductance="0.2nS" leakReversal="-70mV" thresh="-55mV" reset="-70mV" C="3.2pF"/>
```

````

(schema:iafrefcell)=

## iafRefCell




extends {ref}`schema:iafcell`



<i>Integrate and fire cell with capacitance **C,** **leakConductance,** **leakReversal** and refractory period **refract**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**leakConductance**$  *(from {ref}`schema:iafcell`)* ${ref}`schema:dimensions:conductance`
**leakReversal**$  *(from {ref}`schema:iafcell`)* ${ref}`schema:dimensions:voltage`
**refract**$  ${ref}`schema:dimensions:time`
**reset**$  *(from {ref}`schema:baseiafcapcell`)* ${ref}`schema:dimensions:voltage`
**thresh**$  *(from {ref}`schema:baseiafcapcell`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = leakReversal





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;leakConductance * (leakReversal - v) + iSyn&emsp;(exposed as **iMemb**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = reset
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + refract THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; thresh THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = iMemb / C
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafRefCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IafRefCell

variable = IafRefCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, leak_reversal=None, thresh=None, reset=None, C=None, leak_conductance=None, refract=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<iafRefCell id="iafRef" leakReversal="-50mV" thresh="-55mV" reset="-70mV" C="0.2nF" leakConductance="0.01uS" refract="5ms"/>
```

````

(schema:izhikevichcell)=

## izhikevichCell




extends *{ref}`schema:basecellmembpot`*



<i>Cell based on the 2003 model of Izhikevich, see http://izhikevich.org/publications/spikes.htm.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**a**$  $Dimensionless
**b**$  $Dimensionless
**c**$  $Dimensionless
**d**$  $Dimensionless
**thresh**$  ${ref}`schema:dimensions:voltage`
**v0**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**U**$  $Dimensionless
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrentdl`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **U**: Dimensionless &emsp;(exposed as **U**)









<i>**On Start**</i>
: **v** = v0
: **U** = v0 * b / MVOLT



<i>**On Conditions**</i>

: IF v &gt; thresh THEN
: &emsp;&emsp;&emsp;**v** = c * MVOLT
: &emsp;&emsp;&emsp;**U** = U + d
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**





<i>**Derived Variables**</i>
    : **ISyn** =&nbsp;synapses[*]->I(reduce method: add)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = (0.04 * v^2 / MVOLT + 5 * v + (140.0 - U + ISyn) * MVOLT)/MSEC
    : d **U** /dt = a * (b * v / MVOLT - U) / MSEC
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IzhikevichCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IzhikevichCell

variable = IzhikevichCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, v0=None, thresh=None, a=None, b=None, c=None, d=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<izhikevichCell id="izBurst" v0="-70mV" thresh="30mV" a="0.02" b="0.2" c="-50.0" d="2"/>
```

````

(schema:izhikevich2007cell)=

## izhikevich2007Cell




extends *{ref}`schema:basecellmembpotcap`*



<i>Cell based on the modified Izhikevich model in Izhikevich 2007, Dynamical systems in neuroscience, MIT Press.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**a**$  ${ref}`schema:dimensions:per_time`
**b**$  ${ref}`schema:dimensions:conductance`
**c**$  ${ref}`schema:dimensions:voltage`
**d**$  ${ref}`schema:dimensions:current`
**k**$  ${ref}`schema:dimensions:conductance_per_voltage`
**v0**$  ${ref}`schema:dimensions:voltage`
**vpeak**$  ${ref}`schema:dimensions:voltage`
**vr**$  ${ref}`schema:dimensions:voltage`
**vt**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**u**$  ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **u**: {ref}`schema:dimensions:current` &emsp;(exposed as **u**)









<i>**On Start**</i>
: **v** = v0
: **u** = 0



<i>**On Conditions**</i>

: IF v &gt; vpeak THEN
: &emsp;&emsp;&emsp;**v** = c
: &emsp;&emsp;&emsp;**u** = u + d
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iMemb** =&nbsp;k * (v-vr) * (v-vt) + iSyn - u&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb / C
    : d **u** /dt = a * (b * (v-vr) - u)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Izhikevich2007Cell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Izhikevich2007Cell

variable = Izhikevich2007Cell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, C=None, v0=None, k=None, vr=None, vt=None, vpeak=None, a=None, b=None, c=None, d=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<izhikevich2007Cell id="iz2007RS" v0="-60mV" C="100 pF" k="0.7 nS_per_mV" vr="-60 mV" vt="-40 mV" vpeak="35 mV" a="0.03 per_ms" b="-2 nS" c="-50 mV" d="100 pA"/>
```

````

(schema:adexiafcell)=

## adExIaFCell




extends *{ref}`schema:basecellmembpotcap`*



<i>Model based on Brette R and Gerstner W ( 2005 ) Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity. J Neurophysiol 94:3637-3642.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**EL**$  ${ref}`schema:dimensions:voltage`
**VT**$  ${ref}`schema:dimensions:voltage`
**a**$  ${ref}`schema:dimensions:conductance`
**b**$  ${ref}`schema:dimensions:current`
**delT**$  ${ref}`schema:dimensions:voltage`
**gL**$  ${ref}`schema:dimensions:conductance`
**refract**$  ${ref}`schema:dimensions:time`
**reset**$  ${ref}`schema:dimensions:voltage`
**tauw**$  ${ref}`schema:dimensions:time`
**thresh**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**w**$  ${ref}`schema:dimensions:current`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
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
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = reset
: &emsp;&emsp; **w** = w + b
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + refract THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **w** /dt = (a * (v - EL) - w) / tauw

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; thresh THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = iMemb / C
: &emsp;&emsp; d **w** /dt = (a * (v - EL) - w) / tauw
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AdExIaFCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import AdExIaFCell

variable = AdExIaFCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, C=None, g_l=None, EL=None, reset=None, VT=None, thresh=None, del_t=None, tauw=None, refract=None, a=None, b=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<adExIaFCell id="adExBurst" C="281pF" gL="30nS" EL="-70.6mV" reset="-48.5mV" VT="-50.4mV" thresh="-40.4mV" refract="0ms" delT="2mV" tauw="40ms" a="4nS" b="0.08nA"/>
```

````

(schema:fitzhughnagumocell)=

## fitzHughNagumoCell




extends *{ref}`schema:basecellmembpotdl`*



<i>Simple dimensionless model of spiking cell from FitzHugh and Nagumo. Superseded by **fitzHughNagumo1969Cell** ( See https://github.com/NeuroML/NeuroML2/issues/42 ).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$  $Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SEC** = 1s$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**V**$ Membrane potential *(from {ref}`schema:basecellmembpotdl`)* $Dimensionless
**W**$  $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **V**: Dimensionless &emsp;(exposed as **V**)
: **W**: Dimensionless &emsp;(exposed as **W**)










<i>**Time Derivatives**</i>
    : d **V** /dt = ( (V - ((V^3) / 3)) - W + I) / SEC
    : d **W** /dt = (0.08 * (V + 0.7 - 0.8 * W)) / SEC
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=FitzHughNagumoCell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import FitzHughNagumoCell

variable = FitzHughNagumoCell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, I=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<fitzHughNagumoCell id="fn1" I="0.8"/>
```

````

(schema:pinskyrinzelca3cell)=

## pinskyRinzelCA3Cell




extends *{ref}`schema:basecellmembpot`*



<i>Reduced CA3 cell model from Pinsky and Rinzel 1994. See https://github.com/OpenSourceBrain/PinskyRinzelModel.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**alphac**$  $Dimensionless
**betac**$  $Dimensionless
**cm**$  ${ref}`schema:dimensions:specificCapacitance`
**eCa**$  ${ref}`schema:dimensions:voltage`
**eK**$  ${ref}`schema:dimensions:voltage`
**eL**$  ${ref}`schema:dimensions:voltage`
**eNa**$  ${ref}`schema:dimensions:voltage`
**gAmpa**$  ${ref}`schema:dimensions:conductanceDensity`
**gCa**$  ${ref}`schema:dimensions:conductanceDensity`
**gKC**$  ${ref}`schema:dimensions:conductanceDensity`
**gKahp**$  ${ref}`schema:dimensions:conductanceDensity`
**gKdr**$  ${ref}`schema:dimensions:conductanceDensity`
**gLd**$  ${ref}`schema:dimensions:conductanceDensity`
**gLs**$  ${ref}`schema:dimensions:conductanceDensity`
**gNa**$  ${ref}`schema:dimensions:conductanceDensity`
**gNmda**$  ${ref}`schema:dimensions:conductanceDensity`
**gc**$  ${ref}`schema:dimensions:conductanceDensity`
**iDend**$  ${ref}`schema:dimensions:currentDensity`
**iSoma**$  ${ref}`schema:dimensions:currentDensity`
**pp**$  $Dimensionless
**qd0**$  $Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1 ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1 mV$  $ {ref}`schema:dimensions:voltage`
**UAMP_PER_CM2** = 1 uA_per_cm2$  $ {ref}`schema:dimensions:currentDensity`
**Smax** = 125.0$  $ Dimensionless
**Vsyn** = 60.0 mV$  $ {ref}`schema:dimensions:voltage`
**betaqd** = 0.001$  $ Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**Cad**$  $Dimensionless
**ICad**$  ${ref}`schema:dimensions:currentDensity`
**Si**$  $Dimensionless
**Vd**$  ${ref}`schema:dimensions:voltage`
**Vs**$  ${ref}`schema:dimensions:voltage`
**Wi**$  $Dimensionless
**cd**$  $Dimensionless
**hs**$  $Dimensionless
**ns**$  $Dimensionless
**qd**$  $Dimensionless
**sd**$  $Dimensionless
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PinskyRinzelCA3Cell" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import PinskyRinzelCA3Cell

variable = PinskyRinzelCA3Cell(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, i_soma=None, i_dend=None, gc=None, g_ls=None, g_ld=None, g_na=None, g_kdr=None, g_ca=None, g_kahp=None, g_kc=None, g_nmda=None, g_ampa=None, e_na=None, e_ca=None, e_k=None, e_l=None, qd0=None, pp=None, alphac=None, betac=None, cm=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<pinskyRinzelCA3Cell id="pr2A" iSoma="0.75 uA_per_cm2" iDend="0 uA_per_cm2" gc="2.1 mS_per_cm2" qd0="0" gLs="0.1 mS_per_cm2" gLd="0.1 mS_per_cm2" gNa="30 mS_per_cm2" gKdr="15 mS_per_cm2" gCa="10 mS_per_cm2" gKahp="0.8 mS_per_cm2" gKC="15 mS_per_cm2" eNa="60 mV" eCa="80 mV" eK="-75 mV" eL="-60 mV" pp="0.5" cm="3 uF_per_cm2" alphac="2" betac="0.1" gNmda="0 mS_per_cm2" gAmpa="0 mS_per_cm2"/>
```

````
