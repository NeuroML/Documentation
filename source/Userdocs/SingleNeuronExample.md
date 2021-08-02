(userdocs:getting_started:single_example)=
# Simulating a regular spiking Izhikevich neuron

In this section, we wish to simulate a single regular spiking Izhikevich neuron ({cite}`Izhikevich2007`) and record/visualise its membrane potential (as shown in the figure below):

```{figure} ../Userdocs/NML2_examples/example-single-izhikevich2007cell-sim-v.png
:alt: Membrane potential for neuron recorded from the simulation
:align: center

Membrane potential of the simulated regular spiking Izhikevich neuron.
```
This plot, saved as `example-single-izhikevich2007cell-sim-v.png`, is generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
----
```

## Declaring the model in NeuroML

```{admonition} Python is the suggested programming language to use for working with NeuroML.
The Python NeuroML tools and libraries provide a convenient, easy to use interface to use NeuroML.
```
Let us step through the different sections of the Python script.
To start writing a model in NeuroML, we first create a `NeuroMLDocument`.
This document is the top level container for everything that the model should contain.
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 21, 22
----
```

Next, all entities that we want to use in the model must be defined.
The {ref}`NeuroML specification <userdocs:neuromlv2>` includes many standard entities, and it is possible to also define new entities that may not already be included in the NeuroML specification.
We will look at the pre-defined entities, and how NeuroML may be extended later when we look at the {ref}`NeuroML standard <userdocs:specification>` in detail.
For now, we limit ourselves to defining a new `Izhikevich2007Cell` (definition of this {ref}`here <schema:izhikevich2007Cell>`).
The Izhikevich neuron model can take sets of parameters to show different types of spiking behaviour.
Here, we define an instance of the general Izhikevich cell using parameters that exhibit regular spiking.

```{admonition} Units in NeuroML
NeuroML defines a {ref}`standard set of units <schema:neuromlcoredimensions>` that can be used in models.
Learn more about units and dimensions in NeuroML and LEMS {ref}`here <userdocs:unitsanddimensions>`.
```
Once defined, we add this to our `NeuroMLDocument`.
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 24-28
----
```
Now that the neuron has been defined, we declare a {ref}`network <schema:network>` with a {ref}`population <schema:population>` of these neurons to create a network.
Here, our model includes one network which includes only one population, which in turn only consists of a single neuron.
Once the network, its populations, and their neurons have been declared, we again them to our model:
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 30-37
----
```
To record the membrane potential of the neuron, we must give it some external input that makes it spike.
As with the neuron, we create and add a {ref}`pulse generator <schema:pulsegenerator>` to our network.
We then connect it to our neuron, the `target` using an {ref}`explicit input <schema:explicitinput>`.
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 39-46
----
```
This completes our model.
It includes a single network, with one population of one neuron that is driven by one pulse generator.
At this point, we can save our model to a file and validate it to check if it conforms to the NeuroML schema (more on this {ref}`later <userdocs:validating_models>`).
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 48-54
----

```
### The generated NeuroML model

We have now defined our model in NeuroML.
Let us investigate the generated NeuroML file:
```{literalinclude} ./NML2_examples/izhikevich2007_single_cell_network.nml
----
language: xml
```
NeuroML files are written in XML.
So, they consist of tags and attributes and can be processed by general purpose XML tools.
Each entity between chevrons is a *tag*: `<..>`, and each tag may have multiple *attributes* that are defined using the `name=value` format.
For example `<neuroml ..>` is a tag, that contains the `id` attribute with value `NML2_SimpleIonChannel`.

```{admonition} XML Tutorial
For details on XML, have a look through [this tutorial](https://www.w3schools.com/xml/).
```
```{admonition} Is this XML well-formed?
:class: tip
A NeuroML file needs to be both 1) well-formed, as in complies with the general rules of the XML language syntax, and 2) valid, i.e. contains the expected NeuroML specific tags/attributes.

Is the XML shown above well-formed? See for yourself. Copy the NeuroML file listed above and check it using an [online XML syntax checker](https://www.w3schools.com/xml/xml_validator.asp).
```

Let us step through this file to understand the different constructs used in it.
The first segment introduces the `neuroml` tag that includes information on the specification that this NeuroML file adheres to.
```{literalinclude} ./NML2_examples/izhikevich2007_single_cell_network.nml
----
language: xml
lines: 1-1
----
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
```{literalinclude} ./NML2_examples/izhikevich2007_single_cell_network.nml
----
language: xml
lines: 2-7
----
```

The cell, is defined in the `izhikevich2007Cell` tag, which has a number of attributes (see {ref}`here <schema:izhikevich2007Cell>` for more):
- `id`: the name that we want to give to this cell. To refer to it later, for example,
- `v0`: the initial membrane potential for the cell,
- `C`: the leak conductance,
- `k`: conductance per voltage,
- `vr`: the membrane potential after a spike,
- `vt`: the threshold membrane potential, to detect a spike,
- `vpeak`: the peak membrane potential,
- `a`, `b`, `c`, and `d`: are parameters of the Izhikevich neuron model.

Similarly, the `pulseGenerator` is also defined, and the `network` tag includes the `population` and `explicitInput`.
We observe that even though we have declared the entities, and the values for parameters that govern them, we do not state what and how these parameters are used.
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

As is evident, XML files are excellent for storing structured data, but may not be easy to write by hand.
However, NeuroML users *are not expected* to write in XML.
They should use the Python tools as demonstrated here.

## Simulating the model

Until now, we have just declared the model.
We have not, however, included any information related to the simulation of this model.
The same model may be instantiated many times with different random seeds and so on to give rise to different simulations and behaviours.
In NeuroML, the information required to simulate the model is provided using {ref}`LEMS <userdocs:specification:lemsdefs>`.
We will not go into the details of LEMS just yet.
We will limit ourselves to the bits necessary to simulate our Izhikevich neuron only.

The following lines of code instantiate a new simulation with certain simulation parameters: `duration`, `dt`, `simulation_seed`.
Additionally, they also define what information is being recorded from the simulation.
In this case, we create an output file, and then add a new column to record the membrane potential `v` from our one neuron in the one population in it.
You can read more about recording from NeuroML simulations {ref}`here <userdocs:quantitiesandrecording>`.

Finally, like we had saved our NeuroML model to a file, we also save our LEMS document to a file.

```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 60-75
----
```
The generated LEMS file is shown below:

```{literalinclude} ./NML2_examples/LEMS_example-single-izhikevich2007cell-sim.xml
----
language: xml
----
```
Similar to NeuroML, LEMS also has a well defined schema.
I.e., a set of valid tags define a LEMS file.
We observe that whereas the NeuroML tags were related to the modelling parameters, the LEMS tags are related to simulation.
We also note that our NeuroML model has been "included" in the LEMS file, so that all entities defined there are now known to the LEMS simulation also.
Like NeuroML, *users are not expected to write the LEMS XML component by hand*.
They should continue to use the NeuroML Python tools.

Finally, {ref}`pyNeuroML <pyNeuroML>` also includes functions that allow you to run the simulation from the Python script itself:
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 77-80
----
```

Here, we are running our simulation using the {ref}`jNeuroML <jNeuroML>` simulator, which is bundled with {ref}`pyNeuroML <pyNeuroML>`.
Since NeuroML is a well defined standard, models defined in NeuroML can also be run using other {ref}`supported simulators <userdocs:simulators>`.

## Plotting the recorded membrane potential

Once we have simulated our model and the data has been collected in the specified file, we can analyse the data.
pyNeuroML also includes some helpful functions to quickly plot various recorded variables.
The last few lines of code shows how the membrane potential plot at the top of the page is generated.
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
lines: 82-90
----
```

The next section is an interactive Jupyter notebook where you can play with this example.
Click the "launch" button in the top right hand corner to run the notebook in a configured service.
*You do not need to install any software on your computer to run these notebooks.*
