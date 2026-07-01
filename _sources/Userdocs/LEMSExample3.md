(userdocs:lemsexample3)=
# Example 3: Connection dependent synaptic components

In many models, a synapse is only created where a connection exists.
This means that the model of the receiving cell should only declare that particular types of synapse can be added to it, not the actual synapse sub-components themselves.

Not much is needed beyond the elements described in example 1 except for some extensions to the component that declares the connectivity and a new child element in the component that the synapses are attached to.
The full example is shown below.
The synapse type includes an EventPort just like the previously defined cell type.
The cell type however includes a new child element: Attachments defined as:

```{code-block} xml
<Attachments name="synapses" type="synapse" />
```

This operates rather like the Children element except that when a component is defined using this type the sub-elements are not included in the component definition.
Instead it indicates that instances of components of the particular type may be attached later when the model is actually run.
