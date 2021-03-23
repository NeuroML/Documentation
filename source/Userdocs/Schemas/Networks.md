
(schema:networks)=
# Networks



Original ComponentType definitions: [Networks.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Networks.xml).

Schema against which NeuroML based on these should be valid: [NeuroML_v2.1.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.1.xsd).

Generated on 23/03/21 from [this](https://github.com/NeuroML/NeuroML2/commit/ec9d81a59ca05189c89bf48cf3ea06241c917eb5) commit.

Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

(schema:network)=

## network




extends *{ref}`schema:basestandalone`*



<i>Network containing  {ref}`schema:population`s,  {ref}`schema:projection`s and lists of  {ref}`schema:explicitconnection`s (either directly between components of the populations or via synapses).</i>



````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

regions, {ref}`schema:region`
populations, {ref}`schema:basepopulation`
projections, {ref}`schema:projection`
synapticConnections, {ref}`schema:explicitconnection`
electricalProjection, {ref}`schema:electricalprojection`
continuousProjection, {ref}`schema:continuousprojection`
explicitInputs, {ref}`schema:explicitinput`
inputs, {ref}`schema:inputlist`

```
````

(schema:networkwithtemperature)=

## networkWithTemperature




extends {ref}`schema:network`



<i>Network containing  {ref}`schema:population`s,  {ref}`schema:projection`s and lists of  {ref}`schema:explicitconnection`s (either directly between components of the populations or via synapses), and an explicit temperature.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

temperature,{ref}`schema:dimensions:temperature`

```
````

(schema:basepopulation)=

## *basePopulation*




extends *{ref}`schema:basestandalone`*



<i>A population of cells (anything which extends  {ref}`schema:basecell`).</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

component, {ref}`schema:basecell`

```
````

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

(schema:population)=

## population




extends *{ref}`schema:basepopulation`*



<i>A population of components, with just one parameter for the **size**.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

size,Dimensionless

```
````

(schema:populationlist)=

## populationList




extends *{ref}`schema:basepopulation`*



<i>An explicit list of the cells in the population.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

size,

````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

instances, {ref}`schema:instance`

```
````

(schema:instance)=

## instance




<i>Specifies a single instance of a component in a population (placed at  {ref}`schema:location`).</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

location, {ref}`schema:location`

```
````

(schema:location)=

## location




<i>Specifies location of a single  {ref}`schema:instance` of a component in a population.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

x,Dimensionless
y,Dimensionless
z,Dimensionless

```
````

(schema:region)=

## region




<i>Initial attempt to specify 3D region for placing cells. Work in progress...</i>



````{tabbed} Child list
```{csv-table}
:widths: 8, 2
:width: 100%

rectangularExtent, {ref}`schema:rectangularextent`

```
````

(schema:rectangularextent)=

## rectangularExtent




<i>For defining a 3D rectangular box.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

xLength,Dimensionless
xStart,Dimensionless
yLength,Dimensionless
yStart,Dimensionless
zLength,Dimensionless
zStart,Dimensionless

```
````

(schema:projection)=

## projection




<i>Projection from one population, **presynapticPopulation** to another, **postsynapticPopulation,** through **synapse.** Contains lists of  {ref}`schema:connection` or  {ref}`schema:connectionwd` elements.</i>



````{tabbed} Paths
```{csv-table}
:width: 100%

presynapticPopulation,
postsynapticPopulation,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

connections, {ref}`schema:connection`
connectionsWD, {ref}`schema:connectionwd`

```
````

(schema:explicitconnection)=

## explicitConnection




<i>Explicit event connection between components.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

targetPort,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

from,
to,

````

(schema:connection)=

## connection




<i>Event connection directly between named components, which gets processed via a new instance of a **synapse** component which is created on the target component. Normally contained inside a  {ref}`schema:projection` element.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,
preFractionAlong,
postFractionAlong,
preSegmentId,
postSegmentId,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCellId,
postCellId,

````

(schema:synapticconnection)=

## synapticConnection




extends {ref}`schema:explicitconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a **synapse** component which is created on the target component.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

from,
to,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:basesynapse`

```
````

(schema:synapticconnectionwd)=

## synapticConnectionWD




extends {ref}`schema:synapticconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a **synapse** component which is created on the target component, includes setting of **weight** and **delay** for the synaptic connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

delay,{ref}`schema:dimensions:time`
weight,Dimensionless

```
````

````{tabbed} Paths
```{csv-table}
:width: 100%

from,
to,

````

(schema:connectionwd)=

## connectionWD




extends {ref}`schema:connection`



<i>Event connection between named components, which gets processed via a new instance of a synapse component which is created on the target component, includes setting of **weight** and **delay** for the synaptic connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

delay,{ref}`schema:dimensions:time`
weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,
preFractionAlong,
postFractionAlong,
preSegmentId,
postSegmentId,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCellId,
postCellId,

````

(schema:electricalconnection)=

## electricalConnection




<i>To enable connections between populations through gap junctions.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:gapjunction`

```
````

(schema:electricalconnectioninstance)=

## electricalConnectionInstance




<i>To enable connections between populations through gap junctions. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

synapse, {ref}`schema:gapjunction`

```
````

(schema:electricalconnectioninstancew)=

## electricalConnectionInstanceW




extends {ref}`schema:electricalconnectioninstance`



<i>To enable connections between populations through gap junctions. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Includes setting of **weight** for the connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

(schema:electricalprojection)=

## electricalProjection




<i>A projection between **presynapticPopulation** to another **postsynapticPopulation** through gap junctions.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

presynapticPopulation, {ref}`schema:population`
postsynapticPopulation, {ref}`schema:population`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

connections, {ref}`schema:electricalconnection`
connectionInstances, {ref}`schema:electricalconnectioninstance`

```
````

(schema:continuousconnection)=

## continuousConnection




<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Can be used for analog synapses.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

preComponent, {ref}`schema:basegradedsynapse`
postComponent, {ref}`schema:basegradedsynapse`

```
````

(schema:continuousconnectioninstance)=

## continuousConnectionInstance




<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Can be used for analog synapses.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

preComponent, {ref}`schema:basegradedsynapse`
postComponent, {ref}`schema:basegradedsynapse`

```
````

(schema:continuousconnectioninstancew)=

## continuousConnectionInstanceW




extends {ref}`schema:continuousconnectioninstance`



<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Can be used for analog synapses. Includes setting of **weight** for the connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

preFractionAlong,
postFractionAlong,
preSegment,
postSegment,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

preCell,
postCell,

````

(schema:continuousprojection)=

## continuousProjection




<i>A projection between **presynapticPopulation** and **postsynapticPopulation** through components **preComponent** at the start and **postComponent** at the end of a  {ref}`schema:continuousconnection` or  {ref}`schema:continuousconnectioninstance`. Can be used for analog synapses.</i>



````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

presynapticPopulation, {ref}`schema:population`
postsynapticPopulation, {ref}`schema:population`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

connections, {ref}`schema:continuousconnection`
connectionInstances, {ref}`schema:continuousconnectioninstance`

```
````

(schema:explicitinput)=

## explicitInput




<i>An explicit input (anything which extends  {ref}`schema:basepointcurrent`) to a target cell in a population.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,
sourcePort,
targetPort,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

target,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

input, {ref}`schema:basepointcurrent`

```
````

(schema:inputlist)=

## inputList




<i>An explicit list of inputs. Not yet stable...</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

population,

````

````{tabbed} Component References
```{csv-table}
:widths: 8, 2
:width: 100%

component, {ref}`schema:basepointcurrent`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 8, 2
:width: 100%

inputs, {ref}`schema:input`

```
````

(schema:input)=

## input




<i>Specifies input lists.</i>



````{tabbed} Text fields
```{csv-table}
:width: 100%

segmentId,
fractionAlong,
destination,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

target,

````

(schema:inputw)=

## inputW




extends {ref}`schema:input`



<i>Specifies input lists. Can set **weight** to scale individual inputs.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 8, 2
:width: 100%

weight,Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:width: 100%

destination,

````

````{tabbed} Paths
```{csv-table}
:width: 100%

target,

````
