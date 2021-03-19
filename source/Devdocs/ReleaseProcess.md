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
| Tag previous development versions of individual repos | v2.0 |
| Increment all version numbers - to distinguish release from previous development version | v2.0 |
| Commit all work in development branches | v2.0 |
| Test all development branches - rerun Travis-CI at least once | v2.0 |
| Recheck all READMEs & docs | v2.0 |
| Run & check test.py in NeuroML2 repo | v2.0 |
| Check through issues for closed & easily closable ones | v2.0 |
| Update milestones: [https://github.com/NeuroML/NeuroML2/issues](https://github.com/NeuroML/NeuroML2/issues) | v2.0 |
| Update HISTORY.md in NeuroML2 | v2.0 |
| libNeuroML:  Update README; Retest; Merge to master; Tag release; Release to pip; Check [installation docs](https://libneuroml.readthedocs.org/en/latest/install.html) | v2.0 |
| pylems: Update README; Merge to master; Tag release; Release to pip | v2.0 |
| pyNeuroML: Update Readme; Release to pip | v2.0 |
| Java repositories ({ref}`jNeuroML <jNeuroML>`, org.neuroml.* etc.): Merge development to master; Tag releases: `git checkout master ; git pull; git tag -a 'NMLv2beta4' -m 'Version for NeuroML v2 beta 4 release';git tag; git push --tags; git checkout development` | v2.0 |
| Rebuild jNeuroML & commit to nC | v2.0 |
| Regenerate Cells.xml etc. on nml website & commit | v2.0 |
| Update docs on [http://www.neuroml.org](https://www.neuroml.org) | v2.0 |
| Add new binary release on [https://github.com/NeuroML/jNeuroML/releases](https://github.com/NeuroML/jNeuroML/releases) | v2.0 |
| Test on Windows... | v2.0 |
| Release & make doi on zenodo(?) | v2.0 |
| ANNOUNCE | v2.0 |
| Increment version numbers in all | v2.0 |
| New milestone in issues | v2.0 |
| Update version used in neuroConstruct | v2.0 |
| New release neuroConstruct | v2.0 |
