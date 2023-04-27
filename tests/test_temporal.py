from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import Temporal
from fdk_rdf_parser.parse_functions import extract_temporal


def test_temporal_dcat() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    [
                    a                 dct:PeriodOfTime ;
                    dcat:startDate    "2019-04-02T00:00:00"^^xsd:dateTime ;
                    dcat:endDate      "2020-04-02T00:00:00"^^xsd:dateTime
                ] ."""

    expected = [
        Temporal(
            uri=None,
            endDate="2020-04-02T00:00:00",
            startDate="2019-04-02T00:00:00",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/temporal")

    assert extract_temporal(graph, subject) == expected


def test_temporal_uri() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    <https://testdirektoratet.no/model/temporal/0> .

        <https://testdirektoratet.no/model/temporal/0>
                a                 dct:PeriodOfTime ;
                dcat:startDate    "2019-04-02T00:00:00"^^xsd:dateTime ;
                dcat:endDate      "2020-04-02T00:00:00" ."""

    expected = [
        Temporal(
            uri="https://testdirektoratet.no/model/temporal/0",
            startDate="2019-04-02T00:00:00",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/temporal")

    assert extract_temporal(graph, subject) == expected


def test_temporal_owl_time() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix time:  <https://www.w3.org/TR/owl-time/> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    [
                    a                  dct:PeriodOfTime ;
                    time:hasBeginning  [
                        a                   time:Instant ;
                        time:inXSDDateTime  "2001-01-01T00:00:00Z"^^xsd:dateTime
                    ] ;
                    time:hasEnd        [
                        a                   time:Instant ;
                        time:inXSDDateTime  "2046-05-12T00:00:00Z"^^xsd:dateTime
                    ]
                ] ."""

    expected = [
        Temporal(
            uri=None,
            endDate="2046-05-12T00:00:00Z",
            startDate="2001-01-01T00:00:00Z",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/temporal")

    assert extract_temporal(graph, subject) == expected


def test_temporal_schema() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix schema:  <http://schema.org/> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    [ a                 dct:PeriodOfTime ;
                                schema:startDate    "2019-04-02"^^xsd:date ;
                                schema:endDate      "2020-04-02"^^xsd:date] ."""

    expected = [
        Temporal(
            uri=None,
            endDate="2020-04-02",
            startDate="2019-04-02",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/temporal")

    assert extract_temporal(graph, subject) == expected


def test_handles_missing_node() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix schema:  <http://schema.org/> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    [ ] ."""

    expected = [Temporal()]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/temporal")

    assert extract_temporal(graph, subject) == expected
