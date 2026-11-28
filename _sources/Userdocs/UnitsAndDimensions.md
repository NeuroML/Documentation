(userdocs:unitsanddimensions)=
# Units and dimensions

Support for dimensional quantities is a fundamental (and essential) feature of NeuroML, backed up by support for units and dimensions in LEMS.

The basic rules are:

- specify the **dimensions** of quantities in LEMS
- use compatible **units** defined in the NeuroML schema in NeuroML models.

The main motivation for this is that fundamental expressions for defining a model are independent of any particular units.
For example, Ohm's law, **V = I * R** relates to quantities with dimensions voltage, current and resistance, not millivolts, picoamps, ohms, etc.

Users can therefore use a wide range of commonly used units for each dimension defined in the {ref}`standard unit and dimension definitions <schema:neuromlcoredimensions_>` of NeuroML 2 without worrying about conversion factors.

Additionally, please keep in mind that:

- all quantities are saved and {ref}`recorded <userdocs:quantitiesandrecording>` in SI Units
- when plotting data using NeuroML/LEMS using the {ref}`Line <schema:line>` component, users can use the `scale` parameter to convert quantities to other units.
