
(schema:pynn)=
# PyNN



Original ComponentType definitions: [PyNN.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//PyNN.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 23/03/21 from [this](https://github.com/NeuroML/NeuroML2/commit/ec9d81a59ca05189c89bf48cf3ea06241c917eb5) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:basepynncell)=

## *basePyNNCell*




extends *{ref}`schema:basecellmembpot`*



<i>Base type of any PyNN standard cell model. Note: membrane potential **v** has dimensions voltage, but all other parameters are dimensionless. This is to facilitate translation to and from PyNN scripts in Python, where these parameters have implicit units, see http://neuralensemble.org/trac/PyNN/wiki/StandardModels.</i>



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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

iSyn,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
spike_in_E,Direction: in
spike_in_I,Direction: in

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (MVOLT * ((i_offset/cm) +  ((v_rest - (v/MVOLT)) / tau_m))/MSEC) + (iSyn / (cm * NFARAD))
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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (MVOLT * (((i_offset)/cm) +  ((v_rest - (v/MVOLT)) / tau_m))/MSEC) + (iSyn / (cm * NFARAD))
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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (MVOLT * (((i_offset) / cm) +  ((v_rest - (v / MVOLT)) / tau_m)) / MSEC) + (iSyn / (cm * NFARAD))
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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (MVOLT * (((i_offset)/cm) +  ((v_rest - (v / MVOLT)) / tau_m)) / MSEC) + (iSyn / (cm * NFARAD))
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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`
w,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **w**: Dimensionless &emsp;(exposed as **w**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT
: **w** = 0





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    



<i>**Conditional Derived Variables**</i>
    
: IF delta_T &gt; 0 THEN
: &emsp; **delta_I** = delta_T \* exp(((v / MVOLT) - v_thresh) / delta_T) 
: IF delta_T = 0 THEN
: &emsp; **delta_I** = 0 



<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = v_reset \* MVOLT
: &emsp; **w** = w+b
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**
: <i>**Time derivatives**</i>
: &emsp; d **w** /dt = (1 / tau_w) * (a * ((v / MVOLT) - v_rest) - w) / MSEC

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; eif_threshold * MVOLT THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (MVOLT * ((-1 * ((v / MVOLT) - v_rest) + delta_I) / tau_m + (i_offset - w) / cm) / MSEC) + (iSyn / (cm * NFARAD))
: &emsp; d **w** /dt = (1 / tau_w) * (a * ((v / MVOLT) - v_rest) - w) / MSEC
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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`
w,Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **w**: Dimensionless &emsp;(exposed as **w**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT
: **w** = 0





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    



<i>**Conditional Derived Variables**</i>
    
: IF delta_T &gt; 0 THEN
: &emsp; **delta_I** = delta_T \* exp(((v / MVOLT) - v_thresh) / delta_T) 
: IF delta_T = 0 THEN
: &emsp; **delta_I** = 0 



<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp; **lastSpikeTime** = t
: &emsp; **v** = v_reset \* MVOLT
: &emsp; **w** = w + b
: <i>**On Conditions**</i>
: &emsp; IF t &gt; lastSpikeTime + (tau_refrac * MSEC) THEN
: &emsp;&emsp;TRANSITION to REGIME **integrating**
: <i>**Time derivatives**</i>
: &emsp; d **w** /dt = (1 / tau_w) * (a * ((v / MVOLT) - v_rest) - w) / MSEC

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp; IF v &gt; eif_threshold * MVOLT THEN
: &emsp;&emsp;EVENT OUT on port **spike**
: &emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time derivatives**</i>
: &emsp; d **v** /dt = (MVOLT * ((-1 * ( (v / MVOLT) - v_rest) + delta_I) / tau_m + (i_offset - w) / cm) / MSEC) + (iSyn / (cm * NFARAD))
: &emsp; d **w** /dt = (1/ tau_w) * (a*((v/MVOLT)-v_rest) - w) /MSEC
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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

h,Dimensionless
*iSyn (from {ref}`schema:basepynncell`)*,{ref}`schema:dimensions:current`
m,Dimensionless
n,Dimensionless
*v (from {ref}`schema:basecellmembpot`)*,{ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 8, 2
:width: 100%

*spike (from {ref}`schema:basespikingcell`)*,Direction: out
*spike_in_E (from {ref}`schema:basepynncell`)*,Direction: in
*spike_in_I (from {ref}`schema:basepynncell`)*,Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 8, 2
:width: 100%

synapses, {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **m**: Dimensionless &emsp;(exposed as **m**)
: **h**: Dimensionless &emsp;(exposed as **h**)
: **n**: Dimensionless &emsp;(exposed as **n**)









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    : **iLeak** =&nbsp;g_leak * (e_rev_leak - (v / MVOLT))
    : **iNa** =&nbsp;gbar_Na * (m * m * m) * h * (e_rev_Na - (v / MVOLT))
    : **iK** =&nbsp;gbar_K * (n * n * n * n) * (e_rev_K - (v / MVOLT))
    : **iMemb** =&nbsp;iLeak + iNa + iK + i_offset
    : **alpham** =&nbsp;0.32 * (13 - (v / MVOLT) + v_offset) / (exp((13 - (v / MVOLT) + v_offset) / 4.0) - 1)
    : **betam** =&nbsp;0.28 * ((v / MVOLT) - v_offset - 40) / (exp(((v / MVOLT) - v_offset - 40) / 5.0) - 1)
    : **alphah** =&nbsp;0.128 * exp((17 - (v / MVOLT) + v_offset) / 18.0)
    : **betah** =&nbsp;4.0 / (1 + exp((40 - (v / MVOLT) + v_offset) / 5))
    : **alphan** =&nbsp;0.032 * (15 - (v / MVOLT) + v_offset) / (exp((15 - (v / MVOLT) + v_offset) / 5) - 1)
    : **betan** =&nbsp;0.5 * exp((10 - (v / MVOLT) + v_offset) / 40)
    





<i>**Time Derivatives**</i>
    : d **v** /dt = (MVOLT * (iMemb / cm) / MSEC) + (iSyn / (cm * NFARAD))
    : d **m** /dt = (alpham * (1 - m) - betam * m) / MSEC
    : d **h** /dt = (alphah * (1 - h) - betah * h) / MSEC
    : d **n** /dt = (alphan * (1 - n) - betan * n) / MSEC
    

````

(schema:basepynnsynapse)=

## *basePynnSynapse*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Base type for all PyNN synapses. Note, the current **I** produced is dimensionless, but it requires a membrane potential **v** with dimension voltage.</i>



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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

g,Dimensionless
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
: **g**: Dimensionless &emsp;(exposed as **g**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**g** = g+weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (e_rev - (v/MVOLT)) * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = -g / (tau_syn*MSEC)
    

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

```
````

````{tabbed} Dynamics



<i>**State variables**</i>
: **I**: Dimensionless 











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**I** = I + weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;I * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **I** /dt = -I / (tau_syn*MSEC)
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

A,Dimensionless
g,Dimensionless
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
: **g**: Dimensionless &emsp;(exposed as **g**)
: **A**: Dimensionless &emsp;(exposed as **A**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (e_rev - (v/MVOLT)) * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = (2.7182818*A - g)/(tau_syn*MSEC)
    : d **A** /dt = -A /(tau_syn*MSEC)
    

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

````{tabbed} Exposures
```{csv-table}
:widths: 8, 2
:width: 100%

A,{ref}`schema:dimensions:current`
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
: **I**: Dimensionless 
: **A**: Dimensionless &emsp;(exposed as **A**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;**A** = A + weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;I * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **I** /dt = (2.7182818*A - I)/(tau_syn*MSEC)
    : d **A** /dt = -A /(tau_syn*MSEC)
    

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

in,Direction: in
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
: **isi** = start - log(random(1))/rate
: **tsince** = 0
: **tnextIdeal** = isi + H(((isi) - (start+duration))/duration)*LONG_TIME
: **tnextUsed** = tnextIdeal



<i>**On Conditions**</i>

: IF t &gt; tnextUsed THEN
: &emsp;**isi** = -1 * log(random(1))/rate
: &emsp;**tnextIdeal** = (tnextIdeal+isi) + H(((tnextIdeal+isi) - (start+duration))/duration)*LONG_TIME
: &emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;**tsince** = 0
: &emsp;EVENT OUT on port **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

````
