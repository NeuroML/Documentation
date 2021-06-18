
(schema:simulation)=
# Simulation



Original ComponentType definitions: [Simulation.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Simulation.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 17/06/21 from [this](https://github.com/NeuroML/NeuroML2/commit/1d8324c6b04b2aa901b5937dc691c077a6059b88) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:display)=

## Display




<i></i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**timeScale**$  ${ref}`schema:dimensions:time`
**xmax**$  $Dimensionless
**xmin**$  $Dimensionless
**ymax**$  $Dimensionless
**ymin**$  $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**title**$ 

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

(schema:simulation)=

## Simulation




<i></i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**length**$  ${ref}`schema:dimensions:time`
**step**$  ${ref}`schema:dimensions:time`

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**seed**$ 

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
