(userdocs:quantitiesandrecording)=
# Quantities and recording

In LEMS and NeuroML, `quantities` from all `exposures` and all `events` can be recorded by referring to them using {ref}`paths <userdocs:paths>`.
For examples, please see the {ref}`Getting Started with NeuroML <userdocs:getting_started_neuroml>` section.

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
