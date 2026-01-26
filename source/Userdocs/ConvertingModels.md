(userdocs:creating_models:converting_conductance)=
# Converting models to NeuroML and sharing them on Open Source Brain

```{admonition} Walk throughs available
:class: tip
Look at the {ref}`Walkthroughs chapter <userdocs:walkthroughs>` for worked examples.
```
The figure below is taken from the supplementary information of the {ref}`Open Source Brain paper <papers:osb>`, and gives a quick overview of the steps required and tools available for converting a model to NeuroML and sharing it on the OSB platform.

```{figure} ../images/osb-conversion.png
:alt: Schamatic of process of converting models to NeuroML
:align: center
:width: 60 %

Procedures and tools to convert models from native formats to NeuroML and PyNN (Taken from Gleeson et al. 2019 {cite}`Gleeson2019`)
```

## Step 1) Find the original model code

While it should in principle be possible to create the model based only on the description in the accompanying publication, having the original code is invaluable.
The original code allows the identification of all parameters related to the model, and it is required to verify the dynamical behaviour of the NeuroML equivalent.

Scripts for an increasing number of published models are available on [ModelDB](https://modeldb.science).
ModelDB models are also published as [GitHub repositories](https://github.com/ModelDBRepository).
Forks of these are also managed in the [Open Source Brain GitHub organization](https://github.com/opensourcebrain/) and indexed on [Open Source Brain version 2](https://v2.opensourcebrain.org/).


So, the first step is to obtain the original model code and verify that this can be run to reproduce the published results.


(userdocs:creating_models:converting_conductance:github)=
## Step 2) Create GitHub and OSB accounts for sharing the code

### 2a) Sign up to GitHub and OSB

Sign up to [GitHub](https://github.com/signup) to be able to share the updated code publicly. Next, sign up to [Open Source Brain](https://www.opensourcebrain.org/account/register), and adding a reference to your GitHub user account will help link between the two resources.

### 2b) Create GitHub repository

Create a new [GitHub repository](https://docs.github.com/en/repositories) for your new model. There are plenty of examples of repositories containing NeuroML [on OSB](https://github.com/orgs/OpenSourceBrain/repositories). It's fine to share the code under your own user account, but if you would like to host it at https://github.com/OpenSourceBrain, please [get in contact with the OSB team](https://docs.opensourcebrain.org/General/Contacts.html).

Now you can commit the scripts for original version of the model to your GitHub repository. **Please check what the license/redistribution conditions are for the code!** Authors who have shared their code on [ModelDB](https://senselab.med.yale.edu/ModelDB/default) are generally happy for the code to be reused, but it is good to get in contact with them as a courtesy to let them know your plans with the model. They will generally be very supportive as long as the original publications are referenced, and will often have useful information on any updated versions of the model. Adding or updating a [README file](https://docs.opensourcebrain.org/OSBv1/Write_Your_Project_Documentation.html#add-a-readme-file-in-your-github-repository-and-reuse-it-on-your-osb-projects) will be valuable for anyone who comes across the model on GitHub.

### 2c) Create OSB project

Now you can create a project on OSB which will point to the GitHub repository and will be able to find any NeuroML models committed to it. You can also add a link back to the original archived version on ModelDB, and even reuse your README on GitHub as a description. For more details on this see [here](https://docs.opensourcebrain.org/OSBv1/Creating_Your_Own_Project.html).


## Step 3) Improve and test original model code

With the original simulator code shared on GitHub, and a README updated to describe it, new users will be able to clone the repository and start using the code as shared by the authors. Some updates may be required and any changes from the original version will be recorded under the Git history visible on GitHub.


### 3a) Make simpler/modularised versions of original model scripts

Many of the model scripts which get released on ModelDB aim to reproduce one or two of the figures from the associated publication. However, these scripts can be quite complex, and mix simulation with some analysis of the results. They don't always provide a single, simple run of the model with standard parameters, which would be the target for a first version of the model in NeuroML.

Therefore it would be useful to create some additional scripts (reusing cell/channel definition files as much as possible) illustrating the baseline behaviour of the model, including:

- A simple script with a single cell (or one for each if multiple cells present) - applying a simple current pulse into each (e.g. [example1](https://github.com/mbezaire/ca1/blob/development/NeuroML2/olm.hoc), [example2](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/NEURON/mitral.hoc))
- A single compartment (soma only) example with all the ion channels (ideally one where channels can easily be added/commented out) - apply current pulse ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NEURON/Test_Soma.hoc) in NEURON)
- A passive version of multi-compartmental cell with multiple locations recorded
- A multi-compartmental cell with multiple channels and calcium dynamics, with the channels specified in separate files

These will be much easier to compare to equivalents in NeuroML.

(userdocs:creating_models:converting_conductance:add_omv_tests)=
### 3b) Add OMV tests

```{admonition} Optional, but recommended.
:class: dropdown tip
This step is optional, but highly recommended to create automated tests on the behaviour of the model.
```
Once you have some scripts which illustrate (in plots/saved data) the baseline expected behaviour of your model (spiketimes, rate of firing etc.), it would be good to put some checks in place which can be run to ensure this behaviour stays consistent across changes/commits to your repository, different versions of the underlying simulator, as well as providing a target for what the NeuroML version of the model should produce.

The **[Open Source Brain Model validation framework](https://github.com/OpenSourceBrain/osb-model-validation) (OMV)** is designed for exactly this, allowing small scripts to be added to your repository stating what files to execute in what simulation engine and what the expected properties of generated output should be. These tests can be run on your local machine during development, but can also be easily integrated with [GitHub Actions](https://github.com/features/actions), allowing tests across multiple simulators to be run every time there is a commit to the repository ([example](https://github.com/OpenSourceBrain/IzhikevichModel/actions/runs/1520638984)).

To start using this for your project, install OMV and test running it on your local machine (`omv all`) on some standard examples (e.g. [Hay et al.](https://github.com/OpenSourceBrain/L5bPyrCellHayEtAl2011)).

Add OMV tests for your native simulator scripts ([example](https://github.com/OpenSourceBrain/GranCellSolinasEtAl10/blob/master/NEURON/.test.nrnpy.omt)), e.g. test the spike times of cell when simple current pulse applied. Commit this file to GitHub, along with a GitHub Actions workflow ([example](https://github.com/OpenSourceBrain/IzhikevichModel/blob/master/.github/workflows/omv-ci.yml)), and look for runs under the Actions tab of your project on GitHub.

Later, you can add OMV tests too for the equivalent NeuroML versions, reusing the Model Emergent Property (`*.mep`) file ([example](https://github.com/mbezaire/ca1/blob/development/NeuroML2/cells/tests/.test.sca.jnmlnrn.omt)), thus testing that the behaviours of the 2 versions are the same (within a certain tolerance).

(userdocs:creating_models:converting_conductance:initialnml2)=
## 4) Create a version of the model in NeuroML 2

### 4a) Create a LEMS Simulation file to run the model

A {ref}`LEMS Simulation file <userdocs:lemssimulation>` is required to specify how to run a simulation of the NeuroML model, how long to run, what to plot/save etc. Create a LEMS*.xml ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/LEMS_Soma_AllNML2.xml)) with *.net.nml ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Soma_AllNML2.net.nml)) and *.cell.nml ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Soma_AllNML2.cell.nml)) for **a cell with only a soma** (don't try to match a full multi-compartmental cell with all channels to the original version at this early stage).

Start off with only passive parameters (capacitance, axial resistance and 1 leak current) set; gradually add channels as in 4b) below; apply a current pulse and save soma membrane potential to file.

Ensure all `*nml` files are {ref}`valid <userdocs:validating_models>`. Ensure the `LEMS*.xml` runs with `jnml`; visually compare the behaviour with original simple script from the previous section.

Ensure the `LEMS*.xml` runs with `jnml -neuron`, producing similar behaviour. If there is a good correspondence, add OMV tests for the NeuroML version, using the Model Emergent Property (`*.mep`) file from the original script's test.

When ready, commit the LEMS/NeuroML code to GitHub.


(userdocs:creating_models:converting_conductance:convert_channels)=
### 4b) Convert channels to NeuroML

Restructure/annotate/comment channel files in the original model to be as clear as possible and ideally have all use the same overall structure (e.g. see mod files [here](https://github.com/mbezaire/ca1/tree/development)).

(Optional) Create a (Python) script/notebook which contains the core activation variable expressions for the channels; this can be useful to restructure/test/plot/alter units of the expressions before generating the equivalent in NeuroML ([example](https://github.com/OpenSourceBrain/PINGnets/blob/master/NeuroML2/ConvertChannels.ipynb)).

If you are using NEURON, use `pynml-modchananalysis` to generate plots of the activation variables for the channels in the mod files ([example1](https://github.com/NeuroML/pyNeuroML/blob/master/examples/analyseNaMod.sh), [example2](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NEURON/analyse.sh)).

Start from an existing similar example of an ion channel in NeuroML ([examples1](https://github.com/OpenSourceBrain/AllenInstituteNeuroML/tree/master/CellTypesDatabase/models/NeuroML2), [examples2](https://github.com/RokasSt/Thalamocortical/tree/master/NeuroML2/channels), [examples3](https://github.com/mbezaire/ca1/tree/development/NeuroML2/channels)).

Use `pynml-channelanalysis` to generate similar plots for your NeuroML based channels as your mod channels; these can easily be plotted for adding to your GitHub repo as summary pages ([example1](https://github.com/mbezaire/ca1/blob/development/NeuroML2/channels/channel_summary/README.md), [example2](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/NeuroML2/Channels/channel_summary/README.md)).

Create a script to load the output of mod analysis and nml analysis and compare the outputs ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/compare_nml2_mods.py)).


(userdocs:creating_models:converting_conductance:compare_single_comp)=
### 4c) Compare single compartment cell with channels

Ensure you have a passive soma example in NeuroML which reproduces the behaviour of an equivalent passibe version in the original format (from steps 3a and 4a above).

Gradually test the cell with passive conductance and *each channel individually*. Plot v along with rate variables for each channel & compare how they look during current pulse ([example in NEURON](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NEURON/Test_Soma.hoc) vs [example in NeuroML](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Soma_AllNML2.cell.nml) and [LEMS](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/LEMS_Soma_AllNML2.xml))

Test these in `jnml` first, then in Neuron with `jnml -neuron`.

When you are happy with each of the channels, try the soma with all of the channels in place, with the same channel density as present in the soma of the original cell.


(userdocs:creating_models:converting_conductance:compare_multi_comp)=
### 4d) Compare multi-compartmental cell incorporating channels

If the model was created in NEURON, export the 3D morphology from the original NEURON scripts using pyNeuroML ([example](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/export_nml2.py)); this will be easier if there is a hoc script with just a single cell instance as in section 1). While there is the option to use `includeBiophysicalProperties=True` and this will attempt to export the conductance densities on different groups, it may be better to consolidate these and add them afterwards using correctly named groups and the most efficient representation of conductance density to group relationships ([example](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/Python/Export/export_mitral.py)).

```{code-block} python
from pyneuroml.neuron import export_to_neuroml2
..
export_to_neuroml2("test.hoc", "test.morphonly.cell.nml", includeBiophysicalProperties=False)
```

Alternatively manually add the `<channelDensity>` elements to the cell file (as [here](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/L23_NoHotSpot.cell.nml#L16711)).

You can use the tools for {ref}`visualising NeuroML Models <userdocs:visualising_models>` to compare how these versions look against the originals.

As with the single compartment example, it's best to **start off with the passive case**, i.e no active channels on the soma or dendrites, and compare that to the original code (for membrane potential at multiple locations!), and gradually add channels.

Many projects on OSB were originally converted from the original format (NEURON, GENESIS, etc.) to NeuroML v1 using {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>` (see [here](http://www.opensourcebrain.org/search_custom_field?f[]=43&op[43]=~&v[43][]=neuroConstruct) for a list of these). neuroConstruct has good support for export to NeuroML v2, and this code could form the basis for your conversion. More on using neuroConstruct [here](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) and details on conversion of models to NeuroML v1 [here](http://www.neuroconstruct.org/docs/importneuron.html#Converting+mod+file%2FGENESIS+script+channels+into+ChannelML).

Note: you can also export other morphologies from [NeuroMorpho.org](https://neuromorpho.org) in NeuroML2 format ([example](https://github.com/NeuralEnsemble/NeuroinformaticsTutorial/blob/master/Exercises/Exercise1_NeuroMorpho_to_OSB.md)) to try out different reconstructions of the same cell type with your complement of channels.

(userdocs:creating_models:converting_conductance:reoptimise)=
## 4e) (Re)optimising cell models

You can use [Neurotune](https://github.com/NeuralEnsemble/neurotune/) inside pyNeuroML to re-optimise your cell models. An example is [here](https://github.com/NeuroML/pyNeuroML/blob/master/examples/tuneHHCell.py), and a full sequence of optimising a NeuroML model against data in NWB can be found {ref}`here <userdocs:optimising>`.


## 4f) Create an equivalent network model in NeuroML

Creating an equivalent of a complex network model originally built in hoc for example in NeuroML is not trivial. The guide to network building with libNeuroML {ref}`here <userdocs:gettingstarted:izhikevichnetwork>` is a good place to start.

See also {ref}`NeuroMLlite <neuromllite>`.

## 5) Access, view and run your model on OSB

When you're happy that a version of the model is behaving correctly in NeuroML, you can try visualising it on OSB.

See [here](https://docs.opensourcebrain.org/OSBv1/Five_Minute_Introduction.html) for more details about viewing and simulating projects on OSB.

## 6) Share and collaborate

There is more information on how you can disseminate and promote your model once it is on OSB in the main documentation for that platform:
https://docs.opensourcebrain.org.

Consider sharing parts of the model on {ref}`other NeuroML supporting resources <userdocs:finding_models>` (e.g. cell and channel files on NeuroML-DB).

