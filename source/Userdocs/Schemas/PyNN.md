
(schema:pynn)=
# PyNN

**A number of ComponentType description of PyNN standard cells. All of the cells extend  {ref}`schema:basepynncell`, and the synapses extend  {ref}`schema:basepynnsynapse`.**

---


Original ComponentType definitions: [PyNN.xml](https://github.com/NeuroML/NeuroML2/blob/documentation_update/NeuroML2CoreTypes//PyNN.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.2.xsd](https://github.com/NeuroML/NeuroML2/tree/documentation_update/Schemas/NeuroML2/NeuroML_v2.2.xsd).
Generated on 24/06/21 from [this](https://github.com/NeuroML/NeuroML2/commit/df98ff09e9b4a38073d8e73c0bd465bbb9acd05a) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basepynncell)=

## *basePyNNCell*




extends *{ref}`schema:basecellmembpot`*



<i>Base type of any PyNN standard cell model. Note: membrane potential **v** has dimensions voltage, but all other parameters are dimensionless. This is to facilitate translation to and from PyNN scripts in Python, where these parameters have implicit units, see http://neuralensemble.org/trac/PyNN/wiki/StandardModels.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  $Dimensionless
**i_offset**$  $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell $Dimensionless
**v_init**$  $Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1mV$  $ {ref}`schema:dimensions:voltage`
**NFARAD** = 1nF$  $ {ref}`schema:dimensions:capacitance`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$ $Direction: in
**spike_in_I**$ $Direction: in

```
````

(schema:basepynniafcell)=

## *basePyNNIaFCell*




extends *{ref}`schema:basepynncell`*



<i>Base type of any PyNN standard integrate and fire model.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  $Dimensionless
**tau_refrac**$  $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  $Dimensionless
**v_rest**$  $Dimensionless
**v_thresh**$  $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

(schema:basepynniafcondcell)=

## *basePyNNIaFCondCell*




extends *{ref}`schema:basepynniafcell`*



<i>Base type of conductance based PyNN IaF cell models.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**e_rev_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell $Dimensionless
**e_rev_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

(schema:if_curr_alpha)=

## IF_curr_alpha




extends *{ref}`schema:basepynniafcell`*



<i>Leaky integrate and fire model with fixed threshold and alpha-function-shaped post-synaptic current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (MVOLT * ((i_offset/cm) +  ((v_rest - (v/MVOLT)) / tau_m))/MSEC) + (iSyn / (cm * NFARAD))
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_curr_alpha" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IF_curr_alpha

variable = IF_curr_alpha(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, tau_m=None, tau_refrac=None, v_reset=None, v_rest=None, v_thresh=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<IF_curr_alpha id="IF_curr_alpha" cm="1.0" i_offset="0.9" tau_m="20.0" tau_refrac="10.0" tau_syn_E="0.5" tau_syn_I="0.5" v_init="-65" v_reset="-62.0" v_rest="-65.0" v_thresh="-52.0"/>
```

````

(schema:if_curr_exp)=

## IF_curr_exp




extends *{ref}`schema:basepynniafcell`*



<i>Leaky integrate and fire model with fixed threshold and decaying-exponential post-synaptic current.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (MVOLT * (((i_offset)/cm) +  ((v_rest - (v/MVOLT)) / tau_m))/MSEC) + (iSyn / (cm * NFARAD))
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_curr_exp" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IF_curr_exp

variable = IF_curr_exp(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, tau_m=None, tau_refrac=None, v_reset=None, v_rest=None, v_thresh=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<IF_curr_exp id="IF_curr_exp" cm="1.0" i_offset="1.0" tau_m="20.0" tau_refrac="8.0" tau_syn_E="5.0" tau_syn_I="5.0" v_init="-65" v_reset="-70.0" v_rest="-65.0" v_thresh="-50.0"/>
```

````

(schema:if_cond_alpha)=

## IF_cond_alpha




extends *{ref}`schema:basepynniafcondcell`*



<i>Leaky integrate and fire model with fixed threshold and alpha-function-shaped post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**e_rev_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**e_rev_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (MVOLT * (((i_offset) / cm) +  ((v_rest - (v / MVOLT)) / tau_m)) / MSEC) + (iSyn / (cm * NFARAD))
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_cond_alpha" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IF_cond_alpha

variable = IF_cond_alpha(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, tau_m=None, tau_refrac=None, v_reset=None, v_rest=None, v_thresh=None, e_rev_E=None, e_rev_I=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<IF_cond_alpha id="IF_cond_alpha" cm="1.0" e_rev_E="0.0" e_rev_I="-70.0" i_offset="0.9" tau_m="20.0" tau_refrac="5.0" tau_syn_E="0.3" tau_syn_I="0.5" v_init="-65" v_reset="-65.0" v_rest="-65.0" v_thresh="-50.0"/>
```
```{code-block} xml
<IF_cond_alpha id="silent_cell" cm="1.0" e_rev_E="0.0" e_rev_I="-70.0" i_offset="0" tau_m="20.0" tau_refrac="5.0" tau_syn_E="5" tau_syn_I="10" v_init="-65" v_reset="-65.0" v_rest="-65.0" v_thresh="-50.0"/>
```

````

(schema:if_cond_exp)=

## IF_cond_exp




extends *{ref}`schema:basepynniafcondcell`*



<i>Leaky integrate and fire model with fixed threshold and exponentially-decaying post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**e_rev_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**e_rev_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **v**: {ref}`schema:dimensions:voltage` &emsp;(exposed as **v**)
: **lastSpikeTime**: {ref}`schema:dimensions:time` 









<i>**On Start**</i>
: **v** = v_init * MVOLT





<i>**Derived Variables**</i>
    : **iSyn** =&nbsp;synapses[*]->i(reduce method: add)&emsp;(exposed as **iSyn**)
    






<i>**Regime: refractory (initial)**</i>
: <i>**On Entry**</i>
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = v_reset \* MVOLT
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; v_thresh * MVOLT THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (MVOLT * (((i_offset)/cm) +  ((v_rest - (v / MVOLT)) / tau_m)) / MSEC) + (iSyn / (cm * NFARAD))
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_cond_exp" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import IF_cond_exp

variable = IF_cond_exp(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, tau_m=None, tau_refrac=None, v_reset=None, v_rest=None, v_thresh=None, e_rev_E=None, e_rev_I=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<IF_cond_exp id="IF_cond_exp" cm="1.0" e_rev_E="0.0" e_rev_I="-70.0" i_offset="1.0" tau_m="20.0" tau_refrac="5.0" tau_syn_E="5.0" tau_syn_I="5.0" v_init="-65" v_reset="-68.0" v_rest="-65.0" v_thresh="-52.0"/>
```

````

(schema:eif_cond_exp_isfa_ista)=

## EIF_cond_exp_isfa_ista




extends *{ref}`schema:basepynniafcondcell`*



<i>Adaptive exponential integrate and fire neuron according to Brette R and Gerstner W ( 2005 ) with exponentially-decaying post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**a**$  $Dimensionless
**b**$  $Dimensionless
**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**delta_T**$  $Dimensionless
**e_rev_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**e_rev_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_w**$  $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_spike**$  $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**eif_threshold**$  $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**w**$  $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
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
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = v_reset \* MVOLT
: &emsp;&emsp; **w** = w+b
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + (tau_refrac*MSEC) THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **w** /dt = (1 / tau_w) * (a * ((v / MVOLT) - v_rest) - w) / MSEC

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; eif_threshold * MVOLT THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (MVOLT * ((-1 * ((v / MVOLT) - v_rest) + delta_I) / tau_m + (i_offset - w) / cm) / MSEC) + (iSyn / (cm * NFARAD))
: &emsp;&emsp; d **w** /dt = (1 / tau_w) * (a * ((v / MVOLT) - v_rest) - w) / MSEC
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=EIF_cond_exp_isfa_ista" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import EIF_cond_exp_isfa_ista

variable = EIF_cond_exp_isfa_ista(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, tau_m=None, tau_refrac=None, v_reset=None, v_rest=None, v_thresh=None, e_rev_E=None, e_rev_I=None, a=None, b=None, delta_T=None, tau_w=None, v_spike=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<EIF_cond_exp_isfa_ista id="EIF_cond_exp_isfa_ista" a="0.0" b="0.0805" cm="0.281" delta_T="2.0" e_rev_E="0.0" e_rev_I="-80.0" i_offset="0.6" tau_m="9.3667" tau_refrac="5" tau_syn_E="5.0" tau_syn_I="5.0" tau_w="144.0" v_init="-65" v_reset="-68.0" v_rest="-70.6" v_spike="-40.0" v_thresh="-52.0"/>
```

````

(schema:eif_cond_alpha_isfa_ista)=

## EIF_cond_alpha_isfa_ista




extends *{ref}`schema:basepynniafcondcell`*



<i>Adaptive exponential integrate and fire neuron according to Brette R and Gerstner W ( 2005 ) with alpha-function-shaped post-synaptic conductance.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**a**$  $Dimensionless
**b**$  $Dimensionless
**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**delta_T**$  $Dimensionless
**e_rev_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**e_rev_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynniafcondcell`)* $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_m**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_refrac**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_w**$  $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_reset**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_rest**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless
**v_spike**$  $Dimensionless
**v_thresh**$  *(from {ref}`schema:basepynniafcell`)* $Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**eif_threshold**$  $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**w**$  $Dimensionless

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
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
: &emsp;&emsp; **lastSpikeTime** = t
: &emsp;&emsp; **v** = v_reset \* MVOLT
: &emsp;&emsp; **w** = w + b
: <i>**On Conditions**</i>
: &emsp;&emsp; IF t &gt; lastSpikeTime + (tau_refrac * MSEC) THEN
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **integrating**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **w** /dt = (1 / tau_w) * (a * ((v / MVOLT) - v_rest) - w) / MSEC

<i>**Regime: integrating (initial)**</i>
: <i>**On Conditions**</i>
: &emsp;&emsp; IF v &gt; eif_threshold * MVOLT THEN
: &emsp;&emsp;&emsp;&emsp;EVENT OUT on port: **spike**
: &emsp;&emsp;&emsp;&emsp;TRANSITION to REGIME **refractory**
: <i>**Time Derivatives**</i>
: &emsp;&emsp; d **v** /dt = (MVOLT * ((-1 * ( (v / MVOLT) - v_rest) + delta_I) / tau_m + (i_offset - w) / cm) / MSEC) + (iSyn / (cm * NFARAD))
: &emsp;&emsp; d **w** /dt = (1/ tau_w) * (a*((v/MVOLT)-v_rest) - w) /MSEC
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=EIF_cond_alpha_isfa_ista" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import EIF_cond_alpha_isfa_ista

variable = EIF_cond_alpha_isfa_ista(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, tau_m=None, tau_refrac=None, v_reset=None, v_rest=None, v_thresh=None, e_rev_E=None, e_rev_I=None, a=None, b=None, delta_T=None, tau_w=None, v_spike=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<EIF_cond_alpha_isfa_ista id="EIF_cond_alpha_isfa_ista" a="0.0" b="0.0805" cm="0.281" delta_T="0" e_rev_E="0.0" e_rev_I="-80.0" i_offset="0.6" tau_m="9.3667" tau_refrac="5" tau_syn_E="5.0" tau_syn_I="5.0" tau_w="144.0" v_init="-65" v_reset="-68.0" v_rest="-70.6" v_spike="-40.0" v_thresh="-52.0"/>
```

````

(schema:hh_cond_exp)=

## HH_cond_exp




extends *{ref}`schema:basepynncell`*



<i>Single-compartment Hodgkin-Huxley-type neuron with transient sodium and delayed-rectifier potassium currents using the ion channel models from Traub.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**cm**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**e_rev_E**$  $Dimensionless
**e_rev_I**$  $Dimensionless
**e_rev_K**$  $Dimensionless
**e_rev_Na**$  $Dimensionless
**e_rev_leak**$  $Dimensionless
**g_leak**$  $Dimensionless
**gbar_K**$  $Dimensionless
**gbar_Na**$  $Dimensionless
**i_offset**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_E**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**tau_syn_I**$ This parameter is never used in the NeuroML2 description of this cell! Any synapse producing a current can be placed on this cell *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_init**$  *(from {ref}`schema:basepynncell`)* $Dimensionless
**v_offset**$  $Dimensionless

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**h**$  $Dimensionless
**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**m**$  $Dimensionless
**n**$  $Dimensionless
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tabbed} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
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

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=HH_cond_exp" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import HH_cond_exp

variable = HH_cond_exp(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, cm=None, i_offset=None, tau_syn_E=None, tau_syn_I=None, v_init=None, v_offset=None, e_rev_E=None, e_rev_I=None, e_rev_K=None, e_rev_Na=None, e_rev_leak=None, g_leak=None, gbar_K=None, gbar_Na=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<HH_cond_exp id="HH_cond_exp" cm="0.2" e_rev_E="0.0" e_rev_I="-80.0" e_rev_K="-90.0" e_rev_Na="50.0" e_rev_leak="-65.0" g_leak="0.01" gbar_K="6.0" gbar_Na="20.0" i_offset="0.2" tau_syn_E="0.2" tau_syn_I="2.0" v_init="-65" v_offset="-63.0"/>
```

````

(schema:basepynnsynapse)=

## *basePynnSynapse*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Base type for all PyNN synapses. Note, the current **I** produced is dimensionless, but it requires a membrane potential **v** with dimension voltage.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau_syn**$  $Dimensionless

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1mV$  $ {ref}`schema:dimensions:voltage`
**NAMP** = 1nA$  $ {ref}`schema:dimensions:current`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**i**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BasePynnSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import BasePynnSynapse

variable = BasePynnSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, tau_syn=None, extensiontype_=None, **kwargs_)
```



````

(schema:expcondsynapse)=

## expCondSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Conductance based synapse with instantaneous rise and single exponential decay ( with time constant tau_syn ).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**e_rev**$  $Dimensionless
**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**g**$  $Dimensionless
**i**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **g**: Dimensionless &emsp;(exposed as **g**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**g** = g+weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (e_rev - (v/MVOLT)) * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = -g / (tau_syn*MSEC)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpCondSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ExpCondSynapse

variable = ExpCondSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, tau_syn=None, e_rev=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<expCondSynapse id="syn1" tau_syn="5" e_rev="0"/>
```

````

(schema:expcurrsynapse)=

## expCurrSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Current based synapse with instantaneous rise and single exponential decay ( with time constant tau_syn ).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**i**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **I**: Dimensionless 











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**I** = I + weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;I * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **I** /dt = -I / (tau_syn*MSEC)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpCurrSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ExpCurrSynapse

variable = ExpCurrSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, tau_syn=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<expCurrSynapse id="syn3" tau_syn="5"/>
```

````

(schema:alphacondsynapse)=

## alphaCondSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Alpha synapse: rise time and decay time are both tau_syn. Conductance based synapse.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**e_rev**$  $Dimensionless
**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**A**$  $Dimensionless
**g**$  $Dimensionless
**i**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **g**: Dimensionless &emsp;(exposed as **g**)
: **A**: Dimensionless &emsp;(exposed as **A**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**A** = A + weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (e_rev - (v/MVOLT)) * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = (2.7182818*A - g)/(tau_syn*MSEC)
    : d **A** /dt = -A /(tau_syn*MSEC)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AlphaCondSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import AlphaCondSynapse

variable = AlphaCondSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, tau_syn=None, e_rev=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<alphaCondSynapse id="syn2" tau_syn="5" e_rev="0"/>
```

````

(schema:alphacurrsynapse)=

## alphaCurrSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Alpha synapse: rise time and decay time are both tau_syn. Current based synapse.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**A**$  ${ref}`schema:dimensions:current`
**i**$ The total (time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tabbed} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **I**: Dimensionless 
: **A**: Dimensionless &emsp;(exposed as **A**)











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**A** = A + weight





<i>**Derived Variables**</i>
    : **i** =&nbsp;I * NAMP&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **I** /dt = (2.7182818*A - I)/(tau_syn*MSEC)
    : d **A** /dt = -A /(tau_syn*MSEC)
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AlphaCurrSynapse" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import AlphaCurrSynapse

variable = AlphaCurrSynapse(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, tau_syn=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<alphaCurrSynapse id="syn4" tau_syn="5"/>
```

````

(schema:spikesourcepoisson)=

## SpikeSourcePoisson




extends *{ref}`schema:basespikesource`*



<i>Spike source, generating spikes according to a Poisson process.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**duration**$  ${ref}`schema:dimensions:time`
**rate**$  ${ref}`schema:dimensions:per_time`
**start**$  ${ref}`schema:dimensions:time`

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**end**$  ${ref}`schema:dimensions:time`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**LONG_TIME** = 1e9hour$  $ {ref}`schema:dimensions:time`
**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tabbed} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**isi**$  ${ref}`schema:dimensions:time`
**tnextIdeal**$  ${ref}`schema:dimensions:time`
**tnextUsed**$  ${ref}`schema:dimensions:time`
**tsince**$ Time since the last spike was emitted *(from {ref}`schema:basespikesource`)* ${ref}`schema:dimensions:time`

```
````

````{tabbed} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in
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
: **isi** = start - log(random(1))/rate
: **tsince** = 0
: **tnextIdeal** = isi + H(((isi) - (start+duration))/duration)*LONG_TIME
: **tnextUsed** = tnextIdeal



<i>**On Conditions**</i>

: IF t &gt; tnextUsed THEN
: &emsp;&emsp;&emsp;**isi** = -1 * log(random(1))/rate
: &emsp;&emsp;&emsp;**tnextIdeal** = (tnextIdeal+isi) + H(((tnextIdeal+isi) - (start+duration))/duration)*LONG_TIME
: &emsp;&emsp;&emsp;**tnextUsed** = tnextIdeal*H( (tnextIdeal-t)/t ) + (t+SMALL_TIME)*H( (t-tnextIdeal)/t )
: &emsp;&emsp;&emsp;**tsince** = 0
: &emsp;&emsp;&emsp;EVENT OUT on port: **spike**








<i>**Time Derivatives**</i>
    : d **tsince** /dt = 1
    : d **tnextUsed** /dt = 0
    : d **tnextIdeal** /dt = 0
    

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeSourcePoisson" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SpikeSourcePoisson

variable = SpikeSourcePoisson(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, start=None, duration=None, rate=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<SpikeSourcePoisson id="spikes1" start="50ms" duration="400ms" rate="50Hz"/>
```
```{code-block} xml
<SpikeSourcePoisson id="spikes2" start="50ms" duration="300ms" rate="80Hz"/>
```

````
