"""Test cases."""
import pytest

from fdk_rdf_parser.classes import ContactPoint
from fdk_rdf_parser.parse_functions import extractContactPoints
from rdflib import Graph, URIRef

def test_single_contact_point():

    src = """
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/contact>
                a                         dcat:Dataset ;
                dcat:contactPoint         [ a                          vcard:Organization ;
                                            vcard:hasTelephone         "23453345" ;
                                            vcard:hasOrganizationName  "Testdirektoratet" ;
                                            vcard:hasURL               <https://testdirektoratet.no>
                                        ] ."""

    expected = [
        ContactPoint(
            organizationName='Testdirektoratet',
            hasURL='https://testdirektoratet.no',
            hasTelephone='23453345'
        )]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/contact')


    assert extractContactPoints(graph, subject) == expected

def test_several_contact_points():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/contact>
                a                         dcat:Dataset ;
                dcat:contactPoint         [ a                          vcard:Organization ;
                                            vcard:hasEmail             "post@mail.com" ;
                                            vcard:hasOrganizationName  "Testdirektoratet" ;
                                            vcard:organization-unit    "Testenhet" ;
                                            vcard:hasURL               <https://testdirektoratet.no>
                                        ] ;
                dcat:contactPoint         <https://testdirektoratet.no/kontakt/testmann> ;
                dcat:contactPoint         <https://testdirektoratet.no/kontakt/testmann2> .

        <https://testdirektoratet.no/kontakt/testmann>
                a                          vcard:Organization ;
                vcard:fn                   "Test Mann" ;
                vcard:hasTelephone         <tel:12345678> ;
                vcard:hasEmail             <mailto:testmann@mail.com> ."""

    expected = [
                ContactPoint(
                    email='post@mail.com',
                    organizationName='Testdirektoratet',
                    organizationUnit='Testenhet',
                    hasURL='https://testdirektoratet.no'),
                ContactPoint(
                    uri='https://testdirektoratet.no/kontakt/testmann',
                    fullname="Test Mann",
                    email="testmann@mail.com",
                    hasTelephone="12345678"),
                ContactPoint(uri='https://testdirektoratet.no/kontakt/testmann2')
            ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/contact')


    assert extractContactPoints(graph, subject) == expected
