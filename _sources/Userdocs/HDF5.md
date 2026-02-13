(userdocs:hdf5)=
# HDF5 support

The XML serializations of large NeuroML models can be prohibitive to store.
For such cases, NeuroML also includes support for saving models in the binary [HDF5](https://www.hdfgroup.org/solutions/hdf5) format via the [NeuroMLHdf5Writer in libNeuroML](https://libneuroml.readthedocs.io/en/stable/userdocs/writers.html#neuroml.writers.NeuroMLHdf5Writer). The same format can be exported also from the Java API ([example](https://github.com/NeuroML/org.neuroml.model/blob/master/src/test/java/org/neuroml/model/test/HDF5Test.java)).

The format of the export is documented below:


- {ref}`Network <schema:network>` is exported as a `network` HDF5 group with `id`, `notes`, and the `temperature` (optional) stored as attributes.
- {ref}`Population <schema:population>` is exported as a group with id `population_<id of the population>` with `id`, `component`, `size`, `type`, and `property` tags stored as attributes.
  - If the population is a {ref}`population list <schema:populationlist>` that includes {ref}`instances <schema:instance>` of cells, the locations of cells (x, y, z), these are stored in a 3 column table ("chunked array") with a row per instance.

- {ref}`Projection <schema:projection>` is exported as a group with id `project_<id of the projection>` with `id`, `type`, `presynapticPopulation`, `postSynapticPopulation`, `synapse` as attributes.
  - {ref}`Connection <schema:connection>` and {ref}`ConnectionWD <schema:connectionwd>` elements in projections are stored as rows in a table with the first two columns as the `pre_cell_id` and `post_cell_id` respectively, and the successive columns for the necessary attributes.

- {ref}`ElectricalProjection <schema:electricalprojection>` is exported similar to Projection with the {ref}`ElectricalConnection <schema:electricalconnection>`, {ref}`ElectricalConnectionInstance <schema:electricalconnectioninstance>`, and {ref}`ElectricalConnectionInstanceW <schema:electricalconnectioninstancew>` entries stored in tables.
- {ref}`ContinuousProjection <schema:continuousprojection>` is exported similar to Projection with the {ref}`ContinuousConnection <schema:continuousconnection>`, {ref}`ContinuousConnectionInstance <schema:continuousconnectioninstance>`, and {ref}`ContinuousConnectionInstanceW <schema:continuousconnectioninstancew>` entries stored in tables.
- {ref}`InputList <schema:inputlist>` is exported similar to Projection with the {ref}`Input <schema:input>`, and {ref}`InputW <schema:inputw>` entries stored in tables.


For more details, the source code of these export functions can be seen [here in the libNeuroML repository](https://github.com/NeuralEnsemble/libNeuroML/blob/2d8112178d8d82b07a20f8395ec22a23a6323a6c/neuroml/nml/helper_methods.py#L2548) and [here in org.neuroml.model](https://github.com/NeuroML/org.neuroml.model/blob/master/src/main/java/org/neuroml/model/util/hdf5/NeuroMLHDF5Writer.java).

HDF5 NeuroML files can be read and processed by `jnml` and `pynml` in the same way as XML files (see [here](https://github.com/OpenSourceBrain/OpenCortex/tree/master/examples/HDF5) for LEMS Simulation file examples which reference HDF5 NeuroML models).
