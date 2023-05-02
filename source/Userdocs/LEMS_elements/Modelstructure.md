
(lemsschema:page:model_structure_)=
# Model structure

**Models can be spread over multiple files. The root element in each file is Lems.**

---

Generated on 02/05/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:lems_)=
## Lems

<i>Root element for any lems content</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**dimensions**$ {ref}`lemsschema:dimension_`
**constants**$ {ref}`lemsschema:constant_`
**units**$ {ref}`lemsschema:unit_`
**assertions**$ {ref}`lemsschema:assertion_`
**componentTypes**$ {ref}`lemsschema:componenttype_`
**components**$ {ref}`lemsschema:component_`
**targets**$ {ref}`lemsschema:target_`

```
````
`````
(lemsschema:target_)=
## Target

<i>A lems file can contain many component definitions. A Target elements specifies that a components should be treated as the entry point for simulation or other processing</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**component**$ String$ Reference to the entry point component
**reportFile**$ String$ Optional attribute specifying file in which to save short report of simulation
**timesFile**$ String$ Optional attribute specifying file in which to save times used in simulation

```
````
`````
(lemsschema:constant_)=
## Constant

<i>A constant quantity: like a parameter for which the value is supplied in the class definition itself rather than when a component is defined.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**name**$ String$ A readable name for the constant.
**symbol**$ String$ The symbol used in expressions to refer to this constant.
**value**$ String$ The value of a constant must be a plain number (no units) giving the SI magnitude of the quantity or an expression involving only plain numbers or other constants.
**dimension**$ String$ 

```
````
`````