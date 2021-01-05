# Simulating a regular spiking Izhikevich neuron

In this section, we wish to simulate a single regular spiking Izhikevich neuron and record its membrane potential (as shown in the figure below):

```{figure} ../Userdocs/NML2_examples/example-single-izhikevich2007cell-sim-v.png
:alt: Membrane potential for neuron recorded from the simulation
:align: center

Membrane potential of the simulated regular spiking Izhikevich neuron.
```
This plot, saved as `example-single-izhikevich2007cell-sim-v.png`, can be generated using the following Python NeuroML script:
```{literalinclude} ./NML2_examples/izhikevich-single-neuron.py
----
language: python
----
```
