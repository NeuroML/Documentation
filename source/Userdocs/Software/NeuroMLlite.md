# NeuroMLlite

NeuroMLlite is a common framework for reading/writing/generating network specifications which builds on NeuroML 2.

It is intended to provide a high level specification which can be used to generate networks in NeuroML
and many other formats, including graphical and directly in neuronal simulators

## Quick start

```
git clone https://github.com/NeuroML/NeuroMLlite.git
cd NeuroMLlite
python setup.py install
cd examples
python Example4.py                  # Generate the network in JSON
python Example4.py -nml             # Generate the network in NeuroML2
python Example4.py -jnml            # Generate the network in NeuroML2 & run using jNeuroML
python Example4.py -jnmlnetpyne     # Generate the network in NeuroML2 & run using NetPyNE
python Example4.py -jnmlnrn         # Generate the network in NeuroML2 & run using NEURON
python Example4.py -netpyne         # Generate & run the network directly in NetPyNE
python Example4.py -pynnnest        # Generate & run the network in NEST using PyNN
python Example4.py -pynnnrn         # Generate & run the network in NEURON using PyNN
python Example4.py -pynnbrian       # Generate & run the network in Brian using PyNN
...
```

## Source

NeuroMLlite is under development on GitHub at [https://github.com/NeuroML/NeuroMLlite](https://github.com/NeuroML/NeuroMLlite).

## Documentation

More information can be found [here](https://github.com/NeuroML/NeuroMLlite).

## Issue tracker

To report any issues related to NeuroMLlite, please open an issue [here](https://github.com/NeuroML/NeuroMLlite/issues).
