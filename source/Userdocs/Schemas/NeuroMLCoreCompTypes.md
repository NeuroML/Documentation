
(schema:neuromlcorecomptypes)=
# NeuroMLCoreCompTypes



Original ComponentType definitions: [NeuroMLCoreCompTypes.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//NeuroMLCoreCompTypes.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 17/06/21 from [this](https://github.com/NeuroML/NeuroML2/commit/1d8324c6b04b2aa901b5937dc691c077a6059b88) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:notes)=

## notes




<i>Human readable notes/description for a Component.</i>



````{tabbed} Usage



*XML examples*
```{code-block} xml
<notes>An alpha synapse with time for rise equal to decay.</notes>
```
```{code-block} xml
<notes>A simple monoexponential synapse.</notes>
```
```{code-block} xml
<notes>A biexponential synapse.</notes>
```

````

(schema:annotation)=

## annotation




<i>A structured annotation containing metadata, specifically RDF or  {ref}`schema:property` elements.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:RDF**$  $ {ref}`schema:rdf_rdf`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Annotation" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Annotation

variable = Annotation(anytypeobjs_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<annotation xmlns:xi="http://www.w3.org/2001/XInclude">
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
```

````

(schema:property)=

## property




<i>A property ( a **tag** and **value** pair ), which can be on any  {ref}`schema:basestandalone` either as a direct child, or within an  {ref}`schema:annotation`. Generally something which helps the visual display or facilitates simulation of a Component, but is not a core physiological property. Common examples include: **numberInternalDivisions,** equivalent of nseg in NEURON; **radius,** for a radius to use in graphical displays for abstract cells ( i.e. without defined morphologies ); **color,** the color to use for a  {ref}`schema:population` or  {ref}`schema:populationlist` of cells; **recommended_dt_ms,** the recommended timestep to use for simulating a  {ref}`schema:network`, **recommended_duration_ms** the recommended duration to use when running a  {ref}`schema:network`.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**tag**$ 
**value**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Property" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Property

variable = Property(tag=None, value=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<property tag="numberInternalDivisions" value="9"/>
```

````

(schema:basestandalone)=

## *baseStandalone*




<i>Base type of any Component which can have  {ref}`schema:notes`,  {ref}`schema:annotation`, or a  {ref}`schema:property` list.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**annotation**$  $ {ref}`schema:annotation`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`

```
````

(schema:rdf_rdf)=

## rdf_RDF




<i>Structured block in an  {ref}`schema:annotation` based on RDF. See https://github.com/OpenSourceBrain/OSB_API/blob/master/python/examples/grancelllayer.xml.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**xmlns:rdf**$ 

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:Description**$  $ {ref}`schema:rdf_description`

```
````

(schema:rdf_description)=

## rdf_Description




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**rdf:about**$ 

````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**bqbiol:encodes**$  $ {ref}`schema:bqbiol_encodes`
**bqbiol:hasPart**$  $ {ref}`schema:bqbiol_haspart`
**bqbiol:hasProperty**$  $ {ref}`schema:bqbiol_hasproperty`
**bqbiol:hasVersion**$  $ {ref}`schema:bqbiol_hasversion`
**bqbiol:is**$  $ {ref}`schema:bqbiol_is`
**bqbiol:isDescribedBy**$  $ {ref}`schema:bqbiol_isdescribedby`
**bqbiol:isEncodedBy**$  $ {ref}`schema:bqbiol_isencodedby`
**bqbiol:isHomologTo**$  $ {ref}`schema:bqbiol_ishomologto`
**bqbiol:isPartOf**$  $ {ref}`schema:bqbiol_ispartof`
**bqbiol:isPropertyOf**$  $ {ref}`schema:bqbiol_ispropertyof`
**bqbiol:isVersionOf**$  $ {ref}`schema:bqbiol_isversionof`
**bqbiol:occursIn**$  $ {ref}`schema:bqbiol_occursin`
**bqbiol:hasTaxon**$  $ {ref}`schema:bqbiol_hastaxon`
**bqmodel:is**$  $ {ref}`schema:bqmodel_is`
**bqmodel:isDescribedBy**$  $ {ref}`schema:bqmodel_isdescribedby`
**bqmodel:isDerivedFrom**$  $ {ref}`schema:bqmodel_isderivedfrom`

```
````

(schema:basebqbiol)=

## *baseBqbiol*




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:Bag**$  $ {ref}`schema:rdf_bag`

```
````

(schema:bqbiol_encodes)=

## bqbiol_encodes




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_haspart)=

## bqbiol_hasPart




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_hasproperty)=

## bqbiol_hasProperty




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_hasversion)=

## bqbiol_hasVersion




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_is)=

## bqbiol_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_isdescribedby)=

## bqbiol_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_isencodedby)=

## bqbiol_isEncodedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_ishomologto)=

## bqbiol_isHomologTo




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_ispartof)=

## bqbiol_isPartOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_ispropertyof)=

## bqbiol_isPropertyOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_isversionof)=

## bqbiol_isVersionOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**xmlns:bqbiol**$ 

````

(schema:bqbiol_occursin)=

## bqbiol_occursIn




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqbiol_hastaxon)=

## bqbiol_hasTaxon




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqmodel_is)=

## bqmodel_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:bqmodel_isdescribedby)=

## bqmodel_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**xmlns:bqmodel**$ 

````

(schema:bqmodel_isderivedfrom)=

## bqmodel_isDerivedFrom




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>



(schema:rdf_bag)=

## rdf_Bag




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:li**$  $ {ref}`schema:rdf:li`

```
````

(schema:rdf_li)=

## rdf_li




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**rdf:resource**$ 

````

(schema:point3dwithdiam)=

## point3DWithDiam




<i>Base type for ComponentTypes which specify an ( **x,** **y,** **z** ) coordinate along with a **diameter.** Note: no dimension used in the attributes for these coordinates! These are assumed to have dimension micrometer ( 10^-6 m ). This is due to micrometers being the default option for the majority of neuronal morphology formats, and dimensions are omitted here to facilitate reading and writing of morphologies in NeuroML.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**diameter**$ Diameter at point. Note: no dimension used, see note above! $Dimensionless
**x**$ x coordinate of point. Note: no dimension used, see note above! $Dimensionless
**y**$ y coordinate of point. Note: no dimension used, see note above! $Dimensionless
**z**$ z coordinate of point. Note: no dimension used, see note above! $Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**radius**$  ${ref}`schema:dimensions:length`
**xLength**$  ${ref}`schema:dimensions:length`
**yLength**$  ${ref}`schema:dimensions:length`
**zLength**$  ${ref}`schema:dimensions:length`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MICRON** = 1um$  $ {ref}`schema:dimensions:length`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Point3DWithDiam" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Point3DWithDiam

variable = Point3DWithDiam(x=None, y=None, z=None, diameter=None, **kwargs_)
```



````
