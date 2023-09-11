(userdocs:quantitiesandrecording)=
# Quantities and recording

In LEMS and NeuroML, `quantities` from all `exposures` and all `events` are recorded by referring to them using paths.

(userdocs:quantitiesandrecording:events)=
## Recording events

In NeuroML, all `event`s can be recorded to files declared using the {ref}`EventOutputFile <schema:eventoutputfile>` component.
Once an `EventOutputFile` has been declared, events to record can be selected using the {ref}`EventSelection <schema:eventselection>` component.

{ref}`pyNeuroML <pyneuroml>` provides the [create_event_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.create_event_output_file) function to create a `EventOutputFile` to record `events` to, and the [add_selection_to_event_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.add_selection_to_event_output_file) function to record `events` to the declared data file(s).

(userdocs:quantitiesandrecording:exposures)=
## Recording quantities from exposures
In NeuroML, all `quantities` can be recorded to files declared using the {ref}`OutputFile <schema:outputfile>` component.
Once the `OutputFile` has been declared, `quantities` to record can be selected using the {ref}`OutputColumn <schema:outputcolumn>` component.

{ref}`pyNeuroML <pyneuroml>` provides the [create_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.create_event_output_file) function to create a `OutputFile` to record `quantities` to, and the  [add_column_to_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.create_event_output_file) function to select `quantities` to record to the declared data file(s).

(userdocs:quantitiesandrecording:paths)=
## Paths for recording quantities

% examples: https://github.com/search?q=org%3AOpenSourceBrain+%22quantity%3D%22+language%3AXML&type=code&l=XML&p=1

While the hierarchical reference scheme remains the same as that discussed in {ref}`paths <userdocs:paths>`, a number of specific operators are used to refer to specifics to record, for example, what segment in a multi-compartmental cell does one want to record a particular quantity from.

In general, quantities to be recorded can be present on a number of different components:

- on a single compartment cell
- on a cell in a population
- on a cell instance in a population list
- on a segment on an instance of a multi-compartmental cell in a population list

A number of extra operators are also available to help record specific quantities, such as synaptic quantities:
```{list-table}
:header-rows: 1
:name: paths-operators

* - operator
  - description
  - function
  - example
* - {code}`:`
  - colon
  - used to refer to a particular Component instance for {code}`attachments`
  - [ex](https://github.com/NeuroML/NeuroML2/blob/master/LEMSexamples/LEMS_NML2_Ex25_MultiComp.xml#L45)

```

Let us go through the different cases with examples

(userdocs:quantitiesandrecording:paths:single_comp)=
### Quantities on a single compartment cell

TODO: Or single component? Ask Padraig.


(userdocs:quantitiesandrecording:paths:cell_in_pop)=
### Quantities on a cell in a population

pop[0]/cell/segmentid/quantities

#### On synapses

pop/index/cell/segmentid/synapse:...

(userdocs:quantitiesandrecording:paths:cell_in_pop_list)=
### Quantities on a cell in a population list

pop/index/cell/segmentid/quantities

#### On synapses

pop/index/cell/segmentid/synapse:...


(userdocs:quantitiesandrecording:paths:pyneuroml)=
### Helper functions in pyNeuroML

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
