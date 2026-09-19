
(schema:pynn_)=
# PyNN

**A number of ComponentType description of PyNN standard cells. All of the cells extend  {ref}`schema:basepynncell`, and the synapses extend  {ref}`schema:basepynnsynapse`.**

---


Original ComponentType definitions: [PyNN.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//PyNN.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basepynncell)=

## *basePyNNCell*




extends *{ref}`schema:basecellmembpot`*



<i>Base type of any PyNN standard cell model. Note: membrane potential **v** has dimensions voltage, but all other parameters are dimensionless. This is to facilitate translation to and from PyNN scripts in Python, where these parameters have implicit units, see http://neuralensemble.org/trac/PyNN/wiki/StandardModels.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1mV$  $ {ref}`schema:dimensions:voltage`
**NFARAD** = 1nF$  $ {ref}`schema:dimensions:capacitance`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$ $Direction: in
**spike_in_I**$ $Direction: in

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="basePyNNCell">
  <xs:complexContent>
    <xs:extension base="BaseCell">
      <xs:attribute name="cm" type="xs:float" use="required"/>
      <xs:attribute name="i_offset" type="xs:float" use="required"/>
      <xs:attribute name="tau_syn_E" type="xs:float" use="required"/>
      <xs:attribute name="tau_syn_I" type="xs:float" use="required"/>
      <xs:attribute name="v_init" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:basepynniafcell)=

## *basePyNNIaFCell*




extends *{ref}`schema:basepynncell`*



<i>Base type of any PyNN standard integrate and fire model.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="basePyNNIaFCell">
  <xs:complexContent>
    <xs:extension base="basePyNNCell">
      <xs:attribute name="tau_m" type="xs:float" use="required"/>
      <xs:attribute name="tau_refrac" type="xs:float" use="required"/>
      <xs:attribute name="v_reset" type="xs:float" use="required"/>
      <xs:attribute name="v_rest" type="xs:float" use="required"/>
      <xs:attribute name="v_thresh" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:basepynniafcondcell)=

## *basePyNNIaFCondCell*




extends *{ref}`schema:basepynniafcell`*



<i>Base type of conductance based PyNN IaF cell models.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="basePyNNIaFCondCell">
  <xs:complexContent>
    <xs:extension base="basePyNNIaFCell">
      <xs:attribute name="e_rev_E" type="xs:float" use="required"/>
      <xs:attribute name="e_rev_I" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````
`````

(schema:if_curr_alpha)=

## IF_curr_alpha




extends *{ref}`schema:basepynniafcell`*



<i>Leaky integrate and fire model with fixed threshold and alpha-function-shaped post-synaptic current.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IF_curr_alpha">
  <xs:complexContent>
    <xs:extension base="basePyNNIaFCell">
            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_curr_alpha" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IF_curr_alpha
from neuroml.utils import component_factory

variable = component_factory(
    IF_curr_alpha,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    tau_m: 'a float (required)' = None,
    tau_refrac: 'a float (required)' = None,
    v_reset: 'a float (required)' = None,
    v_rest: 'a float (required)' = None,
    v_thresh: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<IF_curr_alpha id="IF_curr_alpha" cm="1.0" i_offset="0.9" tau_m="20.0" tau_refrac="10.0" tau_syn_E="0.5" tau_syn_I="0.5" v_init="-65" v_reset="-62.0" v_rest="-65.0" v_thresh="-52.0"/>
```
````
`````

(schema:if_curr_exp)=

## IF_curr_exp




extends *{ref}`schema:basepynniafcell`*



<i>Leaky integrate and fire model with fixed threshold and decaying-exponential post-synaptic current.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IF_curr_exp">
  <xs:complexContent>
    <xs:extension base="basePyNNIaFCell">
            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_curr_exp" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IF_curr_exp
from neuroml.utils import component_factory

variable = component_factory(
    IF_curr_exp,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    tau_m: 'a float (required)' = None,
    tau_refrac: 'a float (required)' = None,
    v_reset: 'a float (required)' = None,
    v_rest: 'a float (required)' = None,
    v_thresh: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<IF_curr_exp id="IF_curr_exp" cm="1.0" i_offset="1.0" tau_m="20.0" tau_refrac="8.0" tau_syn_E="5.0" tau_syn_I="5.0" v_init="-65" v_reset="-70.0" v_rest="-65.0" v_thresh="-50.0"/>
```
````
`````

(schema:if_cond_alpha)=

## IF_cond_alpha




extends *{ref}`schema:basepynniafcondcell`*



<i>Leaky integrate and fire model with fixed threshold and alpha-function-shaped post-synaptic conductance.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IF_cond_alpha">
  <xs:complexContent>
    <xs:extension base="basePyNNIaFCondCell">
            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_cond_alpha" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IF_cond_alpha
from neuroml.utils import component_factory

variable = component_factory(
    IF_cond_alpha,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    tau_m: 'a float (required)' = None,
    tau_refrac: 'a float (required)' = None,
    v_reset: 'a float (required)' = None,
    v_rest: 'a float (required)' = None,
    v_thresh: 'a float (required)' = None,
    e_rev_E: 'a float (required)' = None,
    e_rev_I: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<IF_cond_alpha id="IF_cond_alpha" cm="1.0" e_rev_E="0.0" e_rev_I="-70.0" i_offset="0.9" tau_m="20.0" tau_refrac="5.0" tau_syn_E="0.3" tau_syn_I="0.5" v_init="-65" v_reset="-65.0" v_rest="-65.0" v_thresh="-50.0"/>
```
```{code-block} xml
<IF_cond_alpha id="silent_cell" cm="1.0" e_rev_E="0.0" e_rev_I="-70.0" i_offset="0" tau_m="20.0" tau_refrac="5.0" tau_syn_E="5" tau_syn_I="10" v_init="-65" v_reset="-65.0" v_rest="-65.0" v_thresh="-50.0"/>
```
````
`````

(schema:if_cond_exp)=

## IF_cond_exp




extends *{ref}`schema:basepynniafcondcell`*



<i>Leaky integrate and fire model with fixed threshold and exponentially-decaying post-synaptic conductance.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="IF_cond_exp">
  <xs:complexContent>
    <xs:extension base="basePyNNIaFCondCell">
            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=IF_cond_exp" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import IF_cond_exp
from neuroml.utils import component_factory

variable = component_factory(
    IF_cond_exp,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    tau_m: 'a float (required)' = None,
    tau_refrac: 'a float (required)' = None,
    v_reset: 'a float (required)' = None,
    v_rest: 'a float (required)' = None,
    v_thresh: 'a float (required)' = None,
    e_rev_E: 'a float (required)' = None,
    e_rev_I: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<IF_cond_exp id="IF_cond_exp" cm="1.0" e_rev_E="0.0" e_rev_I="-70.0" i_offset="1.0" tau_m="20.0" tau_refrac="5.0" tau_syn_E="5.0" tau_syn_I="5.0" v_init="-65" v_reset="-68.0" v_rest="-65.0" v_thresh="-52.0"/>
```
````
`````

(schema:eif_cond_exp_isfa_ista)=

## EIF_cond_exp_isfa_ista




extends *{ref}`schema:basepynniafcondcell`*



<i>Adaptive exponential integrate and fire neuron according to Brette R and Gerstner W ( 2005 ) with exponentially-decaying post-synaptic conductance.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**eif_threshold**$  $Dimensionless
```
&emsp;&emsp;&emsp;**eif_threshold** = v_spike * H(delta_T-1e-12) + v_thresh * H(-1*delta_T+1e-9)

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**w**$  $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EIF_cond_exp_isfa_ista">
  <xs:complexContent>
    <xs:extension base="basePyNNIaFCondCell">
      <xs:attribute name="a" type="xs:float" use="required"/>
      <xs:attribute name="b" type="xs:float" use="required"/>
      <xs:attribute name="delta_T" type="xs:float" use="required"/>
      <xs:attribute name="tau_w" type="xs:float" use="required"/>
      <xs:attribute name="v_spike" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=EIF_cond_exp_isfa_ista" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import EIF_cond_exp_isfa_ista
from neuroml.utils import component_factory

variable = component_factory(
    EIF_cond_exp_isfa_ista,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    tau_m: 'a float (required)' = None,
    tau_refrac: 'a float (required)' = None,
    v_reset: 'a float (required)' = None,
    v_rest: 'a float (required)' = None,
    v_thresh: 'a float (required)' = None,
    e_rev_E: 'a float (required)' = None,
    e_rev_I: 'a float (required)' = None,
    a: 'a float (required)' = None,
    b: 'a float (required)' = None,
    delta_T: 'a float (required)' = None,
    tau_w: 'a float (required)' = None,
    v_spike: 'a float (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<EIF_cond_exp_isfa_ista id="EIF_cond_exp_isfa_ista" a="0.0" b="0.0805" cm="0.281" delta_T="2.0" e_rev_E="0.0" e_rev_I="-80.0" i_offset="0.6" tau_m="9.3667" tau_refrac="5" tau_syn_E="5.0" tau_syn_I="5.0" tau_w="144.0" v_init="-65" v_reset="-68.0" v_rest="-70.6" v_spike="-40.0" v_thresh="-52.0"/>
```
````
`````

(schema:eif_cond_alpha_isfa_ista)=

## EIF_cond_alpha_isfa_ista




extends *{ref}`schema:basepynniafcondcell`*



<i>Adaptive exponential integrate and fire neuron according to Brette R and Gerstner W ( 2005 ) with alpha-function-shaped post-synaptic conductance.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**eif_threshold**$  $Dimensionless
```
&emsp;&emsp;&emsp;**eif_threshold** = v_spike * H(delta_T-1e-12) + v_thresh * H(-1*delta_T+1e-9)

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**iSyn**$  *(from {ref}`schema:basepynncell`)* ${ref}`schema:dimensions:current`
**v**$ Membrane potential *(from {ref}`schema:basecellmembpot`)* ${ref}`schema:dimensions:voltage`
**w**$  $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="EIF_cond_alpha_isfa_ista">
  <xs:complexContent>
    <xs:extension base="EIF_cond_exp_isfa_ista">
            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=EIF_cond_alpha_isfa_ista" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import EIF_cond_alpha_isfa_ista
from neuroml.utils import component_factory

variable = component_factory(
    EIF_cond_alpha_isfa_ista,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    tau_m: 'a float (required)' = None,
    tau_refrac: 'a float (required)' = None,
    v_reset: 'a float (required)' = None,
    v_rest: 'a float (required)' = None,
    v_thresh: 'a float (required)' = None,
    e_rev_E: 'a float (required)' = None,
    e_rev_I: 'a float (required)' = None,
    a: 'a float (required)' = None,
    b: 'a float (required)' = None,
    delta_T: 'a float (required)' = None,
    tau_w: 'a float (required)' = None,
    v_spike: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<EIF_cond_alpha_isfa_ista id="EIF_cond_alpha_isfa_ista" a="0.0" b="0.0805" cm="0.281" delta_T="0" e_rev_E="0.0" e_rev_I="-80.0" i_offset="0.6" tau_m="9.3667" tau_refrac="5" tau_syn_E="5.0" tau_syn_I="5.0" tau_w="144.0" v_init="-65" v_reset="-68.0" v_rest="-70.6" v_spike="-40.0" v_thresh="-52.0"/>
```
````
`````

(schema:hh_cond_exp)=

## HH_cond_exp




extends *{ref}`schema:basepynncell`*



<i>Single-compartment Hodgkin-Huxley-type neuron with transient sodium and delayed-rectifier potassium currents using the ion channel models from Traub.</i>


`````{tab-set}
````{tab-item} Parameters
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

````{tab-item} Exposures
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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**spike**$ Spike event *(from {ref}`schema:basespikingcell`)*$Direction: out
**spike_in_E**$  *(from {ref}`schema:basepynncell`)*$Direction: in
**spike_in_I**$  *(from {ref}`schema:basepynncell`)*$Direction: in

```
````

````{tab-item} Attachments
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapses**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="HH_cond_exp">
  <xs:complexContent>
    <xs:extension base="basePyNNCell">
      <xs:attribute name="v_offset" type="xs:float" use="required"/>
      <xs:attribute name="e_rev_E" type="xs:float" use="required"/>
      <xs:attribute name="e_rev_I" type="xs:float" use="required"/>
      <xs:attribute name="e_rev_K" type="xs:float" use="required"/>
      <xs:attribute name="e_rev_Na" type="xs:float" use="required"/>
      <xs:attribute name="e_rev_leak" type="xs:float" use="required"/>
      <xs:attribute name="g_leak" type="xs:float" use="required"/>
      <xs:attribute name="gbar_K" type="xs:float" use="required"/>
      <xs:attribute name="gbar_Na" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=HH_cond_exp" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import HH_cond_exp
from neuroml.utils import component_factory

variable = component_factory(
    HH_cond_exp,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    cm: 'a float (required)' = None,
    i_offset: 'a float (required)' = None,
    tau_syn_E: 'a float (required)' = None,
    tau_syn_I: 'a float (required)' = None,
    v_init: 'a float (required)' = None,
    v_offset: 'a float (required)' = None,
    e_rev_E: 'a float (required)' = None,
    e_rev_I: 'a float (required)' = None,
    e_rev_K: 'a float (required)' = None,
    e_rev_Na: 'a float (required)' = None,
    e_rev_leak: 'a float (required)' = None,
    g_leak: 'a float (required)' = None,
    gbar_K: 'a float (required)' = None,
    gbar_Na: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<HH_cond_exp id="HH_cond_exp" cm="0.2" e_rev_E="0.0" e_rev_I="-80.0" e_rev_K="-90.0" e_rev_Na="50.0" e_rev_leak="-65.0" g_leak="0.01" gbar_K="6.0" gbar_Na="20.0" i_offset="0.2" tau_syn_E="0.2" tau_syn_I="2.0" v_init="-65" v_offset="-63.0"/>
```
````
`````

(schema:basepynnsynapse)=

## *basePynnSynapse*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Base type for all PyNN synapses. Note, the current **I** produced is dimensionless, but it requires a membrane potential **v** with dimension voltage.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau_syn**$  $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MSEC** = 1ms$  $ {ref}`schema:dimensions:time`
**MVOLT** = 1mV$  $ {ref}`schema:dimensions:voltage`
**NAMP** = 1nA$  $ {ref}`schema:dimensions:current`

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

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BasePynnSynapse">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">
      <xs:attribute name="tau_syn" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BasePynnSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BasePynnSynapse
from neuroml.utils import component_factory

variable = component_factory(
    BasePynnSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    tau_syn: 'a float (required)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:expcondsynapse)=

## expCondSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Conductance based synapse with instantaneous rise and single exponential decay ( with time constant tau_syn ).</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**e_rev**$  $Dimensionless
**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**g**$  $Dimensionless
**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ExpCondSynapse">
  <xs:complexContent>
    <xs:extension base="BasePynnSynapse">
      <xs:attribute name="e_rev" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpCondSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ExpCondSynapse
from neuroml.utils import component_factory

variable = component_factory(
    ExpCondSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    tau_syn: 'a float (required)' = None,
    e_rev: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<expCondSynapse id="syn1" tau_syn="5" e_rev="0"/>
```
````
`````

(schema:expcurrsynapse)=

## expCurrSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Current based synapse with instantaneous rise and single exponential decay ( with time constant tau_syn ).</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ExpCurrSynapse">
  <xs:complexContent>
    <xs:extension base="BasePynnSynapse">

            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpCurrSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ExpCurrSynapse
from neuroml.utils import component_factory

variable = component_factory(
    ExpCurrSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    tau_syn: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<expCurrSynapse id="syn3" tau_syn="5"/>
```
````
`````

(schema:alphacondsynapse)=

## alphaCondSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Alpha synapse: rise time and decay time are both tau_syn. Conductance based synapse.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**e_rev**$  $Dimensionless
**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**A**$  $Dimensionless
**g**$  $Dimensionless
**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="AlphaCondSynapse">
  <xs:complexContent>
    <xs:extension base="BasePynnSynapse">
      <xs:attribute name="e_rev" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AlphaCondSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import AlphaCondSynapse
from neuroml.utils import component_factory

variable = component_factory(
    AlphaCondSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    tau_syn: 'a float (required)' = None,
    e_rev: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<alphaCondSynapse id="syn2" tau_syn="5" e_rev="0"/>
```
````
`````

(schema:alphacurrsynapse)=

## alphaCurrSynapse




extends *{ref}`schema:basepynnsynapse`*



<i>Alpha synapse: rise time and decay time are both tau_syn. Current based synapse.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**tau_syn**$  *(from {ref}`schema:basepynnsynapse`)* $Dimensionless

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

**A**$  ${ref}`schema:dimensions:current`
**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`

```
````

````{tab-item} Requirements
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**v**$ The current may vary with the voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedepsynapse`)* ${ref}`schema:dimensions:voltage`

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Dynamics



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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="AlphaCurrSynapse">
  <xs:complexContent>
    <xs:extension base="BasePynnSynapse">

            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AlphaCurrSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import AlphaCurrSynapse
from neuroml.utils import component_factory

variable = component_factory(
    AlphaCurrSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    tau_syn: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<alphaCurrSynapse id="syn4" tau_syn="5"/>
```
````
`````

(schema:spikesourcepoisson)=

## SpikeSourcePoisson




extends *{ref}`schema:basespikesource`*



<i>Spike source, generating spikes according to a Poisson process.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**duration**$  ${ref}`schema:dimensions:time`
**rate**$  ${ref}`schema:dimensions:per_time`
**start**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**LONG_TIME** = 1e9hour$  $ {ref}`schema:dimensions:time`
**SMALL_TIME** = 1e-9ms$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**end**$  ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**end** = start + duration

````

````{tab-item} Exposures
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

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ $Direction: in
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SpikeSourcePoisson">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="start" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="duration" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="rate" type="Nml2Quantity_pertime" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SpikeSourcePoisson" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SpikeSourcePoisson
from neuroml.utils import component_factory

variable = component_factory(
    SpikeSourcePoisson,
    id: 'a NonNegativeInteger (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    start: 'a Nml2Quantity_time (required)' = None,
    duration: 'a Nml2Quantity_time (required)' = None,
    rate: 'a Nml2Quantity_pertime (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<SpikeSourcePoisson id="spikes1" start="50ms" duration="400ms" rate="50Hz"/>
```
```{code-block} xml
<SpikeSourcePoisson id="spikes2" start="50ms" duration="300ms" rate="80Hz"/>
```
````
`````
