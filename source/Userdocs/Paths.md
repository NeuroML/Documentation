(userdocs:paths)=
# Paths

Since NeuroMLv2 and LEMS are both XML based, entities in models and simulations must be referred to using *paths*.
This page documents how paths can be constructed, and how they can be used to refer to entities in NeuroML/LEMS based models and simulations.

(userdocs:constructingpaths)=
## Constructing paths
Paths start from any element and ascend/descend to refer to the entity that is to be referenced.

The `.` and `..` path constructs are special constructs that mean "the current node" and "the parent node" respectively.

For example, in the {reF}`Izhikevich network example <userdocs:getting_started:single_example>`, the network is defined in NeuroML like this:
```{code-block} xml
    <network id="IzNet">
        <population id="IzPop0" component="iz2007RS0" size="5">
            <property tag="color" value="0 0 .8"/>
        </population>
        <population id="IzPop1" component="iz2007RS0" size="5">
            <property tag="color" value=".8 0 0"/>
        </population>
        <projection id="proj" presynapticPopulation="IzPop0" postsynapticPopulation="IzPop1" synapse="syn0">
            <connection id="0" preCellId="../IzPop0[0]" postCellId="../IzPop1[0]"/>
            <connection id="1" preCellId="../IzPop0[0]" postCellId="../IzPop1[1]"/>
            <connection id="2" preCellId="../IzPop0[0]" postCellId="../IzPop1[2]"/>
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

Additionally, when constructing the path:

- for any `child` elements, the *name* of the element should be used in the path
- for `children` elements, the *id* of the element should be used in the path
- for elements that have a `size` attribute like {ref}`population <schema:population>`, individual elements should be referred to using the `[]` operator

