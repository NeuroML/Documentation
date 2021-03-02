(jlems)=
# jLEMS

Java Interpreter for the Low Entropy Model Specification language. See http://lems.github.com/LEMS for the LEMS specification.

```{admonition} jLEMS is the reference implementation of LEMS
jLEMS was developed by Robert Cannon when the LEMS language was being devised and serves at the key reference for how to implement/interpret the language.
```

## Quick start

Clone this repository:

    git clone git://github.com/LEMS/jLEMS.git

Install with Maven:

    cd jLEMS
    mvn install

Run an example:

    ./lems src/test/resources/example1.xml        (Linux/Mac)
    lems.bat src\test\resources\example1.xml      (Windows)

## Source

jLEMS is under development on GitHub at [https://github.com/LEMS/jLEMS](https://github.com/LEMS/jLEMS).

## Documentation

More information can be found [here](http://lems.github.io/LEMS/).

For more details on LEMS see:

Robert C. Cannon, Padraig Gleeson, Sharon Crook, Gautham Ganapathy, Boris Marin, Eugenio Piasini and R. Angus Silver,
**LEMS: A language for expressing complex biological models in concise and hierarchical form and its use in underpinning NeuroML 2**,
[Frontiers in Neuroinformatics 2014](http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00079/abstract), doi: 10.3389/fninf.2014.00079

## Issue tracker

To report any issues related to jLEMS, please open an issue [here](https://github.com/LEMS/jLEMS/issues).
