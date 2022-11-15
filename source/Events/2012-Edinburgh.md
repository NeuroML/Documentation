(neuromlevents:2012edinburgh)=
# March 2012: Fourth NeuroML Development Workshop

Convergence in Computational Neuroscience 2012
Joint BrainScaleS CodeJam/NeuroML workshop, Edinburgh, 12-16th March

The NeuroML Development Workshops and the [BrainScaleS](http://brainscales.kip.uni-heidelberg.de/) (previously FACETS) [CodeJams](http://neuralensemble.org/meetings.html) have been two important initiatives in recent years for developers of tools in computational and systems neuroscience to present their latest work, exchange ideas and work at achieving interoperability between software applications for investigating brain function.
This year these groups held a joint workshop (Convergence in Computational Neuroscience) on March 12th-16th in the Informatics Forum in Edinburgh, UK.
The meeting was held at the [Informatics Forum](https://www.ed.ac.uk/informatics/about/location/forum) in Edinburgh, UK, from 12th to 16th March 2012.


## Meeting report
Note: details of the meeting activities from Wednesday 14th to Friday 16th are available on the [NeuralEnsemble.org webpage](http://neuralensemble.org/meetings/CodeJam5/).


### Monday 12th March: NeuroML Development Workshop Day 1

#### Morning session: Current state of NeuroML 2 development & relationship to other initiatives
Chair: Andrew Davison

```{list-table}
:header-rows: 1
:widths: 10, 70, 20

* - Time
  - Session
  - Speaker


* - 09:00
  - **Welcome & goals of meeting**

    Angus welcomed attendees, thanking in particular out local organisers at University of Edinburgh, Mike Hull and Mika Pelko!
  - Angus Silver


* - 09:05
  - **Update on latest developments in NeuroML 2/LEMS ([PPT](https://docs.neuroml.org/_static/NeuroML2012/PGleeson_NeuroMLIntro2012.ppt))**

    Padraig presented an introduction to NeuroML, starting with an overview of the modular nature of NeuroML v1.x, advantages of the use of XML, examples of neuronal models in NeuroML, current tools which support the language, (including the recently added NeuroMorpho.org and Channelpedia).

    The requirements for v2.0 were presented. Explicit definitions of model component behaviour allows description of the dynamics of model components in a simulator independent, machine readable way. The relationship between LEMS and NeuroML2 was discussed. A short overview of NeuroML 2.0 was given including dimensions/units. Example of adaptive exponential integrate and cell network was presented. An overview of libNeuroML was given. Export to NEURON, neuroConstruct, interaction with SBML was shown.
  - Padraig Gleeson

* - 09:30
  - **Introduction to NineML & libNineML ([PDF](https://docs.neuroml.org/_static/NeuroML2012/MHull_NineML.pdf))**

    Mike gave an introduction to the NineML object model and libNineML. The INCF Task Force in Multiscale Modelling created the language, consisting of an Abstraction Layer and User Layer. Mike's presentation focused on the abstraction layer which contains many terms for the object model. Core object in the Abstraction layer were presented: ComponentClass, Interface with Parameters, Ports (AnalogPorts, EventPorts and Reduce Ports), Dynamics with StateVariables and a Regime Transition Graph (with Transitions, StateAssignments, Aliases).

    libNineML (in Python) loads and saves models from/to XML to/from Python that helps with code generation, turns models into NEST, NEURON and PyNN.

  - Mike Hull

* - 10:00
  - **The COMBINE Initiative ([PDF](https://docs.neuroml.org/_static/NeuroML2012/NleNovere_NeuroML-COMBINE.pdf))**

    Nicolas presented the Combine Initiative: Standards for describing the whole life-cycle of modelling. Different communities favour different types of models that are more suited for their domain. Current standardisation efforts depend on the initial people, individual funding structure, IP issues. Specifications, API's, test-suites, etc. really need industry-grade support which is not compatible with standard academic usages and possibilities.

    The vision of COMBINE is to pave the space of model descriptions with coordination of standard development (without interference with the development). There are criteria for inclusion in the core COMBINE standards: new standards must be different from those already included, described in technical specification documents, free, open, developed and used by more than one team, democratically elected members, mature software support including API, and must be actively developed.

    COMBINE organises joint meetings replacing standards specific ones (e.g. SBML Hackathon). Next COMBINE meeting is in Toronto in August. HARMONY for hacking will be in Maastricht in May.
   - Nicolas le Novere

* - 10:30
  - **Coffee**
  -

* - 11:00
  - **The International Neuroinformatics Coordinating Facility**

    Sean presented the motivation for, current structure and the aims of the INCF. The goal of neuroscience is to understand the brain. We're at a crisis point in understanding disorders. Big Pharma is pulling out of neuroscience due to the high cost and risk of understanding these disorders. Past centuries have focused on obtaining observations. More recently, models were used to understand these observations. Today we have eScience as a new way of handling large-scale data, modelling, simulations, linking data, etc. One of the INCF's goals is to transform neuroscience into an eScience from level of molecules to clinic.

    Integration of databases is a goal, which requires standardized data formats. There are 16 member countries in INCF. He gave an introduction to the 4 programs from the past few years: Digital Brain Atlasing, Multi-Scale Modeling, Ontologies of Neural Structures  and Standards for Datasharing.

    He discussed future plans for the INCF "Cyberinfrastructure", including a discussion of the planned INCF cloud "Dropbox" for data which could include metadata tags enabling global search.

  - Sean Hill

* - 11:30
  - **Collaborative Modelling Repository update**

    Padraig presented the initial work towards an open source, collaborative repository for NeuroML models, the Open Source Brain project. A preliminary version of this is avaliable here. It will be based on a version control repository (initially Mercurial) storing the model files. It will have automatic generation of online documentation of the models from ChannelML, MorphML, etc. Connectivity matrices for network connections, etc. can be generated for models which are stored in neuroConstruct format. NeuroLex IDs can be used to identify cells and channels to other resources. Feedback on the initial implementation was welcomed.

  - Padraig Gleeson

* - 12:00
  - **Open discussion on model specification initiatives**

    Differences were pointed out between INCF and COMBINE approaches to standards development. IEEE provides an infrastructure for review, etc. Nicolas discussed the burdens of obtaining "official" standards board recognition. Many of the COMBINE procedures imitate W3C procedures. A good standard is one that works. COMBINE criteria don't say anything about the standard document itself.
  -

* - 13:00
  - **Lunch**
  -
```

#### Afternoon session: Specification of detailed biophysical components in NeuroML 2/LEMS
Chair: Sharon Crook

```{list-table}
:header-rows: 1
:widths: 10, 70, 20

* - Time
  - Session
  - Speaker


* - 14:00
  - **Representing channels, synapses & conductance based models ([PDF](https://docs.neuroml.org/_static/NeuroML2012/RCannon_ModellingIonChannels.pdf))**

    Robert gave a presentation on ways to represent synapses and conductances. He defined the Nernst equation with XML based on Hille's description. It is still not clear how some things should be done, in particular how to handle dimensions and units. Currently, dimensions are defined and then assertions about relationships among dimensions can be made. Units are not defined until NeuroML is written (with numerical values, e.g. -70mV). There was some discussion of how dimensions should be defined. Physicists solved this problem by developing SI units. Both space and no space between values and units are allowed in LEMS. There was some discussion of how events can be handled in LEMS.
  - Robert Cannon


* - 14:20
  - **Experiences with using NeuroML 2**

    Avrama gave a brief report of her hands on experience with using NeuroML 2. She has a medium spiny projection neuron model which she's translating to GENESIS. She didn't want to use a GUI unless absolutely necessary and has been manually editing the XML. Many of the (non calcium dependent) channels have already been converted to NeuroML 2. She can only run single compartment versions of her model since LEMS doesn't yet support multi compartmental models. She has produced some some multi segment morphologies in NML2, even though these can't be used in LEMS based simulations yet. She requires a way to specify distance from the soma. Another difficulty is not being able to define a template (dendritic) subbranch and add it multiple times to the cell. She will add spines later. Calcium dependent channels are a work in progress in NeuroML v2.0, but some useful simulations have already been done with her developing model.

  - Avrama Blackwell

* - 14:40
  - **Implementing cerebellar models in PyNEURON, neuroConstruct & NeuroML**

    Sergio is developing cerebellar models (Golgi cells and granular cells) in a network of granule layer. Solinas S, Nieus T and D`Angelo E (2010) A realistic large-scale model of the cerebellum granular layer predicts circuit spatio-temporal filtering properties. Frontiers in Cellular Neuroscience ([link](http://www.frontiersin.org/Cellular_Neuroscience/10.3389/fncel.2010.00012/abstract)) gives an overview of the network. There were improvements made to the model in 2011 and it was translated to Python Neuron for parallel simulation on cluster. Added gap junctions, more realistic inputs. Python eased improvements to the model.

  - Sergio Solinas

* - 15:00
  - **Large scale cortical models for studying LFPs ([PPT](https://docs.neuroml.org/_static/NeuroML2012/RTomsett_LargeScaleCorticalModel.ppt))**

    Richard presented his work on developing large scale cortical models for studying Local Field Potentials. What network properties cause pathological dynamics? Much data comes from electrodes in vitro. Gaute Einevol's work looks at how dendritic structure affects the field potentials in a network (Linden et al Neuron 2010). Richard focused on Bush and Sejnowski J Neurosci Methods 1993 method to reduce model and see what the LFP looks like (and compared to Linden data). Then since it looked pretty good he created a network of these reduced models for simulation and analysis. Then looked at results from Utah array in Matlab. Next he'll add Gaussian connectivity and some patches and long range connections.

  - Richard Tomsett


* - 15:15
  - **Coffee**
  -

* - 15:30
  - **Break out sessions**

    - Channel and synapse specifications
    - Proposed structure for abstract neuron model hierarchy

  -

* - 17:30
  - **Reconvene and presentated discussions*
  -

* - 18:00
  - **Close**
  -
```
