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

- Tag previous development versions of individual repos
- Increment all version numbers - to distinguish release from previous development version
- Commit all work in development branches
- Test all development branches - rerun Travis-CI at least once
- Recheck all READMEs & docs
- Run & check test.py in NeuroML2 repo
- Check through issues for closed & easily closable ones
- Update milestones: [https://github.com/NeuroML/NeuroML2/issues](https://github.com/NeuroML/NeuroML2/issues)
- Update HISTORY.md in NeuroML2
- libNeuroML
   - Update README
   - Retest
   - Merge to master
   - Tag release
	 - Release to pip
   - Check [https://libneuroml.readthedocs.org/en/latest/install.html](https://libneuroml.readthedocs.org/en/latest/install.html)
- pylems
   - Update README
   - Merge to master
	 - Tag release
	 - Release to pip
- pyNeuroML
    - Update Readme
    - Release to pip
- Java repositories ({ref}`jNeuroML <jNeuroML>`, org.neuroml.* etc.)
	 - Merge development to master
- Tag releases
     - `git checkout master ; git pull; git tag -a 'NMLv2beta4' -m 'Version for NeuroML v2 beta 4 release';git tag; git push --tags; git checkout development`
- Rebuild jNeuroML & commit to nC
- Regenerate Cells.xml etc. on nml website & commit
- Update docs on [http://www.neuroml.org](https://www.neuroml.org)
- Add new binary release on [https://github.com/NeuroML/jNeuroML/releases](https://github.com/NeuroML/jNeuroML/releases)
- Test on Windows...
- Release & make doi on zenodo(?)
- ANNOUNCE
- Increment version numbers in all
- New milestone in issues
- Update version used in neuroConstruct
- New release neuroConstruct
