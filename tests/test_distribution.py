"""Test cases."""
import pytest

from fdk_rdf_parser.classes import Distribution
from fdk_rdf_parser.parse_functions import extractDistributions
from rdflib import Graph, URIRef

def test_single_distribution():

    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/distribution>
            a                   dcat:Dataset ;
            dcat:distribution   [ a                  dcat:Distribution ;
                                  dct:conformsTo     <https://testconformsto.org> ;
                                  dct:title          "Testdistribusjon"@nb ;
                                  dct:description    "Description"@en ;
                                  dct:format         "json" ;
                                  dct:license        <https://creativecommons.org/licenses/by/4.0/deed.no> ;
                                  dct:type           "Feed" ;
                                  dcat:accessURL     <https://testdistribusjon.no/access> ;
                                  foaf:page          <https://testdistribusjon.no> ;
                                  dcat:downloadURL   <https://testdistribusjon.no/download> ;
                                  dcat:accessService <https://testdistribusjon.no/service>
                                ] ."""

    expected = [
        Distribution(
            conformsTo=['https://testconformsto.org'],
            title={'nb':'Testdistribusjon'},
            description={'en':'Description'},
            format=['json'],
            license='https://creativecommons.org/licenses/by/4.0/deed.no',
            type='Feed',
            accessURL=['https://testdistribusjon.no/access'],
            page=['https://testdistribusjon.no'],
            downloadURL=['https://testdistribusjon.no/download'],
            accessService='https://testdistribusjon.no/service'
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/distribution')


    assert extractDistributions(graph, subject) == expected

def test_multiple_distributions():
    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/distribution>
            a                   dcat:Dataset ;
            dcat:distribution   [ a                  dcat:Distribution ;
                                  dct:title          "Testdistribusjon"@nb ;
                                  dct:description    "Distribusjon json"@nb ;
                                  dct:format         "json" ;
                                  dct:license        <https://creativecommons.org/licenses/by/4.0/deed.no> ;
                                  dcat:accessURL     <https://testdistribusjon.no/access> 
                                ] ;
            dcat:distribution   <https://testdirektoratet.no/model/distribution/0> , <https://testdirektoratet.no/model/distribution/1>.
            
        <https://testdirektoratet.no/model/distribution/0>
            a                  dcat:Distribution ;
            dct:title          "Testdistribusjon"@nb ;
            dct:description    "Distribusjon xml"@nb ;
            dct:format         "xml" ;
            dct:license        <https://creativecommons.org/licenses/by/4.0/deed.no> ;
            dcat:accessURL     <https://testdistribusjon.no/access> ."""

    expected = [
        Distribution(
            title={'nb':'Testdistribusjon'},
            description={'nb':'Distribusjon json'},
            format=['json'],
            license='https://creativecommons.org/licenses/by/4.0/deed.no',
            accessURL=['https://testdistribusjon.no/access']
        ),
        Distribution(
            uri='https://testdirektoratet.no/model/distribution/0',
            title={'nb':'Testdistribusjon'},
            description={'nb':'Distribusjon xml'},
            format=['xml'],
            license='https://creativecommons.org/licenses/by/4.0/deed.no',
            accessURL=['https://testdistribusjon.no/access']
        ),
        Distribution(
            uri='https://testdirektoratet.no/model/distribution/1'
        )
    ]
