(userdocs:creating_models)=
# Creating NeuroML models

There are 3 main ways of developing a new model of a neuronal system in NeuroML

**1) Reuse elements from previous NeuroML models**

There are an increasing number of resources where you can find and analyse previously developed NeuroML models to use as the basis for a new model. See {ref}`here <userdocs:finding_models>` for details.

(userdocs:creating_models:from_scratch)=
**2) Writing models from scratch using Python NeuroML tools**

The toolchain around NeuroML means that it is possible to create a model in NeuroML format from the start. Please see the {ref}`Getting Started with NeuroML section <userdocs:getting_started_neuroml>` for quick examples on how you can use {ref}`pyNeuroML <pyneuroml>` to create NeuroML models and run them.

**3) Convert a published model developed in a simulator specific format to NeuroML**

Most computational models used in publications are released in the particular format used by the authors during their research, often in a general purpose simulator like {ref}`NEURON <userdocs:supporting:apps:neuron>`. Many of these can be found on [ModelDB](https://senselab.med.yale.edu/ModelDB/default). Converting one of these to NeuroML format will mean that all further developments/modifications of the model will be standards compliant, and will give access to all of the NeuroML compliant tools for visualising/analysing/optimising/sharing the model, as well as providing multiple options for executing the model across multiple simulators.

The rest of this page is a **step by step guide** to creating a new NeuroML model based on an existing published model, verifying its behaviour, and sharing it with the community on the Open Source Brain platform.


(userdocs:creating_models:converting_conductance)=
## Converting cell models to NeuroML and sharing them on Open Source Brain

The figure below is taken from the supplementary information of the {ref}`Open Source Brain paper <papers:osb>`, and gives a quick overview of the steps required and tools available for converting a model to NeuroML and sharing it on the OSB platform.

```{figure} ../images/osb-conversion.png
:alt: Schamatic of process of converting models to NeuroML
:align: center
:width: 60 %

Procedures and tools to convert models from native formats to NeuroML and PyNN (Taken from Gleeson et al. 2019 {cite}`Gleeson2019`)
```

### Step 1) Find the original model code

While it should in principle be possible to create the model based only on the description in the accompanying publication, having the original code will be invaluable for identifying all parameters related to the model and being able to verify the dynamical behaviour of the NeuroML equivalent against the original version.

Scripts for an increasing number of published models are available on [ModelDB](https://senselab.med.yale.edu/ModelDB/default), or the authors can be contacted to obtain the original scripts.

Verifying that these scripts reproduces some aspect of the published model by running them locally is an important first step.

(userdocs:creating_models:converting_conductance:github)=
### Step 2) Create GitHub and OSB accounts for sharing the code

Sign up to [GitHub](https://github.com/signup) to be able to share the updated code publicly. Sign up to [Open Source Brain](https://www.opensourcebrain.org/account/register), and adding a link to your GitHub user account will help link between the two resources.

Create a new [GitHub repository](https://docs.github.com/en/repositories) for your new model. There are plenty of examples of repositories containing NeuroML [on OSB](https://github.com/orgs/OpenSourceBrain/repositories). It's fine to share the code under your own user account, but if you would like to host it at https://github.com/OpenSourceBrain, please [get in contact with the OSB team](https://docs.opensourcebrain.org/General/Contacts.html).

Now you can commit the scripts for original version of the model to your GitHub repository. **Please confirm what the license/redistribution conditions are for the code!** Authors who have shared their code on ModelDB are generally happy for the code to be reused, but it is good to get in contact with them as a courtesy to let them know your plans with the model. They will generally be very supportive as long as the original publications are referenced, and will often have useful information on updated versions of the model. Adding or updating a README file will be valuable for anyone who comes across the model on GitHub.

Now you can create a project on OSB which will point to the GitHub repository and will be able to find any NeuroML models committed to it. You can also add a link back to the original archived version on ModelDB. For more details on this see [here](https://docs.opensourcebrain.org/OSBv1/Creating_Your_Own_Project.html).


### Step 3) Improve and test original model code

- Make simple script with one/each cell - simple current pulse into each ([example1](https://github.com/mbezaire/ca1/blob/development/NeuroML2/olm.hoc), [example2](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/NEURON/mitral.hoc))
- Make soma only example with all channels (ideally one where channels can easily be added/commented out) - apply current pulse ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NEURON/Test_Soma.hoc) in NEURON)
- Make passive version of multi-compartmental cell with multiple locations recorded
- Make multi-compartmental cell with multiple channels and calcium dynamics, with channels specified in separate files

(userdocs:creating_models:converting_conductance:initialnml2)=
### Create an initial version in NeuroML 2

- Create LEMS*.xml ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/LEMS_Soma_AllNML2.xml)) with *.net.nml ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Soma_AllNML2.net.nml)) and *.cell.nml ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Soma_AllNML2.cell.nml)) - for a cell with only a soma (don't try to match a multi-compartmental cell with channels to the original at this first stage)
- Start off with only passive parameters (capacitance, ax resistance and 1 leak current) set; gradually add channels as in 3); apply current pulse and save soma membrane potential to file
- Ensure all `*nml` files are {ref}`valid <userdocs:validating_models>`
- Ensure `LEMS*.xml` runs with `jnml;` visually compare behaviour with original simple script from the previous section)
- Install NEURON; ensure `LEMS*.xml` runs with `jnml -neuron`
- Commit LEMS/NeuroML code to GitHub


(userdocs:creating_models:converting_conductance:convert_channels)=
### Convert channels
- Restructure/annotate/comment channel files in original model to be as clear as possible and ideally all in the same overall structure (see mod files [here](https://github.com/mbezaire/ca1/tree/development)).
- (Optional) Create a (Python) script/notebook which contains the core activation variable expressions for the channels; this can be useful to restructure/test/plot/alter units of the expressions before generating the equivalent in NeuroML ([example](https://github.com/OpenSourceBrain/PINGnets/blob/master/NeuroML2/ConvertChannels.ipynb))
- If you are using NEURON, use `pynml-modchananalysis` to generate plots of the activation variables for the channels in the mod files ([example1](https://github.com/NeuroML/pyNeuroML/blob/master/examples/analyseNaMod.sh), [example2](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NEURON/analyse.sh)).
- Start from an existing similar example of an ion channel in NeuroML ([examples1](https://github.com/OpenSourceBrain/AllenInstituteNeuroML/tree/master/CellTypesDatabase/models/NeuroML2), [examples2](https://github.com/RokasSt/Thalamocortical/tree/master/NeuroML2/channels), [examples3](https://github.com/mbezaire/ca1/tree/development/NeuroML2/channels))
- Use `pynml-channelanalysis` to generate similar plots for your NeuroML based channels as your mod channels; these can easily be plotted for adding to your GitHub repo as summary pages ([example1](https://github.com/mbezaire/ca1/blob/development/NeuroML2/channels/channel_summary/README.md), [example2](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/NeuroML2/Channels/channel_summary/README.md)).
- Create a script to load the output of mod analysis and nml analysis and compare the outputs ([example](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/compare_nml2_mods.py)).


(userdocs:creating_models:converting_conductance:compare_single_comp)=
### Compare single compartment cell with channels

- Start by comparing passive soma example in original to passive NeuroML version
- Gradually test cell with passive conductance and *each channel individually*. Plot v along with rate variables for each channel & compare how they look during current pulse ([example in NEURON](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NEURON/Test_Soma.hoc) vs [example in NeuroML](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/Soma_AllNML2.cell.nml) and [LEMS](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/blob/master/NMC/NeuroML2/LEMS_Soma_AllNML2.xml))
- Test in `jnml` first, then in Neuron with `jnml -neuron`


(userdocs:creating_models:converting_conductance:add_omv_tests)=
### Add OMV tests

```{admonition} Optional, but recommended.
:class: dropdown tip
This step is optional, but recommended.
```

- Install the [Open Source Brain Model validation framework](https://github.com/OpenSourceBrain/osb-model-validation) (OMV) - test on your local machine on standard examples (example: [Hay et al.](https://github.com/OpenSourceBrain/L5bPyrCellHayEtAl2011))
- Add OMV tests to native code ([example](https://github.com/OpenSourceBrain/GranCellSolinasEtAl10/blob/master/NEURON/.test.nrnpy.omt)), e.g. test the spike times of cell when simple current pulse applied
- Add OMV tests for NeuroML version, reusing the Model Emergent Property (`*.mep`) file ([example](https://github.com/mbezaire/ca1/blob/development/NeuroML2/cells/tests/.test.sca.jnmlnrn.omt))

(userdocs:creating_models:converting_conductance:compare_multi_comp)=
### Compare multi-compartmental cell with channels

- You can export morphologies on [NeuroMorpho.org](https://neuromorpho.org) to NeuroML2 ([example](https://github.com/NeuralEnsemble/NeuroinformaticsTutorial/blob/master/Exercises/Exercise1_NeuroMorpho_to_OSB.md))


(userdocs:creating_models:from_neuron)=
## Converting models from NEURON to NeuroML

Model simulations written using the NEURON simulator can be converted to NeuroML using the {ref}`pyNeuroML <pyneuroml>` API:

```{code-block} python
from pyneuroml.neuron import export_to_neuroml2
..
..

export_to_neuroml2("test.hoc", "test.morphonly.cell.nml", includeBiophysicalProperties=False)
```


- If you are using NEURON, export morphology from NEURON using pyNeuroML ([example](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/export_nml2.py)); this will be easier if there is a hoc script with just a single cell instance as in section 1). While there is the option to use `includeBiophysicalProperties=True` and this will attempt to export the conductance densities on different groups, it may be better to consolidate these and add them afterwards using correctly named groups and the most efficient representation of conductance density to group relationships ([example](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/Python/Export/export_mitral.py)).
  - Alternatively manually add the `<channelDensity>` elements to the cell file (as [here](https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes/blob/master/NeuroML2/L23_NoHotSpot.cell.nml#L16711)).
- As with the single compartment example, it's best to start off with the passive case, compare that to the original code (for v at multiple locations), and gradually add channels.
- Many projects on OSB were originally converted from the original format (NEURON, GENESIS, etc.) to NeuroML v1 using {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>` (see [here](http://www.opensourcebrain.org/search_custom_field?f[]=43&op[43]=~&v[43][]=neuroConstruct) for a list of these). neuroConstruct has good support for export to NeuroML v2, and this code could form the basis for your conversion. More on using neuroConstruct [here](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) and details on conversion of models to NeuroML v1 [here](http://www.neuroconstruct.org/docs/importneuron.html#Converting+mod+file%2FGENESIS+script+channels+into+ChannelML).

(userdocs:creating_models:converting_conductance:reoptimise)=
### (Re)optimising cell models

- You can use Neurotune inside pyNeuroML to re-optimise your cell models. An example is [here](https://github.com/NeuroML/pyNeuroML/blob/master/examples/tuneHHCell.py)
