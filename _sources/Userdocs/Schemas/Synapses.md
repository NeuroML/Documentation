
(schema:synapses_)=
# Synapses

**A number of synaptic ComponentTypes for use in NeuroML 2 documents, e.g.  {ref}`schema:exponesynapse`,  {ref}`schema:exptwosynapse`,  {ref}`schema:blockingplasticsynapse`. These extend the  {ref}`schema:basesynapse` ComponentType. Also defined continuously transmitting synapses, e.g.  {ref}`schema:gapjunction` and  {ref}`schema:gradedsynapse`.**

---


Original ComponentType definitions: [Synapses.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Synapses.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:basesynapse)=

## *baseSynapse*




extends *{ref}`schema:basepointcurrent`*



<i>Base type for all synapses, i.e. ComponentTypes which produce a current ( dimension current ) and change Dynamics in response to an incoming event.</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseSynapse.](https://bioportal.bioontology.org/ontologies/CNO/?p=classes&conceptid=cno_0000009)

`````{tab-set}
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BaseSynapse">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseSynapse
from neuroml.utils import component_factory

variable = component_factory(
    BaseSynapse,
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

(schema:basevoltagedepsynapse)=

## *baseVoltageDepSynapse*




extends *{ref}`schema:basesynapse`*



<i>Base type for synapses with a dependence on membrane potential.</i>


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
<xs:complexType name="BaseVoltageDepSynapse">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">

            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseVoltageDepSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseVoltageDepSynapse
from neuroml.utils import component_factory

variable = component_factory(
    BaseVoltageDepSynapse,
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

(schema:basesynapsedl)=

## *baseSynapseDL*




extends *{ref}`schema:basevoltagedeppointcurrentdl`*



<i>Base type for all synapses, i.e. ComponentTypes which produce a dimensionless current and change Dynamics in response to an incoming event.</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseSynapseDL.](https://bioportal.bioontology.org/ontologies/CNO/?p=classes&conceptid=cno_0000009)

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

**V**$ The current may vary with the dimensionless voltage exposed by the ComponentType on which this is placed *(from {ref}`schema:basevoltagedeppointcurrentdl`)* $Dimensionless

```
````
`````

(schema:basecurrentbasedsynapse)=

## *baseCurrentBasedSynapse*




extends *{ref}`schema:basesynapse`*



<i>Synapse model which produces a synaptic current.</i>


`````{tab-set}
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

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BaseCurrentBasedSynapse">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">

            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseCurrentBasedSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseCurrentBasedSynapse
from neuroml.utils import component_factory

variable = component_factory(
    BaseCurrentBasedSynapse,
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

(schema:alphacurrentsynapse)=

## alphaCurrentSynapse




extends *{ref}`schema:basecurrentbasedsynapse`*



<i>Alpha current synapse: rise time and decay time are both **tau.**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**ibase**$ Baseline current increase after receiving a spike ${ref}`schema:dimensions:current`
**tau**$ Time course for rise and decay ${ref}`schema:dimensions:time`

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

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **I**: {ref}`schema:dimensions:current` 
: **J**: {ref}`schema:dimensions:current` 









<i>**On Start**</i>
: **I** = 0
: **J** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**J** = J + weight * ibase





<i>**Derived Variables**</i>
    : **i** =&nbsp;I&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **I** /dt = (2.7182818284590451*J - I)/tau
    : d **J** /dt = -J/tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="AlphaCurrentSynapse">
  <xs:complexContent>
    <xs:extension base="BaseCurrentBasedSynapse">
      <xs:attribute name="tau" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="ibase" type="Nml2Quantity_current" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AlphaCurrentSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import AlphaCurrentSynapse
from neuroml.utils import component_factory

variable = component_factory(
    AlphaCurrentSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    tau: 'a Nml2Quantity_time (required)' = None,
    ibase: 'a Nml2Quantity_current (required)' = None,
)
```
````
`````

(schema:baseconductancebasedsynapse)=

## *baseConductanceBasedSynapse*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Synapse model which exposes a conductance **g** in addition to producing a current. Not necessarily ohmic!!</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseConductanceBasedSynapse.](https://bioportal.bioontology.org/ontologies/CNO/?p=classes&conceptid=cno_0000027)

`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse ${ref}`schema:dimensions:voltage`
**gbase**$ Baseline conductance, generally the maximum conductance following a single spike ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**g**$ Time varying conductance through the synapse ${ref}`schema:dimensions:conductance`
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
<xs:complexType name="BaseConductanceBasedSynapse">
  <xs:complexContent>
    <xs:extension base="BaseVoltageDepSynapse">
      <xs:attribute name="gbase" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="erev" type="Nml2Quantity_voltage" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseConductanceBasedSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseConductanceBasedSynapse
from neuroml.utils import component_factory

variable = component_factory(
    BaseConductanceBasedSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:baseconductancebasedsynapsetwo)=

## *baseConductanceBasedSynapseTwo*




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Synapse model suited for a sum of two expTwoSynapses which exposes a conductance **g** in addition to producing a current. Not necessarily ohmic!!</i>


[Bioportal entry for Computational Neuroscience Ontology related to baseConductanceBasedSynapseTwo.](https://bioportal.bioontology.org/ontologies/CNO/?p=classes&conceptid=cno_0000027)

`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse ${ref}`schema:dimensions:voltage`
**gbase1**$ Baseline conductance 1 ${ref}`schema:dimensions:conductance`
**gbase2**$ Baseline conductance 2 ${ref}`schema:dimensions:conductance`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**g**$ Time varying conductance through the synapse ${ref}`schema:dimensions:conductance`
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
<xs:complexType name="BaseConductanceBasedSynapseTwo">
  <xs:complexContent>
    <xs:extension base="BaseVoltageDepSynapse">
      <xs:attribute name="gbase1" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="gbase2" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="erev" type="Nml2Quantity_voltage" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BaseConductanceBasedSynapseTwo" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BaseConductanceBasedSynapseTwo
from neuroml.utils import component_factory

variable = component_factory(
    BaseConductanceBasedSynapseTwo,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase1: 'a Nml2Quantity_conductance (required)' = None,
    gbase2: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:exponesynapse)=

## expOneSynapse




extends *{ref}`schema:baseconductancebasedsynapse`*



<i>Ohmic synapse model whose conductance rises instantaneously by ( **gbase** * **weight** ) on receiving an event, and which decays exponentially to zero with time course **tauDecay**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:voltage`
**gbase**$ Baseline conductance, generally the maximum conductance following a single spike *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
**tauDecay**$ Time course of decay ${ref}`schema:dimensions:time`

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

**g**$ Time varying conductance through the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
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
: **g**: {ref}`schema:dimensions:conductance` &emsp;(exposed as **g**)









<i>**On Start**</i>
: **g** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**g** = g + (weight * gbase)





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = -g / tauDecay
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ExpOneSynapse">
  <xs:complexContent>
    <xs:extension base="BaseConductanceBasedSynapse">
      <xs:attribute name="tauDecay" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpOneSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ExpOneSynapse
from neuroml.utils import component_factory

variable = component_factory(
    ExpOneSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    tau_decay: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<expOneSynapse id="syn1" gbase="5nS" erev="0mV" tauDecay="3ms"/>
```
```{code-block} xml
<expOneSynapse id="syn2" gbase="10nS" erev="0mV" tauDecay="2ms"/>
```
```{code-block} xml
<expOneSynapse id="syn1" gbase="5nS" erev="0mV" tauDecay="3ms"/>
```
````
`````

(schema:alphasynapse)=

## alphaSynapse




extends *{ref}`schema:baseconductancebasedsynapse`*



<i>Ohmic synapse model where rise time and decay time are both **tau.** Max conductance reached during this time ( assuming zero conductance before ) is **gbase** * **weight.**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:voltage`
**gbase**$ Baseline conductance, generally the maximum conductance following a single spike *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
**tau**$ Time course of rise/decay ${ref}`schema:dimensions:time`

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

**g**$ Time varying conductance through the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
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
: **g**: {ref}`schema:dimensions:conductance` &emsp;(exposed as **g**)
: **A**: {ref}`schema:dimensions:conductance` 









<i>**On Start**</i>
: **g** = 0
: **A** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**A** = A + (gbase*weight)





<i>**Derived Variables**</i>
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **g** /dt = (2.7182818284590451 * A - g)/tau
    : d **A** /dt = -A / tau
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="AlphaSynapse">
  <xs:complexContent>
    <xs:extension base="BaseConductanceBasedSynapse">
      <xs:attribute name="tau" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=AlphaSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import AlphaSynapse
from neuroml.utils import component_factory

variable = component_factory(
    AlphaSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    tau: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<alphaSynapse id="synalpha" gbase="0.5nS" erev="0mV" tau="2ms">
    <notes>An alpha synapse with time for rise equal to decay.</notes>
</alphaSynapse>
```
````
`````

(schema:exptwosynapse)=

## expTwoSynapse




extends *{ref}`schema:baseconductancebasedsynapse`*



<i>Ohmic synapse model whose conductance waveform on receiving an event has a rise time of **tauRise** and a decay time of **tauDecay.** Max conductance reached during this time ( assuming zero conductance before ) is **gbase** * **weight.**.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:voltage`
**gbase**$ Baseline conductance, generally the maximum conductance following a single spike *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
**tauDecay**$  ${ref}`schema:dimensions:time`
**tauRise**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**peakTime**$  ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**peakTime** = log(tauDecay / tauRise) * (tauRise * tauDecay)/(tauDecay - tauRise)
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**waveformFactor**$  $Dimensionless
```
&emsp;&emsp;&emsp;**waveformFactor** = 1 / (-exp(-peakTime / tauRise) + exp(-peakTime / tauDecay))

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

**g**$ Time varying conductance through the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
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
: **A**: Dimensionless 
: **B**: Dimensionless 









<i>**On Start**</i>
: **A** = 0
: **B** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**A** = A + (weight * waveformFactor)
: &emsp;&emsp;&emsp;**B** = B + (weight * waveformFactor)





<i>**Derived Variables**</i>
    : **g** =&nbsp;gbase * (B - A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ExpTwoSynapse">
  <xs:complexContent>
    <xs:extension base="BaseConductanceBasedSynapse">
      <xs:attribute name="tauDecay" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="tauRise" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpTwoSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ExpTwoSynapse
from neuroml.utils import component_factory

variable = component_factory(
    ExpTwoSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    tau_decay: 'a Nml2Quantity_time (required)' = None,
    tau_rise: 'a Nml2Quantity_time (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<expTwoSynapse id="AMPA" gbase="0.5nS" erev="0mV" tauRise="1ms" tauDecay="2ms"/>
```
```{code-block} xml
<expTwoSynapse id="synInput" gbase="8nS" erev="20mV" tauRise="1ms" tauDecay="5ms"/>
```
```{code-block} xml
<expTwoSynapse id="synInputFast" gbase="1nS" erev="20mV" tauRise="0.2ms" tauDecay="1ms"/>
```
````
`````

(schema:expthreesynapse)=

## expThreeSynapse




extends *{ref}`schema:baseconductancebasedsynapsetwo`*



<i>Ohmic synapse similar to expTwoSynapse but consisting of two components that can differ in decay times and max conductances but share the same rise time.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse *(from {ref}`schema:baseconductancebasedsynapsetwo`)* ${ref}`schema:dimensions:voltage`
**gbase1**$ Baseline conductance 1 *(from {ref}`schema:baseconductancebasedsynapsetwo`)* ${ref}`schema:dimensions:conductance`
**gbase2**$ Baseline conductance 2 *(from {ref}`schema:baseconductancebasedsynapsetwo`)* ${ref}`schema:dimensions:conductance`
**tauDecay1**$  ${ref}`schema:dimensions:time`
**tauDecay2**$  ${ref}`schema:dimensions:time`
**tauRise**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**peakTime1**$  ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**peakTime1** = log(tauDecay1 / tauRise) * (tauRise * tauDecay1)/(tauDecay1 - tauRise)
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**peakTime2**$  ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**peakTime2** = log(tauDecay2 / tauRise) * (tauRise * tauDecay2)/(tauDecay2 - tauRise)
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**waveformFactor1**$  $Dimensionless
```
&emsp;&emsp;&emsp;**waveformFactor1** = 1 / (-exp(-peakTime1 / tauRise) + exp(-peakTime1 / tauDecay1))
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**waveformFactor2**$  $Dimensionless
```
&emsp;&emsp;&emsp;**waveformFactor2** = 1 / (-exp(-peakTime2 / tauRise) + exp(-peakTime2 / tauDecay2))

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

**g**$ Time varying conductance through the synapse *(from {ref}`schema:baseconductancebasedsynapsetwo`)* ${ref}`schema:dimensions:conductance`
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
: **A**: Dimensionless 
: **B**: Dimensionless 
: **C**: Dimensionless 









<i>**On Start**</i>
: **A** = 0
: **B** = 0
: **C** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**A** = A + (gbase1*weight * waveformFactor1 + gbase2*weight*waveformFactor2 )/(gbase1+gbase2)
: &emsp;&emsp;&emsp;**B** = B + (weight * waveformFactor1)
: &emsp;&emsp;&emsp;**C** = C + (weight * waveformFactor2)





<i>**Derived Variables**</i>
    : **g** =&nbsp;gbase1*(B - A) + gbase2*(C-A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay1
    : d **C** /dt = -C / tauDecay2
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ExpThreeSynapse">
  <xs:complexContent>
    <xs:extension base="BaseConductanceBasedSynapseTwo">
      <xs:attribute name="tauDecay1" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="tauDecay2" type="Nml2Quantity_time" use="required"/>
      <xs:attribute name="tauRise" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExpThreeSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ExpThreeSynapse
from neuroml.utils import component_factory

variable = component_factory(
    ExpThreeSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase1: 'a Nml2Quantity_conductance (required)' = None,
    gbase2: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    tau_decay1: 'a Nml2Quantity_time (required)' = None,
    tau_decay2: 'a Nml2Quantity_time (required)' = None,
    tau_rise: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<expThreeSynapse id="synInputFastTwo" gbase1="1.5nS" tauRise="0.1ms" tauDecay1="0.7ms" gbase2="0.5nS" tauDecay2="2.5ms" erev="0mV"/>
```
```{code-block} xml
<expThreeSynapse id="AMPA" gbase1="1.5nS" tauRise="0.1ms" tauDecay1="0.7ms" gbase2="0.5nS" tauDecay2="2.5ms" erev="0mV">
    <notes>A synapse consisting of one rise and two decay time courses.</notes>
</expThreeSynapse>
```
````
`````

(schema:baseblockmechanism)=

## *baseBlockMechanism*




<i>Base of any ComponentType which produces a varying scaling ( or blockage ) of synaptic strength of magnitude **scaling**.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**blockFactor**$  $Dimensionless

```
````
`````

(schema:voltageconcdepblockmechanism)=

## voltageConcDepBlockMechanism




extends *{ref}`schema:baseblockmechanism`*



<i>Synaptic blocking mechanism which varys with membrane potential across the synapse, e.g. in NMDA receptor mediated synapses.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**blockConcentration**$  ${ref}`schema:dimensions:concentration`
**scalingConc**$  ${ref}`schema:dimensions:concentration`
**scalingVolt**$  ${ref}`schema:dimensions:voltage`

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

**blockFactor**$  *(from {ref}`schema:baseblockmechanism`)* $Dimensionless

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

````{tab-item} Dynamics








<i>**Derived Variables**</i>
    : **blockFactor** =&nbsp;1/(1 + (blockConcentration / scalingConc)* exp(-1 * (v / scalingVolt)))&emsp;(exposed as **blockFactor**)
    





````
`````

(schema:baseplasticitymechanism)=

## *basePlasticityMechanism*




<i>Base plasticity mechanism.</i>


`````{tab-set}
````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**plasticityFactor**$  $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This is where the plasticity mechanism receives spike events from the parent synapse.$Direction: in

```
````
`````

(schema:tsodyksmarkramdepmechanism)=

## tsodyksMarkramDepMechanism




extends *{ref}`schema:baseplasticitymechanism`*



<i>Depression-only Tsodyks-Markram model, as in Tsodyks and Markram 1997.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**initReleaseProb**$  $Dimensionless
**tauRec**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**plasticityFactor**$  *(from {ref}`schema:baseplasticitymechanism`)* $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This is where the plasticity mechanism receives spike events from the parent synapse. *(from {ref}`schema:baseplasticitymechanism`)*$Direction: in

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **parent** AS **a**
: WITH **this** AS **b**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **R**: Dimensionless 









<i>**On Start**</i>
: **R** = 1


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**R** = R * (1 - U)





<i>**Derived Variables**</i>
    : **U** =&nbsp;initReleaseProb
    : **plasticityFactor** =&nbsp;R * U&emsp;(exposed as **plasticityFactor**)
    





<i>**Time Derivatives**</i>
    : d **R** /dt = (1 - R) / tauRec
    

````
`````

(schema:tsodyksmarkramdepfacmechanism)=

## tsodyksMarkramDepFacMechanism




extends *{ref}`schema:baseplasticitymechanism`*



<i>Full Tsodyks-Markram STP model with both depression and facilitation, as in Tsodyks, Pawelzik and Markram 1998.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**initReleaseProb**$  $Dimensionless
**tauFac**$  ${ref}`schema:dimensions:time`
**tauRec**$  ${ref}`schema:dimensions:time`

```
````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**plasticityFactor**$  *(from {ref}`schema:baseplasticitymechanism`)* $Dimensionless

```
````

````{tab-item} Event Ports
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**in**$ This is where the plasticity mechanism receives spike events from the parent synapse. *(from {ref}`schema:baseplasticitymechanism`)*$Direction: in

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **parent** AS **a**
: WITH **this** AS **b**
: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **R**: Dimensionless 
: **U**: Dimensionless 









<i>**On Start**</i>
: **R** = 1
: **U** = initReleaseProb


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**R** = R * (1 - U)
: &emsp;&emsp;&emsp;**U** = U + initReleaseProb * (1 - U)





<i>**Derived Variables**</i>
    : **plasticityFactor** =&nbsp;R * U&emsp;(exposed as **plasticityFactor**)
    





<i>**Time Derivatives**</i>
    : d **R** /dt = (1 - R) / tauRec
    : d **U** /dt = (initReleaseProb - U) / tauFac
    

````
`````

(schema:blockingplasticsynapse)=

## blockingPlasticSynapse




extends {ref}`schema:exptwosynapse`



<i>Biexponential synapse that allows for optional block and plasticity mechanisms, which can be expressed as child elements.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:voltage`
**gbase**$ Baseline conductance, generally the maximum conductance following a single spike *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
**tauDecay**$  *(from {ref}`schema:exptwosynapse`)* ${ref}`schema:dimensions:time`
**tauRise**$  *(from {ref}`schema:exptwosynapse`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**peakTime**$  *(from {ref}`schema:exptwosynapse`)* ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**peakTime** = log(tauDecay / tauRise) * (tauRise * tauDecay)/(tauDecay - tauRise)
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**waveformFactor**$  *(from {ref}`schema:exptwosynapse`)* $Dimensionless
```
&emsp;&emsp;&emsp;**waveformFactor** = 1 / (-exp(-peakTime / tauRise) + exp(-peakTime / tauDecay))

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**plasticityMechanisms**$  $ {ref}`schema:baseplasticitymechanism`
**blockMechanisms**$  $ {ref}`schema:baseblockmechanism`

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

**g**$ Time varying conductance through the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
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
**relay**$ Used to relay incoming spikes to child plasticity mechanism$Direction: out

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **A**: Dimensionless 
: **B**: Dimensionless 









<i>**On Start**</i>
: **A** = 0
: **B** = 0


<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**A** = A + (weight * plasticityFactor * waveformFactor)
: &emsp;&emsp;&emsp;**B** = B + (weight * plasticityFactor * waveformFactor)
: &emsp;&emsp;&emsp;EVENT OUT on port: **relay**





<i>**Derived Variables**</i>
    : **plasticityFactor** =&nbsp;plasticityMechanisms[*]->plasticityFactor(reduce method: multiply)
    : **blockFactor** =&nbsp;blockMechanisms[*]->blockFactor(reduce method: multiply)
    : **g** =&nbsp;blockFactor * gbase * (B - A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay
    

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="BlockingPlasticSynapse">
  <xs:complexContent>
    <xs:extension base="ExpTwoSynapse">
      <xs:sequence>
        <xs:element name="plasticityMechanism" type="PlasticityMechanism" minOccurs="0"/>
        <xs:element name="blockMechanism" type="BlockMechanism" minOccurs="0"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=BlockingPlasticSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import BlockingPlasticSynapse
from neuroml.utils import component_factory

variable = component_factory(
    BlockingPlasticSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    gbase: 'a Nml2Quantity_conductance (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
    tau_decay: 'a Nml2Quantity_time (required)' = None,
    tau_rise: 'a Nml2Quantity_time (required)' = None,
    plasticity_mechanism: 'a PlasticityMechanism (optional)' = None,
    block_mechanism: 'a BlockMechanism (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<blockingPlasticSynapse id="NMDA" gbase=".8nS" tauRise="1e-3s" tauDecay="13.3333e-3s" erev="0V">
    <blockMechanism type="voltageConcDepBlockMechanism" species="mg" blockConcentration="1.2mM" scalingConc="1.9205441817997078mM" scalingVolt="0.016129032258064516V"/>
</blockingPlasticSynapse>
```
```{code-block} xml
<blockingPlasticSynapse id="blockStpSynDep" gbase="1nS" erev="0mV" tauRise="0.1ms" tauDecay="2ms">
    <notes>A biexponential blocking synapse, with STD.</notes>
    <plasticityMechanism type="tsodyksMarkramDepMechanism" initReleaseProb="0.5" tauRec="120 ms"/>
    <blockMechanism type="voltageConcDepBlockMechanism" species="mg" blockConcentration="1.2 mM" scalingConc="1.920544 mM" scalingVolt="16.129 mV"/>
</blockingPlasticSynapse>
```
```{code-block} xml
<blockingPlasticSynapse id="blockStpSynDepFac" gbase="1nS" erev="0mV" tauRise="0.1ms" tauDecay="2ms">
    <notes>A biexponential blocking synapse with short term
            depression and facilitation.</notes>
    <plasticityMechanism type="tsodyksMarkramDepFacMechanism" initReleaseProb="0.5" tauRec="120 ms" tauFac="10 ms"/>
    <blockMechanism type="voltageConcDepBlockMechanism" species="mg" blockConcentration="1.2 mM" scalingConc="1.920544 mM" scalingVolt="16.129 mV"/>
</blockingPlasticSynapse>
```
````
`````

(schema:doublesynapse)=

## doubleSynapse




extends *{ref}`schema:basevoltagedepsynapse`*



<i>Synapse consisting of two independent synaptic mechanisms ( e.g. AMPA-R and NMDA-R ), which can be easily colocated in connections.</i>


`````{tab-set}
````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**synapse1Path**$ 
**synapse2Path**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse1**$  $ {ref}`schema:basesynapse`
**synapse2**$  $ {ref}`schema:basesynapse`

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
**relay**$ Used to relay incoming spikes to child mechanisms$Direction: out

```
````

````{tab-item} Dynamics

<i>**Structure**</i>
: WITH **this** AS **a**
: WITH **synapse1Path** AS **b**
: WITH **synapse2Path** AS **c**
: CHILD INSTANCE: **synapse1**
: CHILD INSTANCE: **synapse2**
: EVENT CONNECTION from **a** TO  **c**   

: EVENT CONNECTION from **a** TO  **b**   





<i>**State Variables**</i>
: **weightFactor**: Dimensionless 











<i>**On Events**</i>

: EVENT IN on port: **in**
: &emsp;&emsp;&emsp;**weightFactor** = weight
: &emsp;&emsp;&emsp;EVENT OUT on port: **relay**





<i>**Derived Variables**</i>
    : **i1** =&nbsp;synapse1->i
    : **i2** =&nbsp;synapse2->i
    : **i** =&nbsp;weightFactor * (i1 + i2)&emsp;(exposed as **i**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="DoubleSynapse">
  <xs:complexContent>
    <xs:extension base="BaseVoltageDepSynapse">
      <xs:attribute name="synapse1" type="NmlId" use="required"/>
      <xs:attribute name="synapse2" type="NmlId" use="required"/>
      <xs:attribute name="synapse1Path" type="xs:string" use="required"/>
      <xs:attribute name="synapse2Path" type="xs:string" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=DoubleSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import DoubleSynapse
from neuroml.utils import component_factory

variable = component_factory(
    DoubleSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    synapse1: 'a NmlId (required)' = None,
    synapse2: 'a NmlId (required)' = None,
    synapse1_path: 'a string (required)' = None,
    synapse2_path: 'a string (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<doubleSynapse id="AMPA_NMDA" synapse1="AMPA" synapse1Path="./AMPA" synapse2="NMDA" synapse2Path="./NMDA">
    <notes>A single "synapse" which contains both AMPA and NMDA. It is planned that the need for extra synapse1Path/synapse2Path attributes can be removed in later versions.</notes>
</doubleSynapse>
```
````
`````

(schema:stdpsynapse)=

## stdpSynapse




extends {ref}`schema:exptwosynapse`



<i>Spike timing dependent plasticity mechanism, NOTE: EXAMPLE NOT YET WORKING!!!!</i>


[Bioportal entry for Computational Neuroscience Ontology related to stdpSynapse.](https://bioportal.bioontology.org/ontologies/CNO/?p=classes&conceptid=cno_0000034)

`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**erev**$ Reversal potential of the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:voltage`
**gbase**$ Baseline conductance, generally the maximum conductance following a single spike *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
**tauDecay**$  *(from {ref}`schema:exptwosynapse`)* ${ref}`schema:dimensions:time`
**tauRise**$  *(from {ref}`schema:exptwosynapse`)* ${ref}`schema:dimensions:time`

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**tsinceRate** = 1$  $ Dimensionless
**longTime** = 1000s$  $ {ref}`schema:dimensions:time`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**peakTime**$  *(from {ref}`schema:exptwosynapse`)* ${ref}`schema:dimensions:time`
```
&emsp;&emsp;&emsp;**peakTime** = log(tauDecay / tauRise) * (tauRise * tauDecay)/(tauDecay - tauRise)
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**waveformFactor**$  *(from {ref}`schema:exptwosynapse`)* $Dimensionless
```
&emsp;&emsp;&emsp;**waveformFactor** = 1 / (-exp(-peakTime / tauRise) + exp(-peakTime / tauDecay))

````

````{tab-item} Exposures
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**M**$  $Dimensionless
**P**$  $Dimensionless
**g**$ Time varying conductance through the synapse *(from {ref}`schema:baseconductancebasedsynapse`)* ${ref}`schema:dimensions:conductance`
**i**$ The total (usually time varying) current produced by this ComponentType *(from {ref}`schema:basepointcurrent`)* ${ref}`schema:dimensions:current`
**tsince**$  ${ref}`schema:dimensions:time`

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
: &emsp;&emsp;&emsp;**A** = A + waveformFactor
: &emsp;&emsp;&emsp;**B** = B + waveformFactor
: &emsp;&emsp;&emsp;**tsince** = 0





<i>**Derived Variables**</i>
    : **g** =&nbsp;gbase * (B - A)&emsp;(exposed as **g**)
    : **i** =&nbsp;g * (erev - v)&emsp;(exposed as **i**)
    





<i>**Time Derivatives**</i>
    : d **A** /dt = -A / tauRise
    : d **B** /dt = -B / tauDecay
    : d **tsince** /dt = tsinceRate
    

````
`````

(schema:gapjunction)=

## gapJunction




extends *{ref}`schema:basesynapse`*



<i>Gap junction/single electrical connection.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  ${ref}`schema:dimensions:conductance`

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

**v**$  ${ref}`schema:dimensions:voltage`

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








<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **i** =&nbsp;weight * conductance * (vpeer - v)&emsp;(exposed as **i**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GapJunction">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">
      <xs:attribute name="conductance" type="Nml2Quantity_conductance" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GapJunction" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GapJunction
from neuroml.utils import component_factory

variable = component_factory(
    GapJunction,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<gapJunction id="gj1" conductance="10pS"/>
```
```{code-block} xml
<gapJunction id="gj1" conductance="10pS"/>
```
````
`````

(schema:basegradedsynapse)=

## *baseGradedSynapse*




extends *{ref}`schema:basesynapse`*



<i>Base type for graded synapses.</i>


`````{tab-set}
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

**in**$  *(from {ref}`schema:basesynapse`)*$Direction: in

```
````
`````

(schema:silentsynapse)=

## silentSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Dummy synapse which emits no current. Used as presynaptic endpoint for analog synaptic connection.</i>


`````{tab-set}
````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**AMP** = 1A$  $ {ref}`schema:dimensions:current`

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

**v**$  ${ref}`schema:dimensions:voltage`

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








<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **i** =&nbsp;0 * AMP&emsp;(exposed as **i**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SilentSynapse">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">

            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SilentSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SilentSynapse
from neuroml.utils import component_factory

variable = component_factory(
    SilentSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<silentSynapse id="silent1"/>
```
```{code-block} xml
<silentSynapse id="silent2"/>
```
```{code-block} xml
<silentSynapse id="silent1"/>
```
````
`````

(schema:lineargradedsynapse)=

## linearGradedSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Behaves just like a one way gap junction.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**conductance**$  ${ref}`schema:dimensions:conductance`

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

**v**$  ${ref}`schema:dimensions:voltage`

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








<i>**Derived Variables**</i>
    : **vpeer** =&nbsp;peer->v
    : **i** =&nbsp;weight * conductance * (vpeer - v)&emsp;(exposed as **i**)
    





````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="LinearGradedSynapse">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">
      <xs:attribute name="conductance" type="Nml2Quantity_conductance" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=LinearGradedSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import LinearGradedSynapse
from neuroml.utils import component_factory

variable = component_factory(
    LinearGradedSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<linearGradedSynapse id="gs1" conductance="5pS"/>
```
````
`````

(schema:gradedsynapse)=

## gradedSynapse




extends *{ref}`schema:basegradedsynapse`*



<i>Graded/analog synapse. Based on synapse in Methods of http://www.nature.com/neuro/journal/v7/n12/abs/nn1352.html.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**Vth**$ The half-activation voltage of the synapse ${ref}`schema:dimensions:voltage`
**conductance**$  ${ref}`schema:dimensions:conductance`
**delta**$ Slope of the activation curve ${ref}`schema:dimensions:voltage`
**erev**$ The reversal potential of the synapse ${ref}`schema:dimensions:voltage`
**k**$ Rate constant for transmitter-receptor dissociation rate ${ref}`schema:dimensions:per_time`

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
**inf**$  $Dimensionless
**tau**$  ${ref}`schema:dimensions:time`

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
: **s**: Dimensionless 












<i>**On Conditions**</i>

: IF (1-inf) &lt; 1e-4 THEN
: &emsp;&emsp;&emsp;**s** = inf





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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="GradedSynapse">
  <xs:complexContent>
    <xs:extension base="BaseSynapse">
      <xs:attribute name="conductance" type="Nml2Quantity_conductance" use="required"/>
      <xs:attribute name="delta" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="Vth" type="Nml2Quantity_voltage" use="required"/>
      <xs:attribute name="k" type="Nml2Quantity_pertime" use="required"/>
      <xs:attribute name="erev" type="Nml2Quantity_voltage" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=GradedSynapse" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import GradedSynapse
from neuroml.utils import component_factory

variable = component_factory(
    GradedSynapse,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    conductance: 'a Nml2Quantity_conductance (required)' = None,
    delta: 'a Nml2Quantity_voltage (required)' = None,
    Vth: 'a Nml2Quantity_voltage (required)' = None,
    k: 'a Nml2Quantity_pertime (required)' = None,
    erev: 'a Nml2Quantity_voltage (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<gradedSynapse id="gs2" conductance="5pS" delta="5mV" Vth="-55mV" k="0.025per_ms" erev="0mV"/>
```
```{code-block} xml
<gradedSynapse id="gs1" conductance="0.1nS" delta="5mV" Vth="-35mV" k="0.025per_ms" erev="0mV"/>
```
````
`````
