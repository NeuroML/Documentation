(userdocs:get_neuroml)=
# Get NeuroML

While one can use Jupyter Notebooks on different platforms ([Binder](https://binder.org)/[Open Source Brain v2](https://v2.opensourcebrain.org)/[Google Colab](https://colab.research.google.com)) to work with NeuroML models (for example, the tutorials in this documentation can mostly be run on Jupyter Notebooks), for certain use cases, it may be preferable/necessary to install the stack on our own computers.
One such use case, for example, is when one needs to run large scale simulations that require supercomputers/clusters to simulate.

## What you need

The NeuroML stack is written primarily in Python and Java, and so requires:

- a [supported](https://devguide.python.org/versions/), working [Python](https://www.python.org/downloads/) installation
- a working Java Runtime Environment (JRE)

The software stack is currently [tested on](https://github.com/NeuroML/jNeuroML/blob/master/.github/workflows/ci.yml#L19C15-L19C44):

  - Python versions: 3.8--3.12 (3.11 is preferred)
  - Java versions 8, 11, 16, 17, 19 on these [operating systems (OS)](https://github.com/actions/runner-images): Ubuntu 22.04 ("ubuntu-latest"), MacOS 14 Arm 64 ("macos-latest"), Windows 2019 ("windows-2019")


Once you have these programming languages installed, all you need to do is install {ref}`pyNeuroML <pyneuroml>`, and that will install the other parts of the NeuroML software stack for you too.
Please see the {ref}`pyNeuroML <pyneuroml>` page for more details.
