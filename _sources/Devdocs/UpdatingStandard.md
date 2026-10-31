(devdocs:updating_standard)=
# Making changes to the NeuroML standard

The NeuroML standard is stored in two sets of files, each serving a specific purpose:

- the NeuroML [XML Schema Definition](https://en.wikipedia.org/wiki/XML_Schema_(W3C)) (XSD) file: this specifies the structure of a valid NeuroML XML file: what XML tags may be used and the how they are related
- the NeuroML [LEMS](http://lems.github.io/LEMS/) ComponentType definition XML files: these include the definitions of the NeuroML standard ComponentTypes in LEMS constructs, which include the mathematical details underlying these ComponentTypes

These files are housed in the [NeuroML](https://github.com/NeuroML/NeuroML2/) repository.

The XSD schema file is used to validate NeuroML XML files, as shown in the {ref}`page on validating NeuroML files <userdocs:validating_models>`.
Further, the NeuroML Python model in {ref}`libNeuroML <libneuroml>` is also generated from the XSD file using the [generateDS](http://www.davekuhlman.org/generateDS.html) utility.

The LEMS ComponentType definition XML files are also used for a series of additional validation tests, and since they include the details of the underlying dynamics for all ComponentTypes, they are also used for the simulation of NeuroML models either using the reference LEMS interpreter, {ref}`jLEMS <jlems>`, or through automated code generation for supported simulation platforms (via {ref}`jNeuroML <jneuroml>`).
Additionally, the LEMS definition files are also used the generate the {ref}`human readable schema documentation <userdocs:neuromlv2>` included in this documentation resource.

The two sets of files are therefore, tightly coupled.
Any changes to the XSD file must also be followed by corresponding changes to the LEMS definition files.

(devdocs:updating_standard:proc)=
## Procedure

```{admonition} PR waiting
TODO: A pull request to include the `transfer_docs_to_xsd.py` script in the repository is in review here: https://github.com/NeuroML/NeuroML2/pull/172
```

The suggested way of making changes to these files is via pull requests to the NeuroML repository which will undergo review by the NeuroML editorial board and the development team.
As noted in the {ref}`general contribution guidelines <devdocs:devsop>`, the `development` branch tracks the next release of the NeuroML standard.
So, all pull request must be made against the `development` branch.

- New ComponentTypes, and their elements (parameters, variables etc.) that are added in the LEMS definition XML files should be properly documented.
- After both sets of files have been modified, please run the `transfer_docs_to_xsd.py` script in the `scripts` folder to copy documentation over from the XML files to the XSD schema file. This script will also run basic sanity checks to ensure that all ComponentTypes in the LEMS XML definition files are represented in the XSD schema file and vice-versa.
- Please run `xmllint` on the files to ensure they are formatted correctly.
- Please make individual commits for changes to the XSD file, and the XML files. This ensures that their change history is clearly maintained.

(devdocs:updating_standard:schema_docs)=
## Regenerating schema documentation

Once the pull request has been merged in the NeuroML repository, the {ref}`human readable schema documentation included in this documentation resource <userdocs:neuromlv2>` must be updated.
This is done by running the [generate-jupyter-ast.py](https://github.com/NeuroML/Documentation/blob/master/scripts/schemas/generate-jupyter-ast.py) script included in the [documentation source repository](https://github.com/NeuroML/Documentation).
This will read the LEMS XML definition files and regenerate the corresponding documentation pages.
A pull request can then be opened with the updated pages.



(devdocs:updating_standard:org_neuroml_model)=
## Updating the Java API: org.neuroml.model

TODO: Document what needs to be done for https://github.com/NeuroML/org.neuroml.model



(devdocs:updating_standard:libneuroml)=
## Updating the Python API: libNeuroML

```{admonition} PR waiting
TODO: A pull request to include the `regenerate-nml.sh` script in the repository is in review here: https://github.com/NeuralEnsemble/libNeuroML/pull/110
```

Any changes to the XSD schema file require regeneration of the [Python object model in libNeuroML](https://github.com/NeuralEnsemble/libNeuroML/blob/development/neuroml/nml/nml.py):

- copy over the updated XSD schema file to the `neuroml/nml/` directory in the `development` branch
- commit the new XSD file
- run the `regenerate-nml.sh` script to regenerate and reformat `nml.py`
- build and install libNeuroML into a new virtual environment
- run all tests using `pytest`
- run all examples and ensure that they run correctly (please see the [GitHub actions workflow](https://github.com/NeuralEnsemble/libNeuroML/blob/master/.github/workflows/ci.yml#L44) for more information)
- if all checks pass successfully, a pull request can be opened

(devdocs:updating_standard:c_api)=
## Updating the C++ API

TODO: Document what needs to be done for https://github.com/NeuroML/NeuroML_API/

