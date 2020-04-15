"""Test cases."""
import pytest

from fdk_rdf_parser import Temporal, extractTemporal
from rdflib import Graph, URIRef
import isodate

def test_temporal_dcat():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    [ a                 dct:PeriodOfTime ;
                                dcat:startDate    "2019-04-02T00:00:00"^^xsd:dateTime ;
                                dcat:endDate      "2020-04-02T00:00:00"^^xsd:dateTime] ."""

    expected = [
        Temporal(
            uri=None,
            endDate=isodate.parse_datetime("2020-04-02T00:00:00"),
            startDate=isodate.parse_datetime("2019-04-02T00:00:00"))]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/temporal')

    assert extractTemporal(graph, subject) == expected

def test_temporal_uri():

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
                dcat:endDate      "2020-04-02T00:00:00"^^xsd:dateTime ."""

    expected = [
        Temporal(
            uri='https://testdirektoratet.no/model/temporal/0',
            endDate=isodate.parse_datetime("2020-04-02T00:00:00"),
            startDate=isodate.parse_datetime("2019-04-02T00:00:00"))]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/temporal')

    assert extractTemporal(graph, subject) == expected

def test_temporal_owl_time():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix time:  <https://www.w3.org/TR/owl-time/> .

        <https://testdirektoratet.no/model/dataset/temporal>
                a               dcat:Dataset ;
                dct:temporal    [ a                  dct:PeriodOfTime ;
                                   time:hasBeginning  [ a                   time:Instant ;
                                                        time:inXSDDateTime  "2001-01-01T00:00:00Z"^^xsd:dateTime
                                                      ] ;
                                   time:hasEnd        [ a                   time:Instant ;
                                                        time:inXSDDateTime  "2046-05-12T00:00:00Z"^^xsd:dateTime
                                                      ]
                                 ] ."""

    expected = [
        Temporal(
            uri=None,
            endDate=isodate.parse_datetime("2046-05-12T00:00:00Z"),
            startDate=isodate.parse_datetime("2001-01-01T00:00:00Z"))]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/temporal')

    assert extractTemporal(graph, subject) == expected

def test_temporal_schema():

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
            endDate=isodate.parse_date("2020-04-02"),
            startDate=isodate.parse_date("2019-04-02"))]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/temporal')

    assert extractTemporal(graph, subject) == expected