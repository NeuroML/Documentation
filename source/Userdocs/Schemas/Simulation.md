
(schema:simulation)=
# Simulation

**Specification of the LEMS Simulation element which is normally used to define simulations of NeuroML2 files. Note: not actually part of NeuroML v2, but this is required by much of the NeuroML toolchain for defining Simulations ( which NeuroML model to use and how long to run for ), as well as what to  {ref}`schema:display` and what to save in  {ref}`schema:outputfile`s.**

---


Original ComponentType definitions: [Simulation.xml](https://github.com/NeuroML/NeuroML2/blob/documentation_update/NeuroML2CoreTypes//Simulation.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.2.xsd](https://github.com/NeuroML/NeuroML2/tree/documentation_update/Schemas/NeuroML2/NeuroML_v2.2.xsd).
Generated on 04/08/21 from [this](https://github.com/NeuroML/NeuroML2/commit/c6d2535a733aaf07449e6e284be729918a5aca46) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:simulation)=

## Simulation




<i>The main element in a LEMS Simulation file. Defines the **length** of simulation, the timestep ( dt ) **step** and an optional **seed** to use for stochastic elements, as well as **displays,** **outputs** and **events** to record. Specifies a **target** component to run, usually the id of a  {ref}`schema:network`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**length**$ Duration of the simulation run ${ref}`schema:dimensions:time`
**step**$ Time step (dt) to use in simulation ${ref}`schema:dimensions:time`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**seed**$ The seed to use in the random number generator for stochastic entities

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**target**$  $ {ref}`schema:component`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**displays**$  $ {ref}`schema:display`
**outputs**$  $ {ref}`schema:outputfile`
**events**$  $ {ref}`schema:eventoutputfile`

```
````

````{tabbed} Dynamics



<i>**State Variables**</i>
: **t**: {ref}`schema:dimensions:time` 










````

(schema:display)=

## Display




<i>Details of a display to generate ( usually a set of plots in a newly opened window ) on completion of the simulation.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**timeScale**$ A scaling of the time axis, e.g. 1ms means display in milliseconds ${ref}`schema:dimensions:time`
**xmax**$ The maximum value on the x axis (i.e time variable) of the display $Dimensionless
**xmin**$ The minimum value on the x axis (i.e time variable) of the display $Dimensionless
**ymax**$ The maximum value on the x axis of the display $Dimensionless
**ymin**$ The minimum value on the y axis of the display $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**title**$ The title of the dispalcy, e.g. to use for the window

````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**lines**$  $ {ref}`schema:line`

```
````

(schema:line)=

## Line




<i></i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**scale**$  ${ref}`schema:dimensions:*`
**timeScale**$  ${ref}`schema:dimensions:*`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**color**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**quantity**$ 

````

(schema:outputfile)=

## OutputFile




<i></i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**path**$ 
**fileName**$ 

````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**outputColumn**$  $ {ref}`schema:outputcolumn`

```
````

(schema:outputcolumn)=

## OutputColumn




<i></i>



````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**quantity**$ 

````

(schema:eventoutputfile)=

## EventOutputFile




<i></i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**path**$ 
**fileName**$ 
**format**$ 

````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**eventSelection**$  $ {ref}`schema:eventselection`

```
````

(schema:eventselection)=

## EventSelection




<i></i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**eventPort**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**select**$ 

````
