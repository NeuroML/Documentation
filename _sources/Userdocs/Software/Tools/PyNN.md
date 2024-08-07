(userdocs:pynn)=
# PyNN and NeuroML

![PyNN logo](../../../images/tools/pynn.png)


[PyNN](http://neuralensemble.org/PyNN/) is a Python package for simulator independent specification of neuronal network models. Model code can be developed using the PyNN API and then run using [NEURON](http://www.neuron.yale.edu/neuron/), [NEST](https://nest-simulator.org/) or [Brian](https://briansimulator.org/). The developed model also can be stored as a NeuroML document.

The latest version of {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>` can be used to generate executable scripts for PyNN based simulators based on NeuroML components, although the majority of multicompartmental conductance based models which are available in neuroConstruct are outside the current scope of the PyNN API.

See [https://github.com/OpenSourceBrain/PyNNShowcase](https://github.com/OpenSourceBrain/PyNNShowcase) for examples of usage of NeuroML and PyNN.

More info on the latest support for running NeuroML models in PyNN and vice versa can be found [here](https://github.com/NeuroML/NeuroML2/issues/73).

PyNN is also a key target for cross simulator network creation using {ref}`NeuroMLlite <neuromllite>`.
