
(schema:simulation_)=
# Simulation

**Specification of the LEMS Simulation element which is normally used to define simulations of NeuroML2 files. Note: not actually part of NeuroML v2, but this is required by much of the NeuroML toolchain for defining Simulations ( which NeuroML model to use and how long to run for ), as well as what to  {ref}`schema:display` and what to save in  {ref}`schema:outputfile`s.**

---


Original ComponentType definitions: [Simulation.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Simulation.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:simulation)=

## Simulation




<i>The main element in a LEMS Simulation file. Defines the **length** of simulation, the timestep ( dt ) **step** and an optional **seed** to use for stochastic elements, as well as  {ref}`schema:display`s,  {ref}`schema:outputfile`s and  {ref}`schema:eventoutputfile`s to record. Specifies a **target** component to run, usually the id of a  {ref}`schema:network`.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**length**$ Duration of the simulation run ${ref}`schema:dimensions:time`
**step**$ Time step (dt) to use in the simulation ${ref}`schema:dimensions:time`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**seed**$ The seed to use in the random number generator for stochastic entities

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**target**$  $ {ref}`schema:component`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**metas**$  $ {ref}`schema:meta`
**displays**$  $ {ref}`schema:display`
**outputs**$  $ {ref}`schema:outputfile`
**events**$  $ {ref}`schema:eventoutputfile`

```
````

````{tab-item} Dynamics



<i>**State Variables**</i>
: **t**: {ref}`schema:dimensions:time` 










````
`````

(schema:display)=

## Display




<i>Details of a display to generate ( usually a set of traces given by  {ref}`schema:line`s in a newly opened window ) on completion of the simulation.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**timeScale**$ A scaling of the time axis, e.g. 1ms means display in milliseconds. Note: all quantities are recorded in SI units ${ref}`schema:dimensions:time`
**xmax**$ The maximum value on the x axis (i.e time variable) of the display $Dimensionless
**xmin**$ The minimum value on the x axis (i.e time variable) of the display $Dimensionless
**ymax**$ The maximum value on the x axis of the display $Dimensionless
**ymin**$ The minimum value on the y axis of the display $Dimensionless

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**title**$ The title of the display, e.g. to use for the window

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**lines**$  $ {ref}`schema:line`

```
````
`````

(schema:line)=

## Line




<i>Specification of a single time varying **quantity** to plot on the  {ref}`schema:display`. Note that all quantities are handled internally in LEMS in SI units, and so a **scale** should be used if it is to be displayed in other units.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**scale**$ A scaling factor to DIVIDE the quantity by. Can be dimensional, so using scale=1mV means a value of -0.07V is displayed as -70. Alternatively, scale=0.001 would achieve the same thing. ${ref}`schema:dimensions:*`
**timeScale**$ An optional scaling of the time axis, e.g. 1ms means display in milliseconds. Note: if present, this overrides timeScale from _Display_ ${ref}`schema:dimensions:*`

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**color**$ A hex string for the color to display the trace for this quantity, e.g. #aa33ff

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**quantity**$ Path to the quantity to display, see see https://docs.neuroml.org/Userdocs/Paths.html.

````
`````

(schema:outputfile)=

## OutputFile




<i>A file in which to save recorded values from the simulation.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**path**$ Optional path to the directory in which to store the file
**fileName**$ Name of the file to generate. Can include a relative path (from the LEMS Simulation file location).

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**outputColumn**$  $ {ref}`schema:outputcolumn`

```
````
`````

(schema:outputcolumn)=

## OutputColumn




<i>Specification of a single time varying **quantity** to record during the simulation. Note that all quantities are handled internally in LEMS in SI units, and so the value for the quantity in the file ( as well as time ) will be in SI units.</i>


`````{tab-set}
````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**quantity**$ Path to the quantity to save, see see https://docs.neuroml.org/Userdocs/Paths.html. Note that all quantities are saved in SI units.

````
`````

(schema:eventoutputfile)=

## EventOutputFile




<i>A file in which to save event information ( e.g. spikes from cells in a population ) in a specified **format**.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**path**$ Optional path to the directory in which to store the file
**fileName**$ Name of the file to generate. Can include a relative path (from the LEMS Simulation file location).
**format**$ Takes values TIME_ID or ID_TIME, depending on the preferred order of the time or event id (from _EventSelection_) in each row of the file

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**eventSelection**$  $ {ref}`schema:eventselection`

```
````
`````

(schema:eventselection)=

## EventSelection




<i>A specific source of events with an associated **id,** which will be recorded inside the file specified in the parent  {ref}`schema:eventoutputfile`. The attribute **select** should point to a cell inside a  {ref}`schema:population` ( e.g. hhpop[0], see https://docs.neuroml.org/Userdocs/Paths.html ), and the **eventPort** specifies the port for the emitted events, which usually has id: spike. Note: the **id** used on this element ( and appearing in the file alongside the event time ) can be different from the id/index of the cell in the population.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**eventPort**$ The port on the cell which generates the events, usually: spike

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**select**$ The cell which will be emitting the events

````
`````

(schema:meta)=

## Meta




<i>Metadata to add to simulation.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**for**$ Simulator name
**method**$ Integration method to use
**abs_tolerance**$ Absolute tolerance for NEURON's cvode method
**rel_tolerance**$ Relative tolerance for NEURON's cvode method

````
`````
