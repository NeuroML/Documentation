
(schema:networks_)=
# Networks

**Network descriptions for NeuroML 2. Describes  {ref}`schema:network` elements containing  {ref}`schema:population`s ( potentially of type  {ref}`schema:populationlist`, and so specifying a list of cell  {ref}`schema:location`s ),  {ref}`schema:projection`s ( i.e. lists of  {ref}`schema:connection`s ) and  {ref}`schema:input`s.**

---


Original ComponentType definitions: [Networks.xml](https://github.com/NeuroML/NeuroML2/blob/documentation_update/NeuroML2CoreTypes//Networks.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.2.xsd](https://github.com/NeuroML/NeuroML2/tree/documentation_update/Schemas/NeuroML2/NeuroML_v2.2.xsd).
Generated on 18/08/21 from [this](https://github.com/NeuroML/NeuroML2/commit/4d38dbbe8313b7273c206db82dad67aaeacf45f4) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:network)=

## network




extends *{ref}`schema:basestandalone`*



<i>Network containing:  {ref}`schema:population`s ( potentially of type  {ref}`schema:populationlist`, and so specifying a list of cell  {ref}`schema:location`s );  {ref}`schema:projection`s ( with lists of  {ref}`schema:connection`s ) and/or  {ref}`schema:explicitconnection`s; and  {ref}`schema:inputlist`s ( with lists of  {ref}`schema:input`s ) and/or  {ref}`schema:explicitinput`s. Note: often in NeuroML this will be of type  {ref}`schema:networkwithtemperature` if there are temperature dependent elements ( e.g. ion channels ).</i>



````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**regions**$  $ {ref}`schema:region`
**populations**$  $ {ref}`schema:basepopulation`
**projections**$  $ {ref}`schema:projection`
**synapticConnections**$  $ {ref}`schema:explicitconnection`
**electricalProjection**$  $ {ref}`schema:electricalprojection`
**continuousProjection**$  $ {ref}`schema:continuousprojection`
**explicitInputs**$  $ {ref}`schema:explicitinput`
**inputs**$  $ {ref}`schema:inputlist`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Network" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Network

variable = Network(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, type=None, temperature=None, spaces=None, regions=None, extracellular_properties=None, populations=None, cell_sets=None, synaptic_connections=None, projections=None, electrical_projections=None, continuous_projections=None, explicit_inputs=None, input_lists=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<network id="net1">
        <population id="iafPop1" component="iaf" size="1"/>
        <population id="iafPop2" component="iaf" size="1"/>
        <population id="iafPop3" component="iaf" size="1"/>
        <continuousProjection id="testLinearGradedConn" presynapticPopulation="iafPop1" postsynapticPopulation="iafPop2">
            <continuousConnection id="0" preCell="0" postCell="0" preComponent="silent1" postComponent="gs1"/>
        </continuousProjection>
        <continuousProjection id="testGradedConn" presynapticPopulation="iafPop1" postsynapticPopulation="iafPop3">
            <continuousConnection id="0" preCell="0" postCell="0" preComponent="silent2" postComponent="gs2"/>
        </continuousProjection>
        <explicitInput target="iafPop1[0]" input="pulseGen1" destination="synapses"/>
        <explicitInput target="iafPop1[0]" input="pulseGen2" destination="synapses"/>
        <explicitInput target="iafPop1[0]" input="pulseGen3" destination="synapses"/>
    </network>
```
```{code-block} xml
<network id="net2">
        <population id="hhPop1" component="hhcell" size="1" type="populationList">
            <instance id="0">
                <location x="0" y="0" z="0"/>
            </instance>
        </population>
        <population id="hhPop2" component="hhcell" size="1" type="populationList">
            <instance id="0">
                <location x="100" y="0" z="0"/>
            </instance>
        </population>
        <continuousProjection id="testGradedConn" presynapticPopulation="hhPop1" postsynapticPopulation="hhPop2">
            <continuousConnectionInstanceW id="0" preCell="../hhPop1/0/hhcell" postCell="../hhPop2/0/hhcell" preComponent="silent1" postComponent="gs1" weight="1"/>
        </continuousProjection>
        <inputList id="i1" component="pulseGen1" population="hhPop1">
            <input id="0" target="../hhPop1/0/hhcell" destination="synapses"/>
        </inputList>
    </network>
```
```{code-block} xml
<network id="PyrCellNet">   
    
        
        <population id="Population1" component="PyrCell" extracellularProperties="extracellular" size="9"> 
        </population>
        <projection id="Proj1" presynapticPopulation="Population1" postsynapticPopulation="Population1" synapse="AMPA">
           
        </projection>
    </network>
```

````

(schema:networkwithtemperature)=

## networkWithTemperature




extends {ref}`schema:network`



<i>Same as  {ref}`schema:network`, but with an explicit **temperature** for temperature dependent elements ( e.g. ion channels ).</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  ${ref}`schema:dimensions:temperature`

```
````

(schema:basepopulation)=

## *basePopulation*




extends *{ref}`schema:basestandalone`*



<i>A population of multiple instances of a specific **component,** which anything which extends  {ref}`schema:basecell`.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**component**$  $ {ref}`schema:basecell`

```
````

````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**annotation**$  $ {ref}`schema:annotation`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`

```
````

(schema:population)=

## population




extends *{ref}`schema:basepopulation`*



<i>A population of components, with just one parameter for the **size,** i.e. number of components to create. Note: quite often this is used with type= {ref}`schema:populationlist` which means the size is determined by the number of  {ref}`schema:instance`s ( with  {ref}`schema:location`s ) in the list. The **size** attribute is still set, and there will be a validation error if this does not match the number in the list.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**size**$ Number of instances of this Component to create when the population is instantiated $Dimensionless

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Population" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Population

variable = Population(neuro_lex_id=None, id=None, metaid=None, notes=None, properties=None, annotation=None, component=None, size=None, type=None, extracellular_properties=None, layout=None, instances=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<population id="iafPop1" component="iaf" size="1"/>
```
```{code-block} xml
<population id="iafPop2" component="iaf" size="1"/>
```
```{code-block} xml
<population id="iafPop3" component="iaf" size="1"/>
```

````

(schema:populationlist)=

## populationList




extends *{ref}`schema:basepopulation`*



<i>An explicit list of  {ref}`schema:instance`s ( with  {ref}`schema:location`s ) of components in the population.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**size**$ Note: the size of the populationList to create is set by the number of explicitly defined instances. The size attribute is still set, and there will be a validation error if this does not match the number in the list.

````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**instances**$  $ {ref}`schema:instance`

```
````

(schema:instance)=

## instance




<i>Specifies a single instance of a component in a  {ref}`schema:population` ( placed at  {ref}`schema:location` ).</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**location**$  $ {ref}`schema:location`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Instance" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Instance

variable = Instance(id=None, i=None, j=None, k=None, location=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<instance id="0">
                <location x="0" y="0" z="0"/>
            </instance>
```
```{code-block} xml
<instance id="0">
                <location x="100" y="0" z="0"/>
            </instance>
```
```{code-block} xml
<instance id="0">
                <location x="0" y="0" z="0"/>
            </instance>
```

````

(schema:location)=

## location




<i>Specifies the ( x, y, z ) location of a single  {ref}`schema:instance` of a component in a  {ref}`schema:population`.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  $Dimensionless
**y**$  $Dimensionless
**z**$  $Dimensionless

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Location" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Location

variable = Location(x=None, y=None, z=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<location x="0" y="0" z="0"/>
```
```{code-block} xml
<location x="100" y="0" z="0"/>
```
```{code-block} xml
<location x="0" y="0" z="0"/>
```

````

(schema:region)=

## region




<i>Initial attempt to specify 3D region for placing cells. Work in progress...</i>



````{tabbed} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rectangularExtent**$  $ {ref}`schema:rectangularextent`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Region" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Region

variable = Region(neuro_lex_id=None, id=None, spaces=None, anytypeobjs_=None, **kwargs_)
```



````

(schema:rectangularextent)=

## rectangularExtent




<i>For defining a 3D rectangular box.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**xLength**$  $Dimensionless
**xStart**$  $Dimensionless
**yLength**$  $Dimensionless
**yStart**$  $Dimensionless
**zLength**$  $Dimensionless
**zStart**$  $Dimensionless

```
````

(schema:projection)=

## projection




<i>Projection from one population, **presynapticPopulation** to another, **postsynapticPopulation,** through **synapse.** Contains lists of  {ref}`schema:connection` or  {ref}`schema:connectionwd` elements.</i>



````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**presynapticPopulation**$ 
**postsynapticPopulation**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**connections**$  $ {ref}`schema:connection`
**connectionsWD**$  $ {ref}`schema:connectionwd`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Projection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Projection

variable = Projection(neuro_lex_id=None, id=None, presynaptic_population=None, postsynaptic_population=None, synapse=None, connections=None, connection_wds=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<projection id="Proj1" presynapticPopulation="Population1" postsynapticPopulation="Population1" synapse="AMPA">
           
        </projection>
```
```{code-block} xml
<projection id="internal1" presynapticPopulation="iafCells" postsynapticPopulation="iafCells" synapse="syn1">
            <!--TODO: Fix! want to define synapse in here, so that multiple synapses per connection can be defined
            <synapseComponent component="syn1"/>-->
            
            <connection id="0" preCellId="../iafCells/0/iaf" postCellId="../iafCells/1/iaf"/>
        </projection>
```
```{code-block} xml
<projection id="internal2" presynapticPopulation="iafCells" postsynapticPopulation="iafCells" synapse="syn2">
            <connection id="0" preCellId="../iafCells/0/iaf" postCellId="../iafCells/2/iaf"/>
        </projection>
```

````

(schema:explicitconnection)=

## explicitConnection




<i>Explicit event connection between components.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**targetPort**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**from**$ 
**to**$ 

````

(schema:connection)=

## connection




<i>Event connection directly between named components, which gets processed via a new instance of a **synapse** component which is created on the target component. Normally contained inside a  {ref}`schema:projection` element.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 
**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegmentId**$ 
**postSegmentId**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCellId**$ 
**postCellId**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Connection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Connection

variable = Connection(neuro_lex_id=None, id=None, pre_cell_id=None, pre_segment_id='0', pre_fraction_along='0.5', post_cell_id=None, post_segment_id='0', post_fraction_along='0.5', **kwargs_)
```



*XML examples*
```{code-block} xml
<connection id="0" preCellId="../iafCells/0/iaf" postCellId="../iafCells/1/iaf"/>
```
```{code-block} xml
<connection id="0" preCellId="../iafCells/0/iaf" postCellId="../iafCells/2/iaf"/>
```
```{code-block} xml
<connection id="0" preCellId="../pop0/0/MultiCompCell" postCellId="../pop0/1/MultiCompCell" preSegmentId="0" preFractionAlong="0.5" postSegmentId="0" postFractionAlong="0.5"/>
```

````

(schema:synapticconnection)=

## synapticConnection




extends {ref}`schema:explicitconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a **synapse** component which is created on the target component.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**from**$ 
**to**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SynapticConnection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import SynapticConnection

variable = SynapticConnection(from_=None, to=None, synapse=None, destination=None, **kwargs_)
```



````

(schema:synapticconnectionwd)=

## synapticConnectionWD




extends {ref}`schema:synapticconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a **synapse** component which is created on the target component, includes setting of **weight** and **delay** for the synaptic connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**delay**$  ${ref}`schema:dimensions:time`
**weight**$  $Dimensionless

```
````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**from**$ 
**to**$ 

````

(schema:connectionwd)=

## connectionWD




extends {ref}`schema:connection`



<i>Event connection between named components, which gets processed via a new instance of a synapse component which is created on the target component, includes setting of **weight** and **delay** for the synaptic connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**delay**$  ${ref}`schema:dimensions:time`
**weight**$  $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 
**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegmentId**$ 
**postSegmentId**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCellId**$ 
**postCellId**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ConnectionWD" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ConnectionWD

variable = ConnectionWD(neuro_lex_id=None, id=None, pre_cell_id=None, pre_segment_id='0', pre_fraction_along='0.5', post_cell_id=None, post_segment_id='0', post_fraction_along='0.5', weight=None, delay=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<connectionWD id="0" preCellId="../pop_EIF_cond_exp_isfa_ista[0]" postCellId="../pop_target[0]" weight="0.01" delay="10ms"/>
```
```{code-block} xml
<connectionWD id="0" preCellId="../pop_EIF_cond_alpha_isfa_ista[0]" postCellId="../pop_target[1]" weight="0.005" delay="20ms"/>
```
```{code-block} xml
<connectionWD id="0" preCellId="../pop_IF_curr_alpha[0]" postCellId="../pop_target[2]" weight="1" delay="30ms"/>
```

````

(schema:electricalconnection)=

## electricalConnection




<i>To enable connections between populations through gap junctions.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:gapjunction`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalConnection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ElectricalConnection

variable = ElectricalConnection(neuro_lex_id=None, id=None, pre_cell=None, pre_segment='0', pre_fraction_along='0.5', post_cell=None, post_segment='0', post_fraction_along='0.5', synapse=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<electricalConnection id="0" preCell="0" postCell="0" synapse="gj1"/>
```

````

(schema:electricalconnectioninstance)=

## electricalConnectionInstance




<i>To enable connections between populations through gap junctions. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:gapjunction`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalConnectionInstance" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ElectricalConnectionInstance

variable = ElectricalConnectionInstance(neuro_lex_id=None, id=None, pre_cell=None, pre_segment='0', pre_fraction_along='0.5', post_cell=None, post_segment='0', post_fraction_along='0.5', synapse=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<electricalConnectionInstance id="0" preCell="../iafPop1/0/iaf" postCell="../iafPop2/0/iaf" preSegment="0" preFractionAlong="0.5" postSegment="0" postFractionAlong="0.5" synapse="gj1"/>
```

````

(schema:electricalconnectioninstancew)=

## electricalConnectionInstanceW




extends {ref}`schema:electricalconnectioninstance`



<i>To enable connections between populations through gap junctions. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Includes setting of **weight** for the connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**weight**$  $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalConnectionInstanceW" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ElectricalConnectionInstanceW

variable = ElectricalConnectionInstanceW(neuro_lex_id=None, id=None, pre_cell=None, pre_segment='0', pre_fraction_along='0.5', post_cell=None, post_segment='0', post_fraction_along='0.5', synapse=None, weight=None, **kwargs_)
```



````

(schema:electricalprojection)=

## electricalProjection




<i>A projection between **presynapticPopulation** to another **postsynapticPopulation** through gap junctions.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**presynapticPopulation**$  $ {ref}`schema:population`
**postsynapticPopulation**$  $ {ref}`schema:population`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**connections**$  $ {ref}`schema:electricalconnection`
**connectionInstances**$  $ {ref}`schema:electricalconnectioninstance`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalProjection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ElectricalProjection

variable = ElectricalProjection(neuro_lex_id=None, id=None, presynaptic_population=None, postsynaptic_population=None, electrical_connections=None, electrical_connection_instances=None, electrical_connection_instance_ws=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<electricalProjection id="testGJconn" presynapticPopulation="iafPop1" postsynapticPopulation="iafPop2">
            <electricalConnectionInstance id="0" preCell="../iafPop1/0/iaf" postCell="../iafPop2/0/iaf" preSegment="0" preFractionAlong="0.5" postSegment="0" postFractionAlong="0.5" synapse="gj1"/>
        </electricalProjection>
```
```{code-block} xml
<electricalProjection id="testGJconn" presynapticPopulation="iafPop1" postsynapticPopulation="iafPop2">
            <electricalConnection id="0" preCell="0" postCell="0" synapse="gj1"/>
        </electricalProjection>
```

````

(schema:continuousconnection)=

## continuousConnection




<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Can be used for analog synapses.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**preComponent**$  $ {ref}`schema:basegradedsynapse`
**postComponent**$  $ {ref}`schema:basegradedsynapse`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousConnection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ContinuousConnection

variable = ContinuousConnection(neuro_lex_id=None, id=None, pre_cell=None, pre_segment='0', pre_fraction_along='0.5', post_cell=None, post_segment='0', post_fraction_along='0.5', pre_component=None, post_component=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<continuousConnection id="0" preCell="0" postCell="0" preComponent="silent1" postComponent="gs1"/>
```
```{code-block} xml
<continuousConnection id="0" preCell="0" postCell="0" preComponent="silent2" postComponent="gs2"/>
```

````

(schema:continuousconnectioninstance)=

## continuousConnectionInstance




<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Can be used for analog synapses.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**preComponent**$  $ {ref}`schema:basegradedsynapse`
**postComponent**$  $ {ref}`schema:basegradedsynapse`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousConnectionInstance" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ContinuousConnectionInstance

variable = ContinuousConnectionInstance(neuro_lex_id=None, id=None, pre_cell=None, pre_segment='0', pre_fraction_along='0.5', post_cell=None, post_segment='0', post_fraction_along='0.5', pre_component=None, post_component=None, extensiontype_=None, **kwargs_)
```



````

(schema:continuousconnectioninstancew)=

## continuousConnectionInstanceW




extends {ref}`schema:continuousconnectioninstance`



<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Can be used for analog synapses. Includes setting of **weight** for the connection.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**weight**$  $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousConnectionInstanceW" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ContinuousConnectionInstanceW

variable = ContinuousConnectionInstanceW(neuro_lex_id=None, id=None, pre_cell=None, pre_segment='0', pre_fraction_along='0.5', post_cell=None, post_segment='0', post_fraction_along='0.5', pre_component=None, post_component=None, weight=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<continuousConnectionInstanceW id="0" preCell="../hhPop1/0/hhcell" postCell="../hhPop2/0/hhcell" preComponent="silent1" postComponent="gs1" weight="1"/>
```

````

(schema:continuousprojection)=

## continuousProjection




<i>A projection between **presynapticPopulation** and **postsynapticPopulation** through components **preComponent** at the start and **postComponent** at the end of a  {ref}`schema:continuousconnection` or  {ref}`schema:continuousconnectioninstance`. Can be used for analog synapses.</i>



````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**presynapticPopulation**$  $ {ref}`schema:population`
**postsynapticPopulation**$  $ {ref}`schema:population`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**connections**$  $ {ref}`schema:continuousconnection`
**connectionInstances**$  $ {ref}`schema:continuousconnectioninstance`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousProjection" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ContinuousProjection

variable = ContinuousProjection(neuro_lex_id=None, id=None, presynaptic_population=None, postsynaptic_population=None, continuous_connections=None, continuous_connection_instances=None, continuous_connection_instance_ws=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<continuousProjection id="testLinearGradedConn" presynapticPopulation="iafPop1" postsynapticPopulation="iafPop2">
            <continuousConnection id="0" preCell="0" postCell="0" preComponent="silent1" postComponent="gs1"/>
        </continuousProjection>
```
```{code-block} xml
<continuousProjection id="testGradedConn" presynapticPopulation="iafPop1" postsynapticPopulation="iafPop3">
            <continuousConnection id="0" preCell="0" postCell="0" preComponent="silent2" postComponent="gs2"/>
        </continuousProjection>
```
```{code-block} xml
<continuousProjection id="testGradedConn" presynapticPopulation="hhPop1" postsynapticPopulation="hhPop2">
            <continuousConnectionInstanceW id="0" preCell="../hhPop1/0/hhcell" postCell="../hhPop2/0/hhcell" preComponent="silent1" postComponent="gs1" weight="1"/>
        </continuousProjection>
```

````

(schema:explicitinput)=

## explicitInput




<i>An explicit input ( anything which extends  {ref}`schema:basepointcurrent` ) to a target cell in a population.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 
**sourcePort**$ 
**targetPort**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**target**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**input**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExplicitInput" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import ExplicitInput

variable = ExplicitInput(target=None, input=None, destination=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<explicitInput target="iafPop1[0]" input="pulseGen1" destination="synapses"/>
```
```{code-block} xml
<explicitInput target="iafPop1[0]" input="pulseGen2" destination="synapses"/>
```
```{code-block} xml
<explicitInput target="iafPop1[0]" input="pulseGen3" destination="synapses"/>
```

````

(schema:inputlist)=

## inputList




<i>An explicit list of  {ref}`schema:input`s to a **population.**.</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**population**$ 

````

````{tabbed} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**component**$  $ {ref}`schema:basepointcurrent`

```
````

````{tabbed} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**inputs**$  $ {ref}`schema:input`

```
````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InputList" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import InputList

variable = InputList(neuro_lex_id=None, id=None, populations=None, component=None, input=None, input_ws=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<inputList id="i1" component="pulseGen1" population="hhPop1">
            <input id="0" target="../hhPop1/0/hhcell" destination="synapses"/>
        </inputList>
```
```{code-block} xml
<inputList id="i1" component="pulseGen1" population="iafPop1">
            <input id="0" target="../iafPop1/0/iaf" destination="synapses"/>
        </inputList>
```
```{code-block} xml
<inputList id="i2" component="pulseGen2" population="iafPop2">
            <input id="0" target="../iafPop2/0/iaf" destination="synapses"/>
        </inputList>
```

````

(schema:input)=

## input




<i>Specifies a single input to a **target,** optionally giving the **segmentId** ( default 0 ) and **fractionAlong** the segment ( default 0.5 ).</i>



````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentId**$ Optional specification of the segment to target, default 0
**fractionAlong**$ Optional specification of the fraction along the specified segment, default 0.5
**destination**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**target**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Input" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import Input

variable = Input(id=None, target=None, destination=None, segment_id=None, fraction_along=None, extensiontype_=None, **kwargs_)
```



*XML examples*
```{code-block} xml
<input id="0" target="../hhPop1/0/hhcell" destination="synapses"/>
```
```{code-block} xml
<input id="0" target="../iafPop1/0/iaf" destination="synapses"/>
```
```{code-block} xml
<input id="0" target="../iafPop2/0/iaf" destination="synapses"/>
```

````

(schema:inputw)=

## inputW




extends {ref}`schema:input`



<i>Specifies input lists. Can set **weight** to scale individual inputs.</i>



````{tabbed} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**weight**$  $Dimensionless

```
````

````{tabbed} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 

````

````{tabbed} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**target**$ 

````

````{tabbed} Usage

*Python: <a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InputW" target="_blank">libNeuroML API</a>*
```{code-block} python
from neuroml import InputW

variable = InputW(id=None, target=None, destination=None, segment_id=None, fraction_along=None, weight=None, **kwargs_)
```



````
