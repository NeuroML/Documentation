# Getting started with NeuroML

In this section, we will look at some example NeuroML files and how various aspects of a neuron may be represented in NeuroML.
We will not, at this point, dive into the details of these models or how they are to be run.
That will be discussed in later sections.

## Example: Izhikevich point neuron model

In this section, we look at the description of a simple single compartment Izhikevich point neuron model ({cite}`Izhikevich2003a`) in NeuroML, shown below:
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
Each entity between chevrons is a *tag*: `<..>`, and each tag may have multiple *attribute* that are defined using a simple `name=value` format.
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
Next, the `encoding` attribute in this first tag tells us that the common ["UTF-8" encoding](https://en.wikipedia.org/wiki/UTF-8) is in use here.
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
XML itself does not define any tags, so any tags can be used in an XML document.
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
The NeuroML XML schema defines the structure and contents of a valid NeuroML document.
Various tools can then compare NeuroML documents to the NeuroML Schema to validate them.

```{admonition} Purpose of the NeuroML schema
The NeuroML Schema defines the structure and contents of a valid NeuroML document.
```

The `xmlns:xi` attribute documents that NeuroML has a defined XML Schema.
The next attribute, `xsi:schemaLocation` tells us the locations of the NeuroML Schema.
Here, two locations are provided:

- the Web URL: http://www.neuroml.org/schema/neuroml2,
- and the location of the Schema Definition file (xsd file) relative to this example file in the GitHub repository.

We will look at the NeuroML schema in detail in later sections.
All NeuroML files must include the `neuroml` tag, and the attributes related to the NeuroML Schema.

The last attribute, `id` is the identification (or the name) of this particular NeuroML document.

```{note}
Ankur: Continue from here.
```

## Example: Na+ Ion channel model

```{literalinclude} ./NML2_examples/NML2_SimpleIonChannel.nml
---
language: xml
---
```
## Example: Single compartment neuron with HH channels

```{code-block} xml
---
caption: |
  An example NeuroML file that shows a single compartment cell with HH channels.
---

<?xml version="1.0" encoding="UTF-8"?>

<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2 ../Schemas/NeuroML2/NeuroML_v2beta4.xsd"
         id="NML2_SingleCompHHCell">

    <!-- Single compartment cell with HH channels -->

    <!-- This is a "pure" NeuroML 2 file. It can be included in a LEMS file for use in a simulaton
    by the LEMS interpreter, see LEMS_NML2_Ex5_DetCell.xml -->

    <ionChannelHH id="passiveChan" conductance="10pS">
        <notes>Leak conductance</notes>
    </ionChannelHH>


    <ionChannelHH id="naChan" conductance="10pS" species="na">
        <notes>Na channel</notes>

        <gateHHrates id="m" instances="3">
            <forwardRate type="HHExpLinearRate" rate="1per_ms" midpoint="-40mV" scale="10mV"/>
            <reverseRate type="HHExpRate" rate="4per_ms" midpoint="-65mV" scale="-18mV"/>
        </gateHHrates>

        <gateHHrates id="h" instances="1">
            <forwardRate type="HHExpRate" rate="0.07per_ms" midpoint="-65mV" scale="-20mV"/>
            <reverseRate type="HHSigmoidRate" rate="1per_ms" midpoint="-35mV" scale="10mV"/>
        </gateHHrates>

    </ionChannelHH>


    <ionChannelHH id="kChan" conductance="10pS" species="k">

        <gateHHrates id="n" instances="4">
            <forwardRate type="HHExpLinearRate" rate="0.1per_ms" midpoint="-55mV" scale="10mV"/>
            <reverseRate type="HHExpRate" rate="0.125per_ms" midpoint="-65mV" scale="-80mV"/>
        </gateHHrates>

    </ionChannelHH>



    <cell id="hhcell">

        <morphology id="morph1">
            <segment id="0" name="soma">
                <proximal x="0" y="0" z="0" diameter="17.841242"/> <!--Gives a convenient surface area of 1000.0 um^2-->
                <distal x="0" y="0" z="0" diameter="17.841242"/>
            </segment>

            <segmentGroup id="soma_group">
                <member segment="0"/>
            </segmentGroup>

        </morphology>

        <biophysicalProperties id="bioPhys1">

            <membraneProperties>

                <channelDensity id="leak" ionChannel="passiveChan" condDensity="3.0 S_per_m2" erev="-54.3mV" ion="non_specific"/>
                <channelDensity id="naChans" ionChannel="naChan" condDensity="120.0 mS_per_cm2" erev="50.0 mV" ion="na"/>
                <channelDensity id="kChans" ionChannel="kChan" condDensity="360 S_per_m2" erev="-77mV" ion="k"/>

                <spikeThresh value="-20mV"/>
                <specificCapacitance value="1.0 uF_per_cm2"/>
                <initMembPotential value="-65mV"/>

            </membraneProperties>

            <intracellularProperties>
                <resistivity value="0.03 kohm_cm"/>   <!-- Note: not used in single compartment simulations -->
            </intracellularProperties>

        </biophysicalProperties>

    </cell>

    <pulseGenerator id="pulseGen1" delay="100ms" duration="100ms" amplitude="0.08nA"/>


    <network id="net1">
        <population id="hhpop" component="hhcell" size="1"/>
        <explicitInput target="hhpop[0]" input="pulseGen1"/>
    </network>

</neuroml>

```

## Example: Multi-compartmental cell

NML2_FullCell.nml
