
(schema:channels)=
# Channels



Original ComponentType definitions: [Channels.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Channels.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 02/04/21 from [this](https://github.com/NeuroML/NeuroML2/commit/dda624b705adeb399adb497087ed48c9fe2abe22) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:basevoltagedeprate)=

## *baseVoltageDepRate*




<i>Base ComponentType for voltage dependent rate. Produces a time varying rate **r** which depends on **v.**.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  ${ref}`schema:dimensions:per_time`

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

(schema:basevoltageconcdeprate)=

## *baseVoltageConcDepRate*




extends *{ref}`schema:basevoltagedeprate`*



<i>Base ComponentType for voltage and concentration dependent rate. Produces a time varying rate **r** which depends on **v** and **caConc.**.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:basehhrate)=

## *baseHHRate*




extends *{ref}`schema:basevoltagedeprate`*



<i>Base ComponentType for rate which follow one of the typical forms for rate equations in the standard HH formalism, using the parameters **rate,** **midpoint** and **scale**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  ${ref}`schema:dimensions:voltage`
**rate**$  ${ref}`schema:dimensions:per_time`
**scale**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:hhexprate)=

## HHExpRate




extends *{ref}`schema:basehhrate`*



<i>Exponential form for rate equation (Q: Should these be renamed hhExpRate, etc?).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:per_time`
**scale**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **r** =&nbsp;rate * exp((v - midpoint)/scale)&emsp;(exposed as **r**)
    





````

(schema:hhsigmoidrate)=

## HHSigmoidRate




extends *{ref}`schema:basehhrate`*



<i>Sigmoidal form for rate equation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:per_time`
**scale**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **r** =&nbsp;rate / (1 + exp(0 - (v - midpoint)/scale))&emsp;(exposed as **r**)
    





````

(schema:hhexplinearrate)=

## HHExpLinearRate




extends *{ref}`schema:basehhrate`*



<i>Exponential linear form for rate equation. Linear for large positive **v,** exponentially decays for large negative **v.**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:per_time`
**scale**$  *(from {ref}`schema:basehhrate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**r**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeprate`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **x** =&nbsp;(v - midpoint) / scale
    



<i>**Conditional Derived Variables**</i>
    
: IF x != 0 THEN
: &emsp; **r** = rate \* x / (1 - exp(0 - x)) &emsp;(exposed as **r**)
: IF x = 0 THEN
: &emsp; **r** = rate &emsp;(exposed as **r**)


````

(schema:basevoltagedepvariable)=

## *baseVoltageDepVariable*




<i>Base ComponentType for voltage dependent variable  **x,** which depends on **v.** Can be used for inf/steady state of rate variable.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  $Dimensionless

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

(schema:basevoltageconcdepvariable)=

## *baseVoltageConcDepVariable*




extends *{ref}`schema:basevoltagedepvariable`*



<i>Base ComponentType for voltage and calcium concentration dependent variable **x,** which depends on **v** and **caConc.**.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:basehhvariable)=

## *baseHHVariable*




extends *{ref}`schema:basevoltagedepvariable`*



<i>Base ComponentType for voltage dependent dimensionless variable which follow one of the typical forms for variable equations in the standard HH formalism, using the parameters **rate,** **midpoint,** **scale**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  ${ref}`schema:dimensions:voltage`
**rate**$  $Dimensionless
**scale**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:hhexpvariable)=

## HHExpVariable




extends *{ref}`schema:basehhvariable`*



<i>Exponential form for variable equation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhvariable`)* $Dimensionless
**scale**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **x** =&nbsp;rate * exp((v - midpoint)/scale)&emsp;(exposed as **x**)
    





````

(schema:hhsigmoidvariable)=

## HHSigmoidVariable




extends *{ref}`schema:basehhvariable`*



<i>Sigmoidal form for variable equation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhvariable`)* $Dimensionless
**scale**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **x** =&nbsp;rate / (1 + exp(0 - (v - midpoint)/scale))&emsp;(exposed as **x**)
    





````

(schema:hhexplinearvariable)=

## HHExpLinearVariable




extends *{ref}`schema:basehhvariable`*



<i>Exponential linear form for variable equation. Linear for large positive **v,** exponentially decays for large negative **v.**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**midpoint**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`
**rate**$  *(from {ref}`schema:basehhvariable`)* $Dimensionless
**scale**$  *(from {ref}`schema:basehhvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  *(from {ref}`schema:basevoltagedepvariable`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedepvariable`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **a** =&nbsp;(v - midpoint) / scale
    : **x** =&nbsp;rate * a / (1 - exp(0 - a))&emsp;(exposed as **x**)
    





````

(schema:basevoltagedeptime)=

## *baseVoltageDepTime*




<i>Base ComponentType for voltage dependent ComponentType producing value **t** with dimension time (e.g. for time course of rate variable). Note: time course would not normally be fit to exp/sigmoid etc.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**t**$  ${ref}`schema:dimensions:time`

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

(schema:basevoltageconcdeptime)=

## *baseVoltageConcDepTime*




extends *{ref}`schema:basevoltagedeptime`*



<i>Base type for voltage and calcium concentration dependent ComponentType producing value **t** with dimension time (e.g. for time course of rate variable).</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**t**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**v**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:voltage`

```
````

(schema:fixedtimecourse)=

## fixedTimeCourse




extends *{ref}`schema:basevoltagedeptime`*



<i>Time course of a fixed magnitude **tau** which can be used for the time course in  {ref}`schema:gatehhtauinf`,  {ref}`schema:gatehhratestau` or  {ref}`schema:gatehhratestauinf`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau**$  ${ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**t**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:basevoltagedeptime`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **t** =&nbsp;tau&emsp;(exposed as **t**)
    





````

(schema:baseq10settings)=

## *baseQ10Settings*




<i>Base ComponentType for a scaling to apply to gating variable time course, usually temperature dependent.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**q10**$  $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  ${ref}`schema:dimensions:temperature`

```
````

(schema:q10fixed)=

## q10Fixed




extends *{ref}`schema:baseq10settings`*



<i>A fixed value, **fixedQ10,** for the scaling of the time course of the gating variable.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fixedQ10**$  $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**q10**$  *(from {ref}`schema:baseq10settings`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  *(from {ref}`schema:baseq10settings`)* ${ref}`schema:dimensions:temperature`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **q10** =&nbsp;fixedQ10&emsp;(exposed as **q10**)
    





````

(schema:q10exptemp)=

## q10ExpTemp




extends *{ref}`schema:baseq10settings`*



<i>A value for the Q10 scaling which varies as a standard function of the difference between the current temperature, **temperature,** and the temperature at which the gating variable equations were determined, **experimentalTemp**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**experimentalTemp**$  ${ref}`schema:dimensions:temperature`
**q10Factor**$  $Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**TENDEGREES** = 10K$  $ {ref}`schema:dimensions:temperature`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**q10**$  *(from {ref}`schema:baseq10settings`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  *(from {ref}`schema:baseq10settings`)* ${ref}`schema:dimensions:temperature`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **q10** =&nbsp;q10Factor^((temperature - experimentalTemp)/TENDEGREES)&emsp;(exposed as **q10**)
    





````

(schema:baseconductancescaling)=

## *baseConductanceScaling*




<i>Base ComponentType for a scaling to apply to a gate's conductance, e.g. temperature dependent scaling.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**factor**$  $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  ${ref}`schema:dimensions:temperature`

```
````

(schema:q10conductancescaling)=

## q10ConductanceScaling




extends *{ref}`schema:baseconductancescaling`*



<i>A value for the conductance scaling which varies as a standard function of the difference between the current temperature, **temperature,** and the temperature at which the conductance was originally determined, **experimentalTemp**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**experimentalTemp**$  ${ref}`schema:dimensions:temperature`
**q10Factor**$  $Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**TENDEGREES** = 10K$  $ {ref}`schema:dimensions:temperature`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**factor**$  *(from {ref}`schema:baseconductancescaling`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  *(from {ref}`schema:baseconductancescaling`)* ${ref}`schema:dimensions:temperature`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **factor** =&nbsp;q10Factor^((temperature - experimentalTemp)/TENDEGREES)&emsp;(exposed as **factor**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Q10ConductanceScaling" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Q10ConductanceScaling

variable = Q10ConductanceScaling(q10_factor=None, experimental_temp=None, **kwargs_)
```



````

(schema:baseconductancescalingcadependent)=

## *baseConductanceScalingCaDependent*




extends *{ref}`schema:baseconductancescaling`*



<i>Base ComponentType for a scaling to apply to a gate's conductance which depends on Ca concentration. Usually a generic expression of **caConc** (so no standard, non-base form here).</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**factor**$  *(from {ref}`schema:baseconductancescaling`)* $Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**caConc**$  ${ref}`schema:dimensions:concentration`
**temperature**$  *(from {ref}`schema:baseconductancescaling`)* ${ref}`schema:dimensions:temperature`

```
````

(schema:basegate)=

## *baseGate*




<i>Base ComponentType for a voltage and/or concentration dependent gate.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  $Dimensionless
**q**$  $Dimensionless

```
````

(schema:gate)=

## gate




extends *{ref}`schema:basegate`*



<i>Conveniently named baseGate.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

(schema:gatehhrates)=

## gateHHrates




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tabbed} Exposures
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

````{tabbed} Dynamics



<i>**State variables**</i>
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

````{tabbed} Usage



*XML examples*
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
<gateHHrates id="n" instances="4">
            <forwardRate type="HHExpLinearRate" rate="0.1per_ms" midpoint="-55mV" scale="10mV"/>
            <reverseRate type="HHExpRate" rate="0.125per_ms" midpoint="-65mV" scale="-80mV"/>
        </gateHHrates>
```

````

(schema:gatehhtauinf)=

## gateHHtauInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tabbed} Exposures
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

````{tabbed} Dynamics



<i>**State variables**</i>
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

(schema:gatehhinstantaneous)=

## gateHHInstantaneous




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism but is instantaneous, so tau = 0 and gate follows exactly inf value.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**SEC** = 1 s$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
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

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **inf** =&nbsp;steadyState->x&emsp;(exposed as **inf**)
    : **tau** =&nbsp;0 * SEC&emsp;(exposed as **tau**)
    : **q** =&nbsp;inf&emsp;(exposed as **q**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateHHInstantaneous" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import GateHHInstantaneous

variable = GateHHInstantaneous(neuro_lex_id=None, id=None, instances=None, notes=None, steady_state=None, **kwargs_)
```



````

(schema:gatehhratestau)=

## gateHHratesTau




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`
**timeCourse**$  $ {ref}`schema:basevoltagedeptime`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tabbed} Exposures
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

````{tabbed} Dynamics



<i>**State variables**</i>
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

(schema:gatehhratesinf)=

## gateHHratesInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**forwardRate**$  $ {ref}`schema:basevoltagedeprate`
**reverseRate**$  $ {ref}`schema:basevoltagedeprate`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tabbed} Exposures
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

````{tabbed} Dynamics



<i>**State variables**</i>
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

(schema:gatehhratestauinf)=

## gateHHratesTauInf




extends {ref}`schema:gate`



<i>Gate which follows the general Hodgkin Huxley formalism.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Child list
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

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tabbed} Exposures
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

````{tabbed} Dynamics



<i>**State variables**</i>
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

(schema:gatefractional)=

## gateFractional




extends {ref}`schema:gate`



<i>Gate composed of subgates contributing with fractional conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**q10Settings**$  $ {ref}`schema:baseq10settings`
**subGate**$  $ {ref}`schema:subgate`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **q** =&nbsp;subGate[*]->qfrac(reduce method: add)&emsp;(exposed as **q**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateFractional" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import GateFractional

variable = GateFractional(neuro_lex_id=None, id=None, instances=None, notes=None, q10_settings=None, sub_gates=None, **kwargs_)
```



````

(schema:subgate)=

## subGate




<i>Gate composed of subgates contributing with fractional conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fractionalConductance**$  $Dimensionless

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Exposures
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

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rateScale**$  $Dimensionless

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
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

(schema:baseionchannel)=

## *baseIonChannel*




<i>Base for all ion channel ComponentTypes.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

**neuroLexId**

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

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  $Dimensionless
**g**$  ${ref}`schema:dimensions:conductance`

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

(schema:ionchannelpassive)=

## ionChannelPassive




extends {ref}`schema:ionchannel`



<i>Simple passive ion channel where the constant conductance through the channel is equal to **conductance**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

**species**

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **fopen** =&nbsp;1&emsp;(exposed as **fopen**)
    : **g** =&nbsp;conductance&emsp;(exposed as **g**)
    





````

(schema:ionchannelhh)=

## ionChannelHH




extends *{ref}`schema:baseionchannel`*



<i>Note  {ref}`schema:ionchannel` and  {ref}`schema:ionchannelhh` are currently functionally identical. This is needed since many existing examples use ionChannel, some use ionChannelHH. NeuroML v2beta4 should remove one of these, probably ionChannelHH.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

**species**

````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**conductanceScaling**$  $ {ref}`schema:baseconductancescaling`
**gates**$  $ {ref}`schema:gate`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **conductanceScale** =&nbsp;conductanceScaling[*]->factor(reduce method: multiply)
    : **fopen0** =&nbsp;gates[*]->fcond(reduce method: multiply)
    : **fopen** =&nbsp;conductanceScale * fopen0&emsp;(exposed as **fopen**)
    : **g** =&nbsp;conductance * fopen&emsp;(exposed as **g**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannelHH" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IonChannelHH

variable = IonChannelHH(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, q10_conductance_scalings=None, species=None, type=None, conductance=None, gates=None, gate_hh_rates=None, gate_h_hrates_taus=None, gate_hh_tau_infs=None, gate_h_hrates_infs=None, gate_h_hrates_tau_infs=None, gate_hh_instantaneouses=None, gate_fractionals=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<ionChannelHH id="passiveChan" conductance="10pS">
        <notes>Leak conductance</notes>
    </ionChannelHH>
```
```{code-block} xml
<ionChannelHH id="naChan" conductance="10pS" species="na">
        <notes>Na channel</notes>
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
```{code-block} xml
<ionChannelHH id="kChan" conductance="10pS" species="k">
        <gateHHrates id="n" instances="4">
            <forwardRate type="HHExpLinearRate" rate="0.1per_ms" midpoint="-55mV" scale="10mV"/>
            <reverseRate type="HHExpRate" rate="0.125per_ms" midpoint="-65mV" scale="-80mV"/>
        </gateHHrates>
            
    </ionChannelHH>
```

````

(schema:ionchannel)=

## ionChannel




extends {ref}`schema:ionchannelhh`



<i>Note  {ref}`schema:ionchannel` and  {ref}`schema:ionchannelhh` are currently functionally identical. This is needed since many existing examples use ionChannel, some use ionChannelHH. NeuroML v2beta4 should remove one of these, probably ionChannelHH.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **conductanceScale** =&nbsp;conductanceScaling[*]->factor(reduce method: multiply)
    : **fopen0** =&nbsp;gates[*]->fcond(reduce method: multiply)
    : **fopen** =&nbsp;conductanceScale * fopen0&emsp;(exposed as **fopen**)
    : **g** =&nbsp;conductance * fopen&emsp;(exposed as **g**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannel" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IonChannel

variable = IonChannel(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, q10_conductance_scalings=None, species=None, type=None, conductance=None, gates=None, gate_hh_rates=None, gate_h_hrates_taus=None, gate_hh_tau_infs=None, gate_h_hrates_infs=None, gate_h_hrates_tau_infs=None, gate_hh_instantaneouses=None, gate_fractionals=None, extensiontype_=None, **kwargs_)
```



````

(schema:ionchannelvshift)=

## ionChannelVShift




extends {ref}`schema:ionchannel`



<i>Same as  {ref}`schema:ionchannel`, but with a **vShift** parameter to change voltage activation of gates. The exact usage of **vShift** in expressions for rates is determined by the individual gates.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`
**vShift**$  ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

**species**

````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannelVShift" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IonChannelVShift

variable = IonChannelVShift(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, q10_conductance_scalings=None, species=None, type=None, conductance=None, gates=None, gate_hh_rates=None, gate_h_hrates_taus=None, gate_hh_tau_infs=None, gate_h_hrates_infs=None, gate_h_hrates_tau_infs=None, gate_hh_instantaneouses=None, gate_fractionals=None, v_shift=None, **kwargs_)
```



````

(schema:ksstate)=

## KSState




<i>One of the states in which a  {ref}`schema:gateks` can be. The rates of transitions between these states are given by  {ref}`schema:kstransition`s.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**relativeConductance**$  $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**occupancy**$  $Dimensionless
**q**$  $Dimensionless

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **occupancy**: Dimensionless &emsp;(exposed as **occupancy**)







<i>**Derived Variables**</i>
    : **q** =&nbsp;relativeConductance * occupancy&emsp;(exposed as **q**)
    





````

(schema:closedstate)=

## closedState




extends {ref}`schema:ksstate`



<i>A  {ref}`schema:ksstate` with **relativeConductance** of 0.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**relativeConductance**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**occupancy**$  *(from {ref}`schema:ksstate`)* $Dimensionless
**q**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ClosedState" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ClosedState

variable = ClosedState(neuro_lex_id=None, id=None, **kwargs_)
```



````

(schema:openstate)=

## openState




extends {ref}`schema:ksstate`



<i>A  {ref}`schema:ksstate` with **relativeConductance** of 1.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**relativeConductance**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**occupancy**$  *(from {ref}`schema:ksstate`)* $Dimensionless
**q**$  *(from {ref}`schema:ksstate`)* $Dimensionless

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=OpenState" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import OpenState

variable = OpenState(neuro_lex_id=None, id=None, **kwargs_)
```



````

(schema:ionchannelks)=

## ionChannelKS




extends *{ref}`schema:baseionchannel`*



<i>A kinetic scheme based ion channel with multiple  {ref}`schema:gateks`s, each of which consists of multiple  {ref}`schema:ksstate`s and  {ref}`schema:kstransition`s giving the rates of transition between them.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

**species**

````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**conductanceScaling**$  $ {ref}`schema:baseconductancescaling`
**gates**$  $ {ref}`schema:gateks`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fopen**$  *(from {ref}`schema:baseionchannel`)* $Dimensionless
**g**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:conductance`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$  *(from {ref}`schema:baseionchannel`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **fopen** =&nbsp;gates[*]->fcond(reduce method: multiply)&emsp;(exposed as **fopen**)
    : **g** =&nbsp;fopen * conductance&emsp;(exposed as **g**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IonChannelKS" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IonChannelKS

variable = IonChannelKS(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, species=None, conductance=None, gate_kses=None, **kwargs_)
```



````

(schema:kstransition)=

## KSTransition




<i>Specified the forward and reverse rates of transition between two  {ref}`schema:ksstate`s in a  {ref}`schema:gateks`.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  ${ref}`schema:dimensions:per_time`
**rr**$  ${ref}`schema:dimensions:per_time`

```
````

(schema:forwardtransition)=

## forwardTransition




extends {ref}`schema:kstransition`



<i>A forward only  {ref}`schema:kstransition` for a  {ref}`schema:gateks` which specifies a **rate** (type  {ref}`schema:basehhrate`) which follows one of the standard Hodgkin Huxley forms (e.g.  {ref}`schema:hhexprate`,  {ref}`schema:hhsigmoidrate`,  {ref}`schema:hhexplinearrate`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rate**$  $ {ref}`schema:basehhrate`

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

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **rf0** =&nbsp;rate->r
    : **rf** =&nbsp;rf0&emsp;(exposed as **rf**)
    : **rr** =&nbsp;0/SEC&emsp;(exposed as **rr**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ForwardTransition" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ForwardTransition

variable = ForwardTransition(neuro_lex_id=None, id=None, from_=None, to=None, anytypeobjs_=None, **kwargs_)
```



````

(schema:reversetransition)=

## reverseTransition




extends {ref}`schema:kstransition`



<i>A reverse only  {ref}`schema:kstransition` for a  {ref}`schema:gateks` which specifies a **rate** (type  {ref}`schema:basehhrate`) which follows one of the standard Hodgkin Huxley forms (e.g.  {ref}`schema:hhexprate`,  {ref}`schema:hhsigmoidrate`,  {ref}`schema:hhexplinearrate`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rate**$  $ {ref}`schema:basehhrate`

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

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **rr0** =&nbsp;rate->r
    : **rr** =&nbsp;rr0&emsp;(exposed as **rr**)
    : **rf** =&nbsp;0/SEC&emsp;(exposed as **rf**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ReverseTransition" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ReverseTransition

variable = ReverseTransition(neuro_lex_id=None, id=None, from_=None, to=None, anytypeobjs_=None, **kwargs_)
```



````

(schema:vhalftransition)=

## vHalfTransition




extends {ref}`schema:kstransition`



<i>Transition which specifies both the forward and reverse rates of transition.</i>



````{tabbed} Parameters
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

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**kte** = 25.3mV$  $ {ref}`schema:dimensions:voltage`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

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

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **rf0** =&nbsp;exp(z * gamma * (v - vHalf) / kte) / tau
    : **rr0** =&nbsp;exp(-z * (1 - gamma) * (v - vHalf) / kte) / tau
    : **rf** =&nbsp;1 / (1/rf0 + tauMin)&emsp;(exposed as **rf**)
    : **rr** =&nbsp;1 / (1/rr0 + tauMin)&emsp;(exposed as **rr**)
    





````

(schema:tauinftransition)=

## tauInfTransition




extends {ref}`schema:kstransition`



<i>KS Transition specified in terms of time constant  {ref}`schema:tau` and steady state  {ref}`schema:inf`.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**timeCourse**$  $ {ref}`schema:basevoltagedeptime`
**steadyState**$  $ {ref}`schema:basevoltagedepvariable`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**rf**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`
**rr**$  *(from {ref}`schema:kstransition`)* ${ref}`schema:dimensions:per_time`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **tau** =&nbsp;timeCourse->t
    : **inf** =&nbsp;steadyState->x
    : **rf** =&nbsp;inf/tau&emsp;(exposed as **rf**)
    : **rr** =&nbsp;(1-inf)/tau&emsp;(exposed as **rr**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=TauInfTransition" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import TauInfTransition

variable = TauInfTransition(neuro_lex_id=None, id=None, from_=None, to=None, steady_state=None, time_course=None, **kwargs_)
```



````

(schema:gateks)=

## gateKS




extends *{ref}`schema:basegate`*



<i>A gate which consists of multiple  {ref}`schema:ksstate`s and  {ref}`schema:kstransition`s giving the rates of transition between them.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**instances**$  *(from {ref}`schema:basegate`)* $Dimensionless

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**states**$  $ {ref}`schema:ksstate`
**transitions**$  $ {ref}`schema:kstransition`
**q10Settings**$  $ {ref}`schema:baseq10settings`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**fcond**$  *(from {ref}`schema:basegate`)* $Dimensionless
**q**$  *(from {ref}`schema:basegate`)* $Dimensionless
**rateScale**$  $Dimensionless

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **rateScale** =&nbsp;q10Settings[*]->q10(reduce method: multiply)&emsp;(exposed as **rateScale**)
    : **q** =&nbsp;states[*]->q(reduce method: add)&emsp;(exposed as **q**)
    : **fcond** =&nbsp;q^instances&emsp;(exposed as **fcond**)
    





````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GateKS" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import GateKS

variable = GateKS(neuro_lex_id=None, id=None, instances=None, notes=None, q10_settings=None, closed_states=None, open_states=None, forward_transition=None, reverse_transition=None, tau_inf_transition=None, **kwargs_)
```



````
