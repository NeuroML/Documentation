(userdocs:units)=
# Units and dimensions in NeuroML

LEMS, and so NeuroML, have a well defined system of {ref}`units and dimensions <schema:neuromlcoredimensions>`.
This allows NeuroML/LEMS to better validate models to ensure that the correct dimensions have been used to express various quantities.
Next, NeuroML/LEMS also internally translates all units using the correct conversion factors to ensure that the right magnitudes are used for all quantities.

Therefore:
- users can use any of the defined units in NeuroML models without having to worry about conversion factors
- all quantities are saved and {ref}`recorded <userdocs:recording>` in SI Units
- when plotting data using NeuroML/LEMS using the {ref}`Line <schema:line>` component, users can use the `scale` parameter to convert quantities to other units.
