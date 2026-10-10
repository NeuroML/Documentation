(userdocs:optimising)=
# Optimising/fitting NeuroML Models

{ref}`pyNeuroML <pyNeuroML>` includes the [NeuroMLTuner](https://pyneuroml.readthedocs.io/en/development/pyneuroml.tune.html#module-pyneuroml.tune.NeuroMLTuner) module for the tuning and optimisation of NeuroML models against provided data.
This uses the [Neurotune](https://github.com/NeuralEnsemble/neurotune/) Python package for the fitting of models using evolutionary computation.

This page will walk through an example model optimisation.

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/fitted_izhikevich_sim-exp-v.png
:alt: Membrane potential from example experimental data.

Membrane potential from the experimental data.
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/fitted_izhikevich_output.png
:alt: Membrane potential obtained from example fitted model.

Membrane potential obtained from the model with highest fitness.
```

</center>

</div>
</div>
</div>

The Python script used to run the optimisation and generate the graphs is given below.
This can be adapted for other optimisations.
```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
----
```
(userdocs:optimising:data)=
## Loading data and calculating metrics to use for optimisation

The first step in the optimisation of the model is to obtain the data that the model is to be fitted against.
In this example, we will use the data set of CA1 pyramidal cell recordings using an intact whole hippocampus preparation, including recordings of rebound firing {cite}`ferguson_2015_17794`.
The data set is provided in the [Neurodata Without Borders](https://nwb.org) (NWB) format.
It can can be downloaded [here on the Open Source Brain repository](https://github.com/OpenSourceBrain/NWBShowcase/tree/master/FergusonEtAl2015), and can also be viewed on the [NWB Explorer](https://nwbexplorer.opensourcebrain.org) web application:

```{figure} ./NML2_examples/fitted_izhikevich_screenshot_nwbexplorer.png
:alt: Screenshot showing two recordings from FergusonEtAl2015_PYR3.nwb in NWB Explorer.

Screenshot showing two recordings from FergusonEtAl2015_PYR3.nwb in NWB Explorer.
```

For this example, we will use the [FergusonEtAl2015_PYR3.nwb](https://github.com/OpenSourceBrain/NWBShowcase/blob/master/FergusonEtAl2015/FergusonEtAl2015_PYR3.nwb) data file.
We use the [PyNWB](https://pynwb.readthedocs.io/en/stable/) package to read it, and then pass the loaded data to our `get_data_metrics` function to extract the metrics we want to use for model fitting.

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 417-420
----
```

Similar to {ref}`libNeuroML <libneuroml>`, PyNWB provides a Python object model to interact with NWB files.
You can learn more on using PyNWB in its [documentation](https://pynwb.readthedocs.io/en/stable/).

Here, the data file includes recordings from multiple (33 in total) current clamp experiments that are numbered from 1 through 33.
We iterate over each recording individually to extract the membrane potential values and store them in `data_v`.
For each, we also calculate the time stamps for the recordings from the provided sampling rate.
We pass this information to the `simple_network_analysis` function provided by the [PyElectro](https://github.com/NeuralEnsemble/pyelectro) Python package to calculate features (metrics) that we will use for fitting a neuron model.

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 33-71
----
```

The features calculated by PyElectro for each recording, which we store in `analysis_results`, can be seen below:
```{literalinclude} ./NML2_examples/fitted_izhikevich_pyelectro_analysis_results.txt
----
language: console
----
```
We now have the following information:

- `analysis_results`: the results of the analysis by PyElectro; we need these to set the target values for our fitting
- `currents`: the value of stimulation current for each sweep we've chosen; we need this for our models
- `memb_vals`: the time series of the membrane potentials and recordings times; we'll use this to plot the membrane potentials later to compare our fitted model against

(userdocs:optimising:running)=
## Running the optimisation

To run the optimisation, we want to choose which of the 33 time series we want to fit our model against.
Ideally, we would want to fit our model to all of them.
Here, however, for simplicity and to keep the computation time in check, we only pick two of the 33 sweeps.
(As an exercise, you can change the list to see how that affects your fitting.)

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 425-426
----
```

The Neurotune optimiser uses the evolutionary computation method provided by the [Inspyred](https://github.com/aarongarrett/inspyred/) package.
In short:

- the evolutionary algorithm starts with a population of models, each with a random value for a set of parameters constrained by a max/min value we have supplied
- it then calculates a fitness value for each model by comparing the features generated by the model to the target features that we provide
- in each generation, it finds the fittest models (parents)
- it mutates these to generate the next generation of models (offspring)
- it replaces the least fit models with fittest of the new individuals

The idea is that by calculating the fittest parents and offspring, it will find the candidate models that fit the provided target data best.
You can read more about evolutionary computation online (e.g. [Wikipedia](https://en.wikipedia.org/wiki/Evolutionary_algorithm)).
More information on model fitting in computational neuroscience can also be found in the literature.
For example, see this review {cite}`Rossant2011,Prinz2004`.

Here, we follow the following steps:

- we set up a template NeuroML model that will be passed to the optimiser
- we list the parameters we want to fit, and provide the extents of their state spaces
- we list the target features that the optimiser will use to calculate fitness, and set their weights
- finally, we use the `run_optimisation` function to run the optimisation

The `tune_izh_model` function shown below is the main workhorse function that does our fitting:
```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 74-254
----
```

Let us walk through the different sections of this function.

(userdocs:optimising:running:template)=
### Writing a template model

In this example, we want to fit the parameters of an {ref}`Izhikevich cell <schema:izhikevich2007cell>` to our data such that simulating the cell then gives us membrane potentials similar to those observed in the experiment.
Following the {ref}`Izhikevich network example <userdocs:getting_started:single_example>`, we set up a template network with one Izhikevich cell for each experimental recording that we want to fit.
For each of these cells, we provide a current stimulus matching the current used in the current clamp experiments that we obtained our recordings from:
```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 89-143
----
```
The resultant network template model for our two chosen recordings is shown below:

```{literalinclude} ./NML2_examples/TuneIzhFergusonPyr3.net.nml
----
language: xml
----
```
Please note that the initial parameters of the Izhikevich Cell do not matter here because the optimiser will modify these to run the candidate simulations.

(userdocs:optimising:running:params)=
### Setting up the optimisation parameters

The next step is to set the features/metrics that we want to fit:

The `parameters` dictionary contains the specifications of the parameters that we wish to fit, along with their minimum and maximum permitted values.

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 155-167
----
```
The format of the parameter specification is: `ComponentType:ComponentID/VariableName[:VariableID]/Units`.
So, for example, to fit the Capacitance of the Izhikevich cell, our parameter specification string is: `izhikevich2007Cell:Izh2007/C/pF`.

All NeuroML {ref}`Cell <schema:cells_>` and {ref}`Channel <schema:channels_>` ComponentTypes can be fitted using the `NeuroMLTuner`.

Next, we specify the target data that we want to fit against.

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 169-213
----
```

As we have set up a cell for each recording that we want to fit to, we must also set the target value for each cell.
We pick four features from a subset of features that PyElectro provided us with:

- `mean_spike_frequency`
- `average_last_1percent`
- `average_maximum`
- `average_minimum`

The last two can only be calculated for membrane potential data that includes spikes.
Since a few of the experimental recordings to not show any spikes, these two metrics will not be calculated for them.
So, we only add them for the corresponding cell only if they are present in the features for the chosen recording.

The format for the `target_data` is similar to that of the `parameters`.
The keys of the `target_data` dictionary are the specifications for the metrics.
The format for these is: `path/to/variable:pyelectro metric`.
You can learn more about constructing paths in NeuroML {ref}`here <userdocs:paths>`.
The value for the each key is the corresponding metric that was calculated for us by PyElectro (in `analysis_results`).
The for loop will set the `target_data` to this (printed by pyNeuroML when we run the script):

```{code-block} python
target_data =  {
  'Pop0[0]/v:mean_spike_frequency': 7.033585370142431,
  'Pop0[0]/v:average_last_1percent': -60.84635798136393,
  'Pop0[0]/v:average_maximum': 58.73414,
  'Pop0[0]/v:average_minimum': -43.800358,
  'Pop0[1]/v:mean_spike_frequency': 10.8837614279495,
  'Pop0[1]/v:average_last_1percent': -60.380863189697266,
  'Pop0[1]/v:average_maximum': 54.52382,
  'Pop0[1]/v:average_minimum': -39.78882
}
```

Similarly, we also set up the weights for each target metric in the `weights` variable:
```{code-block} python
weights = {
 'Pop0[0]/v:mean_spike_frequency': 1,
 'Pop0[0]/v:average_last_1percent': 1,
 'Pop0[0]/v: average_maximum': 1,
 'Pop0[0]/v:average_minimum': 1,
 'Pop0[1]/v:mean_spike_frequency': 1,
 'Pop0[1]/v:average_last_1percent': 1,
 'Pop0[1]/v:average_maximum': 1,
 'Pop0[1]/v:average_minimum': 1
 }
```
For simplicity, we set the weights for all as `1` here.

(userdocs:optimising:running:call)=
### Calling the optimisation function

The last step is to call our `run_optimisation` function with the various parameters that we have set up.
Here, for simplicity, we use the `jNeuroML` simulator.
For multi-compartmental models, however, we will need to use the `jNeuroML_NEURON` simulator (since `jNeuroML` only supports single compartment simulations).
A number of arguments to the function are specific to evolutionary computation, and their discussion is beyond the scope of this tutorial.
```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 215-254
----
```

The `run_optimisation` function will print out the optimisation report, and also return it so that it can be stored in a variable for further use.
The terminal output is shown below:

```{code-block} console

Ran 500 evaluations (pop: 100) in 582.205449 seconds (9.703424 mins total; 1.164411s per eval)

---------- Best candidate ------------------------------------------
{   'Pop0[0]/v:average_last_1percent': -59.276969863333285,
    'Pop0[0]/v:average_maximum': 47.35760225,
    'Pop0[0]/v:average_minimum': -53.95061271428572,
    'Pop0[0]/v:first_spike_time': 170.1,
    'Pop0[0]/v:interspike_time_covar': 0.1330373936860586,
    'Pop0[0]/v:max_interspike_time': 190.57499999999982,
    'Pop0[0]/v:max_peak_no': 8,
    'Pop0[0]/v:maximum': 47.427714,
    'Pop0[0]/v:mean_spike_frequency': 6.957040276293886,
    'Pop0[0]/v:min_interspike_time': 135.25000000000003,
    'Pop0[0]/v:min_peak_no': 7,
    'Pop0[0]/v:minimum': -68.13577,
    'Pop0[0]/v:peak_decay_exponent': 0.0003379360943630205,
    'Pop0[0]/v:peak_linear_gradient': -3.270149536895308e-05,
    'Pop0[0]/v:spike_broadening': 0.982357731987536,
    'Pop0[0]/v:spike_frequency_adaptation': -0.016935379943933133,
    'Pop0[0]/v:spike_width_adaptation': 0.011971808793771004,
    'Pop0[0]/v:trough_decay_exponent': -0.0008421760726029059,
    'Pop0[0]/v:trough_phase_adaptation': -0.014231837120099502,
    'Pop0[1]/v:average_last_1percent': -59.28251401166662,
    'Pop0[1]/v:average_maximum': 47.242452454545464,
    'Pop0[1]/v:average_minimum': -48.287914,
    'Pop0[1]/v:first_spike_time': 146.7,
    'Pop0[1]/v:interspike_time_covar': 0.01075626702836981,
    'Pop0[1]/v:max_interspike_time': 91.67499999999998,
    'Pop0[1]/v:max_peak_no': 11,
    'Pop0[1]/v:maximum': 47.423363,
    'Pop0[1]/v:mean_spike_frequency': 10.973033769511423,
    'Pop0[1]/v:min_interspike_time': 88.20000000000002,
    'Pop0[1]/v:min_peak_no': 10,
    'Pop0[1]/v:minimum': -62.58064000000001,
    'Pop0[1]/v:peak_decay_exponent': 0.0008036004162568405,
    'Pop0[1]/v:peak_linear_gradient': -0.00012436953066659044,
    'Pop0[1]/v:spike_broadening': 0.9877761288704633,
    'Pop0[1]/v:spike_frequency_adaptation': 0.0064956079899488595,
    'Pop0[1]/v:spike_width_adaptation': 0.008982392557695507,
    'Pop0[1]/v:trough_decay_exponent': -0.004658690933014975,
    'Pop0[1]/v:trough_phase_adaptation': 0.009514671770845617}

TARGETS:
{   'Pop0[0]/v:average_last_1percent': -60.84635798136393,
    'Pop0[0]/v:average_maximum': 58.73414,
    'Pop0[0]/v:average_minimum': -43.800358,
    'Pop0[0]/v:mean_spike_frequency': 7.033585370142431,
    'Pop0[1]/v:average_last_1percent': -60.380863189697266,
    'Pop0[1]/v:average_maximum': 54.52382,
    'Pop0[1]/v:average_minimum': -39.78882,
    'Pop0[1]/v:mean_spike_frequency': 10.8837614279495}

TUNED VALUES:
{   'Pop0[0]/v:average_last_1percent': -59.276969863333285,
    'Pop0[0]/v:average_maximum': 47.35760225,
    'Pop0[0]/v:average_minimum': -53.95061271428572,
    'Pop0[0]/v:mean_spike_frequency': 6.957040276293886,
    'Pop0[1]/v:average_last_1percent': -59.28251401166662,
    'Pop0[1]/v:average_maximum': 47.242452454545464,
    'Pop0[1]/v:average_minimum': -48.287914,
    'Pop0[1]/v:mean_spike_frequency': 10.973033769511423}

FITNESS: 0.003633

FITTEST: {   'izhikevich2007Cell:Izh2007/C/pF': 240.6982897890555,
    'izhikevich2007Cell:Izh2007/a/per_ms': 0.03863507615280202,
    'izhikevich2007Cell:Izh2007/b/nS': 2.0112449831346746,
    'izhikevich2007Cell:Izh2007/c/mV': -43.069939785498356,
    'izhikevich2007Cell:Izh2007/d/pA': 212.50982499591083,
    'izhikevich2007Cell:Izh2007/k/nS_per_mV': 0.24113869560362797,
    'izhikevich2007Cell:Izh2007/vpeak/mV': 47.44063356996336,
    'izhikevich2007Cell:Izh2007/vr/mV': -59.283747806929135,
    'izhikevich2007Cell:Izh2007/vt/mV': -48.9131459978619}

```

It will also generate a number of plots (shown below):

- showing the evolution of the parameters being fitted, with indications of the fitness value: larger circles mean more fitness
- the change in the overall fitness value as the population evolves
- distributions of the values of the parameters being fitted, with indications of the fitness value: darker lines mean higher fitness

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

(userdocs:optimising:results)=
## Viewing results

The tuner also generates a plot with the membrane potential of a cell using the fitted parameter values (shown on the top of the page).
Here, to document how the fitted parameters are to be extracted from the output of the `run_optimisation` function, we also construct a model to use the fitted parameters ourselves and plot the membrane potential to compare it against the experimental data.

(userdocs:optimising:results:run_model)=
### Extracting results and running a fitted model

This is done in the `run_fitted_cell_simulation` function:

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 257-354
----
```

First, we extract the fitted parameters from the dictionary returned by the `run_optimisation` function.
Then, we use these parameters to set up a simple NeuroML network and run a test simulation, recording the values of membrane potentials generated by the cells.
Please note that the current stimulus to the cells in this test model must also match the values that were used in the experiment, and so also in the fitting.

(userdocs:optimising:results:plotting)=
### Plotting model generated and experimentally recorded membrane potentials

Finally, in the `plot_sim_data` function, we plot the membrane potentials from our fitted cells and the experimental data to see visually inspect the results of our fitting:

```{literalinclude} ./NML2_examples/tune-izhikevich.py
----
language: python
lines: 356-409
----
```

This generates the following figures:

<div class="container-fluid">
<div class="row my-2 py-2">
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/fitted_izhikevich_sim-exp-v.png
:alt: Membrane potential from example experimental data.

Membrane potential from the experimental data.
```
</center>

</div>
<div class="col-sm-6 px-2">
<center>

```{figure} ./NML2_examples/fitted_izhikevich_output.png
:alt: Membrane potential obtained from example fitted model.

Membrane potential obtained from the model with highest fitness.
```

</center>

</div>
</div>
</div>


We can clearly see the similarity between our fitted model and the experimental data.
A number of tweaks can be made to improve the fitting.
For example, pyNeuroML also provides a two staged optimisation function: [run_2stage_optimisation](https://pyneuroml.readthedocs.io/en/development/pyneuroml.tune.html#pyneuroml.tune.NeuroMLTuner.run_2stage_optimization) that allows users to optimise sets of parameters in two different stages.
The graphs also show ranges of parameters that provide fits, so users can also hand-tune their models further as required.
