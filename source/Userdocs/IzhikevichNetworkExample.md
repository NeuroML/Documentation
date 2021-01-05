# A two population network of regular spiking Izhikevich neurons

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

## Defining the network using Python

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

