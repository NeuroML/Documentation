(userdocs:conventions)=
# Conventions

This page documents various conventions in use in NeuroML.

In general, please prefer underscores `_` instead of spaces wherever possible, in filenames and ids.

(userdocs:conventions:files)=
## File naming

When naming different NeuroML files, we suggest the following suffixes:

- `channel.nml` for NeuroML files describing ion channels, for example: `Na.channel.nml`
- `cell.nml` for NeuroML files describing cells, for example: `hh.cell.nml`
- `synapse.nml` for NeuroML files describing synapses, for example: `AMPA.synapse.nml`
- `net.nml` for NeuroML files describing networks of cells, for example: `excitatory.net.nml`

For LEMS files that describe simulations of NeuroML models ({ref}`"LEMS Simulation files" <userdocs:lemssimulation>`), we suggest that:

- file names start with the `LEMS_` prefix,
- file names end in `xml`

For example `LEMS_HH_Simulation.xml`.

(userdocs:conventions:segments)=
## Neuron segments

When naming segments in multi-compartmental neuron models, we suggest the following prefixes:

- `axon_` for axonal segments
- `dend_` for dendritic segments
- `soma_` for somatic segments

There are 3 specific recommended names for segment groups which contain **ALL** of the somatic, dendritic or axonal segments

- `axon_group` for the group of all axonal segments
- `dend_group` for the group of all dendritic segments
- `soma_group` for the group of all somatic segments

Ideally every segment should be a member of one and only one of these groups. 
