
(lemsschema:page:geometry_)=
# Geometry



Schema against which LEMS based on these should be valid: [LEMS_v0.7.6.xsd](https://github.com/LEMS/LEMS/tree/master/Schemas/LEMS/LEMS_v0.7.6.xsd).
Generated on 18/06/24 from [this](https://github.com/LEMS/LEMS/commit/fd7b30eceb6735ac343745c8f6992bdde72b248b) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:geometry_)=
## Geometry

<i>Specifies the geometrical interpretation of the properties of components realizing this ComponentType.</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**frustums**$ {ref}`lemsschema:frustum_`
**solids**$ {ref}`lemsschema:solid_`
**skeletons**$ {ref}`lemsschema:skeleton_`

```
````
`````
(lemsschema:frustum_)=
## Frustum

<i></i>


(lemsschema:solid_)=
## Solid

<i></i>


(lemsschema:location_)=
## Location

<i></i>


(lemsschema:skeleton_)=
## Skeleton

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**scalarFields**$ {ref}`lemsschema:scalarfield_`

```
````
`````
(lemsschema:scalarfield_)=
## ScalarField

<i></i>

