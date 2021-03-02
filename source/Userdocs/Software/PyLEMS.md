(pylems)=
# PyLEMS

An application written in Python which can serve as an API, as well as a simulator for
the [LEMS](http://lems.github.io/LEMS) language, and which can also be used to run NeuroML2
models (by including the LEMS core type definitions).


## Quick start

```
pip install pylems        # install using pip
pylems -h                 # get info on usage
pylems lemsexample.xml    # load and simulate a LEMS file

```

Note: to simulate a NeuroML file you must specify the location of the [NeuroML 2 LEMS definitions](https://github.com/NeuroML/NeuroML2/tree/master/NeuroML2CoreTypes) with the -I option, e.g.
```
pylems -I <dir of NeuroML2 install>/NeuroML2CoreTypes/  LEMS_NeuroML2_Model.xml
```

or alternatively simply use {ref}`pyNeuroML <pyNeuroML>`, which bundles these files.

## Source

PyLEMS is under development on GitHub at [https://github.com/LEMS/pylems](https://github.com/LEMS/pylems).

## Documentation

More information can be found [here](https://github.com/LEMS/pylems).

For more about PyLEMS see:

Michael Vella, Robert C. Cannon, Sharon Crook, Andrew P. Davison, Gautham Ganapathy, Hugh P. C. Robinson, R. Angus Silver and Padraig Gleeson,
**libNeuroML and PyLEMS: using Python to combine procedural and declarative modeling approaches in computational neuroscience**
[Frontiers in Neuroinformatics 2014](http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00038/abstract), doi: 10.3389/fninf.2014.00038

_**PLEASE CITE THE PAPER ABOVE IF YOU USE PYLEMS!**_

For more details on LEMS see:

Robert C. Cannon, Padraig Gleeson, Sharon Crook, Gautham Ganapathy, Boris Marin, Eugenio Piasini and R. Angus Silver,
**LEMS: A language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2**,
[Frontiers in Neuroinformatics 2014](http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00079/abstract), doi: 10.3389/fninf.2014.00079

## Issue tracker

To report any issues related to PyLEMS, please open an issue [here](https://github.com/LEMS/pylems/issues).
