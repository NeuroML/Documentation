(userdocs:unitsanddimensions)=
# Units and dimensions

Support for dimensional quantities is a fundamental (and essential) feature of NeuroML, backed up by support for units and dimensions in LEMS.

The basic rules are:

```{admonition} Units and Dimensions
Specify the **dimensions** of quantities in LEMS

Use any<sup>*</sup> compatible **units** in NeuroML

```

The main motivation for this is that fundamental expressions for defining a model are independent of any particular units. For example, Ohm's law, **V = I * R** relates to quantities with dimensions voltage, current and resistance, not millivolts, picoamps, ohms, etc.

<sup>*</sup> While a wide range of commonly used units for each dimension are supported, they need to be present in the {ref}`standard unit and dimension definitions <schema:neuromlcoredimensions>` of NeuroML 2. 
