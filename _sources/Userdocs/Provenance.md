(userdocs:provenance)=
# Maintaining provenance in NeuroML models

It is important to include metadata related to the "provenance" of model elements in NeuroML models.
This ensures that the sources of different components of different models can be easily obtained/verified.
For example, all NeuroML models should ideally include information about the original implementations, original research papers, and the original creators for all model elements.

NeuroML supports the inclusion of such information in the {ref}`annotation <schema:annotation>` model element.
Annotations in NeuroML can include metadata using the [Resource Description Framework (RDF)](https://en.wikipedia.org/wiki/Resource_Description_Framework).
The advantage of using RDF is that it makes the metadata machine readable which enables automated analysis and parsing.

(userdocs:provenance:spec)=
## Annotation specification

NeuroML follows the [COMBINE specification for annotations](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md).
This specification provides a set of well defined relationships that can be used to connect model elements to various metadata.
These are included in the NeuroML schema as {ref}`core NeuroML component types <schema:neuromlcorecomptypes_>`.

The suggested format for inclusion of the RDF metadata in annotations is [Minimum information required in the annotation of models (MIRIAM)](https://en.wikipedia.org/wiki/Minimum_information_required_in_the_annotation_of_models).

(userdocs:provenance:creating)=
## Creating annotations

{ref}`pyNeuroML <pyneuroml>` includes the [create_annotation](https://pyneuroml.readthedocs.io/en/development/pyneuroml.annotations.html#pyneuroml.annotations.Annotation.create_annotation) function for the addition of annotations to model elements.
Please see the API documentation for explanation on its usage.
Note that this functionality is not included by default when installing pyNeuroML.
One must install the annotation extra:

```{code-block} bash
pip install pyneuroml[annotations]
```

An example of an annotation for the NeuroML conversion of Ray et al 2020 {cite}`Ray2020` is shown below:


```{code-block} python
    annotation = create_annotation(
        subject=cell.id, title="Giant GABAergic Neuron model",
        description="Subhasis Ray, Zane N Aldworth, Mark A Stopfer (2020) Feedback inhibition and its control in an insect olfactory circuit eLife 9:e53281.",
        annotation_style="miriam",
        serialization_format="pretty-xml",
        xml_header=False,
        citations={"https://doi.org/10.7554/eLife.53281": "Subhasis Ray, Zane N Aldworth, Mark A Stopfer (2020) Feedback inhibition and its control in an insect olfactory circuit eLife 9:e53281."},
        sources={"https://modeldb.science/262670": "ModelDB",
                 "https://github.com/OpenSourceBrain/262670": "GitHub",
                 "https://v1.opensourcebrain.org/projects/locust-mushroom-body": "Open Source Brain"},
        authors={"Subhasis Ray":
                 {"https://orcid.org/0000-0003-2566-7146": "orcid"},
                 },
        contributors={
            "Ankur Sinha": {"https://orcid.org/0000-0001-7568-7167": "orcid"},
        },
        creation_date="2024-04-25"
    )
    cell.annotation = neuroml.Annotation([annotation])
```

This generates the following RDF annotation in the MIRIAM format to be included in the NeuroML cell file:

```{code-block} xml
    <annotation>
        <rdf:RDF
          xmlns:dc="http://purl.org/dc/elements/1.1/"
          xmlns:dcterms="http://purl.org/dc/terms/"
          xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
          xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
        >
          <rdf:Description rdf:about="GGN">
            <dc:title>Giant GABAergic Neuron model</dc:title>
            <dc:description>Subhasis Ray, Zane N Aldworth, Mark A Stopfer (2020) Feedback inhibition and its control in an insect olfactory circuit eLife 9:e53281.</dc:description>
            <dc:source>
              <rdf:Bag>
                <rdf:_1 rdf:resource="https://modeldb.science/262670"/>
              </rdf:Bag>
            </dc:source>
            <dc:source>
              <rdf:Bag>
                <rdf:_1 rdf:resource="https://github.com/OpenSourceBrain/262670"/>
              </rdf:Bag>
            </dc:source>
            <dc:source>
              <rdf:Bag>
                <rdf:_1 rdf:resource="https://v1.opensourcebrain.org/projects/locust-mushroom-body"/>
              </rdf:Bag>
            </dc:source>
            <bqmodel:isDescribedBy>
              <rdf:Bag>
                <rdf:_1 rdf:resource="https://doi.org/10.7554/eLife.53281"/>
              </rdf:Bag>
            </bqmodel:isDescribedBy>
            <dc:creator>
              <rdf:Bag>
                <rdf:_1>Subhasis Ray</rdf:_1>
                <rdf:_2>https://orcid.org/0000-0003-2566-7146</rdf:_2>
              </rdf:Bag>
            </dc:creator>
            <dc:contributor>
              <rdf:Bag>
                <rdf:_1>Ankur Sinha</rdf:_1>
                <rdf:_2>https://orcid.org/0000-0001-7568-7167</rdf:_2>
              </rdf:Bag>
            </dc:contributor>
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2024-04-25</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>

    </annotation>
```

pyNeuroML also includes functions to extract data from annotations.
