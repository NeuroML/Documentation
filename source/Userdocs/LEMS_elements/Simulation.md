
(lemsschema:page:simulation_)=
# Simulation



Generated on 22/08/23.
Please file any issues or questions at the [issue tracker here](https://github.com/LEMS/LEMS/issues).

---

(lemsschema:simulation_)=
## Simulation

<i></i>

`````{tab-set}
````{tab-item} can contain these elements
```{csv-table}
:widths: 2, 8
:width: 100%
:delim: $

**records**$ {ref}`lemsschema:record_`
**eventRecords**$ {ref}`lemsschema:eventrecord_`
**runs**$ {ref}`lemsschema:run_`
**dataDisplays**$ {ref}`lemsschema:datadisplay_`
**dataWriters**$ {ref}`lemsschema:datawriter_`
**eventWriters**$ {ref}`lemsschema:eventwriter_`

```
````
`````
(lemsschema:record_)=
## Record

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**quantity**$ String$ path to the parameter that will contain the path to the quantity to be recorded
**scale**$ String$ path to the element that defines the scale for rendering the quantity dimensionless
**color**$ String$ hex format color suggestion for how the data should be displayed

```
````
`````
(lemsschema:eventrecord_)=
## EventRecord

<i></i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**quantity**$ String$ path for the component which will emit spikes to be recorded
**eventPort**$ String$ event port for the component which will emit spikes

```
````
`````
(lemsschema:datadisplay_)=
## DataDisplay

<i></i>


(lemsschema:datawriter_)=
## DataWriter

<i></i>


(lemsschema:eventwriter_)=
## EventWriter

<i></i>


(lemsschema:run_)=
## Run

<i>The run element provides a way to make a model runnable. It should point to the parameters that set the step size etc. The target parameters have to be dimensionally consistent.</i>

`````{tab-set}
````{tab-item} Properties
```{csv-table}
:widths: 1, 2, 7
:width: 100%
:delim: $

**component**$ String$ name of the component reference that will set the component to be run
**variable**$ String$ 
**increment**$ String$ path to the parameter that sets the step size
**total**$ String$ path to the parameter that sets the total span of the independent variable to be run

```
````
`````