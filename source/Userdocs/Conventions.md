(userdocs:conventions)=
# Conventions in NeuroML

This page documents various conventions in use in NeuroML.

In general, please prefer underscores `_` instead of spaces wherever possible.

## File naming

When naming different NeuroML files, we suggest the following suffixes:

- `channel.nml` for NeuroML files describing ion channels, for example: `Na.channel.nml`
- `cell.nml` for NeuroML files describing cell, for example: `hh.cell.nml`
- `net.nml` for NeuroML files describing networks of cells, for example: `excitatory.net.nml`

For LEMS files that describe simulations of NeuroML models, we suggest that:

- file names start with the `LEMS_` prefix,
- file names end in `xml`

For example `LEMS_HH_Simulation.xml`

## Neuron segments

When naming segments in multi-compartmental neuron models, we suggest the following prefixes:

- `axon_` for axonal segments
- `dend_` for dendritic segments
- `soma_` for somatic segments
