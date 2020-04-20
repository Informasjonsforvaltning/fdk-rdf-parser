"""Test cases."""
import pytest

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import SkosConcept
from fdk_rdf_parser.parse_functions import extractSkosConcept
from fdk_rdf_parser.rdf_utils import dcatApNoURI

def test_legal_basis_for_restriction():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dcatno:legalBasisForRestriction
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://vg.no" ;
                  skos:prefLabel  "En tittel"@nb , "Ein tittel"@nn
                ] ."""

    expected = [
        SkosConcept(
            uri = 'https://vg.no',
            prefLabel = {'nb':'En tittel', 'nn':'Ein tittel'},
            extraType = 'http://purl.org/dc/terms/RightsStatement'
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef('https://testdirektoratet.no/model/dataset/0')
    predicate = dcatApNoURI('legalBasisForRestriction')


    assert extractSkosConcept(graph, subject, predicate) == expected

def test_ref_uri_used_when_missing_source():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dcatno:informationModel   <https://testdirektoratet.no/model/info/0> .
                
        <https://testdirektoratet.no/model/info/0>
                a               skos:Concept , dct:Standard ;
                skos:prefLabel  "Informasjonsmodell"@nb ."""

    expected = [
        SkosConcept(
            uri = 'https://testdirektoratet.no/model/info/0',
            prefLabel = {'nb':'Informasjonsmodell'},
            extraType = 'http://purl.org/dc/terms/Standard'
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef('https://testdirektoratet.no/model/dataset/0')
    predicate = dcatApNoURI('informationModel')


    assert extractSkosConcept(graph, subject, predicate) == expected

def test_source_is_prioritized_uri():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dct:conformsTo            <https://testdirektoratet.no/model/conforms/0> .
                
        <https://testdirektoratet.no/model/conforms/0>
                a               skos:Concept ;
                dct:source      "https://www.test.no/source/" ;
                skos:prefLabel  "Kilde"@nb ."""

    expected = [
        SkosConcept(
            uri = 'https://www.test.no/source/',
            prefLabel = {'nb':'Kilde'},
            extraType = None
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef('https://testdirektoratet.no/model/dataset/0')
    predicate = DCTERMS.conformsTo


    assert extractSkosConcept(graph, subject, predicate) == expected

def test_handles_literal_uri():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/distribution/0>
                a                 dcat:Distribution ;
                dct:conformsTo    "http://hotell.difi.no/application.wadl" ."""

    expected = [
        SkosConcept(
            uri = 'http://hotell.difi.no/application.wadl'
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef('https://testdirektoratet.no/model/distribution/0')
    predicate = DCTERMS.conformsTo


    assert extractSkosConcept(graph, subject, predicate) == expected