(userdocs:paths)=
# Paths

Since NeuroMLv2 and LEMS are both XML based, entities in models and simulations must be referred to using *paths* ([XPath](https://en.wikipedia.org/wiki/XPath) like).
This page documents how paths can be constructed, and how they can be used to refer to entities in NeuroML/LEMS based models and simulations (e.g. in a {ref}`LEMS Simulation file <userdocs:lemssimulation>`).

```{list-table}
:header-rows: 1
:name: paths-operators

* - operator
  - description
  - function
  - example
* - {code}`/`
  - forward slash
  - used to split the levels in a path string
  - see {ref}`below <userdocs:paths:example>`
* - {code}`.`
  - single period
  - refers to the level of the current node (usually omitted)
  - see {ref}`below <userdocs:paths:example>`
* - {code}`..`
  - two periods
  - refers to the level of the current node's parent node
  - see {ref}`below <userdocs:paths:example>`
* - {code}`[x]`
  - square brackets
  - used to refer to a particular instance (in this case, {code}`x`) in Components/Elements that have a `size` attribute (like {ref}`population <schema:population>`)
  - see {ref}`below <userdocs:paths:example>`
* - {code}`:`
  - colon
  - used to refer to a particular Component instance for {code}`attachments`
  - [ex](https://github.com/NeuroML/NeuroML2/blob/master/LEMSexamples/LEMS_NML2_Ex25_MultiComp.xml#L45)
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

(userdocs:pyneuroml)=
## Helper functions in pyNeuroML

```{note}
These functions require {ref}`pyNeuroML <pyneuroml>` version 0.5.18+, and {ref}`pylems <pylems>` version 0.5.8+.
```

From version 0.5.18, {ref}`pyNeuroML <pyneuroml>` includes the [list_recording_paths_for_exposures](https://pyneuroml.readthedocs.io/en/development/pyneuroml.html#pyneuroml.pynml.list_recording_paths_for_exposures) helper function that can list the exposures and their recordable paths from a NeuroML 2 model:

```{code-block} pycon
>>> import pyneuroml.pynml
>>> help(pynml.list_recording_paths_for_exposures)

Help on function list_recording_paths_for_exposures in module pyneuroml.pynml:

list_recording_paths_for_exposures(nml_doc_fn, substring='', target='')
    List the recording path strings for exposures.

    This wraps around `lems.model.list_recording_paths` to list the recording
    paths in the given NeuroML2 model. The only difference between the two is
    that the `lems.model.list_recording_paths` function is not aware of the
    NeuroML2 component types (since it's for any LEMS models in general), but
    this one is.
```

It can be run on the example {ref}`Izhikevich network example <userdocs:gettingstarted:izhikevichnetwork>`:
```{code-block} pycon
>>> pynml.list_recording_paths_for_exposures("izhikevich2007_network.nml", substring="", target="IzNet")
['IzNet/IzPop0[0]/iMemb',
 'IzNet/IzPop0[0]/iSyn',
 'IzNet/IzPop0[0]/u',
 'IzNet/IzPop0[0]/v',
 'IzNet/IzPop0[1]/iMemb',
 'IzNet/IzPop0[1]/iSyn',
 'IzNet/IzPop0[1]/u',
 'IzNet/IzPop0[1]/v',
 'IzNet/IzPop0[2]/iMemb',
 'IzNet/IzPop0[2]/iSyn',
 'IzNet/IzPop0[2]/u',
 'IzNet/IzPop0[2]/v',
 'IzNet/IzPop0[3]/iMemb',
 'IzNet/IzPop0[3]/iSyn',
 'IzNet/IzPop0[3]/u',
 'IzNet/IzPop0[3]/v',
 'IzNet/IzPop0[4]/iMemb',
 'IzNet/IzPop0[4]/iSyn',
 'IzNet/IzPop0[4]/u',
 'IzNet/IzPop0[4]/v',
 'IzNet/IzPop1[0]/iMemb',
..
]
```


Note that this function parsers the model description only, not the built simulation description.
Therefore, it will not necessarily list the complete list of paths.
Also worth noting is that since it parses and iterates over the expanded representation of the model, it can be slow and return long lists of results on larger models.
It is therefore, best to use this with the `substring` option to narrow its scope.

An associated helper function [list_exposures](https://pyneuroml.readthedocs.io/en/development/pyneuroml.html?highlight=list_exposures#pyneuroml.pynml.list_exposures) is also available:
```{code-block} pycon
>>> import pyneuroml.pynml
>>> help(pynml.list_exposures)

list_exposures(nml_doc_fn, substring='')
    List exposures in a NeuroML model document file.

    This wraps around `lems.model.list_exposures` to list the exposures in a
    NeuroML2 model. The only difference between the two is that the
    `lems.model.list_exposures` function is not aware of the NeuroML2 component
    types (since it's for any LEMS models in general), but this one is.

    The returned dictionary is of the form:

    ..
        {
            "component": ["exp1", "exp2"]
        }
```
When run on the example {ref}`Izhikevich network example <userdocs:gettingstarted:izhikevichnetwork>`, it will return:

```{code-block} pycon
>>> pynml.list_exposures("izhikevich2007_network.nml")

{<lems.model.component.FatComponent at 0x7f25b62caca0>: {'g': <lems.model.component.Exposure at 0x7f25dd1d2be0>,
  'i': <lems.model.component.Exposure at 0x7f25dc921e80>},
 <lems.model.component.FatComponent at 0x7f25b62cad00>: {'u': <lems.model.component.Exposure at 0x7f25b5f57400>,
  'iSyn': <lems.model.component.Exposure at 0x7f25b607a670>,
  'iMemb': <lems.model.component.Exposure at 0x7f25b607aa00>,
  'v': <lems.model.component.Exposure at 0x7f25b6500220>},
 <lems.model.component.FatComponent at 0x7f25b62cadf0>: {'i': <lems.model.component.Exposure at 0x7f25dc921e80>},
 <lems.model.component.FatComponent at 0x7f25b62caf70>: {'i': <lems.model.component.Exposure at 0x7f25dc921e80>},
 <lems.model.component.FatComponent at 0x7f25b5fc2ac0>: {'i': <lems.model.component.Exposure at 0x7f25dc921e80>},
 <lems.model.component.FatComponent at 0x7f25b65be9d0>: {'i': <lems.model.component.Exposure at 0x7f25dc921e80>},
 <lems.model.component.FatComponent at 0x7f25b65bed00>: {'i': <lems.model.component.Exposure at 0x7f25dc921e80>},
..
}
```

This second function is primarily for use by the `list_recording_paths_for_exposures` function.

As noted in the helper documentation, these are both based on a function of the same name implemented in {ref}`PyLEMS <pylems>`, version 0.5.8+.
