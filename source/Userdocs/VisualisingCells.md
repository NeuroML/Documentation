(userdocs:visualising_cells)=
# Visualising and analysing cell models

The NeuroML ecosystem include a number of utilities for analysis and visualisation of cells.
Cell morphologies can either be visualised programmatically using the core tools, or using the many advanced neuroinformatics tools in the ecosystem that support NeuroML.
In addition to the resources listed below, you can also use the visualisation features of any other tools that read NeuroML.
E.g., {ref}`NetPyNE and NetPyNE-UI <userdocs:supporting:apps:netpyne>`, {ref}`neuroConstruct <userdocs:supporting:apps:neuroconstruct>`, {ref}`Arbor <userdocs:supporting:apps:arbor>` and others.


(userdocs:visualising_cells:morph)=
## Visualising morphology of multi-compartmental cell models

Multi-compartmental cells can be visualised using the [plot_2D](https://pyneuroml.readthedocs.io/en/development/pyneuroml.plot.html#pyneuroml.plot.PlotMorphology.plot_2D) and [plot_interactive_3D](https://pyneuroml.readthedocs.io/en/development/pyneuroml.plot.html#pyneuroml.plot.PlotMorphology.plot_interactive_3D) methods included in {ref}`pyNeuroML <pyNeuroML>`.
This functionality is also exposed via the `pynml-plotmorph` command line tool.

```{figure} ../images//test_morphology_plot_2d_Cell_497232312_cell_nml_xy.png
:alt: Morphology of example cell plotted with `plot_2D`
:align: center
:width: 50%

Morphology of example cell plotted with `plot_2D` in the X-Y plane.
```

<center>
    <video src="../_static/files/20231122-HL23PYR.webm" width="70%"  controls loop>
        Your browser does not support the video tag
    </video><br />
    <i>Morphology of example cell visualised interactively using `plot_interactive_3D`</i>
</center>


(userdocs:visualising_cells:morph:nmldb)=
### Visualising morphology of multi-compartmental cell models in NeuroML-db
The {ref}`NeuroML-DB <userdocs:finding_models:neuromldb>` platform shows detailed cell morphologies of all cells included in its database.

```{figure} ../images/nml-db-morphology.png
:alt: Morphology of cell shown in NeuroML-DB.
:align: center
:width: 70%

Visualisation of morphology of an example cell on NeuroML-DB.
```
(userdocs:visualising_cells:morph:osb)=
### Visualising morphology of multi-compartmental cell models in Open Source Brain
The {ref}`Open Source Brain <userdocs:finding_models:osbv1>` platform also provides advanced visualisation capabilities that can be used to visualise the morphologies of NeuroML cells.

```{figure} ../images/osb-morphology.png
:alt: Morphology of cell shown on Open Source Brain.
:align: center
:width: 70%

Interactive visualisation of morphology of an example cell on Open Source Brain.
```


(userdocs:visualising_cells:ephys)=
## Analysing cell electrophysiology

The core tools also include utilities to aid in the analysis of cell electrophysiology.
{ref}`pyNeuroML <pyNeuroML>` includes the [generate_current_vs_frequency_curve](https://pyneuroml.readthedocs.io/en/development/pyneuroml.analysis.html#pyneuroml.analysis.generate_current_vs_frequency_curve) utility function that can be used to generate current-frequency, current-sub-threshold voltage, and to plot voltage traces generated at the soma for different current injections.
For example, we can analyse the {ref}`OLM cell from our tutorial <userdocs:getting_started:multi_compartment_example>`:
```
generate_current_vs_frequency_curve("source/Userdocs/NML2_examples/olm.cell.nml", "olm", simulator="jNeuroML_NEURON", plot_iv=True, plot_if=True, plot_voltage_traces=True)
```

This will generate these figures:

```{figure} ../images/olm-cell-fi.png
:alt: F-I curve for OLM cell generated using `generate_current_vs_frequency_curve`.
:align: center
:width: 70%

F-I curve for OLM cell generated using `generate_current_vs_frequency_curve`.
```

```{figure} ../images/olm-cell-subthresholdVi.png
:alt: Current vs sub-threshold voltage curve for OLM cell generated using `generate_current_vs_frequency_curve`.
:align: center
:width: 70%

Current vs sub-threshold voltage curve for OLM cell generated using `generate_current_vs_frequency_curve`.
```

```{figure} ../images/olm-cell-voltage-traces.png
:alt: Voltage traces for OLM cell with different injection currents generated using `generate_current_vs_frequency_curve`.
:align: center
:width: 70%

Voltage traces for OLM cell with different injection currents generated using `generate_current_vs_frequency_curve`.
```
