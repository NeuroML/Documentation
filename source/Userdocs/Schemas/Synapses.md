
(schema:synapses)=
# Synapses



Original ComponentType definitions: [Synapses.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Synapses.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 25/02/21 from [this](https://github.com/NeuroML/NeuroML2/commit/6e4643d0eaa7246982b351a01e28856eeb320500) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:basesynapse)=

## *baseSynapse*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all synapses, i.e. ComponentTypes which produce a current (dimension current) and change Dynamics in response to an incoming event. .</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseSynapse.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000009)


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

(schema:basevoltagedepsynapse)=

## *baseVoltageDepSynapse*




extends *{ref}`schema:basesynapse`*



<i>Base type for synapses with a dependence on membrane potential.</i>



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

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

(schema:basesynapsedl)=

## *baseSynapseDL*




extends *{ref}`schema:basevoltagedeppointcurrentdl`*



<i>Base type for all synapses, i.e. ComponentTypes which produce a dimensionless current and change Dynamics in response to an incoming event. .</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseSynapseDL.](http://bioportal.bioontology.org/ontologies/46856/?p=terms&conceptid=cno:cno_0000009)


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

*V (from {ref}`schema:basevoltagedeppointcurrentdl`)*,Dimensionless

```
````

(schema:basecurrentbasedsynapse)=

## *baseCurrentBasedSynapse*




extends *{ref}`schema:basesynapse`*



<i>Synapse model which produces a synaptic current.</i>



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

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

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

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **I**: {ref}`schema:dimensions:current` 
: **J**: {ref}`schema:dimensions:current` 









<i>**On Start**</i>
: **I** = 0
: **J** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**J** = J + weight * ibase





<i>**Derived Variables**</i>
    : **i** =&nbsp;I&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **I** /dt = (2.7182818284590451*J - I)/tau
    : d **J** /dt = -J/tau
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

g,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

g,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*g (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **g**: {ref}`schema:dimensions:conductance` &emsp;(exposed as **g**)









<i>**On Start**</i>
: **g** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**g** = g + (weight * gbase)





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = -g / tauDecay
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*g (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **g**: {ref}`schema:dimensions:conductance` &emsp;(exposed as **g**)
: **A**: {ref}`schema:dimensions:conductance` 









<i>**On Start**</i>
: **g** = 0
: **A** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + (gbase*weight)





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = (2.7182818284590451 * A - g)/tau
    : d **A** /dt = -A / tau
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*g (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **A**: Dimensionless 
: **B**: Dimensionless 









<i>**On Start**</i>
: **A** = 0
: **B** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + (weight * waveformFactor)
: &emsp;**B** = B + (weight * waveformFactor)





<i>**Derived Variables**</i>
    : **g** =&nbsp;gbase * (B - A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*g (from {ref}`schema:baseconductancebasedsynapsetwo`)*,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **A**: Dimensionless 
: **B**: Dimensionless 
: **C**: Dimensionless 









<i>**On Start**</i>
: **A** = 0
: **B** = 0
: **C** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + (gbase1*weight * waveformFactor1 + gbase2*weight*waveformFactor2 )/(gbase1+gbase2)
: &emsp;**B** = B + (weight * waveformFactor1)
: &emsp;**C** = C + (weight * waveformFactor2)





<i>**Derived Variables**</i>
    : **g** =&nbsp;gbase1*(B - A) + gbase2*(C-A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay1
    : d **C** /dt = -C / tauDecay2
    

````

(schema:baseblockmechanism)=

## *baseBlockMechanism*




<i>Base of any ComponentType which produces a varying scaling (or blockage) of synaptic strength of magnitude _scaling.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

blockFactor,Dimensionless

```
````

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*blockFactor (from {ref}`schema:baseblockmechanism`)*,Dimensionless

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

v,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **blockFactor** =&nbsp;1/(1 + (blockConcentration / scalingConc)* exp(-1 * (v / scalingVolt)))&emsp;(exposed as **blockFactor**)
    





````

(schema:baseplasticitymechanism)=

## *basePlasticityMechanism*




<i>Base plasticity mechanism.</i>



````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

plasticityFactor,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

in,Direction: in

```
````

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*plasticityFactor (from {ref}`schema:baseplasticitymechanism`)*,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:baseplasticitymechanism`)*,Direction: in

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **parent** AS **a**
: WITH **this** AS **b**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
: **R**: Dimensionless 









<i>**On Start**</i>
: **R** = 1


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**R** = R * (1 - U)





<i>**Derived Variables**</i>
    : **U** =&nbsp;initReleaseProb
    : **plasticityFactor** =&nbsp;R * U&emsp;(exposed as **plasticityFactor**)
    





<i>**Time Derivatives**</i>
    : d **R** /dt = (1 - R) / tauRec
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*plasticityFactor (from {ref}`schema:baseplasticitymechanism`)*,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:baseplasticitymechanism`)*,Direction: in

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **parent** AS **a**
: WITH **this** AS **b**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
: **R**: Dimensionless 
: **U**: Dimensionless 









<i>**On Start**</i>
: **R** = 1
: **U** = initReleaseProb


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**R** = R * (1 - U)
: &emsp;**U** = U + initReleaseProb * (1 - U)





<i>**Derived Variables**</i>
    : **plasticityFactor** =&nbsp;R * U&emsp;(exposed as **plasticityFactor**)
    





<i>**Time Derivatives**</i>
    : d **R** /dt = (1 - R) / tauRec
    : d **U** /dt = (initReleaseProb - U) / tauFac
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*g (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in
relay,Direction: out

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **A**: Dimensionless 
: **B**: Dimensionless 









<i>**On Start**</i>
: **A** = 0
: **B** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + (weight * plasticityFactor * waveformFactor)
: &emsp;**B** = B + (weight * plasticityFactor * waveformFactor)
: &emsp;EVENT OUT on port **relay**





<i>**Derived Variables**</i>
    : **plasticityFactor** =&nbsp;plasticityMechanisms[*]->plasticityFactor(reduce method: multiply)
    : **blockFactor** =&nbsp;blockMechanisms[*]->blockFactor(reduce method: multiply)
    : **g** =&nbsp;blockFactor * gbase * (B - A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay
    

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

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in
relay,Direction: out

```
````

````{tabbed} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **synapse1Path** AS **b**
: WITH **synapse2Path** AS **c**
: CHILD INSTANCE: **synapse1**
: CHILD INSTANCE: **synapse2**
: EVENT CONNECTION from **a** TO  **c**   

: EVENT CONNECTION from **a** TO  **b**   





<i>**State variables**</i>
: **weightFactor**: Dimensionless 











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**weightFactor** = weight
: &emsp;EVENT OUT on port **relay**





<i>**Derived Variables**</i>
    : **i1** =&nbsp;synapse1->i
    : **i2** =&nbsp;synapse2->i
    : **i** =&nbsp;weightFactor * (i1 + i2)&emsp;(exposed as **i**)
    





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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

M,Dimensionless
P,Dimensionless
*g (from {ref}`schema:baseconductancebasedsynapse`)*,{ref}`schema:dimensions:conductance`
*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`
tsince,{ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 8, 2
:width: 100%

*v (from {ref}`schema:basevoltagedepsynapse`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **A**: Dimensionless 
: **B**: Dimensionless 
: **M**: Dimensionless &emsp;(exposed as **M**)
: **P**: Dimensionless &emsp;(exposed as **P**)
: **tsince**: {ref}`schema:dimensions:time` &emsp;(exposed as **tsince**)









<i>**On Start**</i>
: **A** = 0
: **B** = 0
: **M** = 1
: **P** = 1
: **tsince** = longTime


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + waveformFactor
: &emsp;**B** = B + waveformFactor
: &emsp;**tsince** = 0





<i>**Derived Variables**</i>
    : **g** =&nbsp;gbase * (B - A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay
    : d **tsince** /dt = tsinceRate
    

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

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **i** =&nbsp;weight * conductance * (vpeer - v)&emsp;(exposed as **i**)
    





````

(schema:basegradedsynapse)=

## *baseGradedSynapse*




extends *{ref}`schema:basesynapse`*



<i>Base type for graded synapses.</i>



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

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

(schema:silentsynapse)=

## silentSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Dummy synapse which emits no current. Used as presynaptic endpoint for analog synaptic connection.</i>



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

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **i** =&nbsp;0&emsp;(exposed as **i**)
    





````

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

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics








<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **i** =&nbsp;weight * conductance * (vpeer - v)&emsp;(exposed as **i**)
    





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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*i (from {ref}`schema:basepointcurrent`)*,{ref}`schema:dimensions:current`
inf,Dimensionless
tau,{ref}`schema:dimensions:time`

```
````

````{tabbed} Requirements
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

*in (from {ref}`schema:basesynapse`)*,Direction: in

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **s**: Dimensionless 












<i>**On Conditions**</i>

: IF (1-inf) &lt; 1e-4 THEN
: &emsp;**s** = inf





<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **inf** =&nbsp;1/(1 + exp((Vth - vpeer)/delta))&emsp;(exposed as **inf**)
    : **tau** =&nbsp;(1-inf)/k&emsp;(exposed as **tau**)
    : **i** =&nbsp;weight * conductance * s * (erev-v)&emsp;(exposed as **i**)
    



<i>**Conditional Derived Variables**</i>
    
: IF (1-inf) &gt; 1e-4 THEN
: &emsp; **s_rate** = (inf - s)/tau 
: OTHERWISE
: &emsp; **s_rate** = 0 


<i>**Time Derivatives**</i>
    : d **s** /dt = s_rate
    

````
