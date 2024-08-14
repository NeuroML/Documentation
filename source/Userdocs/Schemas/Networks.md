
(schema:networks_)=
# Networks

**Network descriptions for NeuroML 2. Describes  {ref}`schema:network` elements containing  {ref}`schema:population`s ( potentially of type  {ref}`schema:populationlist`, and so specifying a list of cell  {ref}`schema:location`s ),  {ref}`schema:projection`s ( i.e. lists of  {ref}`schema:connection`s ) and  {ref}`schema:input`s.**

---


Original ComponentType definitions: [Networks.xml](https://github.com/NeuroML/NeuroML2/blob/master/NeuroML2CoreTypes//Networks.xml).
Schema against which NeuroML based on these should be valid: [NeuroML_v2.3.xsd](https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2/NeuroML_v2.3.xsd).
Generated on 14/08/24 from [this](https://github.com/NeuroML/NeuroML2/commit/352244cff605cb1ba24fa7c11757dc818fe90fd2) commit.
Please file any issues or questions at the [issue tracker here](https://github.com/NeuroML/NeuroML2/issues).

---

(schema:network)=

## network




extends *{ref}`schema:basestandalone`*



<i>Network containing:  {ref}`schema:population`s ( potentially of type  {ref}`schema:populationlist`, and so specifying a list of cell  {ref}`schema:location`s );  {ref}`schema:projection`s ( with lists of  {ref}`schema:connection`s ) and/or  {ref}`schema:explicitconnection`s; and  {ref}`schema:inputlist`s ( with lists of  {ref}`schema:input`s ) and/or  {ref}`schema:explicitinput`s. Note: often in NeuroML this will be of type  {ref}`schema:networkwithtemperature` if there are temperature dependent elements ( e.g. ion channels ).</i>


`````{tab-set}
````{tab-item} Children list
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

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Network">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:sequence>
        <xs:element name="space" type="Space" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="region" type="Region" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="extracellularProperties" type="ExtracellularPropertiesLocal" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="population" type="Population" maxOccurs="unbounded"/>
        <xs:element name="cellSet" type="CellSet" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="synapticConnection" type="SynapticConnection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="projection" type="Projection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="electricalProjection" type="ElectricalProjection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="continuousProjection" type="ContinuousProjection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="explicitInput" type="ExplicitInput" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="inputList" type="InputList" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="type" type="networkTypes" use="optional"/>
      <xs:attribute name="temperature" type="Nml2Quantity_temperature" use="optional"/>
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Network" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Network
from neuroml.utils import component_factory

variable = component_factory(
    Network,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    type: 'a networkTypes (optional)' = None,
    temperature: 'a Nml2Quantity_temperature (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    spaces: 'list of Space(s) (optional)' = None,
    regions: 'list of Region(s) (optional)' = None,
    extracellular_properties: 'list of ExtracellularPropertiesLocal(s) (optional)' = None,
    populations: 'list of Population(s) (required)' = None,
    cell_sets: 'list of CellSet(s) (optional)' = None,
    synaptic_connections: 'list of SynapticConnection(s) (optional)' = None,
    projections: 'list of Projection(s) (optional)' = None,
    electrical_projections: 'list of ElectricalProjection(s) (optional)' = None,
    continuous_projections: 'list of ContinuousProjection(s) (optional)' = None,
    explicit_inputs: 'list of ExplicitInput(s) (optional)' = None,
    input_lists: 'list of InputList(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:networkwithtemperature)=

## networkWithTemperature




extends {ref}`schema:network`



<i>Same as  {ref}`schema:network`, but with an explicit **temperature** for temperature dependent elements ( e.g. ion channels ).</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**temperature**$  ${ref}`schema:dimensions:temperature`

```
````
`````

(schema:basepopulation)=

## *basePopulation*




extends *{ref}`schema:basestandalone`*



<i>A population of multiple instances of a specific **component,** which anything which extends  {ref}`schema:basecell`.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**component**$  $ {ref}`schema:basecell`

```
````

````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**notes**$  $ {ref}`schema:notes`
**annotation**$  $ {ref}`schema:annotation`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**property**$  $ {ref}`schema:property`

```
````
`````

(schema:population)=

## population




extends *{ref}`schema:basepopulation`*



<i>A population of components, with just one parameter for the **size,** i.e. number of components to create. Note: quite often this is used with type= {ref}`schema:populationlist` which means the size is determined by the number of  {ref}`schema:instance`s ( with  {ref}`schema:location`s ) in the list. The **size** attribute is still set, and there will be a validation error if this does not match the number in the list.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**size**$ Number of instances of this Component to create when the population is instantiated $Dimensionless

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Population">
  <xs:complexContent>
    <xs:extension base="Standalone">
      <xs:choice>
        <xs:element name="layout" type="Layout" minOccurs="0"/>
        <xs:element name="instance" type="Instance" maxOccurs="unbounded"/>
      </xs:choice>
      <xs:attribute name="component" type="NmlId" use="required"/>
      <xs:attribute name="size" type="NonNegativeInteger" use="optional"/>
      <xs:attribute name="type" type="populationTypes" use="optional"/>
      <xs:attribute name="extracellularProperties" type="NmlId" use="optional"/>
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Population" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Population
from neuroml.utils import component_factory

variable = component_factory(
    Population,
    id: 'a NmlId (required)' = None,
    metaid: 'a MetaId (optional)' = None,
    notes: 'a string (optional)' = None,
    properties: 'list of Property(s) (optional)' = None,
    annotation: 'a Annotation (optional)' = None,
    component: 'a NmlId (required)' = None,
    size: 'a NonNegativeInteger (optional)' = None,
    type: 'a populationTypes (optional)' = None,
    extracellular_properties: 'a NmlId (optional)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    layout: 'a Layout (optional)' = None,
    instances: 'list of Instance(s) (required)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:populationlist)=

## populationList




extends *{ref}`schema:basepopulation`*



<i>An explicit list of  {ref}`schema:instance`s ( with  {ref}`schema:location`s ) of components in the population.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**size**$ Note: the size of the populationList to create is set by the number of explicitly defined instances. The size attribute is still set, and there will be a validation error if this does not match the number in the list.

````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**instances**$  $ {ref}`schema:instance`

```
````
`````

(schema:instance)=

## instance




<i>Specifies a single instance of a component in a  {ref}`schema:population` ( placed at  {ref}`schema:location` ).</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**location**$  $ {ref}`schema:location`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Instance">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:sequence>
        <xs:element name="location" type="Location"/>
      </xs:sequence>
      <xs:attribute name="id" type="xs:nonNegativeInteger"/>
      <xs:attribute name="i" type="xs:nonNegativeInteger"/>
      <xs:attribute name="j" type="xs:nonNegativeInteger"/>
      <xs:attribute name="k" type="xs:nonNegativeInteger"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Instance" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Instance
from neuroml.utils import component_factory

variable = component_factory(
    Instance,
    id: 'a nonNegativeInteger (optional)' = None,
    i: 'a nonNegativeInteger (optional)' = None,
    j: 'a nonNegativeInteger (optional)' = None,
    k: 'a nonNegativeInteger (optional)' = None,
    location: 'a Location (required)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:location)=

## location




<i>Specifies the ( x, y, z ) location of a single  {ref}`schema:instance` of a component in a  {ref}`schema:population`.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**x**$  $Dimensionless
**y**$  $Dimensionless
**z**$  $Dimensionless

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Location">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="x" type="xs:float" use="required"/>
      <xs:attribute name="y" type="xs:float" use="required"/>
      <xs:attribute name="z" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Location" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Location
from neuroml.utils import component_factory

variable = component_factory(
    Location,
    x: 'a float (required)' = None,
    y: 'a float (required)' = None,
    z: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:region)=

## region




<i>Initial attempt to specify 3D region for placing cells. Work in progress...</i>


`````{tab-set}
````{tab-item} Child list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**rectangularExtent**$  $ {ref}`schema:rectangularextent`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Region">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:any processContents="skip" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="space" type="NmlId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Region" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Region
from neuroml.utils import component_factory

variable = component_factory(
    Region,
    id: 'a NmlId (required)' = None,
    spaces: 'a NmlId (optional)' = None,
    anytypeobjs_=None,
)
```
````
`````

(schema:rectangularextent)=

## rectangularExtent




<i>For defining a 3D rectangular box.</i>


`````{tab-set}
````{tab-item} Parameters
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
`````

(schema:projection)=

## projection




<i>Projection from one population, **presynapticPopulation** to another, **postsynapticPopulation,** through **synapse.** Contains lists of  {ref}`schema:connection` or  {ref}`schema:connectionwd` elements.</i>


`````{tab-set}
````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**presynapticPopulation**$ 
**postsynapticPopulation**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**connections**$  $ {ref}`schema:connection`
**connectionsWD**$  $ {ref}`schema:connectionwd`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Projection">
  <xs:complexContent>
    <xs:extension base="BaseProjection">
      <xs:sequence>
        <xs:element name="connection" type="Connection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="connectionWD" type="ConnectionWD" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="synapse" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Projection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Projection
from neuroml.utils import component_factory

variable = component_factory(
    Projection,
    id: 'a NmlId (required)' = None,
    presynaptic_population: 'a NmlId (required)' = None,
    postsynaptic_population: 'a NmlId (required)' = None,
    synapse: 'a NmlId (required)' = None,
    connections: 'list of Connection(s) (optional)' = None,
    connection_wds: 'list of ConnectionWD(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<projection id="Proj1" presynapticPopulation="Population1" postsynapticPopulation="Population1" synapse="AMPA">
           
        </projection>
```
```{code-block} xml
<projection id="internal1" presynapticPopulation="iafCells" postsynapticPopulation="iafCells" synapse="syn1">
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
`````

(schema:explicitconnection)=

## explicitConnection




<i>Explicit event connection between components.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**targetPort**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**from**$ 
**to**$ 

````
`````

(schema:connection)=

## connection




<i>Event connection directly between named components, which gets processed via a new instance of a **synapse** component which is created on the target component. Normally contained inside a  {ref}`schema:projection` element.</i>


`````{tab-set}
````{tab-item} Text fields
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

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCellId**$ 
**postCellId**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Connection">
  <xs:complexContent>
    <xs:extension base="BaseConnectionOldFormat">
            </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Connection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Connection
from neuroml.utils import component_factory

variable = component_factory(
    Connection,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell_id: 'a Nml2PopulationReferencePath (required)' = None,
    pre_segment_id: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell_id: 'a Nml2PopulationReferencePath (required)' = None,
    post_segment_id: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:synapticconnection)=

## synapticConnection




extends {ref}`schema:explicitconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a **synapse** component which is created on the target component.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**from**$ 
**to**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:basesynapse`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="SynapticConnection">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="neuroLexId" type="NeuroLexId" use="optional"/>
      <xs:attribute name="from" type="Nml2PopulationReferencePath" use="required"/>
      <xs:attribute name="to" type="Nml2PopulationReferencePath" use="required"/>
      <xs:attribute name="synapse" type="NmlId" use="required"/>
      <xs:attribute name="destination" type="NmlId" use="optional"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=SynapticConnection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import SynapticConnection
from neuroml.utils import component_factory

variable = component_factory(
    SynapticConnection,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    from_: 'a Nml2PopulationReferencePath (required)' = None,
    to: 'a Nml2PopulationReferencePath (required)' = None,
    synapse: 'a NmlId (required)' = None,
    destination: 'a NmlId (optional)' = None,
)
```
````
`````

(schema:synapticconnectionwd)=

## synapticConnectionWD




extends {ref}`schema:synapticconnection`



<i>Explicit event connection between named components, which gets processed via a new instance of a **synapse** component which is created on the target component, includes setting of **weight** and **delay** for the synaptic connection.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**delay**$  ${ref}`schema:dimensions:time`
**weight**$  $Dimensionless

```
````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**from**$ 
**to**$ 

````
`````

(schema:connectionwd)=

## connectionWD




extends {ref}`schema:connection`



<i>Event connection between named components, which gets processed via a new instance of a synapse component which is created on the target component, includes setting of **weight** and **delay** for the synaptic connection.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**delay**$  ${ref}`schema:dimensions:time`
**weight**$  $Dimensionless

```
````

````{tab-item} Text fields
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

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCellId**$ 
**postCellId**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ConnectionWD">
  <xs:complexContent>
    <xs:extension base="BaseConnectionOldFormat">
      <xs:attribute name="weight" type="xs:float" use="required"/>
      <xs:attribute name="delay" type="Nml2Quantity_time" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ConnectionWD" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ConnectionWD
from neuroml.utils import component_factory

variable = component_factory(
    ConnectionWD,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell_id: 'a Nml2PopulationReferencePath (required)' = None,
    pre_segment_id: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell_id: 'a Nml2PopulationReferencePath (required)' = None,
    post_segment_id: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    weight: 'a float (required)' = None,
    delay: 'a Nml2Quantity_time (required)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:electricalconnection)=

## electricalConnection




<i>To enable connections between populations through gap junctions.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:gapjunction`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ElectricalConnection">
  <xs:complexContent>
    <xs:extension base="BaseConnectionNewFormat">
      <xs:attribute name="synapse" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalConnection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ElectricalConnection
from neuroml.utils import component_factory

variable = component_factory(
    ElectricalConnection,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell: 'a string (required)' = None,
    pre_segment: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell: 'a string (required)' = None,
    post_segment: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    synapse: 'a NmlId (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<electricalConnection id="0" preCell="0" postCell="0" synapse="gj1"/>
```
````
`````

(schema:electricalconnectioninstance)=

## electricalConnectionInstance




<i>To enable connections between populations through gap junctions. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**synapse**$  $ {ref}`schema:gapjunction`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ElectricalConnectionInstance">
  <xs:complexContent>
    <xs:extension base="ElectricalConnection"/>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalConnectionInstance" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ElectricalConnectionInstance
from neuroml.utils import component_factory

variable = component_factory(
    ElectricalConnectionInstance,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell: 'a string (required)' = None,
    pre_segment: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell: 'a string (required)' = None,
    post_segment: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    synapse: 'a NmlId (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<electricalConnectionInstance id="0" preCell="../iafPop1/0/iaf" postCell="../iafPop2/0/iaf" preSegment="0" preFractionAlong="0.5" postSegment="0" postFractionAlong="0.5" synapse="gj1"/>
```
````
`````

(schema:electricalconnectioninstancew)=

## electricalConnectionInstanceW




extends {ref}`schema:electricalconnectioninstance`



<i>To enable connections between populations through gap junctions. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Includes setting of **weight** for the connection.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**weight**$  $Dimensionless

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ElectricalConnectionInstanceW">
  <xs:complexContent>
    <xs:extension base="ElectricalConnectionInstance">
      <xs:attribute name="weight" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalConnectionInstanceW" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ElectricalConnectionInstanceW
from neuroml.utils import component_factory

variable = component_factory(
    ElectricalConnectionInstanceW,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell: 'a string (required)' = None,
    pre_segment: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell: 'a string (required)' = None,
    post_segment: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    synapse: 'a NmlId (required)' = None,
    weight: 'a float (required)' = None,
)
```
````
`````

(schema:electricalprojection)=

## electricalProjection




<i>A projection between **presynapticPopulation** to another **postsynapticPopulation** through gap junctions.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**presynapticPopulation**$  $ {ref}`schema:population`
**postsynapticPopulation**$  $ {ref}`schema:population`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**connections**$  $ {ref}`schema:electricalconnection`
**connectionInstances**$  $ {ref}`schema:electricalconnectioninstance`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ElectricalProjection">
  <xs:complexContent>
    <xs:extension base="BaseProjection">
      <xs:sequence>
        <xs:element name="electricalConnection" type="ElectricalConnection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="electricalConnectionInstance" type="ElectricalConnectionInstance" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="electricalConnectionInstanceW" type="ElectricalConnectionInstanceW" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ElectricalProjection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ElectricalProjection
from neuroml.utils import component_factory

variable = component_factory(
    ElectricalProjection,
    id: 'a NmlId (required)' = None,
    presynaptic_population: 'a NmlId (required)' = None,
    postsynaptic_population: 'a NmlId (required)' = None,
    electrical_connections: 'list of ElectricalConnection(s) (optional)' = None,
    electrical_connection_instances: 'list of ElectricalConnectionInstance(s) (optional)' = None,
    electrical_connection_instance_ws: 'list of ElectricalConnectionInstanceW(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:continuousconnection)=

## continuousConnection




<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Can be used for analog synapses.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**preComponent**$  $ {ref}`schema:basegradedsynapse`
**postComponent**$  $ {ref}`schema:basegradedsynapse`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ContinuousConnection">
  <xs:complexContent>
    <xs:extension base="BaseConnectionNewFormat">
      <xs:attribute name="preComponent" type="NmlId" use="required"/>
      <xs:attribute name="postComponent" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousConnection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ContinuousConnection
from neuroml.utils import component_factory

variable = component_factory(
    ContinuousConnection,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell: 'a string (required)' = None,
    pre_segment: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell: 'a string (required)' = None,
    post_segment: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    pre_component: 'a NmlId (required)' = None,
    post_component: 'a NmlId (required)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<continuousConnection id="0" preCell="0" postCell="0" preComponent="silent1" postComponent="gs1"/>
```
```{code-block} xml
<continuousConnection id="0" preCell="0" postCell="0" preComponent="silent2" postComponent="gs2"/>
```
````
`````

(schema:continuousconnectioninstance)=

## continuousConnectionInstance




<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Can be used for analog synapses.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**preComponent**$  $ {ref}`schema:basegradedsynapse`
**postComponent**$  $ {ref}`schema:basegradedsynapse`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ContinuousConnectionInstance">
  <xs:complexContent>
    <xs:extension base="ContinuousConnection"/>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousConnectionInstance" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ContinuousConnectionInstance
from neuroml.utils import component_factory

variable = component_factory(
    ContinuousConnectionInstance,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell: 'a string (required)' = None,
    pre_segment: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell: 'a string (required)' = None,
    post_segment: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    pre_component: 'a NmlId (required)' = None,
    post_component: 'a NmlId (required)' = None,
    extensiontype_=None,
)
```
````
`````

(schema:continuousconnectioninstancew)=

## continuousConnectionInstanceW




extends {ref}`schema:continuousconnectioninstance`



<i>An instance of a connection in a  {ref}`schema:continuousprojection` between **presynapticPopulation** to another **postsynapticPopulation** through a **preComponent** at the start and **postComponent** at the end. Populations need to be of type  {ref}`schema:populationlist` and contain  {ref}`schema:instance` and  {ref}`schema:location` elements. Can be used for analog synapses. Includes setting of **weight** for the connection.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**weight**$  $Dimensionless

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preFractionAlong**$ 
**postFractionAlong**$ 
**preSegment**$ 
**postSegment**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**preCell**$ 
**postCell**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ContinuousConnectionInstanceW">
  <xs:complexContent>
    <xs:extension base="ContinuousConnectionInstance">
      <xs:attribute name="weight" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousConnectionInstanceW" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ContinuousConnectionInstanceW
from neuroml.utils import component_factory

variable = component_factory(
    ContinuousConnectionInstanceW,
    id: 'a NonNegativeInteger (required)' = None,
    neuro_lex_id: 'a NeuroLexId (optional)' = None,
    pre_cell: 'a string (required)' = None,
    pre_segment: 'a NonNegativeInteger (optional)' = '0',
    pre_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    post_cell: 'a string (required)' = None,
    post_segment: 'a NonNegativeInteger (optional)' = '0',
    post_fraction_along: 'a ZeroToOne (optional)' = '0.5',
    pre_component: 'a NmlId (required)' = None,
    post_component: 'a NmlId (required)' = None,
    weight: 'a float (required)' = None,
)
```
````
````{tab-item} Usage: XML
```{code-block} xml
<continuousConnectionInstanceW id="0" preCell="../hhPop1/0/hhcell" postCell="../hhPop2/0/hhcell" preComponent="silent1" postComponent="gs1" weight="1"/>
```
````
`````

(schema:continuousprojection)=

## continuousProjection




<i>A projection between **presynapticPopulation** and **postsynapticPopulation** through components **preComponent** at the start and **postComponent** at the end of a  {ref}`schema:continuousconnection` or  {ref}`schema:continuousconnectioninstance`. Can be used for analog synapses.</i>


`````{tab-set}
````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**presynapticPopulation**$  $ {ref}`schema:population`
**postsynapticPopulation**$  $ {ref}`schema:population`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**connections**$  $ {ref}`schema:continuousconnection`
**connectionInstances**$  $ {ref}`schema:continuousconnectioninstance`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ContinuousProjection">
  <xs:complexContent>
    <xs:extension base="BaseProjection">
      <xs:sequence>
        <xs:element name="continuousConnection" type="ContinuousConnection" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="continuousConnectionInstance" type="ContinuousConnectionInstance" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="continuousConnectionInstanceW" type="ContinuousConnectionInstanceW" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ContinuousProjection" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ContinuousProjection
from neuroml.utils import component_factory

variable = component_factory(
    ContinuousProjection,
    id: 'a NmlId (required)' = None,
    presynaptic_population: 'a NmlId (required)' = None,
    postsynaptic_population: 'a NmlId (required)' = None,
    continuous_connections: 'list of ContinuousConnection(s) (optional)' = None,
    continuous_connection_instances: 'list of ContinuousConnectionInstance(s) (optional)' = None,
    continuous_connection_instance_ws: 'list of ContinuousConnectionInstanceW(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:explicitinput)=

## explicitInput




<i>An explicit input ( anything which extends  {ref}`schema:basepointcurrent` ) to a target cell in a population.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 
**sourcePort**$ 
**targetPort**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**target**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**input**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="ExplicitInput">
  <xs:complexContent>
    <xs:extension base="BaseWithoutId">
      <xs:attribute name="target" type="Nml2PopulationReferencePath" use="required"/>
      <xs:attribute name="input" type="NmlId" use="required"/>
      <xs:attribute name="destination" type="NmlId"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=ExplicitInput" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import ExplicitInput
from neuroml.utils import component_factory

variable = component_factory(
    ExplicitInput,
    target: 'a Nml2PopulationReferencePath (required)' = None,
    input: 'a NmlId (required)' = None,
    destination: 'a NmlId (optional)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:inputlist)=

## inputList




<i>An explicit list of  {ref}`schema:input`s to a **population.**.</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**population**$ 

````

````{tab-item} Component References
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**component**$  $ {ref}`schema:basepointcurrent`

```
````

````{tab-item} Children list
```{csv-table}
:widths: 1, 7, 2
:width: 100%
:delim: $

**inputs**$  $ {ref}`schema:input`

```
````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="InputList">
  <xs:complexContent>
    <xs:extension base="Base">
      <xs:sequence>
        <xs:element name="input" type="Input" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element name="inputW" type="InputW" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="population" type="NmlId" use="required"/>
      <xs:attribute name="component" type="NmlId" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InputList" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import InputList
from neuroml.utils import component_factory

variable = component_factory(
    InputList,
    id: 'a NonNegativeInteger (required)' = None,
    populations: 'a NmlId (required)' = None,
    component: 'a NmlId (required)' = None,
    input: 'list of Input(s) (optional)' = None,
    input_ws: 'list of InputW(s) (optional)' = None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:input)=

## input




<i>Specifies a single input to a **target,** optionally giving the **segmentId** ( default 0 ) and **fractionAlong** the segment ( default 0.5 ).</i>


`````{tab-set}
````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**segmentId**$ Optional specification of the segment to target, default 0
**fractionAlong**$ Optional specification of the fraction along the specified segment, default 0.5
**destination**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**target**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="Input">
  <xs:complexContent>
    <xs:extension base="BaseNonNegativeIntegerId">
      <xs:attribute name="target" type="Nml2PopulationReferencePath" use="required"/>
      <xs:attribute name="destination" type="NmlId" use="required"/>
      <xs:attribute name="segmentId" type="NonNegativeInteger"/>
      <xs:attribute name="fractionAlong" type="ZeroToOne"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=Input" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import Input
from neuroml.utils import component_factory

variable = component_factory(
    Input,
    id: 'a NonNegativeInteger (required)' = None,
    target: 'a Nml2PopulationReferencePath (required)' = None,
    destination: 'a NmlId (required)' = None,
    segment_id: 'a NonNegativeInteger (optional)' = None,
    fraction_along: 'a ZeroToOne (optional)' = None,
    extensiontype_=None,
)
```
````
````{tab-item} Usage: XML
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
`````

(schema:inputw)=

## inputW




extends {ref}`schema:input`



<i>Specifies input lists. Can set **weight** to scale individual inputs.</i>


`````{tab-set}
````{tab-item} Parameters
```{csv-table}
:widths: 1, 7, 2
:width: 100 %
:delim: $

**weight**$  $Dimensionless

```
````

````{tab-item} Text fields
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**destination**$ 

````

````{tab-item} Paths
```{csv-table}
:widths: 1, 7
:width: 100%
:delim: $

**target**$ 

````

````{tab-item} Schema
```{code-block} xml
<xs:complexType name="InputW">
  <xs:complexContent>
    <xs:extension base="Input">
      <xs:attribute name="weight" type="xs:float" use="required"/>
    </xs:extension>
  </xs:complexContent>
</xs:complexType>

```
````

````{tab-item} Usage: Python
*<a href="https://libneuroml.readthedocs.io/en/latest/search.html?q=InputW" target="_blank">Go to the libNeuroML documentation</a>*
```{code-block} python
from neuroml import InputW
from neuroml.utils import component_factory

variable = component_factory(
    InputW,
    id: 'a NonNegativeInteger (required)' = None,
    target: 'a Nml2PopulationReferencePath (required)' = None,
    destination: 'a NmlId (required)' = None,
    segment_id: 'a NonNegativeInteger (optional)' = None,
    fraction_along: 'a ZeroToOne (optional)' = None,
    weight: 'a float (required)' = None,
)
```
````
`````
