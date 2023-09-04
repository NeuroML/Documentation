
(lemsschema:page:structure_)=
# Structure



Generated on 22/08/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:structure_)=
## Structure

<i>By default, each Component in a model gives rise to a single instance of its state variables when the model is executed. The state variables are then governed by the dynamics definition in the associated ComponentType. Elements in the Structure declaration  can be used to change this behavior, for example to make multiple instances of the state variables, or to instantiate a different component. A typical application for the latter would be a Component that defines a population of cells. The population Component might define the number of cells it contains but would refer to a Component defined elsewhere for the actual cell model to use.</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:buildelement_)=
## BuildElement

<i>Base class for elements that can be used in Structures</i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:multiinstantiate_)=
## MultiInstantiate

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:coinstantiate_)=
## CoInstantiate

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:assign_)=
## Assign

<i></i>


(lemsschema:choose_)=
## Choose

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:childinstance_)=
## ChildInstance

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:foreach_)=
## ForEach

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:eventconnection_)=
## EventConnection

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:tunnel_)=
## Tunnel

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**assigns**$ {ref}`lemsschema:assign_`
**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:pairseventconnection_)=
## PairsEventConnection

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:pairfilter_)=
## PairFilter

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:includepair_)=
## IncludePair

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:with_)=
## With

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:if_)=
## If

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:apply_)=
## Apply

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:gather_)=
## Gather

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````
(lemsschema:gatherpairs_)=
## GatherPairs

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**buildElements**$ {ref}`lemsschema:buildelement_`

```
````
`````