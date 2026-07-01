(userdocs:testing_validating_models)=
# Testing/validating NeuroML Models

Models described in NeuroML can be run across multiple simulators, and it it essential that the activity (e.g. spike times) of the models are as close as possible across all of these independently developed platforms.

It is also important to validate that the behaviour of a given NeuroML model reproduces some recorded aspect of the biological equivalent.  

(userdocs:testing_models)=
## Testing behaviour of NeuroML models across simulators

This type of testing addresses the question: **Does a given NeuroML model produce the same results when run across multiple simulators?**

(userdocs:testing_models:omv)=
### OMV - Open Source Brain Model Validation framework

The OSB Model Validation framework was originally developed as an automated model validation package for [Open Source Brain](http://www.opensourcebrain.org) projects, which can be used for testing model behaviour across many [simulation engines](https://github.com/OpenSourceBrain/osb-model-validation/tree/master/omv/engines) both:

- on your local machine when developing models
- on [GitHub Actions](https://github.com/features/actions), to ensure tests pass on every commit.

This framework has been used to test the 30+ NeuroML and PyNN models described in the [Open Source Brain paper (Gleeson et al. 2019)](https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1), and [many more](https://github.com/OpenSourceBrain/.github/blob/main/testsheet/README.md).

See https://github.com/OpenSourceBrain/osb-model-validation for more details.

(userdocs:validating_models_bio)=
## Validating that NeuroML model reproduce biological activity

This type of testing addresses the question: **How well does a given NeuroML model replicate the activity as seen in real neurons/channels/networks?**

### SciUnit/NeuronUnit

[SciUnit](https://scidash.org/sciunit.html) is a Python framework for test-driven validation of scientific models, and [NeuronUnit](https://scidash.org/neuronunit.html)
 is a package based on this for data-driven validation of neuron and ion channel models. See also [SciDash](https://scidash.org/) for more information.

Interactive Jupyter notebooks for running NeuronUnit examples can be found [this repository](https://github.com/scidash/neuronunit/tree/master/docs).

TODO: Add details on using [SciUnit](https://scidash.org/sciunit.html) and [NeuronUnit](https://scidash.org/neuronunit.html) with NeuroML models.
