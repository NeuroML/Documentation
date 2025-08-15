
(schema:cells_)=
# Cells

**Defines both abstract cell models ( e.g.  {ref}`schema:izhikevichcell`, adaptive exponential integrate and fire cell,  {ref}`schema:adexiafcell` ), point conductance based cell models (  {ref}`schema:pointcellcondbased`,  {ref}`schema:pointcellcondbasedca` ) and cells models (  {ref}`schema:cell` ) which specify the  {ref}`schema:morphology` ( containing  {ref}`schema:segment`s ) and  {ref}`schema:biophysicalproperties` separately.**

---


Original ComponentType definitions: [Cells.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Cells.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basecell)=

## *baseCell*




extends *{ref}`schema:basestandalone`*



<i>Base type of any cell ( e.g. point neuron like  {ref}`schema:izhikevich2007cell`, or a morphologically detailed  {ref}`schema:cell` with  {ref}`schema:segment`s ) which can be used in a  {ref}`schema:population`.</i>


`````{tab-set}
````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BaseCell">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseCell
from neuroml.utils import component_factory

variable = component_factory(
    BaseCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:basespikingcell)=

## *baseSpikingCell*




extends *{ref}`schema:basecell`*



<i>Base type of any cell which can emit **spike** events.</i>


`````{tab-set}
````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event$Direction: out

```
````
`````

(schema:basecellmembpot)=

## *baseCellMembPot*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a membrane potential **v** with units of voltage ( as opposed to a dimensionless membrane potential used in  {ref}`schema:basecellmembpotdl` ).</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````
`````

(schema:basecellmembpotdl)=

## *baseCellMembPotDL*




extends *{ref}`schema:basespikingcell`*



<i>Any spiking cell which has a dimensioness membrane potential, **V** ( as opposed to a membrane potential units of voltage,  {ref}`schema:basecellmembpot` ).</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**V**$ Membrane potential $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````
`````

(schema:basechannelpopulation)=

## *baseChannelPopulation*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for any current produced by a population of channels, all of which are of type **ionChannel**.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**ionChannel**$  $ {ref}`schema:baseionchannel`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:channelpopulation)=

## channelPopulation




extends *{ref}`schema:basechannelpopulation`*



<i>Population of a **number** of ohmic ion channels. These each produce a conductance **channelg** across a reversal potential **erev,** giving a total current **i.** Note that active membrane currents are more frequently specified as a density over an area of the  {ref}`schema:cell` using  {ref}`schema:channeldensity`.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`
**number**$ The number of channels present. This will be multiplied by the time varying conductance of the individual ion channel (which extends _baseIonChannel_) to produce the total conductance $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**vShift** = 0mV$ Set to a constant 0mV here to allow ion channels which use _vShift in their rate variable expressions to be used with _channelPopulation_, not just with _channelDensityVShift_ (where _vShift would be explicitly set) $ {ref}`schema:dimensions:voltage`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **channelg** =&nbsp;ionChannel->g
    : **geff** =&nbsp;channelg * number
    : **i** =&nbsp;geff * (erev - v)&emsp;(exposed as **i**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelPopulation">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="variableParameter" type="VariableParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="number" type="NonNegativeInteger" use="required"/>
      <xs:attribute name="erev" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
      <xs:attribute name="segment" type="NonNegativeInteger" use="optional"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelPopulation" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelPopulation
from neuroml.utils import component_factory

variable = component_factory(
    ChannelPopulation,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    number: 'a NonNegativeInteger (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<channelPopulation id="naChansDend" ionChannel="NaConductance" segment="2" number="120000" erev="50mV" ion="na"/>
```
````
`````

(schema:channelpopulationnernst)=

## channelPopulationNernst




extends *{ref}`schema:basechannelpopulation`*



<i>Population of a **number** of channels with a time varying reversal potential **erev** determined by Nernst equation. Note: hard coded for Ca only!</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**number**$ The number of channels present. This will be multiplied by the time varying conductance of the individual ion channel (which extends _baseIonChannel_) to produce the total conductance $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$ $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$ $ Dimensionless
**F** = 96485.3 C_per_mol$ $ {ref}`schema:dimensions:charge_per_mole`
**vShift** = 0mV$ Set to a constant 0mV here to allow ion channels which use _vShift in their rate variable expressions to be used with _channelPopulation_, not just with _channelDensityVShift_ (where _vShift would be explicitly set) $ {ref}`schema:dimensions:voltage`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced, calculated from _caConcExt and _caConc ${ref}`schema:dimensions:voltage`
**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **singleChannelConductance** =&nbsp;ionChannel->g
    : **totalConductance** =&nbsp;singleChannelConductance * number
    : **erev** =&nbsp;(R * temperature / (zCa * F)) * log(caConcExt / caConc)&emsp;(exposed as **erev**)
    : **i** =&nbsp;totalConductance * (erev - v)&emsp;(exposed as **i**)
    





````
`````

(schema:basechanneldensity)=

## *baseChannelDensity*




<i>Base type for a current of density **iDensity** distributed on an area of a  {ref}`schema:cell`, flowing through the specified **ionChannel.** Instances of this ( normally  {ref}`schema:channeldensity` ) are specified in the  {ref}`schema:membraneproperties` of the  {ref}`schema:cell`.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**ionChannel**$  $ {ref}`schema:baseionchannel`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  ${ref}`schema:dimensions:currentDensity`

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

(schema:basechanneldensitycond)=

## *baseChannelDensityCond*




extends *{ref}`schema:basechanneldensity`*



<i>Base type for distributed conductances on an area of a cell producing a ( not necessarily ohmic ) current.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:variableparameter)=

## variableParameter




<i>Specifies a **parameter** ( e.g. condDensity ) which can vary its value across a **segmentGroup.** The value is calculated from **value** attribute of the  {ref}`schema:inhomogeneousvalue` subelement. This element is normally a child of  {ref}`schema:channeldensitynonuniform`,  {ref}`schema:channeldensitynonuniformnernst` or  {ref}`schema:channeldensitynonuniformghk` and is used to calculate the value of the conductance, etc. which will vary on different parts of the cell. The **segmentGroup** specified here needs to define an  {ref}`schema:inhomogeneousparameter` ( referenced from **inhomogeneousParameter** in the  {ref}`schema:inhomogeneousvalue` ), which calculates a **variable** ( e.g. p ) varying across the cell ( e.g. based on the path length from soma ), which is then used in the **value** attribute of the  {ref}`schema:inhomogeneousvalue` ( so for example condDensity = f( p ) ).</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**parameter**$ 
**segmentGroup**$ 

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**inhomogeneousValue**$  $ {ref}`schema:inhomogeneousvalue`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="VariableParameter">
  <xs:sequence>
    <xs:element name="inhomogeneousValue" type="InhomogeneousValue" minOccurs="0"/>
  </xs:sequence>
  <xs:attribute name="parameter" type="xs:string" use="required"/>
  <xs:attribute name="segmentGroup" type="xs:string" use="required"/>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=VariableParameter" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import VariableParameter
from neuroml.utils import component_factory

variable = component_factory(
    VariableParameter,
    parameter: 'a string (required)' = None,
    segment_groups: 'a string (required)' = None,
    inhomogeneous_value: 'a InhomogeneousValue (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<variableParameter parameter="condDensity" segmentGroup="dendrite_group">
    <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>
</variableParameter>
```
````
`````

(schema:inhomogeneousvalue)=

## inhomogeneousValue




<i>Specifies the **value** of an **inhomogeneousParameter.** For usage see  {ref}`schema:variableparameter`.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**inhomogeneousParameter**$ 
**value**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="InhomogeneousValue">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="inhomogeneousParameter" type="xs:string" use="required"/>
      <xs:attribute name="value" type="xs:string" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InhomogeneousValue" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import InhomogeneousValue
from neuroml.utils import component_factory

variable = component_factory(
    InhomogeneousValue,
    inhomogeneous_parameters: 'a string (required)' = None,
    value: 'a string (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>
```
````
`````

(schema:channeldensitynonuniform)=

## channelDensityNonUniform




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying ohmic conductance density, which is distributed on a region of the **cell.** The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**ZERO_CURR_DENS** = 0 A_per_m2$  $ {ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**variableParameter**$  $ {ref}`schema:variableparameter`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityNonUniform">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="variableParameter" type="VariableParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="erev" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNonUniform" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityNonUniform
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityNonUniform,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<channelDensityNonUniform id="nonuniform_na_chans" ionChannel="NaConductance" erev="50mV" ion="na">
    <variableParameter parameter="condDensity" segmentGroup="dendrite_group">
        <inhomogeneousValue inhomogeneousParameter="dendrite_group_x1" value="5e-7 * exp(-p/200)"/>
    </variableParameter>
</channelDensityNonUniform>
```
````
`````

(schema:channeldensitynonuniformnernst)=

## channelDensityNonUniformNernst




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the **cell,** and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>


`````{tab-set}
````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**ZERO_CURR_DENS** = 0 A_per_m2$  $ {ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**variableParameter**$  $ {ref}`schema:variableparameter`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityNonUniformNernst">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="variableParameter" type="VariableParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNonUniformNernst" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityNonUniformNernst
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityNonUniformNernst,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
)
```
````
`````

(schema:channeldensitynonuniformghk)=

## channelDensityNonUniformGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, which is distributed on a region of the **cell,** and whose current is calculated from the Goldman-Hodgkin-Katz equation. Hard coded for Ca only!. The conductance density of the channel is not uniform, but is set using the  {ref}`schema:variableparameter`. Note, there is no dynamical description of this in LEMS yet, as this type only makes sense for multicompartmental cells. A ComponentType for this needs to be present to enable export of NeuroML 2 multicompartmental cells via LEMS/jNeuroML to NEURON.</i>


`````{tab-set}
````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**ZERO_CURR_DENS** = 0 A_per_m2$  $ {ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**variableParameter**$  $ {ref}`schema:variableparameter`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **iDensity** =&nbsp;ZERO_CURR_DENS&emsp;(exposed as **iDensity**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityNonUniformGHK">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="variableParameter" type="VariableParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNonUniformGHK" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityNonUniformGHK
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityNonUniformGHK,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
)
```
````
`````

(schema:channeldensity)=

## channelDensity




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying ohmic conductance density, **gDensity,** which is distributed on an area of the **cell** ( specified in  {ref}`schema:membraneproperties` ) with fixed reversal potential **erev** producing a current density **iDensity**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**vShift** = 0mV$ Set to a constant 0mV here to allow ion channels which use _vShift in their rate variable expressions to be used with _channelDensity_, not just with _channelDensityVShift_ (where _vShift would be explicitly set) $ {ref}`schema:dimensions:voltage`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensity is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **ionChannel**









<i>**Derived Variables**</i>
    : **channelf** =&nbsp;ionChannel->fopen
    : **gDensity** =&nbsp;condDensity * channelf&emsp;(exposed as **gDensity**)
    : **iDensity** =&nbsp;gDensity * (erev - v)&emsp;(exposed as **iDensity**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensity">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="variableParameter" type="VariableParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="condDensity" type="Nml2Quantity_conductanceDensity" use="optional"/>
      <xs:attribute name="erev" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
      <xs:attribute name="segment" type="NonNegativeInteger" use="optional"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensity" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensity
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensity,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    cond_density: 'a Nml2Quantity_conductanceDensity (optional)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<channelDensity id="pasChans" ionChannel="pas" condDensity="3.0 S_per_m2" erev="-70mV" ion="non_specific"/>
```
```{code-block} xml
<channelDensity id="naChansSoma" ionChannel="NaConductance" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" erev="50mV" ion="na"/>
```
```{code-block} xml
<channelDensity id="naChans" ionChannel="HH_Na" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" ion="na" erev="50mV"/>
```
````
`````

(schema:channeldensityvshift)=

## channelDensityVShift




extends {ref}`schema:channeldensity`



<i>Same as  {ref}`schema:channeldensity`, but with a **vShift** parameter to change voltage activation of gates. The exact usage of **vShift** in expressions for rates is determined by the individual gates.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**erev**$ The reversal potential of the current produced *(from {ref}`schema:channeldensity`)* ${ref}`schema:dimensions:voltage`
**vShift**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensity is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityVShift">
  <xs:complexContent>
    <xs:extension base="ChannelDensity">
      <xs:attribute name="vShift" type="Nml2Quantity_voltage" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityVShift" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityVShift
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityVShift,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    cond_density: 'a Nml2Quantity_conductanceDensity (optional)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
    v_shift: 'a Nml2Quantity_voltage (required)' = None,
)
```
````
`````

(schema:channeldensitynernst)=

## channelDensityNernst




extends *{ref}`schema:basechanneldensitycond`*



<i>Specifies a time varying conductance density, **gDensity,** which is distributed on an area of the **cell,** producing a current density **iDensity** and whose reversal potential is calculated from the Nernst equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$ $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$ $ Dimensionless
**F** = 96485.3 C_per_mol$ $ {ref}`schema:dimensions:charge_per_mole`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityNernst is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced, calculated from caConcExt and caConc ${ref}`schema:dimensions:voltage`
**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityNernst">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="variableParameter" type="VariableParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="condDensity" type="Nml2Quantity_conductanceDensity" use="optional"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
      <xs:attribute name="segment" type="NmlId" use="optional"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNernst" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityNernst
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityNernst,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    cond_density: 'a Nml2Quantity_conductanceDensity (optional)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:channeldensitynernstca2)=

## channelDensityNernstCa2




extends *{ref}`schema:basechanneldensitycond`*



<i>This component is similar to the original component type  {ref}`schema:channeldensitynernst` but it is changed in order to have a reversal potential that depends on a second independent Ca++ pool ( ca2 ). See https://github.com/OpenSourceBrain/ghk-nernst.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$ $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$ $ Dimensionless
**F** = 96485.3 C_per_mol$ $ {ref}`schema:dimensions:charge_per_mole`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityNernstCa2 is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ The reversal potential of the current produced ${ref}`schema:dimensions:voltage`
**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityNernstCa2">
  <xs:complexContent>
    <xs:extension base="ChannelDensityNernst">
      </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityNernstCa2" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityNernstCa2
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityNernstCa2,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    cond_density: 'a Nml2Quantity_conductanceDensity (optional)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
    variable_parameters: 'list of VariableParameter(s) (optional)' = None,
)
```
````
`````

(schema:channeldensityghk)=

## channelDensityGHK




extends *{ref}`schema:basechanneldensity`*



<i>Specifies a time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity** and whose reversal potential is calculated from the Goldman Hodgkin Katz equation. Hard coded for Ca only! See https://github.com/OpenSourceBrain/ghk-nernst.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**permeability**$  ${ref}`schema:dimensions:permeability`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**R** = 8.3144621 J_per_K_per_mol$ $ {ref}`schema:dimensions:idealGasConstantDims`
**zCa** = 2$ $ Dimensionless
**F** = 96485.3 C_per_mol$ $ {ref}`schema:dimensions:charge_per_mole`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityGHK is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityGHK">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="permeability" type="Nml2Quantity_permeability" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
      <xs:attribute name="segment" type="NmlId" use="optional"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityGHK" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityGHK
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityGHK,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    permeability: 'a Nml2Quantity_permeability (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
)
```
````
`````

(schema:channeldensityghk2)=

## channelDensityGHK2




extends *{ref}`schema:basechanneldensitycond`*



<i>Time varying conductance density, **gDensity,** which is distributed on an area of the cell, producing a current density **iDensity.** Modified version of Jaffe et al. 1994 ( used also in Lawrence et al. 2006 ). See https://github.com/OpenSourceBrain/ghk-nernst.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**condDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**VOLT_SCALE** = 1 mV$  $ {ref}`schema:dimensions:voltage`
**CONC_SCALE** = 1 mM$  $ {ref}`schema:dimensions:concentration`
**TEMP_SCALE** = 1 K$  $ {ref}`schema:dimensions:temperature`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ Which _segmentGroup_ the channelDensityGHK2 is placed on. If this is missing, it implies it is placed on all _segment_s of the _cell_
**ion**$ Which ion flows through the channel. Note: ideally this needs to be a property of ionChannel only, but it's here as it makes it easier to select channelPopulations transmitting specific ions.

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**gDensity**$  *(from {ref}`schema:basechanneldensitycond`)* ${ref}`schema:dimensions:conductanceDensity`
**iDensity**$  *(from {ref}`schema:basechanneldensity`)* ${ref}`schema:dimensions:currentDensity`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics

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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ChannelDensityGHK2">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:attribute name="ionChannel" type="NmlId" use="required"/>
      <xs:attribute name="condDensity" type="Nml2Quantity_conductanceDensity" use="optional"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
      <xs:attribute name="segment" type="NmlId" use="optional"/>
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ChannelDensityGHK2" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ChannelDensityGHK2
from neuroml.utils import component_factory

variable = component_factory(
    ChannelDensityGHK2,
    id: 'a NmlId (required)' = None,
    ion_channel: 'a NmlId (required)' = None,
    cond_density: 'a Nml2Quantity_conductanceDensity (optional)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
    segments: 'a NonNegativeInteger (optional)' = None,
    ion: 'a NmlId (required)' = None,
)
```
````
`````

(schema:pointcellcondbased)=

## pointCellCondBased




extends *{ref}`schema:basecellmembpotcap`*



<i>Simple model of a conductance based cell, with no separate  {ref}`schema:morphology` element, just an absolute capacitance **C,** and a set of channel **populations.** Note: use of  {ref}`schema:cell` is generally preferable ( and more widely supported ), even for a single compartment cell.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**thresh**$ The voltage threshold above which the cell is considered to be _spiking ${ref}`schema:dimensions:voltage`
**v0**$ The initial membrane potential of the cell ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**populations**$  $ {ref}`schema:basechannelpopulation`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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
`````

(schema:pointcellcondbasedca)=

## pointCellCondBasedCa




extends *{ref}`schema:basecellmembpotcap`*



<i>TEMPORARY: Point cell with conductances and Ca concentration info. Not yet fully tested!!!</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**thresh**$ The voltage threshold above which the cell is considered to be _spiking ${ref}`schema:dimensions:voltage`
**v0**$ The initial membrane potential of the cell ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**populations**$  $ {ref}`schema:basechannelpopulation`
**concentrationModels**$  $ {ref}`schema:concentrationmodel`

```
````

````{tab-item} Exposures
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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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
`````

(schema:distal)=

## distal




extends {ref}`schema:point3dwithdiam`



<i>Point on a  {ref}`schema:segment` furthest from the soma. Should always be present in the description of a  {ref}`schema:segment`, unlike  {ref}`schema:proximal`.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**radius**$ A dimensional quantity given by half the _diameter. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**radius** = MICRON * diameter / 2
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**xLength**$ A version of _x with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**xLength** = MICRON * x
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**yLength**$ A version of _y with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**yLength** = MICRON * y
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**zLength**$ A version of _z with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**zLength** = MICRON * z

````


````{tab-item} Usage: XML
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
`````

(schema:proximal)=

## proximal




extends {ref}`schema:point3dwithdiam`



<i>Point on a  {ref}`schema:segment` closest to the soma. Note, the proximal point can be omitted, and in this case is defined as being the point **fractionAlong** between the proximal and  {ref}`schema:distal` point of the  {ref}`schema:parent`, i.e. if **fractionAlong** = 1 ( as it is by default ) it will be the **distal** on the parent, or if **fractionAlong** = 0, it will be the proximal point. If between 0 and 1, it is the linear interpolation between the two points.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**radius**$ A dimensional quantity given by half the _diameter. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**radius** = MICRON * diameter / 2
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**xLength**$ A version of _x with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**xLength** = MICRON * x
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**yLength**$ A version of _y with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**yLength** = MICRON * y
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**zLength**$ A version of _z with dimension length. *(from {ref}`schema:point3dwithdiam`)* ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**zLength** = MICRON * z

````


````{tab-item} Usage: XML
```{code-block} xml
<proximal x="0" y="0" z="0" diameter="10"/>
```
```{code-block} xml
<proximal x="25" y="0" z="0" diameter="0.1"/>
```
```{code-block} xml
<proximal x="0" y="0" z="0" diameter="10"/>
```
````
`````

(schema:parent)=

## parent




<i>Specifies the  {ref}`schema:segment` which is this segment's parent. The **fractionAlong** specifies where it is connected, usually 1 ( the default value ), meaning the  {ref}`schema:distal` point of the parent, or 0, meaning the  {ref}`schema:proximal` point. If it is between these, a linear interpolation between the 2 points should be used.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ The id of the parent segment
**fractionAlong**$ The fraction along the the parent segment at which this segment is attached. For usage see _proximal_

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SegmentParent">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="segment" type="NonNegativeInteger" use="required"/>
      <xs:attribute name="fractionAlong" type="ZeroToOne" use="optional" default="1"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<parent segment="0"/>
```
```{code-block} xml
<parent segment="1"/>
```
```{code-block} xml
<parent segment="2" fractionAlong="0.5"/>
```
````
`````

(schema:segment)=

## segment




<i>A segment defines the smallest unit within a possibly branching structure (  {ref}`schema:morphology` ), such as a dendrite or axon. Its **id** should be a nonnegative integer ( usually soma/root = 0 ). Its end points are given by the  {ref}`schema:proximal` and  {ref}`schema:distal` points. The  {ref}`schema:proximal` point can be omitted, usually because it is the same as a point on the  {ref}`schema:parent` segment, see  {ref}`schema:proximal` for details.  {ref}`schema:parent` specifies the parent segment. The first segment of a  {ref}`schema:cell` ( with no  {ref}`schema:parent` ) usually represents the soma. The shape is normally a cylinder ( radii of the  {ref}`schema:proximal` and  {ref}`schema:distal` equal, but positions different ) or a conical frustum ( radii and positions different ). If the x, y, x positions of the  {ref}`schema:proximal` and  {ref}`schema:distal` are equal, the segment can be interpreted as a sphere, and in this case the radii of these points must be equal. NOTE: LEMS does not yet support multicompartmental modelling, so the Dynamics here is only appropriate for single compartment modelling.</i>


`````{tab-set}
````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**LEN** = 1m$  $ {ref}`schema:dimensions:length`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**name**$ An optional name for the segment. Convenient for providing a suitable variable name for generated code, e.g. soma, dend0

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**parent**$  $ {ref}`schema:parent`
**distal**$  $ {ref}`schema:distal`
**proximal**$  $ {ref}`schema:proximal`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**length**$  ${ref}`schema:dimensions:length`
**radDist**$  ${ref}`schema:dimensions:length`
**surfaceArea**$  ${ref}`schema:dimensions:area`

```
````

````{tab-item} Dynamics








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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Segment">
  <xs:complexContent>
    <xs:extension base="BaseNonNegativeIntegerId">
      <xs:sequence>
        <xs:element name="parent" type="SegmentParent" minOccurs="0"/>
        <xs:element name="proximal" type="Point3DWithDiam" minOccurs="0"/>
        <xs:element name="distal" type="Point3DWithDiam" minOccurs="1"/>
      </xs:sequence>
      <xs:attribute name="name" type="xs:string" use="optional"/>
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Segment" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Segment
from neuroml.utils import component_factory

variable = component_factory(
    Segment,
    id: 'a NonNegativeInteger (required)' = None,
    name: 'a string (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    parent: 'a SegmentParent (optional)' = None,
    proximal: 'a Point3DWithDiam (optional)' = None,
    distal: 'a Point3DWithDiam (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<segment id="3" name="Spine1">
    <parent segment="2" fractionAlong="0.5"/>
    <proximal x="25" y="0" z="0" diameter="0.1"/>
    <distal x="25" y="0.2" z="0" diameter="0.1"/>
</segment>
```
```{code-block} xml
<segment id="0" name="Soma">
    <proximal x="0" y="0" z="0" diameter="10"/>
    <distal x="10" y="0" z="0" diameter="10"/>
</segment>
```
```{code-block} xml
<segment id="1" name="Dendrite1">
    <parent segment="0"/>
    <distal x="20" y="0" z="0" diameter="3"/>
</segment>
```
````
`````

(schema:segmentgroup)=

## segmentGroup




<i>A method to describe a group of  {ref}`schema:segment`s in a  {ref}`schema:morphology`, e.g. soma_group, dendrite_group, axon_group. While a name is useful to describe the group, the **neuroLexId** attribute can be used to explicitly specify the meaning of the group, e.g. sao1044911821 for 'Neuronal Cell Body', sao1211023249 for 'Dendrite'. The  {ref}`schema:segment`s in this group can be specified as: a list of individual  {ref}`schema:member` segments; a  {ref}`schema:path`, all of the segments along which should be included; a  {ref}`schema:subtree` of the  {ref}`schema:cell` to include; other segmentGroups to  {ref}`schema:include` ( so all segments from those get included here ). An  {ref}`schema:inhomogeneousparameter` can be defined on the region of the cell specified by this group ( see  {ref}`schema:variableparameter` for usage ).</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**neuroLexId**$ An id string for pointing to an entry in the NeuroLex ontology. Use of this attribute is a shorthand for a full         RDF based reference to the MIRIAM Resource urn:miriam:neurolex, with an bqbiol:is qualifier.

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

````{tab-item} Children list
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SegmentGroup">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="notes" type="Notes" minOccurs="0"/>
        <xs:element name="property" type="Property" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="annotation" type="Annotation" minOccurs="0"/>
        <xs:element name="member" type="Member" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="include" type="Include" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="path" type="Path" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="subTree" type="SubTree" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="inhomogeneousParameter" type="InhomogeneousParameter" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SegmentGroup" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SegmentGroup
from neuroml.utils import component_factory

variable = component_factory(
    SegmentGroup,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    members: 'list of Member(s) (optional)' = None,
    includes: 'list of Include(s) (optional)' = None,
    paths: 'list of Path(s) (optional)' = None,
    sub_trees: 'list of SubTree(s) (optional)' = None,
    inhomogeneous_parameters: 'list of InhomogeneousParameter(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<segmentGroup id="dendrite_group" neuroLexId="sao1211023249">
    <member segment="1"/>
    <member segment="2"/>
    <member segment="3"/>
</segmentGroup>
```
```{code-block} xml
<segmentGroup id="soma_group" neuroLexId="sao1044911821">
    <member segment="0"/>
</segmentGroup>
```
```{code-block} xml
<segmentGroup id="spines" neuroLexId="sao1145756102">
    <member segment="3"/>
</segmentGroup>
```
````
`````

(schema:member)=

## member




<i>A single identified **segment** which is part of the  {ref}`schema:segmentgroup`.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Member">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="segment" type="NonNegativeInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Member" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Member
from neuroml.utils import component_factory

variable = component_factory(
    Member,
    segments: 'a NonNegativeInteger (required)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:from)=

## from




<i>In a  {ref}`schema:path` or  {ref}`schema:subtree`, specifies which **segment** ( inclusive ) from which to calculate the  {ref}`schema:segmentgroup`.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SegmentEndPoint">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="segment" type="NonNegativeInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<from segment="1"/>
```
```{code-block} xml
<from segment="1"/>
```
````
`````

(schema:to)=

## to




<i>In a  {ref}`schema:path`, specifies which **segment** ( inclusive ) up to which to calculate the  {ref}`schema:segmentgroup`.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segment**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SegmentEndPoint">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="segment" type="NonNegativeInteger" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````


````{tab-item} Usage: XML
```{code-block} xml
<to segment="2"/>
```
````
`````

(schema:include)=

## include




<i>Include all members of another  {ref}`schema:segmentgroup` in this group.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**href**$ 
**segmentGroup**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Include">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="segmentGroup" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Include" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Include
from neuroml.utils import component_factory

variable = component_factory(
    Include,
    segment_groups: 'a NmlId (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<include href="NML2_SingleCompHHCell.nml"/>
```
```{code-block} xml
<include href="NML2_SimpleIonChannel.nml"/>
```
```{code-block} xml
<include href="NML2_SimpleIonChannel.nml"/>
```
````
`````

(schema:path)=

## path




<i>Include all the  {ref}`schema:segment`s between those specified by  {ref}`schema:from` and  {ref}`schema:to`, inclusive.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**from**$  $ {ref}`schema:from`
**to**$  $ {ref}`schema:to`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Path">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:sequence>
        <xs:element name="from" type="SegmentEndPoint" minOccurs="0"/>
        <xs:element name="to" type="SegmentEndPoint" minOccurs="0"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Path" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Path
from neuroml.utils import component_factory

variable = component_factory(
    Path,
    from_: 'a SegmentEndPoint (optional)' = None,
    to: 'a SegmentEndPoint (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<path>
    <from segment="1"/>
    <to segment="2"/>
</path>
```
````
`````

(schema:subtree)=

## subTree




<i>Include all the  {ref}`schema:segment`s distal to that specified by  {ref}`schema:from` in the  {ref}`schema:segmentgroup`.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**from**$  $ {ref}`schema:from`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SubTree">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:choice>
        <xs:element name="from" type="SegmentEndPoint" minOccurs="0"/>
        <xs:element name="to" type="SegmentEndPoint" minOccurs="0"/>
      </xs:choice>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SubTree" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SubTree
from neuroml.utils import component_factory

variable = component_factory(
    SubTree,
    from_: 'a SegmentEndPoint (optional)' = None,
    to: 'a SegmentEndPoint (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<subTree>
    <from segment="1"/>
</subTree>
```
````
`````

(schema:inhomogeneousparameter)=

## inhomogeneousParameter




<i>An inhomogeneous parameter specified across the  {ref}`schema:segmentgroup` ( see  {ref}`schema:variableparameter` for usage ).</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**variable**$ 
**metric**$ 

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**proximal**$  $ {ref}`schema:proximaldetails`
**distal**$  $ {ref}`schema:distaldetails`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="InhomogeneousParameter">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="proximal" type="ProximalDetails" minOccurs="0"/>
        <xs:element name="distal" type="DistalDetails" minOccurs="0"/>
      </xs:sequence>
      <xs:attribute name="variable" type="xs:string" use="required"/>
      <xs:attribute name="metric" type="Metric" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InhomogeneousParameter" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import InhomogeneousParameter
from neuroml.utils import component_factory

variable = component_factory(
    InhomogeneousParameter,
    id: 'a NmlId (required)' = None,
    variable: 'a string (required)' = None,
    metric: 'a Metric (required)' = None,
    proximal: 'a ProximalDetails (optional)' = None,
    distal: 'a DistalDetails (optional)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:proximaldetails)=

## proximalDetails




<i>What to do at the proximal point when creating an inhomogeneous parameter.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**translationStart**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ProximalDetails">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="translationStart" type="xs:double" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ProximalDetails" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ProximalDetails
from neuroml.utils import component_factory

variable = component_factory(
    ProximalDetails,
    translation_start: 'a double (required)' = None,
)
```
````
`````

(schema:distaldetails)=

## distalDetails




<i>What to do at the distal point when creating an inhomogeneous parameter.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**normalizationEnd**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DistalDetails">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="normalizationEnd" type="xs:double" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=DistalDetails" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import DistalDetails
from neuroml.utils import component_factory

variable = component_factory(
    DistalDetails,
    normalization_end: 'a double (required)' = None,
)
```
````
`````

(schema:morphology)=

## morphology




<i>The collection of  {ref}`schema:segment`s which specify the 3D structure of the cell, along with a number of  {ref}`schema:segmentgroup`s.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**segments**$  $ {ref}`schema:segment`
**segmentGroups**$  $ {ref}`schema:segmentgroup`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Morphology">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="segment" type="Segment" maxOccurs="unbounded"/>
        <xs:element name="segmentGroup" type="SegmentGroup" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Morphology" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Morphology
from neuroml.utils import component_factory

variable = component_factory(
    Morphology,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    segments: 'list of Segment(s) (required)' = None,
    segment_groups: 'list of SegmentGroup(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<morphology id="SpikingCell_morphology">
    <segment id="0" name="Soma">
        <proximal x="0" y="0" z="0" diameter="10"/>
        <distal x="10" y="0" z="0" diameter="10"/>
    </segment>
    <segment id="1" name="Dendrite1">
        <parent segment="0"/>
        <distal x="20" y="0" z="0" diameter="3"/>
    </segment>
    <segment id="2" name="Dendrite2">
        <parent segment="1"/>
        <distal x="30" y="0" z="0" diameter="1"/>
    </segment>
    <segment id="3" name="Spine1">
        <parent segment="2" fractionAlong="0.5"/>
        <proximal x="25" y="0" z="0" diameter="0.1"/>
        <distal x="25" y="0.2" z="0" diameter="0.1"/>
    </segment>
    <segmentGroup id="soma_group" neuroLexId="sao1044911821">
        <member segment="0"/>
    </segmentGroup>
    <segmentGroup id="dendrite_group" neuroLexId="sao1211023249">
        <member segment="1"/>
        <member segment="2"/>
        <member segment="3"/>
    </segmentGroup>
    <segmentGroup id="spines" neuroLexId="sao1145756102">
        <member segment="3"/>
    </segmentGroup>
</morphology>
```
```{code-block} xml
<morphology id="NeuroMorpho_PyrCell123">
    <segment id="0" name="Soma">
        <proximal x="0" y="0" z="0" diameter="10"/>
        <distal x="10" y="0" z="0" diameter="10"/>
    </segment>
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
````
`````

(schema:specificcapacitance)=

## specificCapacitance




<i>Capacitance per unit area.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**specCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **specCap** =&nbsp;value&emsp;(exposed as **specCap**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpecificCapacitance">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="value" type="Nml2Quantity_specificCapacitance" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpecificCapacitance" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpecificCapacitance
from neuroml.utils import component_factory

variable = component_factory(
    SpecificCapacitance,
    value: 'a Nml2Quantity_specificCapacitance (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
```
```{code-block} xml
<specificCapacitance segmentGroup="dendrite_group" value="2.0 uF_per_cm2"/>
```
```{code-block} xml
<specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
```
````
`````

(schema:initmembpotential)=

## initMembPotential




<i>Explicitly set initial membrane potential for the cell.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="InitMembPotential">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="value" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InitMembPotential" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import InitMembPotential
from neuroml.utils import component_factory

variable = component_factory(
    InitMembPotential,
    value: 'a Nml2Quantity_voltage (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<initMembPotential value="-65mV"/>
```
```{code-block} xml
<initMembPotential value="-65mV"/>
```
````
`````

(schema:spikethresh)=

## spikeThresh




<i>Membrane potential at which to emit a spiking event. Note, usually the spiking event will not be emitted again until the membrane potential has fallen below this value and rises again to cross it in a positive direction.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeThresh">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="value" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeThresh" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeThresh
from neuroml.utils import component_factory

variable = component_factory(
    SpikeThresh,
    value: 'a Nml2Quantity_voltage (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spikeThresh value="-20mV"/>
```
```{code-block} xml
<spikeThresh value="-20mV"/>
```
````
`````

(schema:membraneproperties)=

## membraneProperties




<i>Properties specific to the membrane, such as the **populations** of channels, **channelDensities,** **specificCapacitance,** etc.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**initMembPotential**$  $ {ref}`schema:initmembpotential`
**spikeThresh**$  $ {ref}`schema:spikethresh`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**specificCapacitances**$  $ {ref}`schema:specificcapacitance`
**populations**$  $ {ref}`schema:basechannelpopulation`
**channelDensities**$  $ {ref}`schema:basechanneldensity`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iCa**$  ${ref}`schema:dimensions:current`
**totChanCurrent**$  ${ref}`schema:dimensions:current`
**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**surfaceArea**$  ${ref}`schema:dimensions:area`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;specificCapacitances[*]->specCap(reduce method: add)&emsp;(exposed as **totSpecCap**)
    : **totChanPopCurrent** =&nbsp;populations[*]->i(reduce method: add)
    : **totChanDensCurrentDensity** =&nbsp;channelDensities[*]->iDensity(reduce method: add)
    : **totChanCurrent** =&nbsp;totChanPopCurrent + (totChanDensCurrentDensity * surfaceArea)&emsp;(exposed as **totChanCurrent**)
    : **totChanPopCurrentCa** =&nbsp;populations[ion='ca']->i(reduce method: add)
    : **totChanDensCurrentDensityCa** =&nbsp;channelDensities[ion='ca']->iDensity(reduce method: add)
    : **iCa** =&nbsp;totChanPopCurrentCa + (totChanDensCurrentDensityCa * surfaceArea)&emsp;(exposed as **iCa**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="MembraneProperties">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:sequence>
        <xs:element name="channelPopulation" type="ChannelPopulation" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensity" type="ChannelDensity" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityVShift" type="ChannelDensityVShift" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityNernst" type="ChannelDensityNernst" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityGHK" type="ChannelDensityGHK" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityGHK2" type="ChannelDensityGHK2" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityNonUniform" type="ChannelDensityNonUniform" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityNonUniformNernst" type="ChannelDensityNonUniformNernst" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="channelDensityNonUniformGHK" type="ChannelDensityNonUniformGHK" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="spikeThresh" type="SpikeThresh" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="specificCapacitance" type="SpecificCapacitance" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="initMembPotential" type="InitMembPotential" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=MembraneProperties" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import MembraneProperties
from neuroml.utils import component_factory

variable = component_factory(
    MembraneProperties,
    channel_populations: 'list of ChannelPopulation(s) (optional)' = None,
    channel_densities: 'list of ChannelDensity(s) (optional)' = None,
    channel_density_v_shifts: 'list of ChannelDensityVShift(s) (optional)' = None,
    channel_density_nernsts: 'list of ChannelDensityNernst(s) (optional)' = None,
    channel_density_ghks: 'list of ChannelDensityGHK(s) (optional)' = None,
    channel_density_ghk2s: 'list of ChannelDensityGHK2(s) (optional)' = None,
    channel_density_non_uniforms: 'list of ChannelDensityNonUniform(s) (optional)' = None,
    channel_density_non_uniform_nernsts: 'list of ChannelDensityNonUniformNernst(s) (optional)' = None,
    channel_density_non_uniform_ghks: 'list of ChannelDensityNonUniformGHK(s) (optional)' = None,
    spike_threshes: 'list of SpikeThresh(s) (required)' = None,
    specific_capacitances: 'list of SpecificCapacitance(s) (required)' = None,
    init_memb_potentials: 'list of InitMembPotential(s) (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<membraneProperties>
    <channelPopulation id="naChansDend" ionChannel="NaConductance" segment="2" number="120000" erev="50mV" ion="na"/>
    <channelDensity id="pasChans" ionChannel="pas" condDensity="3.0 S_per_m2" erev="-70mV" ion="non_specific"/>
    <channelDensity id="naChansSoma" ionChannel="NaConductance" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" erev="50mV" ion="na"/>
    <specificCapacitance segmentGroup="soma_group" value="1.0 uF_per_cm2"/>
    <specificCapacitance segmentGroup="dendrite_group" value="2.0 uF_per_cm2"/>
</membraneProperties>
```
```{code-block} xml
<membraneProperties>
    <channelDensity id="naChans" ionChannel="HH_Na" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" ion="na" erev="50mV"/>
    <!-- Ions present inside the cell. Note: a fixed reversal potential is specified here  
            <reversalPotential species="na" value="50mV"/>
            <reversalPotential species="k" value="-77mV"/>-->
</membraneProperties>
```
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
````
`````

(schema:membraneproperties2capools)=

## membraneProperties2CaPools




extends {ref}`schema:membraneproperties`



<i>Variant of membraneProperties with 2 independent Ca pools.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**initMembPotential**$  $ {ref}`schema:initmembpotential`
**spikeThresh**$  $ {ref}`schema:spikethresh`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**specificCapacitances**$  $ {ref}`schema:specificcapacitance`
**populations**$  $ {ref}`schema:basechannelpopulation`
**channelDensities**$  $ {ref}`schema:basechanneldensity`

```
````

````{tab-item} Exposures
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

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**surfaceArea**$  ${ref}`schema:dimensions:area`
**surfaceArea**$  *(from {ref}`schema:membraneproperties`)* ${ref}`schema:dimensions:area`

```
````

````{tab-item} Dynamics








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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="MembraneProperties2CaPools">
  <xs:complexContent>
    <xs:extension base="MembraneProperties">
      <xs:sequence>
        <xs:element name="channelDensityNernstCa2" type="ChannelDensityNernstCa2" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=MembraneProperties2CaPools" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import MembraneProperties2CaPools
from neuroml.utils import component_factory

variable = component_factory(
    MembraneProperties2CaPools,
    channel_populations: 'list of ChannelPopulation(s) (optional)' = None,
    channel_densities: 'list of ChannelDensity(s) (optional)' = None,
    channel_density_v_shifts: 'list of ChannelDensityVShift(s) (optional)' = None,
    channel_density_nernsts: 'list of ChannelDensityNernst(s) (optional)' = None,
    channel_density_ghks: 'list of ChannelDensityGHK(s) (optional)' = None,
    channel_density_ghk2s: 'list of ChannelDensityGHK2(s) (optional)' = None,
    channel_density_non_uniforms: 'list of ChannelDensityNonUniform(s) (optional)' = None,
    channel_density_non_uniform_nernsts: 'list of ChannelDensityNonUniformNernst(s) (optional)' = None,
    channel_density_non_uniform_ghks: 'list of ChannelDensityNonUniformGHK(s) (optional)' = None,
    spike_threshes: 'list of SpikeThresh(s) (required)' = None,
    specific_capacitances: 'list of SpecificCapacitance(s) (required)' = None,
    init_memb_potentials: 'list of InitMembPotential(s) (required)' = None,
    channel_density_nernst_ca2s: 'list of ChannelDensityNernstCa2(s) (optional)' = None,
)
```
````
`````

(schema:biophysicalproperties)=

## biophysicalProperties




<i>The biophysical properties of the  {ref}`schema:cell`, including the  {ref}`schema:membraneproperties` and the  {ref}`schema:intracellularproperties`.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**membraneProperties**$  $ {ref}`schema:membraneproperties`
**intracellularProperties**$  $ {ref}`schema:intracellularproperties`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;membraneProperties->totSpecCap&emsp;(exposed as **totSpecCap**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BiophysicalProperties">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="membraneProperties" type="MembraneProperties"/>
        <xs:element name="intracellularProperties" type="IntracellularProperties" minOccurs="0"/>
        <xs:element name="extracellularProperties" type="ExtracellularProperties" minOccurs="0"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BiophysicalProperties" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BiophysicalProperties
from neuroml.utils import component_factory

variable = component_factory(
    BiophysicalProperties,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    membrane_properties: 'a MembraneProperties (required)' = None,
    intracellular_properties: 'a IntracellularProperties (optional)' = None,
    extracellular_properties: 'a ExtracellularProperties (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<biophysicalProperties id="bio_cell">
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
```{code-block} xml
<biophysicalProperties id="PyrCellChanDist">
    <membraneProperties>
        <channelDensity id="naChans" ionChannel="HH_Na" segmentGroup="soma_group" condDensity="120.0 mS_per_cm2" ion="na" erev="50mV"/>
        <!-- Ions present inside the cell. Note: a fixed reversal potential is specified here  
            <reversalPotential species="na" value="50mV"/>
            <reversalPotential species="k" value="-77mV"/>-->
    </membraneProperties>
    <intracellularProperties>
        <resistivity value="0.1 kohm_cm"/>
        <!-- REMOVED UNTIL WE CHECK HOW THE USAGE OF LEMS IMPACTS THIS...
            <biochemistry reactionScheme="InternalCaDynamics"/>  Ref to earlier pathway -->
    </intracellularProperties>
</biophysicalProperties>
```
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
````
`````

(schema:biophysicalproperties2capools)=

## biophysicalProperties2CaPools




<i>The biophysical properties of the  {ref}`schema:cell`, including the  {ref}`schema:membraneproperties2capools` and the  {ref}`schema:intracellularproperties2capools` for a cell with two Ca pools.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**membraneProperties2CaPools**$  $ {ref}`schema:membraneproperties2capools`
**intracellularProperties2CaPools**$  $ {ref}`schema:intracellularproperties2capools`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**totSpecCap**$  ${ref}`schema:dimensions:specificCapacitance`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **totSpecCap** =&nbsp;membraneProperties2CaPools->totSpecCap&emsp;(exposed as **totSpecCap**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BiophysicalProperties2CaPools">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="membraneProperties2CaPools" type="MembraneProperties2CaPools"/>
        <xs:element name="intracellularProperties2CaPools" type="IntracellularProperties2CaPools" minOccurs="0"/>
        <xs:element name="extracellularProperties" type="ExtracellularProperties" minOccurs="0"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BiophysicalProperties2CaPools" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BiophysicalProperties2CaPools
from neuroml.utils import component_factory

variable = component_factory(
    BiophysicalProperties2CaPools,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    membrane_properties2_ca_pools: 'a MembraneProperties2CaPools (required)' = None,
    intracellular_properties2_ca_pools: 'a IntracellularProperties2CaPools (optional)' = None,
    extracellular_properties: 'a ExtracellularProperties (optional)' = None,
)
```
````
`````

(schema:intracellularproperties)=

## intracellularProperties




<i>Biophysical properties related to the intracellular space within the  {ref}`schema:cell`, such as the  {ref}`schema:resistivity` and the list of ionic  {ref}`schema:species` present. **caConc** and **caConcExt** are explicitly exposed here to facilitate accessing these values from other Components, even though **caConcExt** is clearly not an intracellular property.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**resistivity**$  $ {ref}`schema:resistivity`
**speciesList**$  $ {ref}`schema:species`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**caConcExt**$  ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **caConc** =&nbsp;speciesList[ion='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;speciesList[ion='ca']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IntracellularProperties">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:sequence>
        <xs:element name="species" type="Species" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="resistivity" type="Resistivity" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IntracellularProperties" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IntracellularProperties
from neuroml.utils import component_factory

variable = component_factory(
    IntracellularProperties,
    species: 'list of Species(s) (optional)' = None,
    resistivities: 'list of Resistivity(s) (optional)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<intracellularProperties>
    <resistivity value="0.1 kohm_cm"/>
</intracellularProperties>
```
```{code-block} xml
<intracellularProperties>
    <resistivity value="0.1 kohm_cm"/>
    <!-- REMOVED UNTIL WE CHECK HOW THE USAGE OF LEMS IMPACTS THIS...
            <biochemistry reactionScheme="InternalCaDynamics"/>  Ref to earlier pathway -->
</intracellularProperties>
```
```{code-block} xml
<intracellularProperties>
    <resistivity value="0.1 kohm_cm"/>
</intracellularProperties>
```
````
`````

(schema:intracellularproperties2capools)=

## intracellularProperties2CaPools




extends {ref}`schema:intracellularproperties`



<i>Variant of intracellularProperties with 2 independent Ca pools.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**speciesList**$  $ {ref}`schema:species`
**resistivity**$  $ {ref}`schema:resistivity`

```
````

````{tab-item} Exposures
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

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **caConc2** =&nbsp;speciesList[ion='ca2']->concentration(reduce method: add)&emsp;(exposed as **caConc2**)
    : **caConcExt2** =&nbsp;speciesList[ion='ca2']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt2**)
    : **caConc** =&nbsp;speciesList[ion='ca']->concentration(reduce method: add)&emsp;(exposed as **caConc**)
    : **caConcExt** =&nbsp;speciesList[ion='ca']->extConcentration(reduce method: add)&emsp;(exposed as **caConcExt**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IntracellularProperties2CaPools">
  <xs:complexContent>
    <xs:extension base="IntracellularProperties">
      </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IntracellularProperties2CaPools" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IntracellularProperties2CaPools
from neuroml.utils import component_factory

variable = component_factory(
    IntracellularProperties2CaPools,
    species: 'list of Species(s) (optional)' = None,
    resistivities: 'list of Resistivity(s) (optional)' = None,
)
```
````
`````

(schema:resistivity)=

## resistivity




<i>The resistivity, or specific axial resistance, of the cytoplasm.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**value**$  ${ref}`schema:dimensions:resistivity`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentGroup**$ 

````

````{tab-item} Schema
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

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Resistivity" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Resistivity
from neuroml.utils import component_factory

variable = component_factory(
    Resistivity,
    value: 'a Nml2Quantity_resistivity (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<resistivity value="0.1 kohm_cm"/>
```
```{code-block} xml
<resistivity value="0.1 kohm_cm"/>
```
```{code-block} xml
<resistivity value="0.1 kohm_cm"/>
```
````
`````

(schema:concentrationmodel)=

## concentrationModel




<i>Base for any model of an **ion** concentration which changes with time. Internal ( **concentration** ) and external ( **extConcentration** ) values for the concentration of the ion are given.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  ${ref}`schema:dimensions:concentration`
**extConcentration**$  ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**initialConcentration**$  ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  ${ref}`schema:dimensions:concentration`
**surfaceArea**$  ${ref}`schema:dimensions:area`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **concentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **concentration**)
: **extConcentration**: {ref}`schema:dimensions:concentration` &emsp;(exposed as **extConcentration**)









<i>**On Start**</i>
: **concentration** = initialConcentration
: **extConcentration** = initialExtConcentration








````
`````

(schema:decayingpoolconcentrationmodel)=

## decayingPoolConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of an intracellular buffering mechanism for **ion** ( currently hard Coded to be calcium, due to requirement for **iCa** ) which has a baseline level **restingConc** and tends to this value with time course **decayConstant.** The ion is assumed to occupy a shell inside the membrane of thickness **shellThickness.**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**decayConstant**$  ${ref}`schema:dimensions:time`
**restingConc**$  ${ref}`schema:dimensions:concentration`
**shellThickness**$  ${ref}`schema:dimensions:length`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**Faraday** = 96485.3C_per_mol$  $ {ref}`schema:dimensions:charge_per_mole`
**AREA_SCALE** = 1m2$  $ {ref}`schema:dimensions:area`
**LENGTH_SCALE** = 1m$  $ {ref}`schema:dimensions:length`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**extConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DecayingPoolConcentrationModel">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
      <xs:attribute name="restingConc" type="Nml2Quantity_concentration" use="required"/>
      <xs:attribute name="decayConstant" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="shellThickness" type="Nml2Quantity_length" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=DecayingPoolConcentrationModel" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import DecayingPoolConcentrationModel
from neuroml.utils import component_factory

variable = component_factory(
    DecayingPoolConcentrationModel,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    ion: 'a NmlId (required)' = None,
    resting_conc: 'a Nml2Quantity_concentration (required)' = None,
    decay_constant: 'a Nml2Quantity_time (required)' = None,
    shell_thickness: 'a Nml2Quantity_length (required)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:fixedfactorconcentrationmodel)=

## fixedFactorConcentrationModel




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion ( currently hard coded to be calcium, due to requirement for **iCa** ) which has a baseline level **restingConc** and tends to this value with time course **decayConstant.** A fixed factor **rho** is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**decayConstant**$  ${ref}`schema:dimensions:time`
**restingConc**$  ${ref}`schema:dimensions:concentration`
**rho**$  ${ref}`schema:dimensions:rho_factor`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**extConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="FixedFactorConcentrationModel">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="ion" type="NmlId" use="required">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
      <xs:attribute name="restingConc" type="Nml2Quantity_concentration" use="required"/>
      <xs:attribute name="decayConstant" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="rho" type="Nml2Quantity_rhoFactor" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=FixedFactorConcentrationModel" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import FixedFactorConcentrationModel
from neuroml.utils import component_factory

variable = component_factory(
    FixedFactorConcentrationModel,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    ion: 'a NmlId (required)' = None,
    resting_conc: 'a Nml2Quantity_concentration (required)' = None,
    decay_constant: 'a Nml2Quantity_time (required)' = None,
    rho: 'a Nml2Quantity_rhoFactor (required)' = None,
)
```
````
`````

(schema:fixedfactorconcentrationmodeltraub)=

## fixedFactorConcentrationModelTraub




extends {ref}`schema:concentrationmodel`



<i>Model of buffering of concentration of an ion ( currently hard coded to be calcium, due to requirement for **iCa** ) which has a baseline level **restingConc** and tends to this value with time course 1 / **beta.** A fixed factor **phi** is used to scale the incoming current *independently of the size of the compartment* to produce a concentration change. Not recommended for use in models other than Traub et al. 2005!</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**beta**$  ${ref}`schema:dimensions:per_time`
**phi**$  ${ref}`schema:dimensions:rho_factor`
**restingConc**$  ${ref}`schema:dimensions:concentration`

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

**concentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`
**extConcentration**$  *(from {ref}`schema:concentrationmodel`)* ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Requirements
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

````{tab-item} Dynamics



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
`````

(schema:species)=

## species




<i>Description of a chemical species identified by **ion,** which has internal, **concentration,** and external, **extConcentration** values for its concentration.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**initialConcentration**$  ${ref}`schema:dimensions:concentration`
**initialExtConcentration**$  ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**ion**$ 
**segmentGroup**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**concentrationModel**$  $ {ref}`schema:concentrationmodel`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**concentration**$  ${ref}`schema:dimensions:concentration`
**extConcentration**$  ${ref}`schema:dimensions:concentration`

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: CHILD INSTANCE: **concentrationModel**









<i>**Derived Variables**</i>
    : **concentration** =&nbsp;concentrationModel->concentration&emsp;(exposed as **concentration**)
    : **extConcentration** =&nbsp;concentrationModel->extConcentration&emsp;(exposed as **extConcentration**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Species">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:attribute name="concentrationModel" type="NmlId" use="required"/>
      <xs:attribute name="ion" type="NmlId" use="optional">
        <xs:annotation>
        </xs:annotation>
      </xs:attribute>
      <xs:attribute name="initialConcentration" type="Nml2Quantity_concentration" use="required"/>
      <xs:attribute name="initialExtConcentration" type="Nml2Quantity_concentration" use="required"/>
      <xs:attribute name="segmentGroup" type="NmlId" use="optional" default="all"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Species" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Species
from neuroml.utils import component_factory

variable = component_factory(
    Species,
    id: 'a NmlId (required)' = None,
    concentration_model: 'a NmlId (required)' = None,
    ion: 'a NmlId (optional)' = None,
    initial_concentration: 'a Nml2Quantity_concentration (required)' = None,
    initial_ext_concentration: 'a Nml2Quantity_concentration (required)' = None,
    segment_groups: 'a NmlId (optional)' = 'all',
)
```
````
`````

(schema:cell)=

## cell




extends *{ref}`schema:basecellmembpot`*



<i>Cell with  {ref}`schema:segment`s specified in a  {ref}`schema:morphology` element along with details on its  {ref}`schema:biophysicalproperties`. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v** of this cell represents the membrane potential in that isopotential segment.</i>


`````{tab-set}
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

**morphology**$ Should only be used if morphology element is outside the cell. This points to the id of the morphology. $ {ref}`schema:morphology`
**biophysicalProperties**$ Should only be used if biophysicalProperties element is outside the cell.  This points to the id of the biophysicalProperties $ {ref}`schema:biophysicalproperties`

```
````

````{tab-item} Exposures
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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Cell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:sequence>
        <xs:element name="morphology" type="Morphology" minOccurs="0"/>
        <xs:element name="biophysicalProperties" type="BiophysicalProperties" minOccurs="0"/>
      </xs:sequence>
      <xs:attribute name="morphology" type="NmlId" use="optional">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
      <xs:attribute name="biophysicalProperties" type="NmlId" use="optional">
        <xs:annotation>
            </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Cell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Cell
from neuroml.utils import component_factory

variable = component_factory(
    Cell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    morphology_attr: 'a NmlId (optional)' = None,
    biophysical_properties_attr: 'a NmlId (optional)' = None,
    morphology: 'a Morphology (optional)' = None,
    biophysical_properties: 'a BiophysicalProperties (optional)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<cell id="SpikingCell" metaid="HippoCA1Cell">
    <notes>A Simple Spiking cell for testing purposes</notes>
    <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
            <rdf:Description rdf:about="HippoCA1Cell">
                <bqbiol:is>
                    <rdf:Bag>
                        <rdf:li rdf:resource="urn:miriam:neurondb:258"/>
                    </rdf:Bag>
                </bqbiol:is>
            </rdf:Description>
        </rdf:RDF>
    </annotation>
    <morphology id="SpikingCell_morphology">
        <segment id="0" name="Soma">
            <proximal x="0" y="0" z="0" diameter="10"/>
            <distal x="10" y="0" z="0" diameter="10"/>
        </segment>
        <segment id="1" name="Dendrite1">
            <parent segment="0"/>
            <distal x="20" y="0" z="0" diameter="3"/>
        </segment>
        <segment id="2" name="Dendrite2">
            <parent segment="1"/>
            <distal x="30" y="0" z="0" diameter="1"/>
        </segment>
        <segment id="3" name="Spine1">
            <parent segment="2" fractionAlong="0.5"/>
            <proximal x="25" y="0" z="0" diameter="0.1"/>
            <distal x="25" y="0.2" z="0" diameter="0.1"/>
        </segment>
        <segmentGroup id="soma_group" neuroLexId="sao1044911821">
            <member segment="0"/>
        </segmentGroup>
        <segmentGroup id="dendrite_group" neuroLexId="sao1211023249">
            <member segment="1"/>
            <member segment="2"/>
            <member segment="3"/>
        </segmentGroup>
        <segmentGroup id="spines" neuroLexId="sao1145756102">
            <member segment="3"/>
        </segmentGroup>
    </morphology>
    <biophysicalProperties id="bio_cell">
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
</cell>
```
```{code-block} xml
<cell id="PyrCell" morphology="NeuroMorpho_PyrCell123" biophysicalProperties="PyrCellChanDist"/>
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
````
`````

(schema:cell2capools)=

## cell2CaPools




extends {ref}`schema:cell`



<i>Variant of cell with two independent Ca2+ pools. Cell with  {ref}`schema:segment`s specified in a  {ref}`schema:morphology` element along with details on its  {ref}`schema:biophysicalproperties`. NOTE: this can only be correctly simulated using jLEMS when there is a single segment in the cell, and **v** of this cell represents the membrane potential in that isopotential segment.</i>


`````{tab-set}
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

**biophysicalProperties2CaPools**$  $ {ref}`schema:biophysicalproperties2capools`

```
````

````{tab-item} Exposures
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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Cell2CaPools">
  <xs:complexContent>
    <xs:extension base="Cell">
      <xs:sequence>
        <xs:element name="biophysicalProperties2CaPools" type="BiophysicalProperties2CaPools" minOccurs="0"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Cell2CaPools" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Cell2CaPools
from neuroml.utils import component_factory

variable = component_factory(
    Cell2CaPools,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    morphology_attr: 'a NmlId (optional)' = None,
    biophysical_properties_attr: 'a NmlId (optional)' = None,
    morphology: 'a Morphology (optional)' = None,
    biophysical_properties: 'a BiophysicalProperties (optional)' = None,
    biophysical_properties2_ca_pools: 'a BiophysicalProperties2CaPools (optional)' = None,
)
```
````
`````

(schema:basecellmembpotcap)=

## *baseCellMembPotCap*




extends *{ref}`schema:basecellmembpot`*



<i>Any cell with a membrane potential **v** with voltage units and a membrane capacitance **C.** Also defines exposed value **iSyn** for current due to external synapses and **iMemb** for total transmembrane current ( usually channel currents plus **iSyn** ).</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane ${ref}`schema:dimensions:capacitance`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BaseCellMembPotCap">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="C" type="Nml2Quantity_capacitance" use="required">
        <xs:annotation>
          <xs:appinfo>
            <jxb:property name="Cap"/>
          </xs:appinfo>
        </xs:annotation>
      </xs:attribute>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseCellMembPotCap" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseCellMembPotCap
from neuroml.utils import component_factory

variable = component_factory(
    BaseCellMembPotCap,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    C: 'a Nml2Quantity_capacitance (required)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:baseiaf)=

## *baseIaf*




extends *{ref}`schema:basecellmembpot`*



<i>Base ComponentType for an integrate and fire cell which emits a spiking event at membrane potential **thresh** and and resets to **reset**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**reset**$ The value the membrane potential is reset to on spiking ${ref}`schema:dimensions:voltage`
**thresh**$ The membrane potential at which to emit a spiking event and reset voltage ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````
`````

(schema:iaftaucell)=

## iafTauCell




extends *{ref}`schema:baseiaf`*



<i>Integrate and fire cell which returns to its leak reversal potential of **leakReversal** with a time constant **tau**.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IafTauCell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="leakReversal" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="thresh" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="reset" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="tau" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafTauCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IafTauCell
from neuroml.utils import component_factory

variable = component_factory(
    IafTauCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    leak_reversal: 'a Nml2Quantity_voltage (required)' = None,
    thresh: 'a Nml2Quantity_voltage (required)' = None,
    reset: 'a Nml2Quantity_voltage (required)' = None,
    tau: 'a Nml2Quantity_time (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<iafTauCell id="iafTau" leakReversal="-50mV" thresh="-55mV" reset="-70mV" tau="30ms"/>
```
````
`````

(schema:iaftaurefcell)=

## iafTauRefCell




extends {ref}`schema:iaftaucell`



<i>Integrate and fire cell which returns to its leak reversal potential of **leakReversal** with a time course **tau.** It has a refractory period of **refract** after spiking.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IafTauRefCell">
  <xs:complexContent>
    <xs:extension base="IafTauCell">
      <xs:attribute name="refract" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafTauRefCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IafTauRefCell
from neuroml.utils import component_factory

variable = component_factory(
    IafTauRefCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    leak_reversal: 'a Nml2Quantity_voltage (required)' = None,
    thresh: 'a Nml2Quantity_voltage (required)' = None,
    reset: 'a Nml2Quantity_voltage (required)' = None,
    tau: 'a Nml2Quantity_time (required)' = None,
    refract: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<iafTauRefCell id="iafTauRef" leakReversal="-50mV" thresh="-55mV" reset="-70mV" tau="30ms" refract="5ms"/>
```
````
`````

(schema:baseiafcapcell)=

## *baseIafCapCell*




extends *{ref}`schema:basecellmembpotcap`*



<i>Base Type for all Integrate and Fire cells with a capacitance **C,** threshold **thresh** and reset membrane potential **reset**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**reset**$  ${ref}`schema:dimensions:voltage`
**thresh**$  ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````
`````

(schema:iafcell)=

## iafCell




extends *{ref}`schema:baseiafcapcell`*



<i>Integrate and fire cell with capacitance **C,** **leakConductance** and **leakReversal**.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IafCell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="leakReversal" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="thresh" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="reset" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="C" type="Nml2Quantity_capacitance" use="required"/>
      <xs:attribute name="leakConductance" type="Nml2Quantity_conductance" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IafCell
from neuroml.utils import component_factory

variable = component_factory(
    IafCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    leak_reversal: 'a Nml2Quantity_voltage (required)' = None,
    thresh: 'a Nml2Quantity_voltage (required)' = None,
    reset: 'a Nml2Quantity_voltage (required)' = None,
    C: 'a Nml2Quantity_capacitance (required)' = None,
    leak_conductance: 'a Nml2Quantity_conductance (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:iafrefcell)=

## iafRefCell




extends {ref}`schema:iafcell`



<i>Integrate and fire cell with capacitance **C,** **leakConductance,** **leakReversal** and refractory period **refract**.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IafRefCell">
  <xs:complexContent>
    <xs:extension base="IafCell">
      <xs:attribute name="refract" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IafRefCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IafRefCell
from neuroml.utils import component_factory

variable = component_factory(
    IafRefCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    leak_reversal: 'a Nml2Quantity_voltage (required)' = None,
    thresh: 'a Nml2Quantity_voltage (required)' = None,
    reset: 'a Nml2Quantity_voltage (required)' = None,
    C: 'a Nml2Quantity_capacitance (required)' = None,
    leak_conductance: 'a Nml2Quantity_conductance (required)' = None,
    refract: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<iafRefCell id="iafRef" leakReversal="-50mV" thresh="-55mV" reset="-70mV" C="0.2nF" leakConductance="0.01uS" refract="5ms"/>
```
````
`````

(schema:izhikevichcell)=

## izhikevichCell




extends *{ref}`schema:basecellmembpot`*



<i>Cell based on the 2003 model of Izhikevich, see http://izhikevich.org/publications/spikes.htm.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**a**$ Time scale of the recovery variable U $Dimensionless
**b**$ Sensitivity of U to the subthreshold fluctuations of the membrane potential V $Dimensionless
**c**$ After-spike reset value of V $Dimensionless
**d**$ After-spike increase to U $Dimensionless
**thresh**$ Spike threshold ${ref}`schema:dimensions:voltage`
**v0**$ Initial membrane potential ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**U**$ Membrane recovery variable $Dimensionless
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrentdl`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IzhikevichCell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="v0" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="thresh" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="a" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="b" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="c" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="d" type="Nml2Quantity_none" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IzhikevichCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IzhikevichCell
from neuroml.utils import component_factory

variable = component_factory(
    IzhikevichCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    v0: 'a Nml2Quantity_voltage (required)' = None,
    thresh: 'a Nml2Quantity_voltage (required)' = None,
    a: 'a Nml2Quantity_none (required)' = None,
    b: 'a Nml2Quantity_none (required)' = None,
    c: 'a Nml2Quantity_none (required)' = None,
    d: 'a Nml2Quantity_none (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<izhikevichCell id="izBurst" v0="-70mV" thresh="30mV" a="0.02" b="0.2" c="-50.0" d="2"/>
```
````
`````

(schema:izhikevich2007cell)=

## izhikevich2007Cell




extends *{ref}`schema:basecellmembpotcap`*



<i>Cell based on the modified Izhikevich model in Izhikevich 2007, Dynamical systems in neuroscience, MIT Press.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**a**$ Time scale of recovery variable u ${ref}`schema:dimensions:per_time`
**b**$ Sensitivity of recovery variable u to subthreshold fluctuations of membrane potential v ${ref}`schema:dimensions:conductance`
**c**$ After-spike reset value of v ${ref}`schema:dimensions:voltage`
**d**$ After-spike increase to u ${ref}`schema:dimensions:current`
**k**$  ${ref}`schema:dimensions:conductance_per_voltage`
**v0**$ Initial membrane potential ${ref}`schema:dimensions:voltage`
**vpeak**$ Peak action potential value ${ref}`schema:dimensions:voltage`
**vr**$ Resting membrane potential ${ref}`schema:dimensions:voltage`
**vt**$ Spike threshold ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**u**$ Membrane recovery variable ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Izhikevich2007Cell">
  <xs:complexContent>
    <xs:extension base="BaseCellMembPotCap">
      <xs:attribute name="v0" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="k" type="Nml2Quantity_conductancePerVoltage" use="required"/>
      <xs:attribute name="vr" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="vt" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="vpeak" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="a" type="Nml2Quantity_pertime" use="required"/>
      <xs:attribute name="b" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="c" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="d" type="Nml2Quantity_current" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Izhikevich2007Cell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Izhikevich2007Cell
from neuroml.utils import component_factory

variable = component_factory(
    Izhikevich2007Cell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    C: 'a Nml2Quantity_capacitance (required)' = None,
    v0: 'a Nml2Quantity_voltage (required)' = None,
    k: 'a Nml2Quantity_conductancePerVoltage (required)' = None,
    vr: 'a Nml2Quantity_voltage (required)' = None,
    vt: 'a Nml2Quantity_voltage (required)' = None,
    vpeak: 'a Nml2Quantity_voltage (required)' = None,
    a: 'a Nml2Quantity_pertime (required)' = None,
    b: 'a Nml2Quantity_conductance (required)' = None,
    c: 'a Nml2Quantity_voltage (required)' = None,
    d: 'a Nml2Quantity_current (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<izhikevich2007Cell id="iz2007RS" v0="-60mV" C="100 pF" k="0.7 nS_per_mV" vr="-60 mV" vt="-40 mV" vpeak="35 mV" a="0.03 per_ms" b="-2 nS" c="-50 mV" d="100 pA"/>
```
````
`````

(schema:adexiafcell)=

## adExIaFCell




extends *{ref}`schema:basecellmembpotcap`*



<i>Model based on Brette R and Gerstner W ( 2005 ) Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity. J Neurophysiol 94:3637-3642.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**EL**$ Leak reversal potential ${ref}`schema:dimensions:voltage`
**VT**$ Spike threshold ${ref}`schema:dimensions:voltage`
**a**$ Sub-threshold adaptation variable ${ref}`schema:dimensions:conductance`
**b**$ Spike-triggered adaptation variable ${ref}`schema:dimensions:current`
**delT**$ Slope factor ${ref}`schema:dimensions:voltage`
**gL**$ Leak conductance ${ref}`schema:dimensions:conductance`
**refract**$ Refractory period ${ref}`schema:dimensions:time`
**reset**$ Reset potential ${ref}`schema:dimensions:voltage`
**tauw**$ Adaptation time constant ${ref}`schema:dimensions:time`
**thresh**$ Spike detection threshold ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**w**$ Adaptation current ${ref}`schema:dimensions:current`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="AdExIaFCell">
  <xs:complexContent>
    <xs:extension base="BaseCellMembPotCap">
      <xs:attribute name="gL" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="EL" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="reset" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="VT" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="thresh" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="delT" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="tauw" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="refract" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="a" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="b" type="Nml2Quantity_current" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AdExIaFCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import AdExIaFCell
from neuroml.utils import component_factory

variable = component_factory(
    AdExIaFCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    C: 'a Nml2Quantity_capacitance (required)' = None,
    g_l: 'a Nml2Quantity_conductance (required)' = None,
    EL: 'a Nml2Quantity_voltage (required)' = None,
    reset: 'a Nml2Quantity_voltage (required)' = None,
    VT: 'a Nml2Quantity_voltage (required)' = None,
    thresh: 'a Nml2Quantity_voltage (required)' = None,
    del_t: 'a Nml2Quantity_voltage (required)' = None,
    tauw: 'a Nml2Quantity_time (required)' = None,
    refract: 'a Nml2Quantity_time (required)' = None,
    a: 'a Nml2Quantity_conductance (required)' = None,
    b: 'a Nml2Quantity_current (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<adExIaFCell id="adExBurst" C="281pF" gL="30nS" EL="-70.6mV" reset="-48.5mV" VT="-50.4mV" thresh="-40.4mV" refract="0ms" delT="2mV" tauw="40ms" a="4nS" b="0.08nA"/>
```
````
`````

(schema:fitzhughnagumocell)=

## fitzHughNagumoCell




extends *{ref}`schema:basecellmembpotdl`*



<i>Simple dimensionless model of spiking cell from FitzHugh and Nagumo. Superseded by **fitzHughNagumo1969Cell** ( See https://github.com/NeuroML/NeuroML2/issues/42 ).</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$  $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SEC** = 1s$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**V**$ Membrane potential *(from {ref}`schema:basecellmembpotdl`)* $Dimensionless
**W**$  $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **V**: Dimensionless &emsp;(exposed as **V**)
: **W**: Dimensionless &emsp;(exposed as **W**)










<i>**Time Derivatives**</i>
    : d **V** /dt = ( (V - ((V^3) / 3)) - W + I) / SEC
    : d **W** /dt = (0.08 * (V + 0.7 - 0.8 * W)) / SEC
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="FitzHughNagumoCell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="I" type="Nml2Quantity_none" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=FitzHughNagumoCell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import FitzHughNagumoCell
from neuroml.utils import component_factory

variable = component_factory(
    FitzHughNagumoCell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    I: 'a Nml2Quantity_none (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<fitzHughNagumoCell id="fn1" I="0.8"/>
```
````
`````

(schema:pinskyrinzelca3cell)=

## pinskyRinzelCA3Cell




extends *{ref}`schema:basecellmembpot`*



<i>Reduced CA3 cell model from Pinsky, P.F., Rinzel, J. Intrinsic and network rhythmogenesis in a reduced traub model for CA3 neurons. J Comput Neurosci 1, 39-60 ( 1994 ). See https://github.com/OpenSourceBrain/PinskyRinzelModel.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Constants
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**Cad**$  $Dimensionless
**ICad**$  ${ref}`schema:dimensions:currentDensity`
**Si**$  $Dimensionless
**Vd**$ Dendritic membrane potential ${ref}`schema:dimensions:voltage`
**Vs**$ Somatic membrane potential ${ref}`schema:dimensions:voltage`
**Wi**$  $Dimensionless
**cd**$  $Dimensionless
**hs**$  $Dimensionless
**ns**$  $Dimensionless
**qd**$  $Dimensionless
**sd**$  $Dimensionless
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="PinskyRinzelCA3Cell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="iSoma" type="Nml2Quantity_currentDensity" use="required"/>
      <xs:attribute name="iDend" type="Nml2Quantity_currentDensity" use="required"/>
      <xs:attribute name="gc" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gLs" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gLd" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gNa" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gKdr" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gCa" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gKahp" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gKC" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gNmda" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="gAmpa" type="Nml2Quantity_conductanceDensity" use="required"/>
      <xs:attribute name="eNa" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="eCa" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="eK" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="eL" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="qd0" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="pp" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="alphac" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="betac" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="cm" type="Nml2Quantity_specificCapacitance" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PinskyRinzelCA3Cell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import PinskyRinzelCA3Cell
from neuroml.utils import component_factory

variable = component_factory(
    PinskyRinzelCA3Cell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    i_soma: 'a Nml2Quantity_currentDensity (required)' = None,
    i_dend: 'a Nml2Quantity_currentDensity (required)' = None,
    gc: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_ls: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_ld: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_na: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_kdr: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_ca: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_kahp: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_kc: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_nmda: 'a Nml2Quantity_conductanceDensity (required)' = None,
    g_ampa: 'a Nml2Quantity_conductanceDensity (required)' = None,
    e_na: 'a Nml2Quantity_voltage (required)' = None,
    e_ca: 'a Nml2Quantity_voltage (required)' = None,
    e_k: 'a Nml2Quantity_voltage (required)' = None,
    e_l: 'a Nml2Quantity_voltage (required)' = None,
    qd0: 'a Nml2Quantity_none (required)' = None,
    pp: 'a Nml2Quantity_none (required)' = None,
    alphac: 'a Nml2Quantity_none (required)' = None,
    betac: 'a Nml2Quantity_none (required)' = None,
    cm: 'a Nml2Quantity_specificCapacitance (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<pinskyRinzelCA3Cell id="pr2A" iSoma="0.75 uA_per_cm2" iDend="0 uA_per_cm2" gc="2.1 mS_per_cm2" qd0="0" gLs="0.1 mS_per_cm2" gLd="0.1 mS_per_cm2" gNa="30 mS_per_cm2" gKdr="15 mS_per_cm2" gCa="10 mS_per_cm2" gKahp="0.8 mS_per_cm2" gKC="15 mS_per_cm2" eNa="60 mV" eCa="80 mV" eK="-75 mV" eL="-60 mV" pp="0.5" cm="3 uF_per_cm2" alphac="2" betac="0.1" gNmda="0 mS_per_cm2" gAmpa="0 mS_per_cm2"/>
```
````
`````

(schema:hindmarshrose1984cell)=

## hindmarshRose1984Cell




extends *{ref}`schema:basecellmembpotcap`*



<i>The Hindmarsh Rose model is a simplified point cell model which captures complex firing patterns of single neurons, such as periodic and chaotic bursting. It has a fast spiking subsystem, which is a generalization of the FitzHugh-Nagumo system, coupled to a slower subsystem which allows the model to fire bursts. The dynamical variables x, y, z correspond to the membrane potential, a recovery variable, and a slower adaptation current, respectively. See Hindmarsh J. L., and Rose R. M. ( 1984 ) A model of neuronal bursting using three coupled first order differential equations. Proc. R. Soc. London, Ser. B 221:87–102.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**C**$ Total capacitance of the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:capacitance`
**a**$ cubic term in x nullcline $Dimensionless
**b**$ quadratic term in x nullcline $Dimensionless
**c**$ constant term in y nullcline $Dimensionless
**d**$ quadratic term in y nullcline $Dimensionless
**r**$ timescale separation between slow and fast subsystem (r greater than 0; r much less than 1) $Dimensionless
**s**$ related to adaptation $Dimensionless
**v_scaling**$ scaling of x for physiological membrane potential ${ref}`schema:dimensions:voltage`
**x0**$  $Dimensionless
**x1**$ related to the system's resting potential $Dimensionless
**y0**$  $Dimensionless
**z0**$  $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**chi**$  $Dimensionless
**iMemb**$ Total current crossing the cell membrane *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**iSyn**$ Total current due to synaptic inputs *(from {ref}`schema:basecellmembpotcap`)* ${ref}`schema:dimensions:current`
**phi**$  $Dimensionless
**rho**$  $Dimensionless
**spiking**$  $Dimensionless
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**x**$  $Dimensionless
**y**$  $Dimensionless
**z**$  $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **y**: Dimensionless &emsp;(exposed as **y**)
: **z**: Dimensionless &emsp;(exposed as **z**)
: **spiking**: Dimensionless &emsp;(exposed as **spiking**)









<i>**On Start**</i>
: **v** = x0 * v_scaling
: **y** = y0
: **z** = z0



<i>**On Conditions**</i>

: IF v &gt; 0 AND spiking &lt; 0.5 THEN
: &emsp;&emsp;&emsp;**spiking** = 1
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**

: IF v &lt; 0 THEN
: &emsp;&emsp;&emsp;**spiking** = 0





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **x** =&nbsp;v / v_scaling&emsp;(exposed as **x**)
    : **phi** =&nbsp;y - a * x^3 + b * x^2&emsp;(exposed as **phi**)
    : **chi** =&nbsp;c - d * x^2 - y&emsp;(exposed as **chi**)
    : **rho** =&nbsp;s * ( x - x1 ) - z&emsp;(exposed as **rho**)
    : **iMemb** =&nbsp;(C * (v_scaling * (phi - z) / MSEC)) + iSyn&emsp;(exposed as **iMemb**)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = iMemb/C
    : d **y** /dt = chi / MSEC
    : d **z** /dt = r * rho / MSEC
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HindmarshRose1984Cell">
  <xs:complexContent>
    <xs:extension base="BaseCellMembPotCap">
      <xs:attribute name="a" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="b" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="c" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="d" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="s" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="x1" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="r" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="x0" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="y0" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="z0" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="v_scaling" type="Nml2Quantity_voltage" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=HindmarshRose1984Cell" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import HindmarshRose1984Cell
from neuroml.utils import component_factory

variable = component_factory(
    HindmarshRose1984Cell,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    C: 'a Nml2Quantity_capacitance (required)' = None,
    a: 'a Nml2Quantity_none (required)' = None,
    b: 'a Nml2Quantity_none (required)' = None,
    c: 'a Nml2Quantity_none (required)' = None,
    d: 'a Nml2Quantity_none (required)' = None,
    s: 'a Nml2Quantity_none (required)' = None,
    x1: 'a Nml2Quantity_none (required)' = None,
    r: 'a Nml2Quantity_none (required)' = None,
    x0: 'a Nml2Quantity_none (required)' = None,
    y0: 'a Nml2Quantity_none (required)' = None,
    z0: 'a Nml2Quantity_none (required)' = None,
    v_scaling: 'a Nml2Quantity_voltage (required)' = None,
)
```
````
`````
