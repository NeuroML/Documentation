# Adding OMV tests

Now that we have converted the cell models to NeuroML, we want to ensure that we get the same behaviour from the NeuroML converted cell model as from the original NEURON code.
For this, we have the [Open Source Model Validation (OMV) framework](https://github.com/OpenSourceBrain/osb-model-validation/).
The idea here is that we write simple test files that `omv` will run, and we provide data that `omv` can check against to see if the tests results are correct.

We will add OMV tests for the KC here.

## Step 1) Getting spike data from the NEURON model

For `omv` to test the model against, we need to generate some spike data that it knows to be the expected values.
The `test_kc.py` script already provides us with the spike data.
So, we can run the script and note down the spike times in a Model Emergent Properties (MEP) file:

```{code-block} yaml
system: Testing a detailed cell

experiments:
  stepKC:
    expected:
      spike times: [144.45000000000556, 177.64999999997536, 210.29999999994567, 242.74999999991616, 275.0499999998868, 307.19999999985754, 339.2249999998284, 371.07499999979945, 402.74999999977064, 434.1499999997421, 465.2249999997138, 495.87499999968594, 525.9749999997221, 555.3499999998289, 583.8499999999326]

# generated from test-kc.py
```

## Step 2) Adding tests
Next, we can write a OSB Model Test (OMT) file to test the model using the step current simulation we had written before:


```{code-block} yaml
target: LEMS_KC_step_test.xml
engine: jNeuroML_NEURON
mep: .test.kc.mep
experiments:
  stepKC:
    observables:
      spike times:
        file:
          path: KC_step_test.KC_pop.v.dat
          columns: [0,1]
          scaling: [1000,1000]
        spike detection:
          method: threshold
          threshold: -10.
        tolerance: 0.00
```


Note that we start with a tolerance of 0 here.
Let us run the test and see what we get:

```{code-block} console
$ omv test .test.kc.jnmlneuron.omt

[omv]
[omv] Running the tests defined in .test.kc.jnmlnrn.omt
[omv] =================================================
[omv]   Found 1 experiment(s) to run on engine: jNeuroML_NEURON
[omv] PATH: :/home/asinha/.local/share/virtualenvs/neuroml-311-dev/bin
[omv] Env vars: {'PYTHONPATH': '/home/asinha/local/lib/python/site-packages', 'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')}
[omv]   Running file ./LEMS_KC_step_test.xml with jNeuroML_NEURON, env: {'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')}
[omv]     Running the commands: [/usr/bin/jnml /home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/LEMS_KC_step_test.xml -neuron -nogui -run] in (/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; cwd=/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; shell=False; env={'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')})
[omv]     Commands: ['/usr/bin/jnml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/LEMS_KC_step_test.xml', '-neuron', '-nogui', '-run'] completed successfully
[omv]   Success with running jNeuroML_NEURON
[omv]   Running checks for experiment: stepKC
[omv]
[omv] Comparison of
                    (observed data): [143.95, 176.76, 209.23, 241.52, 273.66, 305.68, 337.57, 369.33, 400.94, 432.38, 463.62, 494.59999999999997, 525.28, 555.59, 585.45]
                    and
                    (expected data): [144.45000000000556, 177.64999999997536, 210.29999999994567, 242.74999999991616, 275.0499999998868, 307.19999999985754, 339.2249999998284, 371.07499999979945, 402.74999999977064, 434.1499999997421, 465.2249999997138, 495.87499999968594, 525.9749999997221, 555.3499999998289, 583.8499999999326]
                    failed against tolerance 0
[omv]   A better tolerance to try is: 0.005087969567027844
[omv]       Observable                        Test Passed
[omv]       --------------------------------------------------
[omv]       spike times                            ✘
[omv]       +++++++++++++++++++++ Error info ++++++++++++++++++
[omv]        Return code: 0
```

We see that there's a slight difference in the spike times we obtain from our implementation.
This is not unexpected.
Small variations in how the mod files are written, or how the morphology is set up can result in small variations in the spike times.
`omv` will suggest a tolerance value for us to use.
The smaller the tolerance, the better.

We update our file to use the suggested tolerance and re-run the test:

```{code-block} console
$ omv test .test.kc.jnmlnrn.omt
[omv]
[omv] Running the tests defined in .test.kc.jnmlnrn.omt
[omv] =================================================
[omv]   Found 1 experiment(s) to run on engine: jNeuroML_NEURON
[omv] PATH: :/home/asinha/.local/share/virtualenvs/neuroml-311-dev/bin
[omv] Env vars: {'PYTHONPATH': '/home/asinha/local/lib/python/site-packages', 'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')}
[omv]   Running file ./LEMS_KC_step_test.xml with jNeuroML_NEURON, env: {'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')}
[omv]     Running the commands: [/usr/bin/jnml /home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/LEMS_KC_step_test.xml -neuron -nogui -run] in (/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; cwd=/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; shell=False; env={'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')})
[omv]     Commands: ['/usr/bin/jnml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/LEMS_KC_step_test.xml', '-neuron', '-nogui', '-run'] completed successfully
[omv]   Success with running jNeuroML_NEURON
[omv]   Running checks for experiment: stepKC
[omv]
[omv]       Observable                        Test Passed
[omv]       --------------------------------------------------
[omv]       spike times                            ✔
[omv]
[omv]                   =================================
[omv]                   Test passed: .test.kc.jnmlnrn.omt
```

We can also add a simple validation test that will allow `omv` to validate the various NeuroML files in the repository:

```{code-block} yaml
target: "*.c*.nml"
engine: jNeuroML_validate
```

One can run all the OMV tests in a repository at once:

```{code-block} console
$ omv all
[omv] Python 3. Ignoring tests for non Py3 compatible engines: False
[omv]
[omv]
[omv] Running the tests defined in ./.test.kc.jnmlnrn.omt
[omv] ===================================================
[omv]   Found 1 experiment(s) to run on engine: jNeuroML_NEURON
[omv] PATH: :/home/asinha/.local/share/virtualenvs/neuroml-311-dev/bin
[omv] Env vars: {'PYTHONPATH': '/home/asinha/local/lib/python/site-packages', 'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')}
[omv]   Running file ./LEMS_KC_step_test.xml with jNeuroML_NEURON, env: {'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')}
[omv]     Running the commands: [/usr/bin/jnml /home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/LEMS_KC_step_test.xml -neuron -nogui -run] in (/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; cwd=/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; shell=False; env={'NEURON_HOME': '/home/asinha/.local/share/virtualenvs/neuroml-311-dev', 'JNML_HOME': PosixPath('/usr/bin')})
[omv]     Commands: ['/usr/bin/jnml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/LEMS_KC_step_test.xml', '-neuron', '-nogui', '-run'] completed successfully
[omv]   Success with running jNeuroML_NEURON
[omv]   Running checks for experiment: stepKC
[omv]
[omv]       Observable                        Test Passed
[omv]       --------------------------------------------------
[omv]       spike times                            ✔
[omv]
[omv]
[omv]       [ Test 1 of 2 complete - failed so far: 0 ]
[omv]
[omv]
[omv] Running the tests defined in ./.test.validate.omt
[omv] =================================================
[omv]   No mep file specified. Will only run simulation using: jNeuroML_validate
[omv]   Found 1 experiment(s) to run on engine: jNeuroML_validate
[omv]   Running with jNeuroML_validate, using: ['/usr/bin/jnml', '-validate', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/GGN.morph.cell.nml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/GGN.cell.nml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/KC.cell.nml']...
[omv]     Running the commands: [/usr/bin/jnml -validate /home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/GGN.morph.cell.nml /home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/GGN.cell.nml /home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/KC.cell.nml] in (/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; cwd=/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2; shell=False; env={'JNML_HOME': PosixPath('/usr/bin')})
[omv]     Commands: ['/usr/bin/jnml', '-validate', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/GGN.morph.cell.nml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/GGN.cell.nml', '/home/asinha/Documents/02_Code/00_mine/models/RayEtAl2020/NeuroML2/KC.cell.nml'] completed successfully
[omv]   Running checks for experiment: Dry run
[omv]
[omv]       Observable                        Test Passed
[omv]       --------------------------------------------------
[omv]       dry                                    ✔
[omv]
[omv]
[omv]       [ Test 2 of 2 complete - failed so far: 0 ]
[omv]
[omv]                             -------------
[omv]                             2 test(s) run
[omv]                             -------------
[omv]
[omv]                           All tests passing!
[omv]                           ==================

```

## Step 3) Setting up continuous testing on GitHub Actions

Now that we have set up OMV test, we want to set up ["continuous testing" (CT)](https://en.wikipedia.org/wiki/Continuous_testing).
What this means is that we want these test to run automatically whenever we make any changes.
On GitHub, we can do these using [GitHub Actions](https://docs.github.com/en/actions).

To set up a GitHub Action, we need to set up a "workflow file" in the `.github/workflows` directory.
We create one called `omv-ci.yml`:

```{code-block} yaml

name: Continuous build using OMV

on:
  schedule:
    - cron: "1 1 1 */2 *"
  push:
    branches: [ master, development, experimental ]
  pull_request:
    branches: [ master, development, experimental ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: [ "3.8", "3.10"]
        engine: [ jNeuroML_validate, jNeuroML_NEURON ]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python  ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version:  ${{ matrix.python-version }}

    - name: Install OMV
      run: |
        pip install OSBModelValidation
        pip install scipy sympy matplotlib cython pandas tables

    - name: Run OMV tests on engine ${{ matrix.engine }}
      run: |
        omv all -V --engine=${{ matrix.engine }}

    - name: OMV final version info
      run: |
        omv list -V # list installed engines
        env
```

This installs OMV and runs all test using it in the repository.
Additionally, it tests this out on a couple of Python versions.

Now, whenever we make a change to the repository---either as a pull request, or as a direct push of a commit, these tests will be run immediately to tell us if the model is still working as it should.
These can be seen in the ["actions" tab in the GitHub Repository](https://github.com/OpenSourceBrain/262670/actions).
