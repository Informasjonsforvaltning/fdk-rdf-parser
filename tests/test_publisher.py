from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.parse_functions import extract_publisher
from fdk_rdf_parser.parse_functions.publisher import (
    extract_list_of_publishers,
    set_publisher_name_from_pref_label_if_missing,
)
from fdk_rdf_parser.rdf_utils.ns import cv_uri


def test_uriref_publisher() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/publisher>
                a               dcat:Dataset ;
                dct:publisher
                    <https://blabla.no/organisasjoner/qwesadzx> .

        <https://blabla.no/organisasjoner/qwesadzx>
                a                        vcard:Kind , foaf:Agent ;
                dct:identifier           "112233445" ;
                dct:type
                    <http://purl.org/adms/publishertype/NationalAuthority> ;
                <http://www.w3.org/2002/07/owl#sameAs>
                        "http://data.brreg.no/enhetsregisteret/enhet/112233445" ;
                vcard:hasEmail           <mailto:mail@test.no> ;
                vcard:organization-name  "Norsk testorganisasjon" ;
                foaf:mbox                "mail@test.no" ;
                foaf:name                "Norsk testorganisasjon" ."""

    expected = Publisher(
        uri="https://blabla.no/organisasjoner/qwesadzx",
        id="112233445",
        name="Norsk testorganisasjon",
        prefLabel={"nb": "Norsk testorganisasjon"},
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/publisher")

    assert extract_publisher(graph, subject) == expected


def test_bnode_publisher() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/publisher>
                a               dcat:Dataset ;
                dct:publisher   [ a                 vcard:Kind , foaf:Agent ;
                                  dct:identifier    "123456789" ] ."""

    expected = Publisher(id="123456789")

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/publisher")

    assert extract_publisher(graph, subject) == expected


def test_set_name_from_label() -> None:
    input_0 = Publisher(id="123456789")
    expected_0 = Publisher(id="123456789")
    input_1 = Publisher(id="123456789", name="Original", prefLabel={"nb": "Bokmål"})
    expected_1 = Publisher(id="123456789", name="Original", prefLabel={"nb": "Bokmål"})
    input_2 = Publisher(id="123456789", prefLabel={"nb": "Bokmål"})
    expected_2 = Publisher(id="123456789", name="Bokmål", prefLabel={"nb": "Bokmål"})
    input_3 = Publisher(id="123456789", prefLabel={"no": "Norsk"})
    expected_3 = Publisher(id="123456789", name="Norsk", prefLabel={"no": "Norsk"})
    input_4 = Publisher(id="123456789", prefLabel={"nn": "Nynorsk"})
    expected_4 = Publisher(id="123456789", name="Nynorsk", prefLabel={"nn": "Nynorsk"})
    input_5 = Publisher(id="123456789", prefLabel={"en": "English"})
    expected_5 = Publisher(id="123456789", name="English", prefLabel={"en": "English"})
    input_6 = Publisher(id="123456789", prefLabel={})
    expected_6 = Publisher(id="123456789", prefLabel={})

    assert set_publisher_name_from_pref_label_if_missing(input_0) == expected_0
    assert set_publisher_name_from_pref_label_if_missing(input_1) == expected_1
    assert set_publisher_name_from_pref_label_if_missing(input_2) == expected_2
    assert set_publisher_name_from_pref_label_if_missing(input_3) == expected_3
    assert set_publisher_name_from_pref_label_if_missing(input_4) == expected_4
    assert set_publisher_name_from_pref_label_if_missing(input_5) == expected_5
    assert set_publisher_name_from_pref_label_if_missing(input_6) == expected_6


def test_list_of_publishers() -> None:
    src = """@prefix cpsvno: <https://data.norge.no/vocabulary/cpsvno#> .
        @prefix cv:     <http://data.europa.eu/m8g/> .
        @prefix dct:    <http://purl.org/dc/terms/> .
        @prefix org:    <http://www.w3.org/ns/org#> .
        @prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

        <https://testdirektoratet.no/model/service/publishers>
                a               cpsvno:Service ;
                cv:ownedBy      [
                    a              org:Organization;
                    dct:identifier "https://www.staging.fellesdatakatalog.digdir.no/organizations/123"^^xsd:anyURI ] ."""

    expected = [
        Publisher(
            id="https://www.staging.fellesdatakatalog.digdir.no/organizations/123"
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/service/publishers")

    assert extract_list_of_publishers(graph, subject, cv_uri("ownedBy")) == expected


def test_empty_list_of_publishers_is_none() -> None:
    src = """@prefix cpsvno: <https://data.norge.no/vocabulary/cpsvno#> .
        <https://testdirektoratet.no/model/service/no-publishers>
                a               cpsvno:Service ."""

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/service/no-publishers")

    assert extract_list_of_publishers(graph, subject, cv_uri("ownedBy")) is None
