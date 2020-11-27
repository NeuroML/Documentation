# Getting started with NeuroML

The best way to understand NeuroML is to look at some example NeuroML files and how they are constructed.
In this section, we will walk through a cell model and see how it is defined in NeuroML.
We will use the Python tools for NeuroML, [libNeuroML](https://github.com/NeuralEnsemble/libNeuroML) and [pyNeuroML](https://github.com/NeuroML/pyNeuroML), which are the suggested tools for developing and simulating models in NeuroML.
You can learn more about the different tools in their specific sections where you will also find examples in IPython notebooks to work through.

Please note that to keep this section simple, we will intentionally skip many of the details and only focus on the important bits necessary to grasp how NeuroML works and is to be used.

## The Izhikevich neuron model in NeuroML

The description of a simple single compartment Izhikevich point neuron model ({cite}`Izhikevich2007`) in NeuroML is shown below:
```{code-block} xml
<?xml version="1.0" encoding="UTF-8"?>

<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2  ../Schemas/NeuroML2/NeuroML_v2beta4.xsd"
    id="NML2_AbstractCells">

  <izhikevich2007Cell id="iz2007RS" v0 = "-60mV" C="100 pF" k = "0.7 nS_per_mV"
                      vr = "-60 mV" vt = "-40 mV" vpeak = "35 mV" 
                      a = "0.03 per_ms" b = "-2 nS" c = "-50 mV" d = "100 pA"/>
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
    <izhikevich2007Cell id="iz2007RS" v0 = "-60mV" C="100 pF" k = "0.7 nS_per_mV"
                        vr = "-60 mV" vt = "-40 mV" vpeak = "35 mV" 
                        a = "0.03 per_ms" b = "-2 nS" c = "-50 mV" d = "100 pA"/>
```
The cell, is defined in the `izhikevichCell` tag, which has a number of attributes:
- `id`: the name that we want to give to this cell. To refer to it later, for example,
- `v0`: the initial membrane potential for the cell,
- `C`: the leak conductance,
- `k`: conductance per voltage,
- `vr`: the membrane potential after a spike,
- `vt`: the threshold membrane potential, to detect a spike,
- `vpeak`: the peak membrane potential,
- `a`, `b`, `c`, and `d`: are parameters of the Izhikevich neuron model.

We observe that even though we have declared the cell, and the values for parameters that govern it, we do not state what and how these parameters are used.
This is because NeuroML is a [declarative language](https://en.wikipedia.org/wiki/Declarative_programming) that defines the structure of models.
We do not need to define how the dynamics of the different parts of the model are implemented.
As we will see further below, these are already defined in NeuroML.
```{admonition} NeuroML is a declarative language.
Users describe the various components of the model but do not need to worry about how they are implemented.
```
We have seen how an Izhikevich cell can be declared in NeuroML, with all its parameters.
However, given that NeuroML develops a standard and defines what tags and attributes can be used, let us see how these are defined for the Izhikevich cell.
The Izhikevich cell is defined in version 2 of the NeuroML schema [here](https://github.com/NeuroML/NeuroML2/blob/master/Schemas/NeuroML2/NeuroML_v2.0.xsd#L1422):
```{code-block} xml
    <xs:complexType name="Izhikevich2007Cell">
        <xs:complexContent>
            <xs:extension base="BaseCellMembPotCap">
                <xs:attribute name="v0" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="k" type="Nml2Quantity_conductancePerVoltage" use="required"/>
                <xs:attribute name="vr" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="vt" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="vpeak" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="a" type="Nml2Quantity_pertime" use="required"/>
                <xs:attribute name="b" type="Nml2Quantity_conductance" use="required"/>
                <xs:attribute name="c" type="Nml2Quantity_voltage" use="required"/>
                <xs:attribute name="d" type="Nml2Quantity_current" use="required"/>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
```

The `xs:` prefix indicates that these are all part of an XML Schema.
The Izhikevich cell and all its parameters are defined in the schema.
As we saw before, parameters of the model are defined as attributes in NeuroML files.
So, here in the schema, they are also defined as `attributes` of the `complexType` that the schema describes.
The schema also specifies which of the parameters are necessary, and what their dimensions (units) are using the `use` and `type` properties.

This schema gives us all the information we need to describe an Izhikevich cell in NeuroML.
Using the specification in the Schema, any number of Izhikevich cells can be defined in a NeuroML file with the necessary parameter sets to create networks of Izhikevich cells.

### Defining the Izhikevich cell in NeuroML using Python

Until now, we have only looked at the XML file themselves.
As is evident, XML files are excellent for storing structured data, but may not be easy to write by hand.
However, NeuroML users *are not expected* to write in XML.
Instead, they use various tools to write their models and their descriptions, and then can *export* their models in to NeuroML to run them on different simulators and to share them with others.

In the Python script below, we can see how NeuroML description of the Izhikevich cell can be generated:
```{code-block} python
#!/usr/bin/python3
# saved as izhikevich2007.py
from neuroml import NeuroMLDocument
from neuroml import Izhikevich2007Cell
from neuroml.writers import NeuroMLWriter
from neuroml.utils import validate_neuroml2


nml_filename = "IzhikevichCell2007.nml.xml"
nml_doc = NeuroMLDocument(id="SingleIzhikevich")

iz0 = Izhikevich2007Cell(id="iz2007RS", v0="-60mV", C="100pF",
                         k="0.7nS_per_mV", vr="-60mV", vt="-40mV",
                         vpeak="35mV", a="0.03per_ms", b="-2nS", c="-50.0mV",
                         d="100pA")

nml_doc.izhikevich2007_cells.append(iz0)

NeuroMLWriter.write(nml_doc, nml_filename)
validate_neuroml2(nml_filename)
```
We can now run this using Python:
```{code-block}
$ python3 ./izhikevich2007.py
Validating IzhikevichCell2007.nml.xml against /usr/lib/python3.9/site-packages/neuroml/nml/NeuroML_v2.1.xsd
It's valid!
```
Next, we can check its contents and verify that we get the same NeuroML code that we've seen above:
```{code-block}
$ cat IzhikevichCell2007.nml.xml
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"  xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2 https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2.1.xsd" id="SingleIzhikevich">
    <izhikevich2007Cell id="iz2007RS" C="100pF" v0="-60mV" k="0.7nS_per_mV" vr="-60mV" vt="-40mV" vpeak="35mV" a="0.03per_ms" b="-2nS" c="-50.0mV" d="100pA"/>
    </neuroml>
```

The Python code is quite self-explanatory.
We first create a NeuroML document with the preferred `id`, an instance of the `NeuroMLDocument` class.
We then define our Izhikevich cell, and add it to the document.
We then use the `NeuroMLWriter` to write this to a file.
Finally, we use the `validate_neuroml2` function to check if our NeuroML file is valid according to the NeuroML schema or not.

## A network of Izhikevich cells in NeuroML

### Defining a network of Izhikevich Cells in NeuroML using Python


## Simulating the generated NeuroML model

### Simulating the NeuroML model using Python using PyNeuroML

