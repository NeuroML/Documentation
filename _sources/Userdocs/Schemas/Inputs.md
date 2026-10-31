
(schema:inputs_)=
# Inputs

**A number of ComponentTypes for providing spiking ( e.g.  {ref}`schema:spikegeneratorpoisson`,  {ref}`schema:spikearray` ) and current inputs ( e.g.  {ref}`schema:pulsegenerator`,  {ref}`schema:voltageclamp`,  {ref}`schema:timedsynapticinput`,  {ref}`schema:poissonfiringsynapse` ) to other ComponentTypes**

---


Original ComponentType definitions: [Inputs.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Inputs.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basepointcurrent)=

## *basePointCurrent*




extends *{ref}`schema:basestandalone`*



<i>Base type for all ComponentTypes which produce a current **i** ( with dimension current ).</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType ${ref}`schema:dimensions:current`

```
````
`````

(schema:basevoltagedeppointcurrent)=

## *baseVoltageDepPointCurrent*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all ComponentTypes which produce a current **i** ( with dimension current ) and require a voltage **v** exposed on the parent Component, which would often be the membrane potential of a Component extending  {ref}`schema:basecellmembpot`.</i>


`````{tab-set}
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

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed ${ref}`schema:dimensions:voltage`

```
````
`````

(schema:basevoltagedeppointcurrentspiking)=

## *baseVoltageDepPointCurrentSpiking*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for all ComponentTypes which produce a current **i,** require a membrane potential **v** exposed on the parent and emit spikes ( on a port **spike** ). The exposed variable **tsince** can be used for plotting the time since the Component has spiked last.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**tsince**$ Time since the last spike was emitted ${ref}`schema:dimensions:time`

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted$Direction: out

```
````
`````

(schema:basepointcurrentdl)=

## *basePointCurrentDL*




<i>Base type for all ComponentTypes which produce a dimensionless current **I.** There are many dimensionless equivalents of all the core current producing ComponentTypes such as  {ref}`schema:pulsegenerator` /  {ref}`schema:pulsegeneratordl`,  {ref}`schema:sinegenerator` /  {ref}`schema:sinegeneratordl` and  {ref}`schema:rampgenerator` /  {ref}`schema:rampgeneratordl`.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType $Dimensionless

```
````
`````

(schema:basevoltagedeppointcurrentdl)=

## *baseVoltageDepPointCurrentDL*




extends *{ref}`schema:basepointcurrentdl`*



<i>Base type for all ComponentTypes which produce a dimensionless current **I** and require a dimensionless membrane potential **V** exposed on the parent Component.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**V**$ The current may vary with the dimensionless voltage exposed by the ComponentType on which this is placed $Dimensionless

```
````
`````

(schema:basespikesource)=

## *baseSpikeSource*




<i>Base for any ComponentType whose main purpose is to emit spikes ( on a port **spike** ). The exposed variable **tsince** can be used for plotting the time since the Component has spiked last.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tsince**$ Time since the last spike was emitted ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted$Direction: out

```
````
`````

(schema:spikegenerator)=

## spikeGenerator




extends *{ref}`schema:basespikesource`*



<i>Simple generator of spikes at a regular interval set by **period**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**period**$ Time between spikes. The first spike will be emitted after this time. ${ref}`schema:dimensions:time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$ A useful constant for use as a non zero time increment $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tnext**$ When the next spike should ideally be emitted (dt permitting) ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnext**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnext**)









<i>**On Start**</i>
: **tsince** = 0
: **tnext** = period



<i>**On Conditions**</i>

: IF tnext - t &lt; SMALL_TIME THEN
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;**tnext** = tnext+period
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnext** /dt = 0
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeGenerator">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="period" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGenerator" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeGenerator
from neuroml.utils import component_factory

variable = component_factory(
    SpikeGenerator,
    id: 'a NonNegativeInteger (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    period: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spikeGenerator id="spikeGenRegular" period="20 ms"/>
```
````
`````

(schema:spikegeneratorrandom)=

## spikeGeneratorRandom




extends *{ref}`schema:basespikesource`*



<i>Generator of spikes with a random interspike interval of at least **minISI** and at most **maxISI**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**maxISI**$ Maximum interspike interval ${ref}`schema:dimensions:time`
**minISI**$ Minimum interspike interval ${ref}`schema:dimensions:time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$ Required for converting time values to/from dimensionless quantities $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**isi**$ The interval until the next spike ${ref}`schema:dimensions:time`
**tnext**$ When the next spike should ideally be emitted (dt permitting) ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnext**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnext**)
: **isi**: {ref}`schema:dimensions:time` &emsp;(exposed as **isi**)









<i>**On Start**</i>
: **tsince** = 0
: **isi** = minISI + MSEC * random((maxISI - minISI) / MSEC)
: **tnext** = isi



<i>**On Conditions**</i>

: IF t &gt; tnext THEN
: &emsp;&emsp;&emsp;**isi** = minISI + MSEC * random((maxISI - minISI) / MSEC)
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;**tnext** = tnext+isi
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnext** /dt = 0
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeGeneratorRandom">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="maxISI" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="minISI" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGeneratorRandom" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeGeneratorRandom
from neuroml.utils import component_factory

variable = component_factory(
    SpikeGeneratorRandom,
    id: 'a NonNegativeInteger (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    max_isi: 'a Nml2Quantity_time (required)' = None,
    min_isi: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spikeGeneratorRandom id="spikeGenRandom" minISI="10 ms" maxISI="30 ms"/>
```
````
`````

(schema:spikegeneratorpoisson)=

## spikeGeneratorPoisson




extends *{ref}`schema:basespikesource`*



<i>Generator of spikes whose ISI is distributed according to an exponential PDF with scale: 1 / **averageRate**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$ The average rate at which spikes are emitted ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**isi**$ The interval until the next spike ${ref}`schema:dimensions:time`
**tnextIdeal**$ This is the ideal/perfect next spike time, based on a newly generated isi, but dt precision will mean that it's usually slightly later than this ${ref}`schema:dimensions:time`
**tnextUsed**$ This is the next spike time for practical purposes, ensuring that it's later than the current time ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnextIdeal**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextIdeal**)
: **tnextUsed**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextUsed**)
: **isi**: {ref}`schema:dimensions:time` &emsp;(exposed as **isi**)









<i>**On Start**</i>
: **tsince** = 0
: **isi** = -1 * log(random(1)) / averageRate
: **tnextIdeal** = isi
: **tnextUsed** = isi



<i>**On Conditions**</i>

: IF t &gt; tnextUsed THEN
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;**isi** = -1 * log(random(1)) / averageRate
: &emsp;&emsp;&emsp;**tnextIdeal** = (tnextIdeal+isi)
: &emsp;&emsp;&emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeGeneratorPoisson">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="averageRate" type="Nml2Quantity_pertime" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGeneratorPoisson" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeGeneratorPoisson
from neuroml.utils import component_factory

variable = component_factory(
    SpikeGeneratorPoisson,
    id: 'a NonNegativeInteger (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    average_rate: 'a Nml2Quantity_pertime (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spikeGeneratorPoisson id="spikeGenPoisson" averageRate="50 Hz"/>
```
````
`````

(schema:spikegeneratorrefpoisson)=

## spikeGeneratorRefPoisson




extends {ref}`schema:spikegeneratorpoisson`



<i>Generator of spikes whose ISI distribution is the maximum entropy distribution over [ **minimumISI,** +infinity ) with mean: 1 / **averageRate**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$ The average rate at which spikes are emitted *(from {ref}`schema:spikegeneratorpoisson`)* ${ref}`schema:dimensions:per_time`
**minimumISI**$ The minimum interspike interval ${ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageIsi**$ The average interspike interval ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**averageIsi** = 1 / averageRate

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**isi**$ The interval until the next spike *(from {ref}`schema:spikegeneratorpoisson`)* ${ref}`schema:dimensions:time`
**tnextIdeal**$ This is the ideal/perfect next spike time, based on a newly generated isi, but dt precision will mean that it's usually slightly later than this *(from {ref}`schema:spikegeneratorpoisson`)* ${ref}`schema:dimensions:time`
**tnextUsed**$ This is the next spike time for practical purposes, ensuring that it's later than the current time *(from {ref}`schema:spikegeneratorpoisson`)* ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnextIdeal**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextIdeal**)
: **tnextUsed**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextUsed**)
: **isi**: {ref}`schema:dimensions:time` &emsp;(exposed as **isi**)









<i>**On Start**</i>
: **tsince** = 0
: **isi** = minimumISI - (averageIsi-minimumISI) * log(random(1))
: **tnextIdeal** = isi
: **tnextUsed** = isi



<i>**On Conditions**</i>

: IF t &gt; tnextUsed THEN
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;**isi** = minimumISI - (averageIsi-minimumISI) * log(random(1))
: &emsp;&emsp;&emsp;**tnextIdeal** = (tnextIdeal+isi)
: &emsp;&emsp;&emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeGeneratorRefPoisson">
  <xs:complexContent>
    <xs:extension base="SpikeGeneratorPoisson">
      <xs:attribute name="minimumISI" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGeneratorRefPoisson" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeGeneratorRefPoisson
from neuroml.utils import component_factory

variable = component_factory(
    SpikeGeneratorRefPoisson,
    id: 'a NonNegativeInteger (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    average_rate: 'a Nml2Quantity_pertime (required)' = None,
    minimum_isi: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spikeGeneratorRefPoisson id="spikeGenRefPoisson" averageRate="50 Hz" minimumISI="10 ms"/>
```
````
`````

(schema:poissonfiringsynapse)=

## poissonFiringSynapse




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Poisson spike generator firing at **averageRate,** which is connected to single **synapse** that is triggered every time a spike is generated, producing an input current. See also  {ref}`schema:transientpoissonfiringsynapse`.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$ The average rate at which spikes are emitted ${ref}`schema:dimensions:per_time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageIsi**$ The average interspike interval ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**averageIsi** = 1 / averageRate

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**spikeTarget**$ The target of the spikes, i.e. the synapse

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**isi**$ The interval until the next spike ${ref}`schema:dimensions:time`
**tnextIdeal**$  ${ref}`schema:dimensions:time`
**tnextUsed**$  ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)* ${ref}`schema:dimensions:time`

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in
**spike**$ Port on which spikes are emitted$Direction: out
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)*$Direction: out

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **spikeTarget** AS **b**
: CHILD INSTANCE: **synapse**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnextIdeal**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextIdeal**)
: **tnextUsed**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextUsed**)
: **isi**: {ref}`schema:dimensions:time` &emsp;(exposed as **isi**)









<i>**On Start**</i>
: **tsince** = 0
: **isi** = - averageIsi * log(random(1))
: **tnextIdeal** = isi
: **tnextUsed** = isi



<i>**On Conditions**</i>

: IF t &gt; tnextUsed THEN
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;**isi** = - averageIsi * log(1 - random(1))
: &emsp;&emsp;&emsp;**tnextIdeal** = (tnextIdeal+isi)
: &emsp;&emsp;&emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapse->i
    : **i** =&nbsp;weight * iSyn&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="PoissonFiringSynapse">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="averageRate" type="Nml2Quantity_pertime" use="required"/>
      <xs:attribute name="synapse" type="xs:string" use="required"/>
      <xs:attribute name="spikeTarget" type="xs:string" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PoissonFiringSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import PoissonFiringSynapse
from neuroml.utils import component_factory

variable = component_factory(
    PoissonFiringSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    average_rate: 'a Nml2Quantity_pertime (required)' = None,
    synapse: 'a string (required)' = None,
    spike_target: 'a string (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<poissonFiringSynapse id="poissonFiringSyn" averageRate="10 Hz" synapse="synInput" spikeTarget="./synInput"/>
```
````
`````

(schema:transientpoissonfiringsynapse)=

## transientPoissonFiringSynapse




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Poisson spike generator firing at **averageRate** after a **delay** and for a **duration,** connected to single **synapse** that is triggered every time a spike is generated, providing an input current. Similar to ComponentType  {ref}`schema:poissonfiringsynapse`.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$  ${ref}`schema:dimensions:per_time`
**delay**$  ${ref}`schema:dimensions:time`
**duration**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`
**LONG_TIME** = 1e9hour$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageIsi**$  ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**averageIsi** = 1 / averageRate

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**spikeTarget**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**isi**$  ${ref}`schema:dimensions:time`
**tnextIdeal**$  ${ref}`schema:dimensions:time`
**tnextUsed**$  ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)* ${ref}`schema:dimensions:time`

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in
**spike**$ Port on which spikes are emitted$Direction: out
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)*$Direction: out

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **spikeTarget** AS **b**
: CHILD INSTANCE: **synapse**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnextIdeal**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextIdeal**)
: **tnextUsed**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnextUsed**)
: **isi**: {ref}`schema:dimensions:time` &emsp;(exposed as **isi**)









<i>**On Start**</i>
: **tsince** = 0
: **isi** = - averageIsi * log(1 - random(1))  +delay
: **tnextIdeal** = isi
: **tnextUsed** = isi



<i>**On Conditions**</i>

: IF t &gt; tnextUsed THEN
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;**isi** = - averageIsi * log(1 - random(1))
: &emsp;&emsp;&emsp;**tnextIdeal** = (tnextIdeal+isi) + H(((t+isi) - (delay+duration))/duration)*LONG_TIME
: &emsp;&emsp;&emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapse->i
    : **i** =&nbsp;weight * iSyn&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="TransientPoissonFiringSynapse">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="averageRate" type="Nml2Quantity_pertime" use="required"/>
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="synapse" type="xs:string" use="required"/>
      <xs:attribute name="spikeTarget" type="xs:string" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=TransientPoissonFiringSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import TransientPoissonFiringSynapse
from neuroml.utils import component_factory

variable = component_factory(
    TransientPoissonFiringSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    average_rate: 'a Nml2Quantity_pertime (required)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    synapse: 'a string (required)' = None,
    spike_target: 'a string (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<transientPoissonFiringSynapse id="transPoissonFiringSyn" delay="50ms" duration="50ms" averageRate="300 Hz" synapse="synInputFast" spikeTarget="./synInputFast"/>
```
```{code-block} xml
<transientPoissonFiringSynapse id="transPoissonFiringSyn2" delay="50ms" duration="500ms" averageRate="10 Hz" synapse="synInputFastTwo" spikeTarget="./synInputFastTwo"/>
```
````
`````

(schema:timedsynapticinput)=

## timedSynapticInput




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Spike array connected to a single **synapse,** producing a current triggered by each  {ref}`schema:spike` in the array.</i>


`````{tab-set}
````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**spikeTarget**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**spikes**$  $ {ref}`schema:spike`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)* ${ref}`schema:dimensions:time`

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This will receive events from the children$Direction: in
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)*$Direction: out

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **spikeTarget** AS **b**
: CHILD INSTANCE: **synapse**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapse->i
    : **i** =&nbsp;weight * iSyn&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="TimedSynapticInput">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="spike" type="Spike" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="synapse" type="NmlId" use="required"/>
      <xs:attribute name="spikeTarget" type="xs:string" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=TimedSynapticInput" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import TimedSynapticInput
from neuroml.utils import component_factory

variable = component_factory(
    TimedSynapticInput,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    synapse: 'a NmlId (required)' = None,
    spike_target: 'a string (required)' = None,
    spikes: 'list of Spike(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<timedSynapticInput id="synTrain" synapse="synInputFastTwo" spikeTarget="./synInputFastTwo">
    <spike id="0" time="2 ms"/>
    <spike id="1" time="15 ms"/>
    <spike id="2" time="27 ms"/>
    <spike id="3" time="40 ms"/>
    <spike id="4" time="45 ms"/>
    <spike id="5" time="50 ms"/>
    <spike id="6" time="52 ms"/>
    <spike id="7" time="54 ms"/>
    <spike id="8" time="54.5 ms"/>
    <spike id="9" time="54.6 ms"/>
    <spike id="10" time="54.7 ms"/>
    <spike id="11" time="54.8 ms"/>
    <spike id="12" time="54.9 ms"/>
    <spike id="13" time="55 ms"/>
    <spike id="14" time="55.1 ms"/>
    <spike id="15" time="55.2 ms"/>
</timedSynapticInput>
```
````
`````

(schema:spikearray)=

## spikeArray




extends *{ref}`schema:basespikesource`*



<i>Set of spike ComponentTypes, each emitting one spike at a certain time. Can be used to feed a predetermined spike train into a cell.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**spikes**$  $ {ref}`schema:spike`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This will receive events from the children$Direction: in
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)









<i>**On Start**</i>
: **tsince** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeArray">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="spike" type="Spike" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeArray" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeArray
from neuroml.utils import component_factory

variable = component_factory(
    SpikeArray,
    id: 'a NonNegativeInteger (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    spikes: 'list of Spike(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spikeArray id="spkArr">
    <spike id="0" time="50 ms"/>
    <spike id="1" time="100 ms"/>
    <spike id="2" time="150 ms"/>
    <spike id="3" time="155 ms"/>
    <spike id="4" time="250 ms"/>
</spikeArray>
```
````
`````

(schema:spike)=

## spike




extends *{ref}`schema:basespikesource`*



<i>Emits a single spike at the specified **time**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**time**$ Time at which to emit one spike event ${ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spiked**$ 0 signals not yet spiked, 1 signals has spiked $Dimensionless
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **parent** AS **b**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **spiked**: Dimensionless &emsp;(exposed as **spiked**)









<i>**On Start**</i>
: **tsince** = 0



<i>**On Conditions**</i>

: IF (t &gt;= time) AND (spiked = 0) THEN
: &emsp;&emsp;&emsp;**spiked** = 1
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Spike">
  <xs:complexContent>
    <xs:extension base="BaseNonNegativeIntegerId">
      <xs:attribute name="time" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Spike" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Spike
from neuroml.utils import component_factory

variable = component_factory(
    Spike,
    id: 'a NonNegativeInteger (required)' = None,
    time: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<spike id="0" time="50 ms"/>
```
```{code-block} xml
<spike id="1" time="100 ms"/>
```
```{code-block} xml
<spike id="2" time="150 ms"/>
```
````
`````

(schema:pulsegenerator)=

## pulseGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a constant current pulse of a certain **amplitude** for a specified **duration** after a **delay.** Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**amplitude**$ Amplitude of current pulse ${ref}`schema:dimensions:current`
**delay**$ Delay before change in current. Current is zero  prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is zero after delay + duration. ${ref}`schema:dimensions:time`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note: this is not used here. Will be removed in future$Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**i** = 0

: IF t &gt;= delay AND t &lt; duration + delay THEN
: &emsp;&emsp;&emsp;**i** = weight * amplitude

: IF t &gt;= duration + delay THEN
: &emsp;&emsp;&emsp;**i** = 0








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="PulseGenerator">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="amplitude" type="Nml2Quantity_current" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PulseGenerator" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import PulseGenerator
from neuroml.utils import component_factory

variable = component_factory(
    PulseGenerator,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    amplitude: 'a Nml2Quantity_current (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<pulseGenerator id="pulseGen1" delay="50ms" duration="200ms" amplitude="0.0032nA"/>
```
```{code-block} xml
<pulseGenerator id="pulseGen2" delay="400ms" duration="200ms" amplitude="0.0020nA"/>
```
```{code-block} xml
<pulseGenerator id="pulseGen3" delay="700ms" duration="200ms" amplitude="0.0010nA"/>
```
````
`````

(schema:compoundinput)=

## compoundInput




extends *{ref}`schema:basepointcurrent`*



<i>Generates a current which is the sum of all its child  {ref}`schema:basepointcurrent` element, e.g. can be a combination of  {ref}`schema:pulsegenerator`,  {ref}`schema:sinegenerator` elements producing a single **i.** Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**currents**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tab-item} Dynamics












<i>**On Events**</i>

: EVENT IN on port: **in**





<i>**Derived Variables**</i>
    : **i_total** =&nbsp;currents[*]->i(reduce method: add)
    : **i** =&nbsp;weight * i_total&emsp;(exposed as **i**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="CompoundInput">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="pulseGenerator" type="PulseGenerator" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="sineGenerator" type="SineGenerator" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="rampGenerator" type="RampGenerator" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=CompoundInput" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import CompoundInput
from neuroml.utils import component_factory

variable = component_factory(
    CompoundInput,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    pulse_generators: 'list of PulseGenerator(s) (optional)' = None,
    sine_generators: 'list of SineGenerator(s) (optional)' = None,
    ramp_generators: 'list of RampGenerator(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<compoundInput id="ci0">
    <pulseGenerator id="pg1" delay="50ms" duration="200ms" amplitude=".8 nA"/>
    <pulseGenerator id="pg2" delay="100ms" duration="100ms" amplitude=".4 nA"/>
    <sineGenerator id="sg0" phase="0" delay="125ms" duration="50ms" amplitude=".4nA" period="25ms"/>
</compoundInput>
```
````
`````

(schema:compoundinputdl)=

## compoundInputDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Generates a current which is the sum of all its child  {ref}`schema:basepointcurrentdl` elements, e.g. can be a combination of  {ref}`schema:pulsegeneratordl`,  {ref}`schema:sinegeneratordl` elements producing a single **i.** Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**currents**$  $ {ref}`schema:basepointcurrentdl`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tab-item} Dynamics












<i>**On Events**</i>

: EVENT IN on port: **in**





<i>**Derived Variables**</i>
    : **I_total** =&nbsp;currents[*]->I(reduce method: add)
    : **I** =&nbsp;weight * I_total&emsp;(exposed as **I**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="CompoundInputDL">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="pulseGeneratorDL" type="PulseGeneratorDL" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="sineGeneratorDL" type="SineGeneratorDL" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="rampGeneratorDL" type="RampGeneratorDL" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=CompoundInputDL" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import CompoundInputDL
from neuroml.utils import component_factory

variable = component_factory(
    CompoundInputDL,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    pulse_generator_dls: 'list of PulseGeneratorDL(s) (optional)' = None,
    sine_generator_dls: 'list of SineGeneratorDL(s) (optional)' = None,
    ramp_generator_dls: 'list of RampGeneratorDL(s) (optional)' = None,
)
```
````
`````

(schema:pulsegeneratordl)=

## pulseGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of  {ref}`schema:pulsegenerator`. Generates a constant current pulse of a certain **amplitude** for a specified **duration** after a **delay.** Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**amplitude**$ Amplitude of current pulse $Dimensionless
**delay**$ Delay before change in current. Current is zero  prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is zero after delay + duration. ${ref}`schema:dimensions:time`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **I**: Dimensionless &emsp;(exposed as **I**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**I** = 0

: IF t &gt;= delay AND t &lt; duration + delay THEN
: &emsp;&emsp;&emsp;**I** = weight * amplitude

: IF t &gt;= duration + delay THEN
: &emsp;&emsp;&emsp;**I** = 0








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="PulseGeneratorDL">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="amplitude" type="Nml2Quantity_none" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PulseGeneratorDL" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import PulseGeneratorDL
from neuroml.utils import component_factory

variable = component_factory(
    PulseGeneratorDL,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    amplitude: 'a Nml2Quantity_current (required)' = None,
)
```
````
`````

(schema:sinegenerator)=

## sineGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a sinusoidally varying current after a time **delay,** for a fixed **duration.** The **period** and maximum **amplitude** of the current can be set as well as the **phase** at which to start. Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**amplitude**$ Maximum amplitude of current ${ref}`schema:dimensions:current`
**delay**$ Delay before change in current. Current is zero  prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is zero after delay + duration. ${ref}`schema:dimensions:time`
**period**$ Time period of oscillation ${ref}`schema:dimensions:time`
**phase**$ Phase (between 0 and 2*pi) at which to start the varying current (i.e. at time given by delay) $Dimensionless

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**i** = 0

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;&emsp;&emsp;**i** = weight * amplitude * sin(phase + (2 * 3.14159265 * (t-delay)/period) )

: IF t &gt;= duration+delay THEN
: &emsp;&emsp;&emsp;**i** = 0








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SineGenerator">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="phase" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="amplitude" type="Nml2Quantity_current" use="required"/>
      <xs:attribute name="period" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SineGenerator" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SineGenerator
from neuroml.utils import component_factory

variable = component_factory(
    SineGenerator,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    phase: 'a Nml2Quantity_none (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    amplitude: 'a Nml2Quantity_current (required)' = None,
    period: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<sineGenerator id="sg0" phase="0" delay="50ms" duration="200ms" amplitude="1.4nA" period="50ms"/>
```
```{code-block} xml
<sineGenerator id="sg0" phase="0" delay="125ms" duration="50ms" amplitude=".4nA" period="25ms"/>
```
````
`````

(schema:sinegeneratordl)=

## sineGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of  {ref}`schema:sinegenerator`. Generates a sinusoidally varying current after a time **delay,** for a fixed **duration.** The **period** and maximum **amplitude** of the current can be set as well as the **phase** at which to start. Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**amplitude**$ Maximum amplitude of current $Dimensionless
**delay**$ Delay before change in current. Current is zero  prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is zero after delay + duration. ${ref}`schema:dimensions:time`
**period**$ Time period of oscillation ${ref}`schema:dimensions:time`
**phase**$ Phase (between 0 and 2*pi) at which to start the varying current (i.e. at time given by delay) $Dimensionless

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **I**: Dimensionless &emsp;(exposed as **I**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**I** = 0

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;&emsp;&emsp;**I** = weight * amplitude * sin(phase + (2 * 3.14159265 * (t-delay)/period) )

: IF t &gt;= duration+delay THEN
: &emsp;&emsp;&emsp;**I** = 0








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SineGeneratorDL">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="phase" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="amplitude" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="period" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SineGeneratorDL" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SineGeneratorDL
from neuroml.utils import component_factory

variable = component_factory(
    SineGeneratorDL,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    phase: 'a Nml2Quantity_none (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    amplitude: 'a Nml2Quantity_current (required)' = None,
    period: 'a Nml2Quantity_time (required)' = None,
)
```
````
`````

(schema:rampgenerator)=

## rampGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a ramping current after a time **delay,** for a fixed **duration.** During this time the current steadily changes from **startAmplitude** to **finishAmplitude.** Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**baselineAmplitude**$ Amplitude of current before time delay, and after time delay + duration ${ref}`schema:dimensions:current`
**delay**$ Delay before change in current. Current is baselineAmplitude prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is baselineAmplitude after delay + duration. ${ref}`schema:dimensions:time`
**finishAmplitude**$ Amplitude of linearly varying current at time delay + duration ${ref}`schema:dimensions:current`
**startAmplitude**$ Amplitude of linearly varying current at time delay ${ref}`schema:dimensions:current`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)









<i>**On Start**</i>
: **i** = baselineAmplitude


<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**i** = weight * baselineAmplitude

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;&emsp;&emsp;**i** = weight * (startAmplitude + (finishAmplitude - startAmplitude) * (t - delay) / (duration))

: IF t &gt;= duration+delay THEN
: &emsp;&emsp;&emsp;**i** = weight * baselineAmplitude








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="RampGenerator">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="startAmplitude" type="Nml2Quantity_current" use="required"/>
      <xs:attribute name="finishAmplitude" type="Nml2Quantity_current" use="required"/>
      <xs:attribute name="baselineAmplitude" type="Nml2Quantity_current" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=RampGenerator" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import RampGenerator
from neuroml.utils import component_factory

variable = component_factory(
    RampGenerator,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    start_amplitude: 'a Nml2Quantity_current (required)' = None,
    finish_amplitude: 'a Nml2Quantity_current (required)' = None,
    baseline_amplitude: 'a Nml2Quantity_current (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<rampGenerator id="rg0" delay="50ms" duration="200ms" startAmplitude="0.5nA" finishAmplitude="4nA" baselineAmplitude="0nA"/>
```
````
`````

(schema:rampgeneratordl)=

## rampGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of  {ref}`schema:rampgenerator`. Generates a ramping current after a time **delay,** for a fixed **duration.** During this time the dimensionless current steadily changes from **startAmplitude** to **finishAmplitude.** Scaled by **weight,** if set.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**baselineAmplitude**$ Amplitude of current before time delay, and after time delay + duration $Dimensionless
**delay**$ Delay before change in current. Current is baselineAmplitude prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is baselineAmplitude after delay + duration. ${ref}`schema:dimensions:time`
**finishAmplitude**$ Amplitude of linearly varying current at time delay + duration $Dimensionless
**startAmplitude**$ Amplitude of linearly varying current at time delay $Dimensionless

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **I**: Dimensionless &emsp;(exposed as **I**)









<i>**On Start**</i>
: **I** = baselineAmplitude


<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**I** = weight * baselineAmplitude

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;&emsp;&emsp;**I** = weight * (startAmplitude + (finishAmplitude - startAmplitude) * (t - delay) / (duration))

: IF t &gt;= duration+delay THEN
: &emsp;&emsp;&emsp;**I** = weight * baselineAmplitude








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="RampGeneratorDL">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="startAmplitude" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="finishAmplitude" type="Nml2Quantity_none" use="required"/>
      <xs:attribute name="baselineAmplitude" type="Nml2Quantity_none" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=RampGeneratorDL" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import RampGeneratorDL
from neuroml.utils import component_factory

variable = component_factory(
    RampGeneratorDL,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    start_amplitude: 'a Nml2Quantity_current (required)' = None,
    finish_amplitude: 'a Nml2Quantity_current (required)' = None,
    baseline_amplitude: 'a Nml2Quantity_current (required)' = None,
)
```
````
`````

(schema:voltageclamp)=

## voltageClamp




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Voltage clamp. Applies a variable current **i** to try to keep parent at **targetVoltage.** Not yet fully tested!!! Consider using voltageClampTriple!!</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**delay**$ Delay before change in current. Current is zero prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for attempting to keep parent at targetVoltage. Current is zero after delay + duration. ${ref}`schema:dimensions:time`
**simpleSeriesResistance**$ Current will be calculated by the difference in voltage between the target and parent, divided by this value ${ref}`schema:dimensions:resistance`
**targetVoltage**$ Current will be applied to try to get parent to this target voltage ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;&emsp;&emsp;**i** = 0

: IF t &gt;= delay THEN
: &emsp;&emsp;&emsp;**i** = weight * (targetVoltage - v) / simpleSeriesResistance

: IF t &gt; duration + delay THEN
: &emsp;&emsp;&emsp;**i** = 0








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="VoltageClamp">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="targetVoltage" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="simpleSeriesResistance" type="Nml2Quantity_resistance" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=VoltageClamp" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import VoltageClamp
from neuroml.utils import component_factory

variable = component_factory(
    VoltageClamp,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    target_voltage: 'a Nml2Quantity_voltage (required)' = None,
    simple_series_resistance: 'a Nml2Quantity_resistance (required)' = None,
)
```
````
`````

(schema:voltageclamptriple)=

## voltageClampTriple




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Voltage clamp with 3 clamp levels. Applies a variable current **i** ( through **simpleSeriesResistance** ) to try to keep parent cell at **conditioningVoltage** until time **delay,** **testingVoltage** until **delay** + **duration,** and **returnVoltage** afterwards. Only enabled if **active** = 1.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**active**$ Whether the voltage clamp is active (1) or inactive (0). $Dimensionless
**conditioningVoltage**$ Target voltage before time delay ${ref}`schema:dimensions:voltage`
**delay**$ Delay before switching from conditioningVoltage to testingVoltage. ${ref}`schema:dimensions:time`
**duration**$ Duration to hold at testingVoltage. ${ref}`schema:dimensions:time`
**returnVoltage**$ Target voltage after time duration ${ref}`schema:dimensions:voltage`
**simpleSeriesResistance**$ Current will be calculated by the difference in voltage between the target and parent, divided by this value ${ref}`schema:dimensions:resistance`
**testingVoltage**$ Target voltage between times delay and delay + duration ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF active = 1 AND t &lt; delay THEN
: &emsp;&emsp;&emsp;**i** = weight * (conditioningVoltage - v) / simpleSeriesResistance

: IF active = 1 AND t &gt;= delay THEN
: &emsp;&emsp;&emsp;**i** = weight * (testingVoltage - v) / simpleSeriesResistance

: IF active = 1 AND t &gt; duration + delay THEN
: &emsp;&emsp;&emsp;**i** = weight * (returnVoltage - v) / simpleSeriesResistance








````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="VoltageClampTriple">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="active" type="ZeroOrOne" use="required"/>
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="conditioningVoltage" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="testingVoltage" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="returnVoltage" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="simpleSeriesResistance" type="Nml2Quantity_resistance" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=VoltageClampTriple" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import VoltageClampTriple
from neuroml.utils import component_factory

variable = component_factory(
    VoltageClampTriple,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    active: 'a ZeroOrOne (required)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    conditioning_voltage: 'a Nml2Quantity_voltage (required)' = None,
    testing_voltage: 'a Nml2Quantity_voltage (required)' = None,
    return_voltage: 'a Nml2Quantity_voltage (required)' = None,
    simple_series_resistance: 'a Nml2Quantity_resistance (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<voltageClampTriple id="vClamp0" active="1" delay="50ms" duration="200ms" conditioningVoltage="-70mV" testingVoltage="-50mV" returnVoltage="-70mV" simpleSeriesResistance="1e6ohm"/>
```
````
`````
