from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import Distribution, SkosConcept
from fdk_rdf_parser.parse_functions import extract_distributions
from fdk_rdf_parser.rdf_utils import dcat_uri


def test_single_distribution() -> None:

    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/distribution>
            a                   dcat:Dataset ;
            dcat:distribution
                [ a                  dcat:Distribution ;
                  dct:conformsTo
                    <https://testconformsto.org> ;
                  dct:title
                    "Testdistribusjon"@nb ;
                  dct:description
                    "Description"@en ;
                  dct:format
                    "json" ;
                  dct:license
                    <https://creativecommons.org/licenses/by/4.0/deed.no> ;
                  dct:type
                    "Feed" ;
                  dcat:accessURL
                    <https://testdistribusjon.no/access> ;
                  foaf:page
                    <https://testdistribusjon.no> ;
                  dcat:downloadURL
                    <https://testdistribusjon.no/download>
                ] ."""

    expected = [
        Distribution(
            conformsTo=[SkosConcept(uri="https://testconformsto.org")],
            title={"nb": "Testdistribusjon"},
            description={"en": "Description"},
            format={"json"},
            license=[
                SkosConcept(uri="https://creativecommons.org/licenses/by/4.0/deed.no")
            ],
            type="Feed",
            accessURL={"https://testdistribusjon.no/access"},
            page=[SkosConcept(uri="https://testdistribusjon.no")],
            downloadURL={"https://testdistribusjon.no/download"},
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model/dataset/distribution")

    assert extract_distributions(graph, subject, dcat_uri("distribution")) == expected


def test_multiple_distributions() -> None:
    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/distribution>
            a                   dcat:Dataset ;
            dcat:distribution
                [ a                  dcat:Distribution ;
                  dct:title          "Testdistribusjon"@nb ;
                  dct:description    "Distribusjon json"@nb ;
                  dct:format         "json" ;
                  dct:license
                    <https://creativecommons.org/licenses/by/4.0/deed.no> ;
                  dcat:accessURL
                    <https://testdistribusjon.no/access>
                ] ;
            dcat:distribution
                <https://testdirektoratet.no/model/distribution/0> ,
                <https://testdirektoratet.no/model/distribution/1> .

        <https://testdirektoratet.no/model/distribution/0>
            a                  dcat:Distribution ;
            dct:title          "Testdistribusjon"@nb ;
            dct:description    "Distribusjon xml"@nb ;
            dct:format         "xml" ;
            dct:license        <https://creativecommons.org/licenses/by/4.0/deed.no> ;
            dcat:accessURL     <https://testdistribusjon.no/access> ."""

    expected = [
        Distribution(
            title={"nb": "Testdistribusjon"},
            description={"nb": "Distribusjon json"},
            format={"json"},
            license=[
                SkosConcept(uri="https://creativecommons.org/licenses/by/4.0/deed.no")
            ],
            accessURL={"https://testdistribusjon.no/access"},
        ),
        Distribution(
            uri="https://testdirektoratet.no/model/distribution/0",
            title={"nb": "Testdistribusjon"},
            description={"nb": "Distribusjon xml"},
            format={"xml"},
            license=[
                SkosConcept(uri="https://creativecommons.org/licenses/by/4.0/deed.no")
            ],
            accessURL={"https://testdistribusjon.no/access"},
        ),
        Distribution(uri="https://testdirektoratet.no/model/distribution/1"),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model/dataset/distribution")

    assert extract_distributions(graph, subject, dcat_uri("distribution")) == expected
