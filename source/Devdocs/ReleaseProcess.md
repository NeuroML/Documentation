(devdocs:release)=
# Release Process

## Overview

```{admonition} Needs work
TODO: Add more information to each of these
```

In general, work is carried out in the **development** branches of the [main NeuroML repositories](https://github.com/NeuroML)
and these are merged to **master** branches on a new major release, e.g. move from NeuroML v2.1 to v2.2.

## Steps for new major release

These are the steps required for a new release of the NeuroML development tools.

| Task | Version this was last done |
| --- | --- |
| Tag previous development versions of individual repos | v2.1 |
| Increment all version numbers - to distinguish release from previous development version | v2.1 |
| Commit all work in development branches | v2.1 |
| Test all development branches - rerun Travis-CI at least once | v2.1 |
| Recheck all READMEs & docs | v2.1 |
| Run & check [test.py](https://github.com/NeuroML/NeuroML2/blob/master/test.py) in NeuroML2 repo | v2.1 |
| Check through issues for closed & easily closable ones | v2.1 |
| Update NeuroML [milestones](https://github.com/NeuroML/NeuroML2/milestones) | v2.1 |
| Update HISTORY.md in NeuroML2 | v2.1 |
| libNeuroML:  Update README; Retest; Merge to master; Tag release; Release to pip; Check [installation docs](https://libneuroml.readthedocs.org/en/latest/install.html) | v2.0 |
| pylems: Update README; Merge to master; Tag release; Release to pip | v2.1 |
| pyNeuroML: Update Readme; Tag release; Release to pip | v2.0 |
| Java repositories ({ref}`jNeuroML <jNeuroML>`, org.neuroml.* etc.): Merge development to master; Tag releases | v2.0 |
| Rebuild jNeuroML & commit to [jNeuroMLJar](https://sourceforge.net/p/neuroml/code/HEAD/tree/jNeuroMLJar/) | v2.1 |
| Regenerate Cells.xml etc. on nml website & commit | v2.1 |
| Update docs on [http://www.neuroml.org](https://www.neuroml.org) | v2.1 |
| Add new binary release on [https://github.com/NeuroML/jNeuroML/releases](https://github.com/NeuroML/jNeuroML/releases) | v2.0 |
| Test on Windows... | v2.0 |
| Release & make doi on zenodo(?) | v2.0 |
| ANNOUNCE (mailing list, Twitter) | v2.0 |
| Increment version numbers in all development branches | v2.0 |
| New milestone in issues | v2.1 |
| Update version used in neuroConstruct | v2.0 |
| New release of neuroConstruct | v2.0 |
