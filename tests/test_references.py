from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import Reference
from fdk_rdf_parser.parse_functions import extractReferences


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
            referenceType="http://purl.org/dc/terms/hasVersion",
            source="https://testdirektoratet.no/model/dataset/hasVersion",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/isVersionOf",
            source="https://testdirektoratet.no/model/dataset/isVersionOf",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/isPartOf",
            source="https://testdirektoratet.no/model/dataset/isPartOf",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/hasPart",
            source="https://testdirektoratet.no/model/dataset/hasPart",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/references",
            source="https://testdirektoratet.no/model/dataset/references",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/isReferencedBy",
            source="https://testdirektoratet.no/model/dataset/isReferencedBy",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/replaces",
            source="https://testdirektoratet.no/model/dataset/replaces",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/isReplacedBy",
            source="https://testdirektoratet.no/model/dataset/isReplacedBy",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/requires",
            source="https://testdirektoratet.no/model/dataset/requires",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/isRequiredBy",
            source="https://testdirektoratet.no/model/dataset/isRequiredBy",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/relation",
            source="https://testdirektoratet.no/model/dataset/relation",
        ),
        Reference(
            referenceType="http://purl.org/dc/terms/source",
            source="https://testdirektoratet.no/model/dataset/source",
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model/dataset/reference")

    assert extractReferences(graph, subject) == expected
