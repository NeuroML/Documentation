
(schema:inputs_)=
# Inputs

**A number of ComponentTypes for providing spiking ( e.g.  {ref}`schema:spikegeneratorpoisson`,  {ref}`schema:spikearray` ) and current inputs ( e.g.  {ref}`schema:pulsegenerator`,  {ref}`schema:voltageclamp`,  {ref}`schema:timedsynapticinput`,  {ref}`schema:poissonfiringsynapse` ) to other ComponentTypes**

---


Original ComponentType definitions: [Inputs.xml](https://github.com/NeuroML/NeuroML2/blob/documentation_update/NeuroML2CoreTypes//Inputs.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.2.xsd](https://github.com/NeuroML/NeuroML2/tree/documentation_update/Schemas/NeuroML2/NeuroML_v2.2.xsd).
Generated on 05/08/21 from [this](https://github.com/NeuroML/NeuroML2/commit/2e11cc54c858240d64275ffdb633f9219bac232d) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basepointcurrent)=

## *basePointCurrent*




extends *{ref}`schema:basestandalone`*



<i>Base type for all ComponentTypes which produce a current **i** ( with dimension current ).</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType ${ref}`schema:dimensions:current`

```
````

(schema:basevoltagedeppointcurrent)=

## *baseVoltageDepPointCurrent*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all ComponentTypes which produce a current **i** ( with dimension current ) and require a voltage **v** exposed on the parent Component, which would often be the membrane potential of a Component extending  {ref}`schema:basecellmembpot`.</i>



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

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed ${ref}`schema:dimensions:voltage`

```
````

(schema:basevoltagedeppointcurrentspiking)=

## *baseVoltageDepPointCurrentSpiking*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for all ComponentTypes which produce a current **i,** require a membrane potential **v** exposed on the parent and emit spikes ( on a port **spike** ). The exposed variable **tsince** can be used for plotting the time since the Component has spiked last.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**tsince**$ Time since the last spike was emitted ${ref}`schema:dimensions:time`

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted$Direction: out

```
````

(schema:basepointcurrentdl)=

## *basePointCurrentDL*




<i>Base type for all ComponentTypes which produce a dimensionless current **I.** There are many dimensionless equivalents of all the core current producing ComponentTypes such as  {ref}`schema:pulsegenerator` /  {ref}`schema:pulsegeneratordl`,  {ref}`schema:sinegenerator` /  {ref}`schema:sinegeneratordl` and  {ref}`schema:rampgenerator` /  {ref}`schema:rampgeneratordl`.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType $Dimensionless

```
````

(schema:basevoltagedeppointcurrentdl)=

## *baseVoltageDepPointCurrentDL*




extends *{ref}`schema:basepointcurrentdl`*



<i>Base type for all ComponentTypes which produce a dimensionless current **I** and require a dimensionless membrane potential **V** exposed on the parent Component.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**V**$ The current may vary with the dimensionless voltage exposed by the ComponentType on which this is placed $Dimensionless

```
````

(schema:basespikesource)=

## *baseSpikeSource*




<i>Base for any ComponentType whose main purpose is to emit spikes ( on a port **spike** ). The exposed variable **tsince** can be used for plotting the time since the Component has spiked last.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tsince**$ Time since the last spike was emitted ${ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted$Direction: out

```
````

(schema:spikegenerator)=

## spikeGenerator




extends *{ref}`schema:basespikesource`*



<i>Simple generator of spikes at a regular interval set by **period**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**period**$ Time between spikes. The first spike will be emitted after this time. ${ref}`schema:dimensions:time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tnext**$ When the next spike should ideally be emitted (dt permitting) ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGenerator" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeGenerator

variable = SpikeGenerator(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, period=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<spikeGenerator id="spikeGenRegular" period="20 ms"/>
```

````

(schema:spikegeneratorrandom)=

## spikeGeneratorRandom




extends *{ref}`schema:basespikesource`*



<i>Generator of spikes with a random interspike interval of at least **minISI** and at most **maxISI**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**maxISI**$ Maximum interspike interval ${ref}`schema:dimensions:time`
**minISI**$ Minimum interspike interval ${ref}`schema:dimensions:time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**isi**$ The interval until the next spike ${ref}`schema:dimensions:time`
**tnext**$ When the next spike should ideally be emitted (dt permitting) ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGeneratorRandom" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeGeneratorRandom

variable = SpikeGeneratorRandom(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, max_isi=None, min_isi=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<spikeGeneratorRandom id="spikeGenRandom" minISI="10 ms" maxISI="30 ms"/>
```

````

(schema:spikegeneratorpoisson)=

## spikeGeneratorPoisson




extends *{ref}`schema:basespikesource`*



<i>Generator of spikes whose ISI is distributed according to an exponential PDF with scale: 1 / **averageRate**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$ The average rate at which spikes are emitted ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGeneratorPoisson" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeGeneratorPoisson

variable = SpikeGeneratorPoisson(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, average_rate=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<spikeGeneratorPoisson id="spikeGenPoisson" averageRate="50 Hz"/>
```

````

(schema:spikegeneratorrefpoisson)=

## spikeGeneratorRefPoisson




extends {ref}`schema:spikegeneratorpoisson`



<i>Generator of spikes whose ISI distribution is the maximum entropy distribution over [ **minimumISI,** +infinity ) with mean: 1 / **averageRate**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$ The average rate at which spikes are emitted *(from {ref}`schema:spikegeneratorpoisson`)* ${ref}`schema:dimensions:per_time`
**minimumISI**$ The minimum interspike interval ${ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageIsi**$ The average interspike interval ${ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeGeneratorRefPoisson" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeGeneratorRefPoisson

variable = SpikeGeneratorRefPoisson(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, average_rate=None, minimum_isi=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<spikeGeneratorRefPoisson id="spikeGenRefPoisson" averageRate="50 Hz" minimumISI="10 ms"/>
```

````

(schema:poissonfiringsynapse)=

## poissonFiringSynapse




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Poisson spike generator firing at **averageRate,** which is connected to single **synapse** that is triggered every time a spike is generated, producing an input current. See also  {ref}`schema:transientpoissonfiringsynapse`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$ The average rate at which spikes are emitted ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageIsi**$ The average interspike interval ${ref}`schema:dimensions:time`

```
````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**spikeTarget**$ The target of the spikes, i.e. the synapse

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
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

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in
**spike**$ Port on which spikes are emitted$Direction: out
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)*$Direction: out

```
````

````{tabbed} Dynamics

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PoissonFiringSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import PoissonFiringSynapse

variable = PoissonFiringSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, average_rate=None, synapse=None, spike_target=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<poissonFiringSynapse id="poissonFiringSyn" averageRate="10 Hz" synapse="synInput" spikeTarget="./synInput"/>
```

````

(schema:transientpoissonfiringsynapse)=

## transientPoissonFiringSynapse




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Poisson spike generator firing at **averageRate** after a **delay** and for a **duration,** connected to single **synapse** that is triggered every time a spike is generated, providing an input current. Similar to ComponentType  {ref}`schema:poissonfiringsynapse`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageRate**$  ${ref}`schema:dimensions:per_time`
**delay**$  ${ref}`schema:dimensions:time`
**duration**$  ${ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**averageIsi**$  ${ref}`schema:dimensions:time`

```
````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**spikeTarget**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`
**LONG_TIME** = 1e9hour$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
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

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrent`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in
**spike**$ Port on which spikes are emitted$Direction: out
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)*$Direction: out

```
````

````{tabbed} Dynamics

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=TransientPoissonFiringSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import TransientPoissonFiringSynapse

variable = TransientPoissonFiringSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, average_rate=None, delay=None, duration=None, synapse=None, spike_target=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<transientPoissonFiringSynapse id="transPoissonFiringSyn" delay="50ms" duration="50ms" averageRate="300 Hz" synapse="synInputFast" spikeTarget="./synInputFast"/>
```
```{code-block} xml
<transientPoissonFiringSynapse id="transPoissonFiringSyn2" delay="50ms" duration="500ms" averageRate="10 Hz" synapse="synInputFastTwo" spikeTarget="./synInputFastTwo"/>
```

````

(schema:timedsynapticinput)=

## timedSynapticInput




extends *{ref}`schema:basevoltagedeppointcurrentspiking`*



<i>Spike array connected to a single **synapse,** producing a current triggered by each  {ref}`schema:spike` in the array.</i>



````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**spikeTarget**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**spikes**$  $ {ref}`schema:spike`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)* ${ref}`schema:dimensions:time`

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This will receive events from the children$Direction: in
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basevoltagedeppointcurrentspiking`)*$Direction: out

```
````

````{tabbed} Dynamics

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=TimedSynapticInput" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import TimedSynapticInput

variable = TimedSynapticInput(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, synapse=None, spike_target=None, spikes=None, **kwargs_)
```



*XML examples*
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

(schema:spikearray)=

## spikeArray




extends *{ref}`schema:basespikesource`*



<i>Set of spike ComponentTypes, each emitting one spike at a certain time. Can be used to feed a predetermined spike train into a cell.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**spikes**$  $ {ref}`schema:spike`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This will receive events from the children$Direction: in
**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeArray" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeArray

variable = SpikeArray(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, spikes=None, **kwargs_)
```



*XML examples*
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

(schema:spike)=

## spike




extends *{ref}`schema:basespikesource`*



<i>Emits a single spike at the specified **time**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**time**$ Time at which to emit one spike event ${ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spiked**$ 0 signals not yet spiked, 1 signals has spiked $Dimensionless
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Port on which spikes are emitted *(from {ref}`schema:basespikesource`)*$Direction: out

```
````

````{tabbed} Dynamics

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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Spike" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Spike

variable = Spike(neuro_lex_id=None, id=None, time=None, **kwargs_)
```



*XML examples*
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

(schema:pulsegenerator)=

## pulseGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a constant current pulse of a certain **amplitude** for a specified **duration** after a **delay.** Scaled by **weight,** if set.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**amplitude**$ Amplitude of current pulse ${ref}`schema:dimensions:current`
**delay**$ Delay before change in current. Current is zero  prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is zero after delay + duration. ${ref}`schema:dimensions:time`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note: this is not used here. Will be removed in future$Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PulseGenerator" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import PulseGenerator

variable = PulseGenerator(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, duration=None, amplitude=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<pulseGenerator id="pulseGen1" delay="50ms" duration="200ms" amplitude="0.0032nA"/>
```
```{code-block} xml
<pulseGenerator id="pulseGen2" delay="400ms" duration="200ms" amplitude="0.0032nA"/>
```
```{code-block} xml
<pulseGenerator id="pulseGen2" delay="20ms" duration="100ms" amplitude="0.2nA"/>
```

````

(schema:compoundinput)=

## compoundInput




extends *{ref}`schema:basepointcurrent`*



<i>Generates a current which is the sum of all its child  {ref}`schema:basepointcurrent` element, e.g. can be a combination of  {ref}`schema:pulsegenerator`,  {ref}`schema:sinegenerator` elements producing a single **i.** Scaled by **weight,** if set.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**currents**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tabbed} Dynamics












<i>**On Events**</i>

: EVENT IN on port: **in**





<i>**Derived Variables**</i>
    : **i_total** =&nbsp;currents[*]->i(reduce method: add)
    : **i** =&nbsp;weight * i_total&emsp;(exposed as **i**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=CompoundInput" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import CompoundInput

variable = CompoundInput(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, pulse_generators=None, sine_generators=None, ramp_generators=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<compoundInput id="ci0">
        <pulseGenerator id="pg1" delay="50ms" duration="200ms" amplitude=".8 nA"/>
        <pulseGenerator id="pg2" delay="100ms" duration="100ms" amplitude=".4 nA"/>
        <sineGenerator id="sg0" phase="0" delay="125ms" duration="50ms" amplitude=".4nA" period="25ms"/>
    </compoundInput>
```

````

(schema:compoundinputdl)=

## compoundInputDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Generates a current which is the sum of all its child  {ref}`schema:basepointcurrentdl` elements, e.g. can be a combination of  {ref}`schema:pulsegeneratordl`,  {ref}`schema:sinegeneratordl` elements producing a single **i.** Scaled by **weight,** if set.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**currents**$  $ {ref}`schema:basepointcurrentdl`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tabbed} Dynamics












<i>**On Events**</i>

: EVENT IN on port: **in**





<i>**Derived Variables**</i>
    : **I_total** =&nbsp;currents[*]->I(reduce method: add)
    : **I** =&nbsp;weight * I_total&emsp;(exposed as **I**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=CompoundInputDL" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import CompoundInputDL

variable = CompoundInputDL(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, pulse_generator_dls=None, sine_generator_dls=None, ramp_generator_dls=None, **kwargs_)
```



````

(schema:pulsegeneratordl)=

## pulseGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of  {ref}`schema:pulsegenerator`. Generates a constant current pulse of a certain **amplitude** for a specified **duration** after a **delay.** Scaled by **weight,** if set.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**amplitude**$ Amplitude of current pulse $Dimensionless
**delay**$ Delay before change in current. Current is zero  prior to this. ${ref}`schema:dimensions:time`
**duration**$ Duration for holding current at amplitude. Current is zero after delay + duration. ${ref}`schema:dimensions:time`

```
````

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=PulseGeneratorDL" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import PulseGeneratorDL

variable = PulseGeneratorDL(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, duration=None, amplitude=None, **kwargs_)
```



````

(schema:sinegenerator)=

## sineGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a sinusoidally varying current after a time **delay,** for a fixed **duration.** The **period** and maximum **amplitude** of the current can be set as well as the **phase** at which to start. Scaled by **weight,** if set.</i>



````{tabbed} Parameters
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

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SineGenerator" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SineGenerator

variable = SineGenerator(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, phase=None, duration=None, amplitude=None, period=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<sineGenerator id="sg0" phase="0" delay="50ms" duration="200ms" amplitude="1.4nA" period="50ms"/>
```
```{code-block} xml
<sineGenerator id="sg0" phase="0" delay="125ms" duration="50ms" amplitude=".4nA" period="25ms"/>
```

````

(schema:sinegeneratordl)=

## sineGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of  {ref}`schema:sinegenerator`. Generates a sinusoidally varying current after a time **delay,** for a fixed **duration.** The **period** and maximum **amplitude** of the current can be set as well as the **phase** at which to start. Scaled by **weight,** if set.</i>



````{tabbed} Parameters
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

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SineGeneratorDL" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SineGeneratorDL

variable = SineGeneratorDL(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, phase=None, duration=None, amplitude=None, period=None, **kwargs_)
```



````

(schema:rampgenerator)=

## rampGenerator




extends *{ref}`schema:basepointcurrent`*



<i>Generates a ramping current after a time **delay,** for a fixed **duration.** During this time the current steadily changes from **startAmplitude** to **finishAmplitude.** Scaled by **weight,** if set.</i>



````{tabbed} Parameters
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

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=RampGenerator" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import RampGenerator

variable = RampGenerator(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, duration=None, start_amplitude=None, finish_amplitude=None, baseline_amplitude=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<rampGenerator id="rg0" delay="50ms" duration="200ms" startAmplitude="0.5nA" finishAmplitude="4nA" baselineAmplitude="0nA"/>
```

````

(schema:rampgeneratordl)=

## rampGeneratorDL




extends *{ref}`schema:basepointcurrentdl`*



<i>Dimensionless equivalent of  {ref}`schema:rampgenerator`. Generates a ramping current after a time **delay,** for a fixed **duration.** During this time the dimensionless current steadily changes from **startAmplitude** to **finishAmplitude.** Scaled by **weight,** if set.</i>



````{tabbed} Parameters
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

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**I**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrentdl`)* $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=RampGeneratorDL" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import RampGeneratorDL

variable = RampGeneratorDL(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, duration=None, start_amplitude=None, finish_amplitude=None, baseline_amplitude=None, **kwargs_)
```



````

(schema:voltageclamp)=

## voltageClamp




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Voltage clamp. Applies a variable current **i** to try to keep parent at **targetVoltage.** Not yet fully tested!!! Consider using voltageClampTriple!!</i>



````{tabbed} Parameters
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

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=VoltageClamp" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import VoltageClamp

variable = VoltageClamp(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, delay=None, duration=None, target_voltage=None, simple_series_resistance=None, **kwargs_)
```



````

(schema:voltageclamptriple)=

## voltageClampTriple




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Voltage clamp with 3 clamp levels. Applies a variable current **i** ( through **simpleSeriesResistance** ) to try to keep parent cell at **conditioningVoltage** until time **delay,** **testingVoltage** until **delay** + **duration,** and **returnVoltage** afterwards. Only enabled if **active** = 1.</i>



````{tabbed} Parameters
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

````{tabbed} Properties
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**weight** (default: 1)$  $ Dimensionless

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

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ Note this is not used here. Will be removed in future$Direction: in

```
````

````{tabbed} Dynamics



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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=VoltageClampTriple" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import VoltageClampTriple

variable = VoltageClampTriple(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, active=None, delay=None, duration=None, conditioning_voltage=None, testing_voltage=None, return_voltage=None, simple_series_resistance=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<voltageClampTriple id="vClamp0" active="1" delay="50ms" duration="200ms" conditioningVoltage="-70mV" testingVoltage="-50mV" returnVoltage="-70mV" simpleSeriesResistance="1e6ohm"/>
```

````
