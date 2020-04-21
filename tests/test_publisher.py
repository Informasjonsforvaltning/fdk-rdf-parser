"""Test cases."""
import pytest

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.parse_functions import extractPublisher
from rdflib import Graph, URIRef

def test_uriref_publisher():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/publisher>
                a               dcat:Dataset ;
                dct:publisher   <https://blabla.no/organisasjoner/qwesadzx-5544-rree-6677-1234213fdaaw> .
                                        
        <https://blabla.no/organisasjoner/qwesadzx-5544-rree-6677-1234213fdaaw>
                a                        vcard:Kind , foaf:Agent ;
                dct:identifier           "112233445" ;
                dct:type                 <http://purl.org/adms/publishertype/NationalAuthority> ;
                <http://www.w3.org/2002/07/owl#sameAs>
                        "http://data.brreg.no/enhetsregisteret/enhet/112233445" ;
                vcard:hasEmail           <mailto:mail@test.no> ;
                vcard:organization-name  "Norsk testorganisasjon" ;
                foaf:mbox                "mail@test.no" ;
                foaf:name                "Norsk testorganisasjon" ."""

    expected = Publisher(
        uri = 'https://blabla.no/organisasjoner/qwesadzx-5544-rree-6677-1234213fdaaw',
        id = '112233445'
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/publisher')

    assert extractPublisher(graph, subject) == expected

def test_bnode_publisher():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/publisher>
                a               dcat:Dataset ;
                dct:publisher   [ a                 vcard:Kind , foaf:Agent ;
                                  dct:identifier    "123456789" ] ."""

    expected = Publisher(
        id = '123456789'
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/publisher')

    assert extractPublisher(graph, subject) == expected