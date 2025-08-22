(userdocs:faq)=
# Frequently asked questions (FAQ)

```{admonition} Please help improve the FAQ.
:class: note
This page lists some commonly asked questions related to NeuroML.
Please [open issues](https://github.com/NeuroML/Documentation/issues) to add more entries to this FAQ.
```

(userdocs:faq:zero_length_segments)=
## 1. Are length 0 segments allowed in NeuroML?

Discussion link: https://github.com/NeuroML/NeuroML2/issues/115

There are a lot of SWC reconstructions which have adjacent points, which would get converted to zero length segments.
This shouldn't be an issue for most visualisation applications, so no need for them to say that they can't visualise the cell if they see it's invalid.

The `jnml -validate` option could throw a warning when it sees these segments, but currently doesn't (it could be added [here](https://github.com/NeuroML/org.neuroml.model/blob/development/src/main/java/org/neuroml/model/util/NeuroML2Validator.java#L199)).

For individual simulators, they could have an issue with this, if they map each segment to a compartment (as Moose might), but for Neuron using cables/sections with multiple segments, it shouldn't matter as long as the section doesn't just have one segment.

So ideally it should be the application which loads the NeuroML in (or the conversion/export code) which decides whether this is an issue.

(userdocs:faq:pyneuroml_or_neuroml)=
## 2. What is the difference between reader/writer methods in pyNeuroML and libNeuroML?

Both {ref}`libNeuroML <libneuroml>` and {ref}`pyNeuroML <pyneuroml>` include methods that can read and write NeuroML files.
However, they are not the same.

libNeuroML is the low level Python API for working with NeuroML.
The loaders/writers included here can therefore read/write NeuroML files.
However, these are "low level" functions and do not include additional features.

The readers/writers in pyNeuroML use these low level functions from libNeuroML but also run other checks and include other features.

So,

- [pyneuroml.io.read_neuroml2_file](https://pyneuroml.readthedocs.io/en/latest/pyneuroml.io.html#pyneuroml.io.read_neuroml2_file) should be preferred over [neuroml.loaders.read_neuroml2_file](https://libneuroml.readthedocs.io/en/latest/userdocs/loaders.html#neuroml.loaders.read_neuroml2_file): it also allows pre-loading validation checks, and it also handles morphologies referenced in other files.
- [pyneuroml.io.write_neuroml2_file](https://pyneuroml.readthedocs.io/en/latest/pyneuroml.io.html#pyneuroml.io.write_neuroml2_file) should be preferred over [neuroml.writers.NeuroMLWriter.write](https://libneuroml.readthedocs.io/en/latest/userdocs/writers.html#neuroml.writers.NeuroMLWriter.write): it also validates the file after writing it.
