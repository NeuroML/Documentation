
(schema:neuromlcorecomptypes_)=
# NeuroMLCoreCompTypes




Original ComponentType definitions: [NeuroMLCoreCompTypes.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//NeuroMLCoreCompTypes.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.2.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.2.xsd).
Generated on 03/08/22 from [this](https://github.com/NeuroML/NeuroML2/commit/2c397d00bd4b9aa03313165777d6ca4cfa437755) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:notes)=

## notes




<i>Human readable notes/description for a Component.</i>


`````{tab-set}

````{tab-item} Usage: XML
```{code-block} xml
<notes>A Simple Spiking cell for testing purposes</notes>
```
```{code-block} xml
<notes>Multicompartmental cell</notes>
```
```{code-block} xml
<notes>Leak conductance</notes>
```
````
`````

(schema:annotation)=

## annotation




<i>A structured annotation containing metadata, specifically RDF or  {ref}`schema:property` elements.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:RDF**$  $ {ref}`schema:rdf_rdf`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Annotation" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Annotation

variable = Annotation(anytypeobjs_=None, gds_collector_=None, **kwargs_)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<annotation>
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
`````

(schema:property)=

## property




<i>A property ( a **tag** and **value** pair ), which can be on any  {ref}`schema:basestandalone` either as a direct child, or within an  {ref}`schema:annotation`. Generally something which helps the visual display or facilitates simulation of a Component, but is not a core physiological property. Common examples include: **numberInternalDivisions,** equivalent of nseg in NEURON; **radius,** for a radius to use in graphical displays for abstract cells ( i.e. without defined morphologies ); **color,** the color to use for a  {ref}`schema:population` or  {ref}`schema:populationlist` of cells; **recommended_dt_ms,** the recommended timestep to use for simulating a  {ref}`schema:network`, **recommended_duration_ms** the recommended duration to use when running a  {ref}`schema:network`.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**tag**$ Name of the property
**value**$ Value of the property

````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Property" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Property

variable = Property(tag=None, value=None, gds_collector_=None, **kwargs_)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<property tag="numberInternalDivisions" value="9"/>
```
````
`````

(schema:basestandalone)=

## *baseStandalone*




<i>Base type of any Component which can have  {ref}`schema:notes`,  {ref}`schema:annotation`, or a  {ref}`schema:property` list.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**annotation**$  $ {ref}`schema:annotation`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`

```
````
`````

(schema:rdf_rdf)=

## rdf_RDF




<i>Structured block in an  {ref}`schema:annotation` based on RDF. See https://github.com/OpenSourceBrain/OSB_API/blob/master/python/examples/grancelllayer.xml.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**xmlns:rdf**$ 

````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:Description**$  $ {ref}`schema:rdf_description`

```
````
`````

(schema:rdf_description)=

## rdf_Description




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**rdf:about**$ 

````

````{tab-item} Child list
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
`````

(schema:basebqbiol)=

## *baseBqbiol*




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:Bag**$  $ {ref}`schema:rdf_bag`

```
````
`````

(schema:bqbiol_encodes)=

## bqbiol_encodes




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_haspart)=

## bqbiol_hasPart




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_hasproperty)=

## bqbiol_hasProperty




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_hasversion)=

## bqbiol_hasVersion




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_is)=

## bqbiol_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_isdescribedby)=

## bqbiol_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_isencodedby)=

## bqbiol_isEncodedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_ishomologto)=

## bqbiol_isHomologTo




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_ispartof)=

## bqbiol_isPartOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_ispropertyof)=

## bqbiol_isPropertyOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_isversionof)=

## bqbiol_isVersionOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**xmlns:bqbiol**$ 

````
`````

(schema:bqbiol_occursin)=

## bqbiol_occursIn




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqbiol_hastaxon)=

## bqbiol_hasTaxon




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqmodel_is)=

## bqmodel_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:bqmodel_isdescribedby)=

## bqmodel_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**xmlns:bqmodel**$ 

````
`````

(schema:bqmodel_isderivedfrom)=

## bqmodel_isDerivedFrom




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers.</i>


`````{tab-set}`````

(schema:rdf_bag)=

## rdf_Bag




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>


`````{tab-set}
````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rdf:li**$  $ {ref}`schema:rdf:li`

```
````
`````

(schema:rdf_li)=

## rdf_li




<i>Structured block in an  {ref}`schema:annotation` based on RDF.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**rdf:resource**$ 

````
`````

(schema:point3dwithdiam)=

## point3DWithDiam




<i>Base type for ComponentTypes which specify an ( **x,** **y,** **z** ) coordinate along with a **diameter.** Note: no dimension used in the attributes for these coordinates! These are assumed to have dimension micrometer ( 10^-6 m ). This is due to micrometers being the default option for the majority of neuronal morphology formats, and dimensions are omitted here to facilitate reading and writing of morphologies in NeuroML.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**diameter**$ Diameter of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. $Dimensionless
**x**$ x coordinate of the point. Note: no dimension used, see description of _point3DWithDiam_ for details. $Dimensionless
**y**$ y coordinate of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. $Dimensionless
**z**$ z coordinate of the ppoint. Note: no dimension used, see description of _point3DWithDiam_ for details. $Dimensionless

```
````

````{tab-item} Constants
```{csv-table}
:widths: 3, 5, 2
:width: 100%
:delim: $

**MICRON** = 1um$  $ {ref}`schema:dimensions:length`

```
````

````{tab-item} Derived parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**radius**$ A dimensional quantity given by half the _diameter. ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**radius** = MICRON * diameter / 2
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**xLength**$ A version of _x with dimension length. ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**xLength** = MICRON * x
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**yLength**$ A version of _y with dimension length. ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**yLength** = MICRON * y
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**zLength**$ A version of _z with dimension length. ${ref}`schema:dimensions:length`
```
&emsp;&emsp;&emsp;**zLength** = MICRON * z

````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Point3DWithDiam" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Point3DWithDiam

variable = Point3DWithDiam(x=None, y=None, z=None, diameter=None, gds_collector_=None, **kwargs_)
```
````
`````
