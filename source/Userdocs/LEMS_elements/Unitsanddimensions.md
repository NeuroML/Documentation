
(lemsschema:page:units_and_dimensions_)=
# Units and dimensions



Generated on 02/05/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:dimension_)=
## Dimension

<i>A Dimenson element associated a name with a particular combination of  the standards SI base dimensions, mass, lenght, time, current, temperature and amount if substance (moles). Fractional dimensions are not currently supported.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ The name to be used when referring to this dimension from variable declaration or units
**m**$ int$ Mass
**l**$ int$ Length
**t**$ int$ Time
**i**$ int$ Current
**k**$ int$ Temperature
**n**$ int$ Amount of substance
**j**$ int$ Luminous intensity

```
````
`````
(lemsschema:unit_)=
## Unit

<i>A Unit asociates a symbol with a dimension and a power of ten. For non-metric units a scale can be provided, as in '1 inch = 0.0254 m'. In this case there is a degeneracy between the power and the scale which is best resolved by not using the two together. The offset parameter is available for units which are not zero-offset, such as farenheit.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ As with constants, units are only referred to within expressions using their symbols, so the name is just for readability.
**symbol**$ String$ The symbol is used to refer to this unit inside compound expressions coutaining a number and a unit symbol. Such expressions can only occur on the right hand side of assignments statements.
**dimension**$ String$ Reference to the dimension for this unit
**power**$ int$ Power of ten
**scale**$ double$ Scale, only to be used for scales which are not powers of ten
**offset**$ double$ Offset for non zero-offset units

```
````
`````
(lemsschema:assertion_)=
## Assertion

<i>Assertions are not strictly part of the model, but can be included in a file as a consistency check.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**dimension**$ String$ The name of a dimension
**matches**$ String$ An expression involving dimensions. The dimensionality of the expression should match the dimensionality of the dimension reference.

```
````
`````
(lemsschema:component_)=
## Component

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**id**$ String$ 
**name**$ String$ Name by which the component was declared - this shouldn't be accessible.
**declaredType**$ String$ Name by which the component was declared - this shouldn't be accessible.
**type**$ String$ 
**eXtends**$ String$ 

```
````

````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**insertions**$ {ref}`lemsschema:insertion_`
**components**$ {ref}`lemsschema:component_`
**abouts**$ {ref}`lemsschema:about_`
**metas**$ {ref}`lemsschema:meta_`

```
````
`````