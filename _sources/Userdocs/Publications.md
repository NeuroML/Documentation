(citing)=
# Citing NeuroML and related publications

This page documents how one can cite NeuroML in their work, and lists publications associated with the NeuroML initiative.

## Citing NeuroML

Please cite NeuroML in your work whenever you have used it.
Generally, you should cite the particular paper while discussing NeuroML in the text, and also note and cite the specific version of the NeuroML tool that has been used in the work.

### Papers

Please cite the following papers as required:

(papers:neuroml2)=
#### NeuroML 2 and LEMS
```{admonition} The main citation for NeuroML 2
:class: tip
Please cite the following paper when discussing NeuroML v2.0 or LEMS.
```

**Cannon RC, Gleeson P, Crook S, Ganapathy G, Marin B, Piasini E and Silver RA (2014)**
<a  href="http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00079/abstract">LEMS: A language for expressing complex biological models
    in concise and hierarchical form and its use in underpinning NeuroML 2</a>,
<em>Frontiers in Neuroinformatics</em> 8: 79.

```{code-block} bibtex

@Article{Cannon2014,
  author    = {Robert C. Cannon and Padraig Gleeson and Sharon Crook and Gautham Ganapathy and Boris Marin and Eugenio Piasini and R. Angus Silver},
  title     = {{LEMS}: a language for expressing complex biological models in concise and hierarchical form and its use in underpinning {NeuroML} 2},
  doi       = {10.3389/fninf.2014.00079},
  volume    = {8},
  journal   = {Frontiers in Neuroinformatics},
  publisher = {Frontiers Media {SA}},
  year      = {2014},
}
```

(papers:libneuroml)=
#### libNeuroML and PyLEMS
```{admonition} Citation for Python & NeuroML
:class: tip
Please cite the following paper when using the Python NeuroML libraries
```
**Vella M, Cannon RC, Crook S, Davison AP, Ganapathy G, Robinson HP, Silver RA and Gleeson P (2014)**
<a  href="http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00038/abstract">libNeuroML and PyLEMS: using Python to combine procedural and declarative
    modeling approaches in computational neuroscience.</a>
<em>Frontiers in Neuroinformatics</em> 8: 38.

```{code-block} bibtex
@Article{Vella2014,
  author       = {Vella, Michael and Cannon, Robert C. and Crook, Sharon and Davison, Andrew P. and Ganapathy, Gautham and Robinson, Hugh P. C. and Silver, R. Angus and Gleeson, Padraig},
  title        = {libNeuroML and PyLEMS: using Python to combine procedural and declarative modeling approaches in computational neuroscience.},
  doi          = {10.3389/fninf.2014.00038},
  pages        = {38},
  volume       = {8},
  journal      = {Frontiers in neuroinformatics},
  year         = {2014},
}
```


(papers:neuroml1)=
#### NeuroML v1
```{admonition} Citation for NeuroML v1
:class: tip
Please cite the following paper when discussing NeuroML version 1. (deprecated)
```
**Gleeson, P., S. Crook, R. C. Cannon, M. L. Hines, G. O. Billings, et al. (2010)**
<a  href="http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1000815">NeuroML: A Language for Describing Data Driven
  Models of Neurons and Networks with a High Degree of Biological Detail.</a>
<em>PLoS Computational Biology</em> 6(6): e1000815.

```{code-block} bibtex
@Article{Gleeson2010,
  author    = {Padraig Gleeson and Sharon Crook and Robert C. Cannon and Michael L. Hines and Guy O. Billings and Matteo Farinella and Thomas M. Morse and Andrew P. Davison and Subhasis Ray and Upinder S. Bhalla and Simon R. Barnes and Yoana D. Dimitrova and R. Angus Silver},
  title     = {{NeuroML}: A Language for Describing Data Driven Models of Neurons and Networks with a High Degree of Biological Detail},
  doi       = {10.1371/journal.pcbi.1000815},
  editor    = {Karl J. Friston},
  number    = {6},
  pages     = {e1000815},
  volume    = {6},
  journal   = {{PLoS} Computational Biology},
  publisher = {Public Library of Science ({PLoS})},
  year      = {2010},
}
```

(papers:osb)=
#### Open Source Brain

This paper describes version 1 of the [Open Source Brain](https://www.opensourcebrain.org) platform. Please cite this paper if you have made use of OSB in your work:

**Gleeson P, Cantarelli M, Marin B, Quintana A, Earnshaw M, et al. (2019)**
<a  href="https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1">Open Source Brain: a collaborative resource for visualizing, analyzing, simulating and developing standardized models of neurons and circuits.</a> <em>Neuron</em> 103 (3):395–411

```{code-block} bibtex
@Article{Gleeson2019,
  author    = {Padraig Gleeson and Matteo Cantarelli and Boris Marin and Adrian Quintana and Matt Earnshaw and Sadra Sadeh and Eugenio Piasini and Justas Birgiolas and Robert C. Cannon and N. Alex Cayco-Gajic and Sharon Crook and Andrew P. Davison and Salvador Dura-Bernal and Andr{\'{a}}s Ecker and Michael L. Hines and Giovanni Idili and Frederic Lanore and Stephen D. Larson and William W. Lytton and Amitava Majumdar and Robert A. McDougal and Subhashini Sivagnanam and Sergio Solinas and Rokas Stanislovas and Sacha J. van Albada and Werner van Geit and R. Angus Silver},
  title     = {Open Source Brain: A Collaborative Resource for Visualizing, Analyzing, Simulating, and Developing Standardized Models of Neurons and Circuits},
  doi       = {10.1016/j.neuron.2019.05.019},
  number    = {3},
  pages     = {395--411},
  volume    = {103},
  journal   = {Neuron},
  publisher = {Elsevier {BV}},
  year      = {2019},
}
```
### Software

It is important to cite software used in scientific work to:

- aid reproducibility of work
- to ensure that the developers of tools receive credit for their work.

You can learn more about Software Citation Principles as set out by the [F1000 Software Citation working group](https://www.force11.org/group/software-citation-working-group) in [this work](https://peerj.com/articles/cs-86/) {cite}`Smith2016`.

You can obtain the version of {ref}`pyNeuroML <pyneuroml>` and associated tools using the following command (with example output):

```{code-block} console
$ pynml -version
pyNeuroML v0.5.20 (libNeuroML v0.3.1, jNeuroML v0.11.1)
```

Each NeuroML software tool has a unique DOI and reference associated with each release at the [Zenodo archival facility](https://zenodo.org/search?page=1&size=20&q=neuroml).
On each entry, you will be able to find the DOI and citation of the particular version you are using, and you will also be able to download the citation in different formats at the bottom of the right hand side bar.

## Other publications

This section lists other publications related to NeuroML.

**G&uuml;nay, C. et al. (2008)** <a href="http://springerlink.com/content/2177143636k14816/"> Computational intelligence in electrophysiology: Trends and open problems</a>.
In Smolinski, Milanova and Hassanien, eds. <em>Applications of Computational Intelligence
    in Biology</em>. Springer, Berlin/Heidelberg.

**Gleeson, P., V. Steuber, and R. A. Silver (2007)**
<a  href="http://www.ncbi.nlm.nih.gov/pubmed/17442244">neuroConstruct: A Tool for Modeling Networks of Neurons in 3D Space</a>. <em>Neuron.</em> 54(2):219-235.

**Cannon R. C., M. O. Gewaltig, P. Gleeson, U. S. Bhalla, H. Cornelis, M. L. Hines, F. W. Howell, E. Muller, J. R. Stiles, S. Wils, E. De Schutter (2007)**
  <a  href="http://www.ncbi.nlm.nih.gov/pubmed/17873374">Interoperability of Neuroscience Modeling Software: Current Status and Future Directions.</a>
  <em>Neuroinformatics</em> Volume 5, 127-138.


**Crook, S., P. Gleeson, F. Howell, J. Svitak and R.A. Silver (2007)**
<a href="http://www.ncbi.nlm.nih.gov/pubmed/17873371">MorphML: Level 1 of the NeuroML
  standards for neuronal morphology data and model specification.</a> <em>Neuroinformatics. </em> 5(2):96-104.


**Crook, S. and F. Howell (2007)**
<a href="http://www.amazon.com/Neuroinformatics-Methods-Molecular-Biology-Koslow/dp/1588297209">XML for data representation and model
specification in neuroscience.</a> In <em>Methods in Molecular Biology Book Series: Neuroinformatics</em>. ed. C. Crasto,
Humana Press.</p>

**Crook, S., D. Beeman, P. Gleeson and F. Howell (2005)** <a href="http://www.brains-minds-media.org/archive/228"> XML for model specification in neuroscience: An introduction and workshop summary. </a> <em>Brains, Minds, and Media.</em>  1:bmm228 (urn:nbn:de:0009-3-2282).</p>

**Qi, W. and S. Crook (2004)**
<a href="https://www.sciencedirect.com/science/article/pii/S0925231204001766">
Tools for neuroinformatic data exchange: An XML
application for neuronal morphology data.</a> <em>Neurocomputing.</em>
58-60C:1091-1095.</p>

**Goddard, N., M. Hucka, F. Howell, H. Cornelis, K. Shankar and D. Beeman (2001)**
 <a href="http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=1088511">Towards NeuroML: Model
description methods for collaborative modeling
in neuroscience</a>. <em>Philosophical Transactions of the Royal Society B</em>. 356:1209-1228.</p>

### Book Chapters
**Crook, SM, HE Plesser, AP Davison (2013)**
Lessons from the past: approaches for reproducibility in computational neuroscience.
In <em>JM Bower</em>, ed. 20 Years of Computational Neuroscience, Springer

**Gleeson, P, V Steuber, RA Silver and S Crook (2012)**
NeuroML. In <em>Le Novere</em>, ed. Computational Systems Biology, Springer.



### Abstracts
**Cannon, R, P Gleeson, S Crook, RA Silver (2012)** <a href="http://www.biomedcentral.com/1471-2202/13/S1/P42">A declarative model specification system allowing NeuroML to be extended with user-defined component types</a>. <em>BMC Neuroscience</em>. 13(Suppl 1): P42.
</p>

**Gleeson P, S Crook, A Silver, R Cannon (2011)**
 <a href="http://www.biomedcentral.com/1471-2202/12/S1/P29">Development of NeuroML version 2.0: Greater extensibility, support for abstract neuronal models and interaction with Systems Biology languages</a>. <em>BMC Neuroscience</em>. 12:P29.

**Gleeson, P., S. Crook, S. Barnes and R.A. Silver (2008)**
<a href="http://frontiersin.org/conferences/individual_abstract_listing.php?conferid=2&pap=491&ind_abs=1&pg=5">
Interoperable model components for biologically
realistic single neuron and network models implemented in NeuroML.</a>
<em>Frontiers in Neuroinformatics. Conference Abstract: Neuroinformatics 2008.</em> doi: 10.3389/conf.neuro.11.2008.01.135.

**Larson, S. and M. Martone (2008)**
 <a href="http://frontiersin.org/conferences/individual_abstract_listing.php?conferid=2&pap=490&ind_abs=1">
A spatial framework for multi-scale
computational neuroanatomy.</a> <em>Frontiers in Neuroinformatics. Conference Abstract: Neuroinformatics 2008.</em> doi: 10.3389/conf.neuro.11.2008.01.134.

**Crook, S., P. Gleeson and R.A. Silver (2007)**
NetworkML: Level 3 of the NeuroML standards for multiscale model specification and
exchange. <em>Society for Neuroscience Abstracts.</em> 102.28.

**Gleeson, P., S. Crook, V. Steuber and R.A. Silver (2007)**
  <a href="http://www.biomedcentral.com/1471-2202/8/S2/P1">
      Using NeuroML and neuroConstruct to build neuronal network models for multiple
      simulators</a>. <em>BMC Neuroscience.</em> 8(2):P101.
