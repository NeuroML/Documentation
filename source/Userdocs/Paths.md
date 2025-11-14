(userdocs:paths)=
# Paths

Since there is a well defined hierarchy of model components in NeuroML and LEMS, there is always a "path" from one component to another.
These paths are used when a model component needs to refer to another.
The table below lists the primary operators that one can use when creating a path, and the example below illustrates some paths.

Paths are also used when recording information from simulations.
These are similar to the "reference paths" discussed here, but have some special features.
There are discussed in the page on {ref}`quantities and recording <userdocs:quantitiesandrecording>`.

```{list-table}
:header-rows: 1
:name: paths-operators

* - operator
  - description
  - function
* - {code}`/`
  - forward slash
  - used to split the levels in a path string
* - {code}`.`
  - single period
  - refers to the level of the current node (usually omitted)
* - {code}`..`
  - two periods
  - refers to the level of the current node's parent node
* - {code}`[x]`
  - square brackets
  - used to refer to a particular instance (in this case, {code}`x`) in Components/Elements that have a `size` attribute (like {ref}`population <schema:population>`)
```
Paths start from any element and ascend/descend to refer to the entity that is to be referenced.

(userdocs:paths:example)=
## Example

For example, in the following block of code, based on the  {ref}`Izhikevich network example <userdocs:gettingstarted:izhikevichnetwork>`, a network is defined in NeuroML with 2 populations:
```{code-block} xml
    <network id="IzNet">
        <population id="IzPop0" component="iz2007RS0" size="5">
            <property tag="color" value="0 0 .8"/>
        </population>
        <populationList id="IzPop1" component="iz2007RS0">
            <property tag="color" value=".8 0 0"/>
            <instance id=0>
                <location x="0" y="0" z="0" />
            </instance>
            <instance id=1>
                <location x="1" y="0" z="0" />
            </instance>
            <instance id=2>
                <location x="2" y="0" z="0" />
            </instance>
            <instance id=3>
                <location x="3" y="0" z="0" />
            </instance>
            <instance id=4>
                <location x="4" y="0" z="0" />
            </instance>
        </populationList>
        <projection id="proj" presynapticPopulation="IzPop0" postsynapticPopulation="IzPop1" synapse="syn0">
            <connection id="0" preCellId="../IzPop0[0]" postCellId="../IzPop1/0"/>
            <connection id="1" preCellId="../IzPop0[0]" postCellId="../IzPop1/1"/>
            <connection id="2" preCellId="../IzPop0[0]" postCellId="../IzPop1/2"/>
            ...
        </projection>
        <explicitInput target="IzPop0[0]" input="pg_0"/>
        <explicitInput target="IzPop0[1]" input="pg_1"/>
        <explicitInput target="IzPop0[2]" input="pg_2"/>
        <explicitInput target="IzPop0[3]" input="pg_3"/>
        <explicitInput target="IzPop0[4]" input="pg_4"/>
    </network>
</neuroml>
```
Here, in the `explicitInput` node, we need to refer to neurons of the `IzPop0` `population` node.
Since `explicitInput` and `population` are *siblings* (both have the `IzNet` `network` as *parent*), they are at the same *level*.
Therefore, in `explicitInput`, one can refer directly to `IzPop0`.

The `projection` and `population` nodes are also *siblings* and therefore are at the same level.
So, in the `projection` tag also, we can refer to the `population` nodes directly.
The `connection` nodes, however, are *children* of the `projection` node.
Therefore, for the `connection` nodes, the `population` nodes are at the *parent* level, and we must use `../IzPop0` to refer to them.

`../IzPop0` means "go up one level to the parent level (to `projection`) and then refer to `IzPop0`".
`../` can be used as many times as required and wherever required in the path.
For example, `../../../` would mean "go up three levels".
