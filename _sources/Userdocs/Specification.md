(userdocs:specification)=
# Schema/Specification

```{admonition} NeuroML v2.3 is the current stable release of the language, and is described below.
For an overview of the various releases of the language see: {ref}`A brief history of NeuroML <history>`.
```

We've briefly seen the XML representation of NeuroML models and simulations in the {ref}`Getting Started <userdocs:getting_started_neuroml>` tutorials.
Here, we dive a little deeper into the underlying details of NeuroML.

XML itself does not define a set of standard tags: any tags may be used as long as the resultant document is [well-formed](https://en.wikipedia.org/wiki/Well-formed_document).
Therefore, NeuroML defines a standard set of XML elements (the tags and attributes which specify the model and parameters, e.g. `<iafCell id="iaf" leakReversal="-60mV"...>`) that may be used in NeuroML documents: the NeuroML [XML Schema Definition](https://en.wikipedia.org/wiki/XML_Schema_(W3C)).
This is referred to as the NeuroML *schema* or the NeuroML *specification*.

As the wiki page says:
```{epigraph}
XSD (XML Schema Definition), a recommendation of the World Wide Web Consortium (W3C), specifies how to formally describe the elements in an Extensible Markup Language (XML) document. It can be used by programmers to verify each piece of item content in a document, to assure it adheres to the description of the element it is placed in.
```

This gives us an idea of the advantages of using an XML based system.
All NeuroML models must use these pre-defined tags/components---this is what we check for when we {ref}`validate NeuroML models <userdocs:validating_models>`.
A valid NeuroML model is said to adhere to the NeuroML schema.

```{admonition} Purpose of the NeuroML specification/schema.
:class: note
The NeuroML schema/specification defines the structure of a valid NeuroML document. The {ref}`core NeuroML tools <userdocs:software>` adhere to this specification and can read/write/interpret the language correctly.
```

In the next section, we learn more about the NeuroML 2 schema, and see how the dynamics of the NeuroML 2 entities are defined in LEMS.
