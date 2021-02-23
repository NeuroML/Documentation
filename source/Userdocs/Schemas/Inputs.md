
(schema:inputs)=
# Inputs



Original ComponentType definitions: [Inputs.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Inputs.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 25/02/21 from [this](https://github.com/NeuroML/NeuroML2/commit/6e4643d0eaa7246982b351a01e28856eeb320500) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:basepointcurrent)=

## *basePointCurrent*




extends *{ref}`schema:basestandalone`*



<i>Base type for all ComponentTypes which produce a current _i (with dimension current).</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

i,{ref}`schema:dimensions:current`

```
````

(schema:basevoltagedeppointcurrent)=

## *baseVoltageDepPointCurrent*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all ComponentTypes which produce a current _i (with dimension current) and require a membrane potential _v exposed on the parent Component.</i>



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

v,{ref}`schema:dimensions:voltage`

```
````

(schema:basevoltagedeppointcurrentspiking)=

## *baseVoltageDepPointCurrentSpiking*




extends *{ref}`schema:basevoltagedeppointcurrent`*



<i>Base type for all ComponentTypes which produce a current _i, require a membrane potential _v exposed on the parent and emit spikes (on a port _spike). The exposed variable _tsince can be used for plotting the time since the Component has spiked last.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`
tsince,{ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

spike,Direction: out

```
````

(schema:basepointcurrentdl)=

## *basePointCurrentDL*




<i>Base type for all ComponentTypes which produce a dimensionless current _I. There will eventually be dimensionless equivalents of all the core current producing ComponentTypes such as _pulseGenerator_, _sineGenerator_ and _rampGenerator_.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

I,Dimensionless

```
````

(schema:basevoltagedeppointcurrentdl)=

## *baseVoltageDepPointCurrentDL*




extends *{ref}`schema:basepointcurrentdl`*



<i>Base type for all ComponentTypes which produce a dimensionless current _I and require a dimensionless membrane potential _V exposed on the parent Component.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*I (from {ref}`schema:basepointcurrentdl`)*,Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

V,Dimensionless

```
````

(schema:basespikesource)=

## *baseSpikeSource*




<i>Base for any ComponentType whose main purpose is to emit spikes (on a port _spike). The exposed variable _tsince can be used for plotting the time since the Component has spiked last.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

tsince,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

spike,Direction: out

```
````

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

tnext,{ref}`schema:dimensions:time`
*tsince (from {ref}`schema:basespikesource`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikesource`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnext**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnext**)









<i>**On Start**</i>
: **tsince** = 0
: **tnext** = period



<i>**On Conditions**</i>

: IF tnext-t &lt; SMALL_TIME THEN
: &emsp;**tsince** = 0
: &emsp;**tnext** = tnext+period
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnext** /dt = 0
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

isi,{ref}`schema:dimensions:time`
tnext,{ref}`schema:dimensions:time`
*tsince (from {ref}`schema:basespikesource`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikesource`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **tnext**: {ref}`schema:dimensions:time` &emsp;(exposed as **tnext**)
: **isi**: {ref}`schema:dimensions:time` &emsp;(exposed as **isi**)









<i>**On Start**</i>
: **tsince** = 0
: **isi** = minISI + MSEC * random((maxISI - minISI) / MSEC)
: **tnext** = isi



<i>**On Conditions**</i>

: IF t &gt; tnext THEN
: &emsp;**isi** = minISI + MSEC * random((maxISI - minISI) / MSEC)
: &emsp;**tsince** = 0
: &emsp;**tnext** = tnext+isi
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnext** /dt = 0
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

isi,{ref}`schema:dimensions:time`
tnextIdeal,{ref}`schema:dimensions:time`
tnextUsed,{ref}`schema:dimensions:time`
*tsince (from {ref}`schema:basespikesource`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikesource`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
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
: &emsp;**tsince** = 0
: &emsp;**isi** = -1 * log(random(1)) / averageRate
: &emsp;**tnextIdeal** = (tnextIdeal+isi)
: &emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*isi (from {ref}`schema:spikegeneratorpoisson`)*,{ref}`schema:dimensions:time`
*tnextIdeal (from {ref}`schema:spikegeneratorpoisson`)*,{ref}`schema:dimensions:time`
*tnextUsed (from {ref}`schema:spikegeneratorpoisson`)*,{ref}`schema:dimensions:time`
*tsince (from {ref}`schema:basespikesource`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikesource`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
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
: &emsp;**tsince** = 0
: &emsp;**isi** = minimumISI - (averageIsi-minimumISI) * log(random(1))
: &emsp;**tnextIdeal** = (tnextIdeal+isi)
: &emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`
isi,{ref}`schema:dimensions:time`
tnextIdeal,{ref}`schema:dimensions:time`
tnextUsed,{ref}`schema:dimensions:time`
*tsince (from {ref}`schema:basevoltagedeppointcurrentspiking`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in
spike,Direction: out
*spike (from {ref}`schema:basevoltagedeppointcurrentspiking`)*,Direction: out

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **spikeTarget** AS **b**
: CHILD INSTANCE: **synapse**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
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
: &emsp;**tsince** = 0
: &emsp;**isi** = - averageIsi * log(1 - random(1))
: &emsp;**tnextIdeal** = (tnextIdeal+isi)
: &emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;EVENT OUT on port **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapse->i
    : **i** =&nbsp;weight * iSyn&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`
isi,{ref}`schema:dimensions:time`
tnextIdeal,{ref}`schema:dimensions:time`
tnextUsed,{ref}`schema:dimensions:time`
*tsince (from {ref}`schema:basevoltagedeppointcurrentspiking`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in
spike,Direction: out
*spike (from {ref}`schema:basevoltagedeppointcurrentspiking`)*,Direction: out

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **spikeTarget** AS **b**
: CHILD INSTANCE: **synapse**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
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
: &emsp;**tsince** = 0
: &emsp;**isi** = - averageIsi * log(1 - random(1))
: &emsp;**tnextIdeal** = (tnextIdeal+isi) + H(((t+isi) - (delay+duration))/duration)*LONG_TIME
: &emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;EVENT OUT on port **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapse->i
    : **i** =&nbsp;weight * iSyn&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`
*tsince (from {ref}`schema:basevoltagedeppointcurrentspiking`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedeppointcurrent`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in
*spike (from {ref}`schema:basevoltagedeppointcurrentspiking`)*,Direction: out

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **spikeTarget** AS **b**
: CHILD INSTANCE: **synapse**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**tsince** = 0
: &emsp;EVENT OUT on port **spike**





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapse->i
    : **i** =&nbsp;weight * iSyn&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**i** = 0

: IF t &gt;= delay AND t &lt; duration + delay THEN
: &emsp;**i** = weight * amplitude

: IF t &gt;= duration + delay THEN
: &emsp;**i** = 0








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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics












<i>**On Events**</i>

: EVENT IN on port: **in**





<i>**Derived Variables**</i>
    : **i_total** =&nbsp;currents[*]->i(reduce method: add)
    : **i** =&nbsp;weight * i_total&emsp;(exposed as **i**)
    





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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*I (from {ref}`schema:basepointcurrentdl`)*,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics












<i>**On Events**</i>

: EVENT IN on port: **in**





<i>**Derived Variables**</i>
    : **I_total** =&nbsp;currents[*]->I(reduce method: add)
    : **I** =&nbsp;weight * I_total&emsp;(exposed as **I**)
    





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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*I (from {ref}`schema:basepointcurrentdl`)*,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **I**: Dimensionless &emsp;(exposed as **I**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**I** = 0

: IF t &gt;= delay AND t &lt; duration + delay THEN
: &emsp;**I** = weight * amplitude

: IF t &gt;= duration + delay THEN
: &emsp;**I** = 0








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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**i** = 0

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;**i** = weight * amplitude * sin(phase + (2 * 3.14159265 * (t-delay)/period) )

: IF t &gt;= duration+delay THEN
: &emsp;**i** = 0








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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*I (from {ref}`schema:basepointcurrentdl`)*,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **I**: Dimensionless &emsp;(exposed as **I**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**I** = 0

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;**I** = weight * amplitude * sin(phase + (2 * 3.14159265 * (t-delay)/period) )

: IF t &gt;= duration+delay THEN
: &emsp;**I** = 0








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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)









<i>**On Start**</i>
: **i** = baselineAmplitude


<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**i** = weight * baselineAmplitude

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;**i** = weight * (startAmplitude + (finishAmplitude - startAmplitude) * (t - delay) / (duration))

: IF t &gt;= duration+delay THEN
: &emsp;**i** = weight * baselineAmplitude








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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*I (from {ref}`schema:basepointcurrentdl`)*,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **I**: Dimensionless &emsp;(exposed as **I**)









<i>**On Start**</i>
: **I** = baselineAmplitude


<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**I** = weight * baselineAmplitude

: IF t &gt;= delay AND t &lt; duration+delay THEN
: &emsp;**I** = weight * (startAmplitude + (finishAmplitude - startAmplitude) * (t - delay) / (duration))

: IF t &gt;= duration+delay THEN
: &emsp;**I** = weight * baselineAmplitude








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

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF t &lt; delay THEN
: &emsp;**i** = 0

: IF t &gt;= delay THEN
: &emsp;**i** = weight * (targetVoltage - v) / simpleSeriesResistance

: IF t &gt; duration + delay THEN
: &emsp;**i** = 0








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

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **i**: {ref}`schema:dimensions:current` &emsp;(exposed as **i**)











<i>**On Events**</i>

: EVENT IN on port: **in**



<i>**On Conditions**</i>

: IF active = 1 AND t &lt; delay THEN
: &emsp;**i** = weight * (conditioningVoltage - v) / simpleSeriesResistance

: IF active = 1 AND t &gt;= delay THEN
: &emsp;**i** = weight * (testingVoltage - v) / simpleSeriesResistance

: IF active = 1 AND t &gt; duration + delay THEN
: &emsp;**i** = weight * (returnVoltage - v) / simpleSeriesResistance








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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*tsince (from {ref}`schema:basespikesource`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in
*spike (from {ref}`schema:basespikesource`)*,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)









<i>**On Start**</i>
: **tsince** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**tsince** = 0
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

spiked,Dimensionless
*tsince (from {ref}`schema:basespikesource`)*,{ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikesource`)*,Direction: out

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **parent** AS **b**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)
: **spiked**: Dimensionless &emsp;(exposed as **spiked**)









<i>**On Start**</i>
: **tsince** = 0



<i>**On Conditions**</i>

: IF (t &gt;= time) AND (spiked = 0) THEN
: &emsp;**spiked** = 1
: &emsp;**tsince** = 0
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    

````
