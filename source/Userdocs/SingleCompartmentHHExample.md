(userdocs:getting_started:single_comparment_example)=
# Simulating a single compartment Hodgkin-Huxley neuron

In this section we will model and simulate a Hodgkin-Huxley neuron ({cite}`Hodgkin1952`).
A Hodgkin-Huxley neuron includes Sodium (Na), Potassium (K), and leak ion channels.
For more information on this neuron model, please see [this tutorial](https://hodgkin-huxley-tutorial.readthedocs.io/en/latest/index.html).


```{figure} ../Userdocs/NML2_examples/HH_single_compartment_example_sim-v.png
:alt: Membrane potential for neuron recorded from the simulation
:align: center

Membrane potential of the simulated regular spiking Izhikevich neuron.
```
This plot, saved as `example-single-izhikevich2007cell-sim-v.png`, is generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
