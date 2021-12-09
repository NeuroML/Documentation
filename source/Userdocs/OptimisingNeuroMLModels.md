(userdocs:optimising)=
# Optimising/Fitting NeuroML Models

{ref}`pyNeuroML <pyNeuroML>` includes the `NeuroMLTuner` module for the tuning and optimisation of NeuroML models against provided data.
This uses the [PyElectro](https://github.com/NeuralEnsemble/pyelectro) Python package for the extraction of features to be used in tuning, along with the [NeuroTune](https://github.com/NeuralEnsemble/neurotune/) Python package for the fitting of models using a genetic algorithm.

This page will walk through an example model optimisation.
Note that the goal here is not to obtain a well fitted model.
Instead, it is to demonstrate how this is to be done using the available tools.
```{admonition} Work in progress
:class: note
This page is a work in progress. Please see https://github.com/NeuroML/Documentation/issues/106
```

```{admonition} Validate NeuroML 2 files before using them.
:class: tip
It is good practice to {ref}`validate NeuroML 2 files <userdocs:validating_models>` to check them for correctness before optimising/fitting them.
```

```{figure} ./NML2_examples/fitted_izhikevich_scatter.png
:alt: Evolution of parameters.

The figure shows the values of various parameters throughout the evolution, with larger circles having higher values of fitness.
```
```{figure} ./NML2_examples/fitted_izhikevich_fitness.png
:alt: Evolution of fitness.

The figure shows the trend of the fitness throughout the evolution.
```
```{figure} ./NML2_examples/fitted_izhikevich_hist.png
:alt: Histograms of values of fitting parameters.

The figure shows the distribution of values that for each parameter throughout the evolution. Darker lines have higher fitness values.
```

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/fitted_izhikevich_output.png
:alt: Membrane potential obtained from example fitted model.

The figure shows the membrane potential obtained from the model with highest fitness.
```

</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/fitted_izhikevich_sim-exp-v.png
:alt: Membrane potential from example experimental data.

Membrane potential from the experimental data.
```
</center>

</div>
</div>
</div>

The Python script used to run the optimisation and generate the graphs is given below.
```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
----
```
(userdocs:optimising:data)=
## Loading data and metrics to use for optimisation

The first step in the optimisation of the model is to obtain the data that the model is to be fitted against.
In this example, we will use the data set of CA1 pyramidal cell recordings using an intact whole hippocampus preparation, including recordings of rebound firing {cite}`ferguson_2015_17794`.
This data set can be viewed [here on the Open Source Brain repository](https://github.com/OpenSourceBrain/NWBShowcase/tree/master/FergusonEtAl2015), and can also be viewed on the [NWB Explorer](https://nwbexplorer.opensourcebrain.org) platform.
For this example, we will use [FergusonEtAl2015_PYR3.nwb](https://github.com/OpenSourceBrain/NWBShowcase/blob/master/FergusonEtAl2015/FergusonEtAl2015_PYR3.nwb).


The data is provided in the [Neurodata Without Borders](https://nwb.org) (NWB) format.
We use the [PyNWB](https://pynwb.readthedocs.io/en/stable/) package to read it, and then pass the loaded data to our `get_data_metrics` function to extract the metrics we want to use for model fitting.

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 233-236
----
```

Similar to {ref}`libNeuroML <libneuroml>`, PyNWB also provides a Python object model to interact with NWB files.
You can learn more about this in the PyNWB documentation.

Here, the data file includes recordings from multiple (33 in total) current clamp experiments.
So, we iterate over each individually to extract the recorded membrane potential values in `data_v`.
For each, we also calculate the time stamps for the recordings from the provided sampling rate
We pass this information to the `simple_network_analysis` function provided by PyElectro to calculate some metrics that we can use for fitting a neuron model.

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 27-54
----
```

(userdocs:optimising:running)=
## Running the optimisation
