from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import (
    Reference,
    ReferenceDataCode,
    SkosConcept,
)
from fdk_rdf_parser.parse_functions import extract_references


def test_references() -> None:
    src = """
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/reference>
                a                   dcat:Dataset ;
                dct:hasVersion
                    <https://testdirektoratet.no/model/dataset/hasVersion> ;
                dct:isVersionOf
                    <https://testdirektoratet.no/model/dataset/isVersionOf> ;
                dct:isPartOf
                    <https://testdirektoratet.no/model/dataset/isPartOf> ;
                dct:hasPart
                    <https://testdirektoratet.no/model/dataset/hasPart> ;
                dct:references
                    <https://testdirektoratet.no/model/dataset/references> ;
                dct:isReferencedBy
                    <https://testdirektoratet.no/model/dataset/isReferencedBy> ;
                dct:replaces
                    <https://testdirektoratet.no/model/dataset/replaces> ;
                dct:isReplacedBy
                    <https://testdirektoratet.no/model/dataset/isReplacedBy> ;
                dct:requires
                    <https://testdirektoratet.no/model/dataset/requires> ;
                dct:isRequiredBy
                    <https://testdirektoratet.no/model/dataset/isRequiredBy> ;
                dct:relation
                    <https://testdirektoratet.no/model/dataset/relation> ;
                dct:source
                    <https://testdirektoratet.no/model/dataset/source> ."""

    expected = [
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/hasVersion"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/hasVersion"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/isVersionOf"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/isVersionOf"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/isPartOf"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/isPartOf"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/hasPart"),
            source=SkosConcept(uri="https://testdirektoratet.no/model/dataset/hasPart"),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/references"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/references"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(
                uri="http://purl.org/dc/terms/isReferencedBy"
            ),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/isReferencedBy"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/replaces"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/replaces"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(
                uri="http://purl.org/dc/terms/isReplacedBy"
            ),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/isReplacedBy"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/requires"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/requires"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(
                uri="http://purl.org/dc/terms/isRequiredBy"
            ),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/isRequiredBy"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/relation"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/relation"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/source"),
            source=SkosConcept(uri="https://testdirektoratet.no/model/dataset/source"),
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/reference")

    assert extract_references(graph, subject) == expected


def test_several_of_same_reference_type() -> None:
    src = """
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/reference-list>
            a                   dcat:Dataset ;
            dct:isPartOf        <https://testdirektoratet.no/model/dataset/isPartOf> ;
            dct:relation        <https://testdirektoratet.no/model/dataset/relation0> ,
                                <https://testdirektoratet.no/model/dataset/relation1> ,
                                <https://testdirektoratet.no/model/dataset/relation2> ."""

    expected = [
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/isPartOf"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/isPartOf"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/relation"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/relation0"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/relation"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/relation1"
            ),
        ),
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/relation"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/relation2"
            ),
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/reference-list")

    assert extract_references(graph, subject) == expected


def test_references_label() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .

        <https://testdirektoratet.no/model/dataset/reference>
                a                   dcat:Dataset ;
                dct:relation
                    <https://testdirektoratet.no/model/dataset/relation> .

        <https://testdirektoratet.no/model/dataset/relation>
                a                   rdf:Resource;
                rdfs:label
                    "Relasjon"@nb .
            """

    expected = [
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/relation"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/relation",
                prefLabel={"nb": "Relasjon"},
            ),
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/reference")

    assert extract_references(graph, subject) == expected


def test_literal_reference() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/reference>
                a                   dcat:Dataset ;
                dct:relation
                    "https://testdirektoratet.no/model/dataset/relation" .

            """

    expected = [
        Reference(
            referenceType=ReferenceDataCode(uri="http://purl.org/dc/terms/relation"),
            source=SkosConcept(
                uri="https://testdirektoratet.no/model/dataset/relation",
            ),
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/reference")

    assert extract_references(graph, subject) == expected
