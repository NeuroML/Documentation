(userdocs:visualising_models)=
# Visualising NeuroML Models

A number of the {ref}`NeuroML software tools <userdocs:software>` can be used to easily visualise models described in NeuroML.

(userdoc:visualising_models:summary)=
## Get a quick summary of your model

(userdoc:visualising_models:summary:cli)=
### Using command line tools

You can get a quick summary of your NeuroML model using the  `pynml-summary` command line tool that is provided by {ref}`pyNeuroML <pyneuroml>`:

```{code-block} console
Usage:
pynml-summary <NeuroML file>
```

For example, to get a quick summary of the [Primary Auditory Cortex model by Dave Beeman](https://github.com/OpenSourceBrain/ACnet2/blob/master/neuroConstruct/generatedNeuroML2/MediumNet.net.nml) (see it [here on Open Source Brain](https://www.opensourcebrain.org/projects/acnet2)), one can run:
```{code-block} console
pynml-summary MediumNet.net.nml

*******************************************************
* NeuroMLDocument: network_ACnet2
*
*  PulseGenerator: ['BackgroundRandomIClamps']
*
*  Network: network_ACnet2 (temperature: 6.3 degC)
*
*   60 cells in 2 populations
*     Population: baskets_12 with 12 components of type bask
*       Locations: [(372.5585, 75.3425, 459.2106), ...]
*       Properties: color=0.0 0.19921875 0.59765625;
*     Population: pyramidals_48 with 48 components of type pyr_4_sym
*       Locations: [(64.2564, 0.6838, 94.8305), ...]
*       Properties: color=0.796875 0.0 0.0;
*
*   984 connections in 4 projections
*     Projection: SmallNet_bask_bask from baskets_12 to baskets_12, synapse: GABA_syn_inh
*       60 connections: [(Connection 0: 3:0(0.41661) -> 0:0(0.68577)), ...]
*     Projection: SmallNet_bask_pyr from baskets_12 to pyramidals_48, synapse: GABA_syn
*       336 connections: [(Connection 0: 10:0(0.05824) -> 0:6(0.02628)), ...]
*     Projection: SmallNet_pyr_bask from pyramidals_48 to baskets_12, synapse: AMPA_syn_inh
*       252 connections: [(Connection 0: 1:0(0.89734) -> 0:1(0.09495)), ...]
*     Projection: SmallNet_pyr_pyr from pyramidals_48 to pyramidals_48, synapse: AMPA_syn
*       336 connections: [(Connection 0: 14:0(0.52814) -> 0:3(0.10797)), ...]
*
*   14 inputs in 1 input lists
*     Input list: BackgroundRandomIClamps to pyramidals_48, component BackgroundRandomIClamps
*       14 inputs: [(Input 0: 37:0(0.500000)), ...]
*
*******************************************************
```
(userdoc:visualising_models:summary:pyNeuroML)=
### Using pyNeuroML

You can also get a summary of your model from within your {ref}`pyNeuroML <pyneuroml>` script itself using the `summary` function:

```{code-block} python
import pyneuroml.pynml

...


pyneuroml.pynml.summary(nml2_doc)
```

(userdoc:visualising_models:png)=
## View the 3D structure of your model

(userdoc:visualising_models:png:cli)=
### Using command line tools

You can generate an image of the 3D structure of the NeuroML model using the `pynml` command provided by {ref}`pyNeuroML <pyneuroml>`, or using the `jnml` command provided by {ref}`jNeuroML <jneuroml>`:

```{code-block} console
Usage:
pynml -png/-svg <NeuroML file>
jnml -png/-svg <NeuroML file>
```

For example, to generate a PNG image of the Auditory Cortex model used above, we can use (use `-svg` to generate a vectorised SVG image instead of a PNG):

```{code-block} console
pynml -png MediumNet.net.nml
```

This generates the following image showing different views of the network :

```{figure} ../images/Acnet-medium.net.png
:alt: Graphical view of the Auditory Cortex model generated with pynml
:align: center
:scale: 20 %

Graphical view of the Auditory Cortex model generated with pynml
```

An visualiser is also included in pyneuroml as `pynml-plotmorph` which includes both 2D and 3D views:

```{code-block} console
Usage:
pynml-plotmorph <NeuroML file>
pynml-plotmorph -i <NeuroML file>
```

```{figure} ../images/20231122-ACNet.png
:alt: A network visualised with `pynml-plotmorph`
:align: center
:width: 30%

Matplotlib based 2D visualisation of a network with `pynml-plotmorph`.
```
<center>
    <video src="../_static/files/20231122-ACNet.webm" width="70%"  controls loop>
        Your browser does not support the video tag
    </video><br />
    <i>Example network visualised interactively using `pynml-plotmorph`</i><br /><br />
</center>


You can also generate graphical representations that can be viewed with the [Persistence of Vision Raytracer (POV-Ray)](http://povray.org/) tool using the `pynml-povray` tool.
For example:

```{code-block} console
pynml-povray MediumNet.net.nml -scalez 8
povray Antialias=On Antialias_Depth=10 Antialias_Threshold=0.1 Output_to_File=y Output_File_Type=N Output_File_Name=Acnet-medium.povray +W1200 +H900 MediumNet.net.nml.pov

```
generates this image:

```{figure} ../images/Acnet-medium.povray.png
:alt: Graphical view of the Auditory Cortex model generated with pynml-povray and POV-Ray
:align: center
:scale: 50 %

Graphical view of the Auditory Cortex model generated with pynml-povray and POV-Ray
```


You can also use POV-Ray interactively.
Please refer to the [official website](http://povray.org/download/) for more information on installing and using POV-Ray.
On Fedora Linux systems, you can install it from the Fedora repositories using `dnf`:

```{code-block} console
sudo dnf install povray
```

(userdoc:visualising_models:png:pyNeuroML)=
### Using pyNeuroML

These functions are also exposed as Python functions in {ref}`pyNeuroML <pyneuroml>`, so that you can use them directly in Python scripts:

```{code-block} python
import pyneuroml.pynml

pyneuroml.pynml.nml2_to_png(nml2_doc)
pyneuroml.pynml.nml2_to_svg(nml2_doc)


from pyneuroml.plot.PlotMorphology import plot_2D
from pyneuroml.plot.PlotMorphologyVispy import plot_interactive_3D

plot_2D(nml2_doc)
plot_interactive_3D(nml2_doc)
```

```{admonition} Open Source Brain uses NeuroML.
:class: tip
The [Open Source Brain platform](https://www.opensourcebrain.org) generates the interactive visualisations from NeuroML sources.
See the Auditory Cortex model on Open Source Brain [here](https://www.opensourcebrain.org/projects/acnet2).
```


(userdoc:visualising_models:graph)=
## View the connectivity graph of your model

(userdoc:visualising_models:graph:cli)=
### Using command line tools
```{admonition} Use levels to generate connectivity graphs with different levels of detail.
:class: tip dropdown

Positive values for levels will generate figures at the population level, while negative values will generate them at the level of cells.
```

You can generate an image of the 3D structure of the NeuroML model using `pynml`:

```{code-block} console
Usage:
pynml <NeuroML file> -graph <level, engine>
```

For example, to generate a PNG image of the Auditory Cortex model used above, we can use:

```{code-block} console
pynml MediumNet.net.nml -graph 1d
```

This generates the following image showing different views of the network :

```{figure} ../images/Acnet-medium-graph-level1.png
:alt: Level 1 network graph generated by pynml
:align: center

Level 1 network graph generated by pynml
```

You can modify the level of detail included in the graph by using different values of levels.
For example, this command generates a level 5 graph:

```{code-block} console
pynml MediumNet.net.nml -graph 5d
```

```{figure} ../images/Acnet-medium-graph-level5.png
:alt: Level 5 network graph generated by pynml
:align: center
:scale: 60 %

Level 5 network graph generated by pynml
```
(userdoc:visualising_models:graph:pyNeuroML)=
### Using pyNeuroML

You can also generated these figures from within your {ref}`pyNeuroML <pyneuroml>` script itself using the `generate_nmlgraph` function:

```{code-block} python
import pyneuroml.pynml

...


pyneuroml.pynml.generate_nmlgraph(nml2_doc, level="1", engine="dot")
```


(userdoc:visualising_models:matrix)=
## View the connectivity matrices of the model

You can generate the connectivity matrices of projections between neuronal populations of the NeuroML model using `pynml`:

```{code-block} console
Usage:
pynml <NeuroML file> -matrix <level>
```

For example, to generate a PNG image of the connectivity matrices in the Auditory Cortex model used above, we can use:

```{code-block} console
pynml MediumNet.net.nml -matrix 1
```

This generates the following images showing different views of the connectivity matrices in the network :

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{image} ../images/Acnet-matrix-1.png
:alt: Connectivity matrix generated by pynml - sum of signed weights
:scale: 50 %
```

</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{image} ../images/Acnet-matrix-2.png
:alt: Connectivity matrix generated by pynml - average magnitude of conductance received by post-synaptic neurons
:scale: 50 %
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{image} ../images/Acnet-matrix-3.png
:alt: Connectivity matrix generated by pynml - number of connections
:scale: 50 %
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{image} ../images/Acnet-matrix-4.png
:alt: Connectivity matrix generated by pynml - average conductance received by post-synaptic neurons
:scale: 50 %
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{image} ../images/Acnet-matrix-5.png
:alt: Connectivity matrix generated by pynml - average weight per connection
:scale: 50 %
```

</center>

</div>
</div>
</div>


(userdoc:visualising_models:lemsgraph)=
## View graph of the simulation instance of the model

(userdoc:visualising_models:lemsgraph:cli)=
### Using command line tools

When you have created a simulation instance of the NeuroML model using LEMS, you can also visualise this using `pynml` or `jnml`:

```{code-block} console
Usage:
pynml <LEMS simulation file> -lems-graph
jnml <LEMS simulation file> -lems-graph
```

For example, to generate the LEMS graph for the {ref}`Izhikevich neuron network example <userdocs:gettingstarted:izhikevichnetwork>`, we will use:

```{code-block} console
jnml LEMS_example_izhikevich2007network_sim.xml -lems-graph
```
will generate:
```{figure} ../Userdocs/NML2_examples/LEMS_example_izhikevich2007network_sim.png
:alt: Model summary graph generated using jnml.
:align: center
:scale: 50%

A summary graph of the model generated using jnml.
```

Note that the `-lems-graph` option does not take options for levels of detail.
It shows all the details of the simulation instance, and so is better suited for simpler models rather than detailed conductance based network models.
For example, for the Auditory Cortex model, {download}`this <../images/Acnet-LEMS.png>` very very detailed image is generated (please click to open: it is too large to display in the page).


(userdoc:visualising_models:lemsgraph:pyneuroml)=
### Using pyNeuroML

You can also generated these figures from within your {ref}`pyNeuroML <pyneuroml>` script itself using the `generate_lemsgraph` function:

```{code-block} python
import pyneuroml.pynml

...

pyneuroml.pynml.generate_lemsgraph(lems_file)
```

## Viewing/analysing ion channel dynamics

There is a dedicated section on {ref}`visualising and analysing ion channel models <userdocs:visualising_channels>`.
