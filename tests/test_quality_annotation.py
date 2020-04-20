"""Test cases."""
import pytest

from fdk_rdf_parser.classes import QualityAnnotation
from fdk_rdf_parser.parse_functions import extractQualityAnnotation
from rdflib import Graph, URIRef

def test_quality_annotations():

    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dqv:   <http://www.w3.org/ns/dqvNS#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .

        <https://testdirektoratet.no/model/dataset/quality>
                a                   dcat:Dataset ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Currentness> ;
                    prov:hasBody     [] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Availability> ;
                    prov:hasBody     [ rdf:value  "availability"@en ] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Accuracy> ;
                    prov:hasBody     [ rdf:value  "Accuracy"@en ] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Relevance> ;
                    prov:hasBody     [ rdf:value  "relevans"@nb ] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Completeness> ;
                    prov:hasBody     [ rdf:value  "Completeness"@en ] ] ."""

    expected = {
        'http://iso.org/25012/2008/dataquality/Currentness': QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Currentness'
        ),
        'http://iso.org/25012/2008/dataquality/Availability': QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Availability',
            hasBody={'en':'availability'}
        ),
        'http://iso.org/25012/2008/dataquality/Accuracy': QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Accuracy',
            hasBody={'en':'Accuracy'}
        ),
        'http://iso.org/25012/2008/dataquality/Relevance': QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Relevance',
            hasBody={'nb':'relevans'}
        ),
        'http://iso.org/25012/2008/dataquality/Completeness': QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Completeness',
            hasBody={'en':'Completeness'}
        )
    }

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/quality')


    assert extractQualityAnnotation(graph, subject) == expected
