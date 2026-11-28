(userdocs:usage)=
# How to use this documentation

This documentation is generated using [Jupyter books](https://jupyterbook.org/intro.html).
You can learn more about the project on their website.

(userdocs:usage:structure)=
## Structure and navigation

```{admonition} Close the left hand side bar using the burger menu on the left side of the top panel.
:class: tip
You can close the left hand side bar by clicking the burger menu on the left side of the top panel.
This increases the width of the middle section of the documentation and can be helpful on smaller screens.
Clicking the hamburger menu again will re-open it.
```

The documentation is divided into a few parts that can be seen in the *left hand side navigation bar*:

- **User documentation**: this includes documentation for anyone looking to use NeuroML
- **NeuroML events**: any events related to NeuroML will be listed here
- **The NeuroML Initiative**: this includes documentation on the NeuroML community
- **Developer documentation**: this includes information for individuals looking to contribute to NeuroML (either the standard or the software)
- **Reference**: this includes the glossary of terms and the bibliography.

Each part contains different chapters, which can each contain different sections.
Each page in the documentation also has its own navigation in the *right hand side bar*.

(userdocs:usage:jupyterbooks)=
## Using Jupyter notebooks included in the documentation
```{admonition} Familiar with Jupyter Notebooks? Skip ahead to the next section.
:class: tip
If you are familiar with Jupyter Notebooks, you can skip ahead to the {ref}`Getting started with NeuroML <userdocs:getting_started_neuroml>` section.
```


The most important feature of Jupyter books is that it allows you to include [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) in the documentation.
This allows us to write documentation which includes code examples that can be modified and executed by users interactively in their browsers *without having to install anything on their local machines*.
For example, these are used in the {ref}`Getting Started <userdocs:getting_started_neuroml>` section.

Each Jupyter notebook in the documentation includes a rocket icon 🚀 in the top bar:

```{figure} ../images/izhikevich-rocket.png
:alt: Click the rocket icon in top panel of executable pages to execute them in Binder or Google Collaboratory.
:align: center

Click the rocket icon in top panel of executable pages to execute them in Binder or Google Collaboratory.
```
Clicking this icon will allow you to run the Jupyter Notebook:

```{figure} ../images/izhikevich-rocket-options.png
:alt: You can run the Jupyter Notebook on Binder or Google Colaboratory.
:align: center

You can run the Jupyter Notebook on Binder or Google Colaboratory.
```

You can choose from freely available services such as [Binder](https://mybinder.org/) and [Google Colaboratory](https://colab.research.google.com/).
Both Binder and Google Colaboratory will take you to these services and load the Jupyter Notebook for you to use.
The Live code option uses Binder but allows you to run the code in the current tab itself.
However, please note that this option does not include the full Jupyter Notebook features that Binder and Google Colaboratory provide.

```{admonition} Run Binder and Google Colaboratory in a new tab.
:class: tip
It is suggested to right click and select "Open in new tab" so that the tab with the NeuroML documentation remains open.
In most browsers, you can also use `Ctrl + click` to open links in a new tab:
```

```{figure} ../images/izhikevich-binder.png
:alt: Izhikevich example running in Binder.
:align: center
:scale: 30 %

Izhikevich example running in Binder
```
```{figure} ../images/izhikevich-google.png
:alt: Izhikevich example running in Google Colaboratory.
:align: center
:scale: 30 %

Izhikevich example running in Google Colaboratory.
```

```{figure} ../images/izhikevich-livecode.png
:alt: Izhikevich example running on Binder but using the Live Code option.
:align: center
:scale: 30 %

Izhikevich example running in Binder but using the Live Code option.
```

When running the Jupyter notebooks using these services, you can make changes to the code and re-run it as required.
On Binder and Google Colaboratory, which provide the full range of Jupyter Notebook features, you can also run all the code cells at once in sequence.
Please see the documentation pages to learn more about using Binder and Google Colaboratory [here](https://mybinder.readthedocs.io/en/latest/) and [here](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) respectively.
General information on using Jupyter Notebooks and the interface can be found in the documentation [here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#starting-the-notebook-server).

(userdocs:usage:jupyterbooks:locally)=
### Downloading Jupyter Notebooks to run locally on your machine

Jupyter Notebooks can also be downloaded and run locally on your machine.
To download the notebooks, use the Download link in the top panel:

```{figure} ../images/jupyter-download.png
:alt: Jupyter notebooks can be downloaded using the Download link in the top panel.
:align: center

Jupyter notebooks can be downloaded using the Download link in the top panel.
```

You will need to install the Python Jupyter Notebook packages to do so.
Please refer to the Jupyter Notebook [documentation](https://jupyter.readthedocs.io/en/latest/install/notebook-classic.html#alternative-for-experienced-python-users-installing-jupyter-with-pip) to see how you can install Jupyter Notebooks.
Additionally, you will also need to install the {ref}`NeuroML software <userdocs:software>` to run these notebooks.
Information on using Jupyter Notebooks and the interface can be found in the documentation [here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#starting-the-notebook-server).


(userdocs:usage:pdf)=
## Downloading this documentation as PDF

You can download this documentation as PDF pages for offline use.

To download individual pages, use the download icon in the top bar.
This will generate a PDF page of the current page for you, using your browser's "print to file" functionality.

% relative links to external files don't yet work. See https://github.com/executablebooks/jupyter-book/issues/1657
You can also download the complete book as a PDF [here](https://docs.neuroml.org/_static/files/neuroml-documentation.pdf).

(userdocs:usage:bugs)=
## Reporting bugs and issues

Please report any issues that you may find in the documentation so that it can be improved.
To report an issue on a particular page, you can use the "open issue" link under the GitHub icon in the top panel.
Additionally, you can also suggest edits by editing the page in a fork and opening a pull request using the "suggest and edit" link.

```{figure} ../images/jupyterbook-issue.png
:alt: You can report issues and suggest edits to the documentation to help us improve it using the options in the GitHub icon in the top panel.
:align: center

You can report issues and suggest edits to the documentation to help us improve it using the options in the GitHub icon in the top panel.
```

You can also always contact the NeuroML community using our {ref}`communication channels <contact>` if required.
