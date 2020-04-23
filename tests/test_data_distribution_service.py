"""Test cases."""
import pytest

from fdk_rdf_parser.classes import Distribution, DataDistributionService, SkosConcept
from fdk_rdf_parser.parse_functions import extractDistributions
from rdflib import Graph, URIRef
from fdk_rdf_parser.rdf_utils import dcatURI

def test_bnode_distribution_access_service():

    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix dcatapi: <http://dcat.no/dcatapi/> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/distributionservice>
            a                   dcat:Dataset ;
            dcat:distribution   
                    [ a     dcat:Distribution ;
                      dcatapi:accessService
                            [ a                 dcatapi:DataDistributionService ;
                              dcatapi:endpointDescription  
                                    [ a           foaf:Document , skos:Concept ;
                                      dct:source  "https://testdirektoratet.no/model/0"
                                    ] ;
                              dct:description   "DESCRIPTION"@en
                            ]
                    ] ."""

    expected = [
        Distribution(
            accessService = [
                DataDistributionService(
                    description = {'en':'DESCRIPTION'},
                    endpointDescription = [SkosConcept(
                        uri = 'https://testdirektoratet.no/model/0',
                        extraType = 'http://xmlns.com/foaf/0.1/Document'
                    )]
                )
            ]
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/distributionservice')

    assert extractDistributions(graph, subject, dcatURI('distribution')) == expected

def test_uriref_distribution_access_service():
    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatapi: <http://dcat.no/dcatapi/> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/distributionservice>
            a                   dcat:Dataset ;
            dcat:distribution   <https://testdirektoratet.no/model/distribution/0> .
            
        <https://testdirektoratet.no/model/distribution/0>
            a                         dcat:Distribution ;
            dcatapi:accessService     <https://testdistribusjon.no/accessservice/0> , <https://testdistribusjon.no/accessservice/1> .
            
        <https://testdistribusjon.no/accessservice/0>
                a                               dcatapi:DataDistributionService ;
                dcatapi:endpointDescription     [ a           foaf:Document , skos:Concept ;
                                                  dct:source  "https://testdirektoratet.no/model/1"
                                                ] ;
                dct:description                 "Beskrivelse 0"@nb ;
                dct:title                       "Tittel 0"@nb .

        <https://testdistribusjon.no/accessservice/1>
                a                               dcatapi:DataDistributionService ;
                dcatapi:endpointDescription     [ a           foaf:Document , skos:Concept ;
                                                  dct:source  "https://testdirektoratet.no/model/2"
                                                ] ;
                dct:description                 "Beskrivelse 1"@nb ;
                dct:title                       "Tittel 1"@nb .
        """

    expected = [
        Distribution(
            uri = 'https://testdirektoratet.no/model/distribution/0',
            accessService = [
                DataDistributionService(
                    uri = 'https://testdistribusjon.no/accessservice/0',
                    title = {'nb':'Tittel 0'},
                    description = {'nb':'Beskrivelse 0'},
                    endpointDescription = [SkosConcept(
                        uri = 'https://testdirektoratet.no/model/1',
                        extraType = 'http://xmlns.com/foaf/0.1/Document'
                    )]
                ),
                DataDistributionService(
                    uri = 'https://testdistribusjon.no/accessservice/1',
                    title = {'nb':'Tittel 1'},
                    description = {'nb':'Beskrivelse 1'},
                    endpointDescription = [SkosConcept(
                        uri = 'https://testdirektoratet.no/model/2',
                        extraType = 'http://xmlns.com/foaf/0.1/Document'
                    )]
                )
            ]
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/distributionservice')

    assert extractDistributions(graph, subject, dcatURI('distribution')) == expected
