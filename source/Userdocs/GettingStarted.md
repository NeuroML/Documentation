(userdocs:getting_started_neuroml)=
# Getting started with NeuroML

The best way to understand NeuroML is to look at some example NeuroML files and how they are constructed.
In this section, we will walk through a cell model and see how it is defined in NeuroML.
We will use the Python tools for NeuroML, [libNeuroML](https://github.com/NeuralEnsemble/libNeuroML) and [pyNeuroML](https://github.com/NeuroML/pyNeuroML), which are the suggested tools for developing and simulating models in NeuroML.
You can learn more about the different tools in their specific sections where you will also find examples in IPython notebooks to work through.

Please note that to keep this section simple, we will intentionally skip many of the details and only focus on the important bits necessary to grasp how NeuroML works and is to be used.

## Simulating a regular spiking Izhikevich neuron


## A two population network of regular spiking Izhikevich neurons

Now that we have seen how a single Izhikevich neuron may be specified and simulated using NeuroML, let us build and simulate a network.
As noted above, the description of a simple single compartment Izhikevich point neuron model with regular spiking ({cite}`Izhikevich2007`) in NeuroML is:
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

### Defining the Izhikevich cell using Python

```{admonition} Python is the suggested programming language to use for working with NeuroML.
The Python NeuroML tools and libraries provide a convenient, easy to use interface to use NeuroML.
```
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
```{code-block} xml
$ cat IzhikevichCell2007.nml.xml
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"  xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2 https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2.1.xsd" id="SingleIzhikevich">
    <izhikevich2007Cell id="iz2007RS" C="100pF" v0="-60mV" k="0.7nS_per_mV" vr="-60mV" vt="-40mV" vpeak="35mV" a="0.03per_ms" b="-2nS" c="-50.0mV" d="100pA"/>
    </neuroml>
```

In the Python code, we first create a NeuroML *document* with the preferred `id`, an instance of the `NeuroMLDocument` class.
We then define our Izhikevich cell, and add it to the document.
We then use the `NeuroMLWriter` to write this to a file.
Finally, we use the `validate_neuroml2` function to check if our NeuroML file is valid according to the NeuroML schema or not.

All the cell types that are defined in the NeuroML schema are available in the Python API.
It is also possible to extend NeuroML to define new cell types and so on.
We will cover this in later sections.

## A network of Izhikevich cells in NeuroML

Now that we have defined a cell, let us see how a network of these cells may be declared:

```{code-block} xml
<neuroml xmlns="http://www.neuroml.org/schema/neuroml2"  xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.neuroml.org/schema/neuroml2 https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2.1.xsd" id="IafNet">
    <izhikevich2007Cell id="iz2007RS0" C="100pF" v0="-60mV" k="0.7nS_per_mV" vr="-60mV" vt="-40mV" vpeak="35mV" a="0.03per_ms" b="-2nS" c="-50.0mV" d="100pA"/>
    <network id="IzNet">
        <population id="IzPop0" component="iz2007RS0" size="5"/>
        <population id="IzPop1" component="iz2007RS0" size="5"/>
    </network>
</neuroml>
```
Here, after defining our `izhikevich2007Cell` as before, we now create a network using the `network` NeuroML tag.
Similarly, we give it an `id`, so we can refer to it later.
Next, in this network, we create two populations of our Izhikevich cells: `IzPop0` and `IzPop1`, of 5 cells each.
We do this by using the `id` of the `izhikevich2007Cell`, `iz2007RS0`, in the `population` tag's `component` attribute with the `size` attribute to specify the number of cells.

Let us now connect these two populations such that `IzPop0` projects on to `IzPop1` with some probability of connection.
This can be seen in the snippet below:
```{literalinclude} ./NML2_examples/getting-started-izhikevich2008_network.nml
----
language: xml
----
```
We have now defined a `expOneSynapse` synapse type with certain parameters, and connected the two populations using it.
Note that here, each connection between pairs of neurons is explicitly listed as a new `synapticConnection`.

### Defining the network using Python

Since users are not expected to write NeuroML files by hand in XML, let us see how this network can be generated using the libNeuroML Python API:
```{literalinclude} ./NML2_examples/getting-started-izhikevich2008_network.py
----
language: python
----
```
We see here that the probability of connection is defined as `0.5`, and we use that to easily generate the network.
By changing the seed for Python's `random` function here, we can generate multiple instances of the network to simulate.

## Simulating the generated NeuroML model

Now that we have a network of cells, the next step is to simulate our model.
For this, first we need to provide some input to the network.
We can do this by adding `pulseGenerators` to the projecting population of cells:
```{literalinclude} ./NML2_examples/getting-started-izhikevich2008_network-with-inputs.py
----
language: python
----
```

This generates the following NeuroML file:
```{literalinclude} ./NML2_examples/getting-started-izhikevich2008_network-with-inputs.nml
----
language: xml
----
```

Now that we have a complete network model, in NeuroML, we need to be able to simulate it.
NeuroML itself is limited to descriptions of models only, and does not include functionality to simulate the generated model instances.
To see how we can simulate NeuroML models, we take a short segue into [LEMS](http://lems.github.io/LEMS/index.html).

### Adding information to simulate the model with LEMS

[LEMS](http://lems.github.io/LEMS/index.html), the Low Entropy Model Specification language, is an XML based language with interpreter for specifying generic models of hybrid dynamical systems.

LEMS plays 2 roles in the NeuroML eco-system:

- LEMS provides the lower level specification that is used by NeuroML to define specific *components types* which form the standard NeuroML schema.
- LEMS provides the necessary components to simulate the dynamics of models described in NeuroML

You will read about LEMS and the tools for using and developing with LEMS in detail in later sections.
Here, we will only discuss bits that are necessary to run the NeuroML network that we have constructed.

We will use the second Python based NeuroML tool, pyNeuroML to set up the simulation.
We import `LEMSSimulation` from `pyneuroml`, and add a few lines of code to create a simulation.
We also need to record spikes from the neurons in our simulation, so we add
```{literalinclude} ./NML2_examples/getting-started-izhikevich2008_network-lems.py
----
language: python
----
```
Running the script will result in an additional LEMS file:
```{code-block} console
$ python3 ./getting-started-izhikevich.py
Written network file to: izhikevich2007_network.nml
Validating izhikevich2007_network.nml against /usr/lib/python3.9/site-packages/neuroml/nml/NeuroML_v2.1.xsd
It's valid!
pyNeuroML >>> Written LEMS Simulation example-izhikevich2007cell-sim to file: LEMS_example-izhikevich2007cell-sim.xml

$ ls *nml *xml
izhikevich2007_network.nml  LEMS_example-izhikevich2007cell-sim.xml
```

Let us inspect the new LEMS simulation file:
```{literalinclude} ./NML2_examples/LEMS_example-izhikevich2007cell-sim.xml
----
language: xml
----
```

You will see that it has a similar XML structure to the NeuroML file.
However, instead of describing the model, it *includes* the NeuroML model file and uses other tags, **Target** and **Simulation**, to set up a simulation instance of the network we wrote in NeuroML.
It also defines a new **EventOutputFile** section with information on what events we want to track.
Finally, the LEMS XML file also automatically includes the NeuroML definitions that are needed to run this simulation.

### Running the model using pyNeuroML

It is important to note the difference between the libNeuroML and pyNeuroML libraries.
As we have seen, libNeuroML provides a Python API to create (and read) NeuroML files.
It is *strongly linked* to the standard NeuroML specification, and does not include additional functionality, for example: to export a NeuroML model into NEURON code.
pyNeuroML, on the other hand, provides functionality related to the simulation of NeuroML models.
It provides an API with helper functions to carry out different tasks, and also provides the `pynml` command:

Let us run our simulation using `pynml`:
```{code-block} console
$ pynml -nogui LEMS_example-izhikevich2007cell-sim.xml
pyNeuroML >>> Successfully ran the following command using pyNeuroML v0.5.6:
pyNeuroML >>>     java -Xmx400M  -Djava.awt.headless=true -jar  "/usr/share/java/jNeuroML-0.10.0.jar"  "LEMS_example-izhikevich2007cell-sim.xml" -nogui
pyNeuroML >>> Output:
pyNeuroML >>>
pyNeuroML >>>  jNeuroML v0.10.0
pyNeuroML >>> Loading: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/LEMS_example-izhikevich2007cell-sim.xml with jLEMS, NO GUI mode...
pyNeuroML >>> INFO Dec 03,2020 19:36  (INFO) Loading LEMS file from: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/LEMS_example-izhikevich2007cell-sim.xml
pyNeuroML >>> INFO Dec 03,2020 19:36  (INFO) Reading from: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/LEMS_example-izhikevich2007cell-sim.xml
pyNeuroML >>> INFO Dec 03,2020 19:36  (INFO) Finished 100000 steps in 1.495 seconds (sim duration: 10000.0ms; dt: 0.1ms)
pyNeuroML >>> INFO Dec 03,2020 19:36  (INFO) Written to the event file /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/./example-izhikevich2007cell-sim.spikes.dat 3340
pyNeuroML >>> INFO Dec 03,2020 19:36  (INFO) Finished reading, building, running and displaying LEMS model
pyNeuroML >>>
```
Let us check the output file:
```{code-block} console
$ head example-izhikevich2007cell-sim.spikes.dat
4       0.0519
1       0.0586
3       0.0708
4       0.132
0       0.1333
1       0.15
3       0.1804
4       0.214
1       0.2424
3       0.2906
..
```

Looks good!
Now, this simulation did *not* use an external simulator.
It ran using the in-built LEMS interpreter.
The LEMS interpreter can run single compartment models.
For anything more sophisticated, we need to use external simulators.

Let us generate code for the NEURON simulator from our simulation file.
First we see what options we need to use with `pynml`:
```{code-block} console
$ pynml -h
usage: pynml [-h|--help] [<shared options>] <one of the mutually-exclusive options>

pyNeuroML v0.5.6: Python utilities for NeuroML2
    libNeuroML v0.2.52
    jNeuroML v0.10.0

optional arguments:
  -h, --help            show this help message and exit

Shared options:
  These options can be added to any of the mutually-exclusive options

  -verbose              Verbose output
  -java_max_memory MAX  Java memory for jNeuroML, e.g. 400M, 2G (used in
                        -Xmx argument to java)
  -nogui                Suppress GUI,
                        i.e. show no plots, just save results
  <LEMS/NeuroML 2 file>
                        LEMS/NeuroML 2 file to process

Mutually-exclusive options:
  Only one of these options can be selected

...
  -neuron ...           (Via jNeuroML) Load a LEMS file, and convert it to
                        NEURON format.
                        The full format of the '-neuron' option is:
                        -neuron [-nogui] [-run] [-outputdir dir] <LEMS file>
                            -nogui
                                do not generate gtaphical elements in NEURON,
                                just run, save data, and quit
                            -run
                                compile NMODL files and run the main NEURON
                                hoc file (Linux only currently)
                            -outputdir <dir>
                                generate NEURON files in directory <dir>
                            <LEMS file>
                                the LEMS file to use

...
```
To generate our NEURON code, we run:
```{code-block} console
$ pynml LEMS_example-izhikevich2007cell-sim.xml -neuron -nogui
pyNeuroML >>> Successfully ran the following command using pyNeuroML v0.5.6:
pyNeuroML >>>     java -Xmx400M  -jar  "/usr/share/java/jNeuroML-0.10.0.jar"  "LEMS_example-izhikevich2007cell-sim.xml" -neuron
pyNeuroML >>> Output:
pyNeuroML >>>
pyNeuroML >>>  jNeuroML v0.10.0
pyNeuroML >>> (INFO) Reading from: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/LEMS_example-izhikevich2007cell-sim.xml
pyNeuroML >>> (INFO) Creating NeuronWriter to output files to /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test
pyNeuroML >>> (INFO) Adding simulation Component(id=example-izhikevich2007cell-sim type=Simulation) of network/component: IzNet (Type: network)
pyNeuroML >>> (INFO) Adding population: IzPop0
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/iz2007RS0.mod
pyNeuroML >>> (INFO) Adding population: IzPop1
pyNeuroML >>> (INFO) -- Mod file for: iz2007RS0 has already been created
pyNeuroML >>> (INFO) Adding projections/connections...
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/syn0.mod
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/pulseGen_0.mod
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/pulseGen_1.mod
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/pulseGen_2.mod
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/pulseGen_3.mod
pyNeuroML >>> (INFO) -- Writing to mod: /home/asinha/Documents/02_Code/00_mine/2020-OSB/NeuroML-Documentation/test/pulseGen_4.mod
pyNeuroML >>>
```

It generates all the necessary files required to run the simulation in NEURON.
This includes the required mod files and a Python script to run the simulation (ends with `nrn.py` for clarity):
```{code-block} console
$ ls
iz2007RS0.mod                               pulseGen_0.mod  pulseGen_4.mod
izhikevich2007_network.nml                  pulseGen_1.mod  syn0.mod
LEMS_example-izhikevich2007cell-sim_nrn.py  pulseGen_2.mod
LEMS_example-izhikevich2007cell-sim.xml     pulseGen_3.mod
```
We can now compile the mod files and run our simulation in NEURON:
```{code-block} console
# Compile the mod files
$ nrnivmodl .
...
Successfully created x86_64/special

# Run the simulation using the NEURON Python API.
$ python LEMS_example-izhikevich2007cell-sim_nrn.py

    Starting simulation in NEURON of 10000ms generated from NeuroML2 model...

Population IzPop0 contains 5 instance(s) of component: iz2007RS0 of type: izhikevich2007Cell
Population IzPop1 contains 5 instance(s) of component: iz2007RS0 of type: izhikevich2007Cell
Setting up the network to simulate took 0.001971 seconds
Running a simulation of 10000.0ms (dt = 0.1ms; seed=123)
Finished NEURON simulation in 0.259033 seconds (0.004317 mins)...
Saving results at t=9999.999999994727...
Saved data to: time.dat
Saved data to: example-izhikevich2007cell-sim.spikes.dat
Finished saving results in 0.036492 seconds
Done
```
We can now verify the spikes we recorded again:
```{code-block} console
$ head *spikes.dat
4       0.05060000000009927
1       0.05730000000009888
3       0.06950000000009819
4       0.13010000000009533
0       0.13200000000009576
1       0.14830000000009946
3       0.1788000000001064
4       0.21170000000011388
1       0.24050000000012042
3       0.2886000000001313
...
```

Looks good too!
The last couple of steps, where we compile the mod files and then run the simulation in NEURON will repeat for each simulation.
To make this easier, pyNeuroML provides a utility function that will do this for us.
Let us add one final line to our Python script:
```{literalinclude} ./NML2_examples/getting-started-izhikevich2008_network-lems-run.py
----
language: python
----
```
You can now design your model, generate the NeuroML representation, export the NEURON code, compile and run it all from one Python script.

To summarise, this page introduces the NeuroML file format, shows how one can describe a model in NeuroML, briefly introduces LEMS to create a simulation from the model, and demonstrates how the Python tools can be used to carry out all these functions and also run the simulations.
More detailed information on these steps and the individual tools can also be found in the documentation.
In the next section, you can experiment with this example using the provided IPython notebook.
