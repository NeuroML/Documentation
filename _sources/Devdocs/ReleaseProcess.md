(devdocs:release)=
# Release Process

## Overview

In general, work is carried out in the **development** branches of the [main NeuroML repositories](https://github.com/NeuroML/.github/blob/main/testsheet/README.md)
and these are merged to **master** branches on a new major release, e.g. move from NeuroML v2.1 to v2.2.

A single page showing the **status of the automated test** as well as any **open Pull Requests** on all of the core NeuroML repositories can be found [here](https://github.com/NeuroML/.github/blob/main/testsheet/README.md).

## Steps for new major release

These are the steps required for a new release of the NeuroML development tools.

| Task | Version this was last done |
| --- | --- |
| Commit final stable work in development branches | v2.3 |
| Make releases (not just tag - generates DOI) previous development versions of individual repos | v2.3 |
| Increment all version numbers - to distinguish release from previous development version | v2.3 |
| Test all development branches - rerun GitHub Actions at least once | v2.3 |
| Recheck all READMEs & docs | v2.3 |
| Run & check [test.py](https://github.com/NeuroML/NeuroML2/blob/master/test.py) in NeuroML2 repo | v2.3 |
| Check through issues for closed & easily closable ones | v2.3 |
| Update version in {ref}`documentation pages <userdocs:neuromlv2>` | v2.3 |
| Update [HISTORY.md](https://github.com/NeuroML/NeuroML2/blob/master/HISTORY.md) in NeuroML2 | v2.3 |
| pylems: Update README; Merge to master; Tag release; Release to pip | v2.3 |
| libNeuroML:  Update README; Retest; Merge to master; Tag release; Release to pip; Check [installation docs](https://libneuroml.readthedocs.org/en/latest/install.html) | v2.3 |
| pyNeuroML: Update Readme; Tag release; Release to pip | v2.3 |
| NeuroMLlite: Update Readme; Tag release; Release to pip | v2.3 |
| Java repositories ({ref}`jNeuroML <jNeuroML>`, org.neuroml.* etc.): Merge development to master; Tag releases | v2.3 |
| Rebuild jNeuroML & commit to [jNeuroMLJar](https://sourceforge.net/p/neuroml/code/HEAD/tree/jNeuroMLJar/) and use latest for [jNeuroML for OMV](https://github.com/OpenSourceBrain/osb-model-validation/blob/master/omv/engines/getjnml.py#L8) | v2.3 |
| Add new binary release on [https://github.com/NeuroML/jNeuroML/releases](https://github.com/NeuroML/jNeuroML/releases) | v2.3 |
| Update version used in [neuroConstruct](https://github.com/NeuralEnsemble/neuroConstruct) | v2.3 |
| Update docs on [http://docs.neuroml.org](https://docs.neuroml.org) | v2.3 |
| Update version on [COMBINE website](https://github.com/combine-org/combine-org.github.io/blob/master/content/authors/NeuroML/_index.md) | v2.2 |
| ANNOUNCE (mailing list, Twitter) | v2.2 |
| Increment version numbers in all development branches | v2.3 |
| DOI on [Zenodo](https://doi.org/10.5281/zenodo.593108) | v2.3 |
| Update NeuroML [milestones](https://github.com/NeuroML/NeuroML2/milestones) | v2.2 |
| New release of [neuroConstruct](https://github.com/NeuralEnsemble/neuroConstruct/releases) | v2.3 |
| Test toolchain on Windows... | v2.0 |
