from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import ContactPoint
from fdk_rdf_parser.parse_functions import extract_contact_points


def test_single_contact_point() -> None:

    src = """
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/contact>
                a                         dcat:Dataset ;
                dcat:contactPoint
                    [ a                          vcard:Organization ;
                      vcard:hasTelephone         "23453345" ;
                      vcard:hasOrganizationName  "Testdirektoratet"@nb ;
                      vcard:hasURL               <https://testdirektoratet.no>
                    ] ."""

    expected = [
        ContactPoint(
            organizationName={"nb": "Testdirektoratet"},
            hasURL="https://testdirektoratet.no",
            hasTelephone="23453345",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/contact")

    assert extract_contact_points(graph, subject) == expected


def test_several_contact_points() -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/contact>
                a                         dcat:Dataset ;
                dcat:contactPoint
                    [ a                          vcard:Organization ;
                      vcard:hasEmail             "post@mail.com" ;
                      vcard:hasOrganizationName  "Testdirektoratet"@nb , "Testdirektoratet"@nn , "Directorate of test"@en ;
                      vcard:organization-unit    "Testenhet"@nb , "Testenhet"@nn , "Test unit"@en ;
                      vcard:hasURL               <https://testdirektoratet.no>
                    ] ;
                dcat:contactPoint
                    <https://testdirektoratet.no/kontakt/testmann> ;
                dcat:contactPoint
                    <https://testdirektoratet.no/kontakt/testmann2> .

        <https://testdirektoratet.no/kontakt/testmann>
                a                          vcard:Organization ;
                vcard:fn                   "Test Mann" ;
                vcard:hasTelephone         <tel:12345678> ;
                vcard:hasEmail             <mailto:testmann@mail.com> ."""

    expected = [
        ContactPoint(
            email="post@mail.com",
            organizationName={
                "nb": "Testdirektoratet",
                "nn": "Testdirektoratet",
                "en": "Directorate of test",
            },
            organizationUnit={"nb": "Testenhet", "nn": "Testenhet", "en": "Test unit"},
            hasURL="https://testdirektoratet.no",
        ),
        ContactPoint(
            uri="https://testdirektoratet.no/kontakt/testmann",
            fullname="Test Mann",
            email="testmann@mail.com",
            hasTelephone="12345678",
        ),
        ContactPoint(uri="https://testdirektoratet.no/kontakt/testmann2"),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/contact")

    assert extract_contact_points(graph, subject) == expected


def test_telephone_and_email_is_nodes() -> None:

    src = """
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .

        <https://testdirektoratet.no/model/dataset/contact>
                a                         dcat:Dataset ;
                dcat:contactPoint
                    [ a                          vcard:Organization ;
                      vcard:hasTelephone         <https://testdirektoratet.no/telephone> ;
                      vcard:hasEmail             [ a               vcard:Email ;
                                                   vcard:hasValue  "post@mail.com" ]
                    ] .

        <https://testdirektoratet.no/telephone>
            a               vcard:TelephoneType ;
            vcard:hasValue  <tel:99999999> ."""

    expected = [
        ContactPoint(
            email="post@mail.com",
            hasTelephone="99999999",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/contact")

    assert extract_contact_points(graph, subject) == expected
