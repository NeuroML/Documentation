
(lemsschema:page:defining_components_)=
# Defining Components



Generated on 03/05/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

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