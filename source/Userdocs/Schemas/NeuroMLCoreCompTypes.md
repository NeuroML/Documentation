
(schema:neuromlcorecomptypes)=
# NeuroMLCoreCompTypes



Original ComponentType definitions: [NeuroMLCoreCompTypes.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//NeuroMLCoreCompTypes.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 02/03/21 from [this](https://github.com/NeuroML/NeuroML2/commit/6e4643d0eaa7246982b351a01e28856eeb320500) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:notes)=

## notes




<i>Human readable notes on a Component .</i>



(schema:annotation)=

## annotation




<i>Annotation... .</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:RDF, {ref}`schema:rdf_rdf`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

property, {ref}`schema:property`

```
````

(schema:property)=

## property




<i>Property in Annotation... .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

tag,
value,

````

(schema:basestandalone)=

## *baseStandalone*




<i>Base type of any component which will require notes, annotation, etc. .</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

notes, {ref}`schema:notes`
annotation, {ref}`schema:annotation`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

property, {ref}`schema:property`

```
````

(schema:rdf_rdf)=

## rdf_RDF




<i>Work in progress... .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

xmlns:rdf,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:Description, {ref}`schema:rdf_description`

```
````

(schema:rdf_description)=

## rdf_Description




<i>Work in progress... .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

rdf:about,

````

````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

bqbiol:encodes, {ref}`schema:bqbiol_encodes`
bqbiol:hasPart, {ref}`schema:bqbiol_haspart`
bqbiol:hasProperty, {ref}`schema:bqbiol_hasproperty`
bqbiol:hasVersion, {ref}`schema:bqbiol_hasversion`
bqbiol:is, {ref}`schema:bqbiol_is`
bqbiol:isDescribedBy, {ref}`schema:bqbiol_isdescribedby`
bqbiol:isEncodedBy, {ref}`schema:bqbiol_isencodedby`
bqbiol:isHomologTo, {ref}`schema:bqbiol_ishomologto`
bqbiol:isPartOf, {ref}`schema:bqbiol_ispartof`
bqbiol:isPropertyOf, {ref}`schema:bqbiol_ispropertyof`
bqbiol:isVersionOf, {ref}`schema:bqbiol_isversionof`
bqbiol:occursIn, {ref}`schema:bqbiol_occursin`
bqbiol:hasTaxon, {ref}`schema:bqbiol_hastaxon`
bqmodel:is, {ref}`schema:bqmodel_is`
bqmodel:isDescribedBy, {ref}`schema:bqmodel_isdescribedby`
bqmodel:isDerivedFrom, {ref}`schema:bqmodel_isderivedfrom`

```
````

(schema:basebqbiol)=

## *baseBqbiol*




<i>Work in progress... .</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:Bag, {ref}`schema:rdf_bag`

```
````

(schema:bqbiol_encodes)=

## bqbiol_encodes




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_haspart)=

## bqbiol_hasPart




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_hasproperty)=

## bqbiol_hasProperty




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_hasversion)=

## bqbiol_hasVersion




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_is)=

## bqbiol_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_isdescribedby)=

## bqbiol_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_isencodedby)=

## bqbiol_isEncodedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_ishomologto)=

## bqbiol_isHomologTo




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_ispartof)=

## bqbiol_isPartOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_ispropertyof)=

## bqbiol_isPropertyOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_isversionof)=

## bqbiol_isVersionOf




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

xmlns:bqbiol,

````

(schema:bqbiol_occursin)=

## bqbiol_occursIn




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqbiol_hastaxon)=

## bqbiol_hasTaxon




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqmodel_is)=

## bqmodel_is




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:bqmodel_isdescribedby)=

## bqmodel_isDescribedBy




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

xmlns:bqmodel,

````

(schema:bqmodel_isderivedfrom)=

## bqmodel_isDerivedFrom




extends *{ref}`schema:basebqbiol`*



<i>See http://co.mbine.org/standards/qualifiers .</i>



(schema:rdf_bag)=

## rdf_Bag




<i>Work in progress... .</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

rdf:li, {ref}`schema:rdf:li`

```
````

(schema:rdf_li)=

## rdf_li




<i>Annotation... .</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

rdf:resource,

````

(schema:point3dwithdiam)=

## point3DWithDiam




<i>Base type for ComponentTypes which specify an ( **x,** **y,** **z** ) coordinate along with a **diameter.** Note: no dimension used in the attributes for these coordinates! These are assumed to have dimension micrometer (10^-6 m). This is due to micrometers being the default option for the majority of neuronal morphology formats, and dimensions are omitted here to facilitate reading and writing of morphologies in NeuroML. .</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

diameter,Dimensionless
x,Dimensionless
y,Dimensionless
z,Dimensionless

```
````

````{tabbed} Derived parameters
```{csv-table}
:widths: 8, 2
:width: 100%

radius,{ref}`schema:dimensions:length`
xLength,{ref}`schema:dimensions:length`
yLength,{ref}`schema:dimensions:length`
zLength,{ref}`schema:dimensions:length`

```
````

````{tabbed} Constants
```{csv-table}
:widths: 8, 2
:width: 100%

MICRON = 1um, {ref}`schema:dimensions:length`

```
````
