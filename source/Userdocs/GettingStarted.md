# Getting started with NeuroML

The best way to understand NeuroML is to look at some example NeuroML files and how they are constructed.
In this section, we will walk through a cell model and see how it is defined in NeuroML.
To keep this section simple, we will intentionally gloss over many of the details and only focus on the salient, important bits necessary to grasp how NeuroML works and is to be used.


% Needs a better heading
## Izhikevich neuron model in NeuroML

The description of a simple single compartment Izhikevich point neuron model ({cite}`Izhikevich2003a`) in NeuroML is shown below:
```{code-block} xml
<?xml version="1.0" encoding="UTF-8"?>

<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2  ../Schemas/NeuroML2/NeuroML_v2beta4.xsd"
    id="NML2_AbstractCells">

  <izhikevichCell id="izBurst" v0 = "-70mV" thresh = "30mV" a="0.02" b = "0.2" c = "-50.0" d = "2"/>
</neuroml>
```

NeuroML files are written in XML.
So, they consist of tags and attributes and can be processed by general purpose XML tools.
Each entity between chevrons is a *tag*: `<..>`, and each tag may have multiple *attributes* that are defined using the `name=value` format.
For example `<neuroml ..>` is a tag, that contains the `id` attribute with value `NML2_SimpleIonChannel`.

```{admonition} XML Tutorial
For details on XML, consider skimming through [this tutorial](https://www.w3schools.com/xml/).
```
```{admonition} Is this XML valid?
:class: tip
Is the XML shown above valid? See for yourself. Copy the NeuroML file listed above and validate is using an [online XML validator](https://www.w3schools.com/xml/xml_validator.asp).
```

Let us step through this file to understand the different constructs used in it.
```{code-block} xml
<?xml version="1.0" encoding="UTF-8"?>

```
The first line is the XML header.
This tells us that this file is using version 1 of the XML standard.
Next, the `encoding` attribute tells us that the common ["UTF-8" encoding](https://en.wikipedia.org/wiki/UTF-8) is in use in this file.
All XML files, and so all NeuroML files, must start with this line.

The next segment introduces the `neuroml` tag that includes information on the specification that this NeuroML file adheres to.
```{code-block} xml
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2  ../Schemas/NeuroML2/NeuroML_v2beta4.xsd"
    id="NML2_AbstractCells">
```

The first attribute, `xmlns` defines the XML *namespace*.
All the tags that are defined for use in NeuroML are defined for use in the NeuroML namespace.
This prevents conflicts with other XML schemas that may use the same tags.
Read more on XML namespaces [here](https://en.wikipedia.org/wiki/XML_namespace).

The remaining lines in this snippet refer to the *XML Schema* that is defined for NeuroML.
XML itself does not define any tags, so any tags can be used in a general XML document.
Here is an example of a valid XML document, a simple HTML snippet:

```{code-block} xml
<html>
<head>
<title>A title</title>
</head>
</html>
```
NeuroML, however, does not use these tags.
It defines its own set of standard tags using an [XML Schema](http://www.w3.org/2001/XMLSchema-instance).
In other words, the NeuroML XML schema defines the structure and contents of a valid NeuroML document.
Various tools can then compare NeuroML documents to the NeuroML Schema to validate them.

```{admonition} Purpose of the NeuroML schema
The NeuroML Schema defines the structure and contents of a valid NeuroML document.
```

The `xmlns:xi` attribute documents that NeuroML has a defined XML Schema.
The next attribute, `xsi:schemaLocation` tells us the locations of the NeuroML Schema.
Here, two locations are provided:

- the Web URL: [http://www.neuroml.org/schema/neuroml2](http://www.neuroml.org/schema/neuroml2),
- and the location of the Schema Definition file (an `xsd` file) relative to this example file in the GitHub repository.

We will look at the NeuroML schema in detail in later sections.
All NeuroML files must include the `neuroml` tag, and the attributes related to the NeuroML Schema.

The last attribute, `id` is the identification (or the name) of this particular NeuroML document.

The remaining part of the file is the *declaration* of the model and its dynamics:
```{code-block} xml
  <izhikevichCell id="izBurst" v0 = "-70mV" thresh = "30mV" a="0.02" b = "0.2" c = "-50.0" d = "2"/>
```
The cell, is defined in the `izhikevichCell` tag, which has a number of attributes:
- `id`: the name that we want to give to this cell to refer to it later, for example,
- `v0`: the initial membrane potential for the cell,
- `thresh`: the threshold membrane potential, to detect a spike,
- `a`, `b`, `c`, and `d`: are parameters of the Izhikevich neuron model.


We observe that even though we have declared the cell, and the parameters that govern it, we do not state what and how these parameters are used.
This is because NeuroML is a [declarative language](https://en.wikipedia.org/wiki/Declarative_programming).
That is, it describes *what* needs to be done rather than *how* it should be done.
The *how* is left to the various simulators, which each have their own implementation of various dynamics.
This will become clearer later in this document.
```{admonition} NeuroML is a declarative language.
We describe the various components of the model but not how they are to be simulated.
```

We have seen how an Izhikevich cell can be declared in NeuroML, with all its parameters.
However, given that NeuroML develops a standard and defines what tags and attributes can be used, let us see how these are defined for the Izhikevich cell.
The Izhikevich cell is defined in the NeuroML schema [here](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.0.xsd#L1392):

```{code-block} xml
    <xs:complexType name="IzhikevichCell">
        <xs:complexContent>
            <xs:extension base="BaseCell">
                <xs:attribute name="v0" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="thresh" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="a" type="Nml2Quantity_none" use="required"/>
                <xs:attribute name="b" type="Nml2Quantity_none" use="required"/>
                <xs:attribute name="c" type="Nml2Quantity_none" use="required"/>
                <xs:attribute name="d" type="Nml2Quantity_none" use="required"/>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
```

The `xs:` prefix indicates that these are all part of an XML Schema.
As we can see above, the Izhikevich cell and its parameters are defined in the schema, with their dimensions (units).
As we saw before, parameters of the model are defined as attributes in NeuroML files.
So, here in the schema, they are also defined as `attributes` of the `complexType` that the schema describes.
The schema also specifies which of the parameters are necessary, and what their dimensions (units) are using the `use` and `type` properties.

This schema gives us all the information we need to describe an Izhikevich cell in NeuroML.
Using the specification in the Schema, any number of Izhikevich cells can be defined in a NeuroML file with the necessary parameter sets.

Different aspects of computational models---cells, synapses, ion channels, and so on---generally have some *dynamics* associated with them.
The dynamics of the Izhikevich cell model, for example, are defined by two differential equations:

\begin{align}
\frac{dv}{dt} &= 0.5v^2 + 5v + 140.0 -U \\
\frac{dU}{dt} &= a (bv -U)
\end{align}

Additionally, a spike is detected when the membrane potential `v` is greater than the threshold `thresh`.
When this occurs, some variables are updated:

- `v` is set to `c`,
- `U` is incremented: `U = U+d`.

How are these dynamics represented in NeuroML?
The answer is: "with [LEMS](http://lems.github.io/LEMS)".
Let us take a short segue to understand LEMS, and we will return to the Izhikevich model after.

## Defining dynamical systems with LEMS

[LEMS](http://lems.github.io/LEMS) (Low Entropy Model Specification) is an XML based language with interpreter originally developed by Robert Cannon for specifying generic models of hybrid dynamical systems.

In other words, similar to NeuroML, LEMS defines a Schema but one that allows us to describe dynamical systems.

For example, a class can be defined as follows:
```{code-block} cpp
class rectangle {
  int length;
  int breadth;
}
```

There can be many rectangles of different dimensions, so we can *instantiate* different objects of this class:
```{code-block} cpp
/* A rectangle */
rectangle r1 = rectangle();
r1.length = 5;
r1.breadth = 6;

/* A different rectangle */
rectangle r1 = rectangle();
r1.length = 10;
r1.breadth = 50;
```
In the same way, once the `izhikevichCell` ComponentType has been defined in the NeuroML standard with its parameters and dynamics, any number of cells of this type can be instantiated.
