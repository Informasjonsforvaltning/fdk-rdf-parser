from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.parse_functions import extractPublisher


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
        prefLabel={"nb": "Norsk testorganisasjon"},
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model/dataset/publisher")
    catalog_subject = URIRef(u"https://testdirektoratet.no/model/dataset/catalog")

    assert extractPublisher(graph, subject, catalog_subject) == expected


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
    subject = URIRef(u"https://testdirektoratet.no/model/dataset/publisher")
    catalog_subject = URIRef(u"https://testdirektoratet.no/model/dataset/catalog")

    assert extractPublisher(graph, subject, catalog_subject) == expected


def test_uses_catalog_publisher_when_none_exists_on_resource() -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/dataservices/0>
            a                         dcat:DataService ;
            dcat:endpointDescription  <https://testdirektoratet.no/specification/dataservice-0.yaml> .

        <https://testdirektoratet.no/catalogs/0>
            a              dcat:Catalog ;
            dct:publisher  <https://testdirektoratet.no/organizations/123456789> ;
            dct:title      "Dataservicekatalog 0"@nb ;
            dcat:service   <https://testdirektoratet.no/dataservices/0> ."""

    expected = Publisher(uri="https://testdirektoratet.no/organizations/123456789")

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/dataservices/0")
    catalog_subject = URIRef(u"https://testdirektoratet.no/catalogs/0")

    assert extractPublisher(graph, subject, catalog_subject) == expected
