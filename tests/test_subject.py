from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import Subject
from fdk_rdf_parser.parse_functions import extract_subjects


def test_uriref_subject() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/subject>
                a                         dcat:Dataset ;
                dct:subject
                    <https://testdirektoratet.no/model/concept/0> ,
                    <https://testdirektoratet.no/model/concept/1> .

        <https://testdirektoratet.no/model/concept/0>
                a                skos:Concept ;
                dct:identifier   "http://begrepskatalogen/begrep/123" ;
                skos:definition  "Norsk definisjon"@nb , "English definition"@en ;
                skos:prefLabel   "dokument"@nb , "document"@en .

        <https://testdirektoratet.no/model/concept/1>
                a                skos:Concept ;
                dct:identifier   "http://begrepskatalogen/begrep/321" ;
                skos:definition  "er lei seg fordi noko ikkje vart slik ein venta eller vona"@nn ;
                skos:prefLabel   "vonbroten"@nn ."""

    expected = [
        Subject(
            uri="https://testdirektoratet.no/model/concept/0",
            identifier="http://begrepskatalogen/begrep/123",
            definition={"nb": "Norsk definisjon", "en": "English definition"},
            prefLabel={"nb": "dokument", "en": "document"},
        ),
        Subject(
            uri="https://testdirektoratet.no/model/concept/1",
            identifier="http://begrepskatalogen/begrep/321",
            definition={
                "nn": "er lei seg fordi noko ikkje vart slik ein venta eller vona"
            },
            prefLabel={"nn": "vonbroten"},
        ),
    ]

    datasets_graph = Graph().parse(data=src, format="turtle")
    dataset_uri = URIRef("https://testdirektoratet.no/model/dataset/subject")

    assert extract_subjects(datasets_graph, dataset_uri) == expected


def test_blank_node_subject() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/subject>
                a               dcat:Dataset ;
                dct:subject     [  a                skos:Concept ;
                                   dct:identifier   "http://begrepskatalogen/begrep/123" ;
                                   skos:definition  "Definisjon"@nb ;
                                   skos:prefLabel   "dokument"@nb
                                ] ."""

    expected = [
        Subject(
            identifier="http://begrepskatalogen/begrep/123",
            definition={"nb": "Definisjon"},
            prefLabel={"nb": "dokument"},
        ),
    ]

    datasets_graph = Graph().parse(data=src, format="turtle")
    dataset_uri = URIRef("https://testdirektoratet.no/model/dataset/subject")

    assert extract_subjects(datasets_graph, dataset_uri) == expected
