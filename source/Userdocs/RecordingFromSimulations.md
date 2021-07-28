(userdocs:recording)=
# Recording from NeuroML simulations

In LEMS and NeuroML, events and values from all `exposures` can be recorded.
This page documents how this can be done.
For examples, please see the {ref}`Getting Started with NeuroML <userdocs:getting_started_neuroml>` section.

(userdocs:recording:events)=
## Recording events

In {ref}`pyNeuroML <pyneuroml>`, the [create_event_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.create_event_output_file) function can be used to create a file to record events to.
Then, the [add_selection_to_event_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.add_selection_to_event_output_file) function can be used to record events to data files.

(userdocs:recording:exposures)=
## Recording values from exposures
```{note}
TODO: document `list_exposures()` once https://github.com/NeuroML/pyNeuroML/pull/118 is merged.
```

In {ref}`pyNeuroML <pyneuroml>`, an output file to record values from exposures can be created using the [create_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.create_event_output_file) function.
Values can then be recorded to this output file in columns using the [add_column_to_output_file](https://pyneuroml.readthedocs.io/en/development/pyneuroml.lems.html?highlight=add_selection_to_event_output_file#pyneuroml.lems.LEMSSimulation.LEMSSimulation.create_event_output_file) function.

(userdocs:recording:paths)=
## Constructing paths
```{note}
TODO: document `list_recording_paths()` once https://github.com/NeuroML/pyNeuroML/pull/118 is merged.
```

Recording events and values from exposures requires us to provide the *path* to the entity we want to record from.
Paths start from the first level node inside the element that is designated the `target` element, and then descend to the element that needs to be recorded.

While constructing the path:

- for any `child` elements, the name of the element should be used in the path
- for children elements, the id of the element should be used in the path
- for elements that have a `size` attribute like {ref}`population <schema:population>`, individual elements should be referred to using the `[]` operator


Additionally, the `..` expression can be used to refer to the parent levels relative to the current node.
For example, `../../` would refer to the parent of the parent, or the second ancestor relate to the current node.
