from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import (
    EuDataTheme,
    Eurovoc,
    PartialDcatResource,
    Publisher,
    ReferenceDataCode,
)
from fdk_rdf_parser.parse_functions import parse_dcat_resource


def test_dcat_resource_parser() -> None:
    src = """
@prefix at:    <http://publications.europa.eu/ontology/authority/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dc:   <http://purl.org/dc/elements/1.1/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

<https://testdirektoratet.no/model/dataset/dcatresource>
        a                         dcat:Dataset ;
        dct:accessRights
            <http://pubs.europa.eu/resource/authority/access-right/PUBLIC> ;
        dct:accrualPeriodicity
            <http://pubs.europa.eu/resource/authority/frequency> ;
        dct:description
            "Beskrivelse av datasett 0"@nb , "Description of dataset 0"@en ;
        dct:identifier
            "adb4cf00-31c8-460c-9563-55f204cf8221" ;
        dct:publisher
            <http://data.brreg.no/enhetsregisteret/enhet/987654321> ;
        dct:title                 "Datasett 0"@nb , "Dataset 0"@en ;
        dcat:endpointDescription
            <https://testdirektoratet.no/openapi/dataset/0.yaml> ;
        dct:issued                "2019-03-22T13:11:16.546902"^^xsd:dateTime ;
        dct:modified              "2019-03-23T13:11:16.546902"^^xsd:dateTime ;
        dct:language
            <http://publications.europa.eu/resource/authority/language/NOR> ;
        dcat:landingPage          <https://testdirektoratet.no> ;
        dct:temporal              [ a                          dct:PeriodOfTime ;
                                    dcat:startDate
                                        "2019-04-02T00:00:00"^^xsd:dateTime ] ;
        dcat:keyword              "test"@nb ;
        dcat:theme
            <http://publications.europa.eu/resource/authority/data-theme/GOVE> ,
            <http://publications.europa.eu/resource/authority/data-theme/TECH> ,
            <http://eurovoc.europa.eu/1338> ;
        dct:subject               <https://testdirektoratet.no/model/concept/0> ,
                                  <https://testdirektoratet.no/model/concept/1> ;
        dct:type                  "Kodelister" ;
        foaf:page                 <https://testdirektoratet.no> .

<http://publications.europa.eu/resource/authority/language/NOR>
        a           skos:Concept;
        at:authority-code      "NOR";
        skos:prefLabel     "Norwegian"@en , "Norsk"@nb , "Norsk"@nn , "Norsk"@no .

<http://publications.europa.eu/resource/authority/data-theme/GOVE>
        skos:prefLabel	"Forvaltning og offentleg sektor"@nn ;
        skos:prefLabel	"Government and public sector"@en ;
        skos:prefLabel	"Forvaltning og offentlig sektor"@nb ;
        skos:prefLabel	"Forvaltning og offentlig sektor"@no .

<http://publications.europa.eu/resource/authority/data-theme/TECH>
        skos:prefLabel	"Vitskap og teknologi"@nn ;
        skos:prefLabel	"Science and technology"@en ;
        skos:prefLabel	"Vitenskap og teknologi"@nb ;
        skos:prefLabel	"Vitenskap og teknologi"@no .

<http://eurovoc.europa.eu/1338>
        skos:prefLabel  "India"@en ;
        <https://fellesdatakatalog.digdir.no/ontology/internal/themePath> "8367/1338" ;
        <https://fellesdatakatalog.digdir.no/ontology/internal/themePath> "c_964c9649/1338" ;
        <https://fellesdatakatalog.digdir.no/ontology/internal/themePath> "2848/1338" ."""

    expected = PartialDcatResource(
        identifier={"adb4cf00-31c8-460c-9563-55f204cf8221"},
        title={"nb": "Datasett 0", "en": "Dataset 0"},
        description={
            "nb": "Beskrivelse av datasett 0",
            "en": "Description of dataset 0",
        },
        descriptionFormatted={
            "nb": "Beskrivelse av datasett 0",
            "en": "Description of dataset 0",
        },
        uri="https://testdirektoratet.no/model/dataset/dcatresource",
        accessRights=ReferenceDataCode(
            uri="http://pubs.europa.eu/resource/authority/access-right/PUBLIC"
        ),
        publisher=Publisher(
            uri="http://data.brreg.no/enhetsregisteret/enhet/987654321"
        ),
        themeUris=[
            "http://eurovoc.europa.eu/1338",
            "http://publications.europa.eu/resource/authority/data-theme/GOVE",
            "http://publications.europa.eu/resource/authority/data-theme/TECH",
        ],
        theme=[
            EuDataTheme(
                uri="http://publications.europa.eu/resource/authority/data-theme/GOVE",
                code="GOVE",
                title={
                    "nn": "Forvaltning og offentleg sektor",
                    "no": "Forvaltning og offentlig sektor",
                    "nb": "Forvaltning og offentlig sektor",
                    "en": "Government and public sector",
                },
            ),
            EuDataTheme(
                uri="http://publications.europa.eu/resource/authority/data-theme/TECH",
                code="TECH",
                title={
                    "nn": "Vitskap og teknologi",
                    "no": "Vitenskap og teknologi",
                    "nb": "Vitenskap og teknologi",
                    "en": "Science and technology",
                },
            ),
        ],
        eurovocThemes=[
            Eurovoc(
                uri="http://eurovoc.europa.eu/1338",
                code="1338",
                label={"en": "India"},
                eurovocPaths=["2848/1338", "8367/1338", "c_964c9649/1338"],
            )
        ],
        keyword=[{"nb": "test"}],
        issued="2019-03-22T13:11:16",
        modified="2019-03-23T13:11:16",
        language=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/language/NOR",
                code="NOR",
                prefLabel={
                    "en": "Norwegian",
                    "nb": "Norsk",
                    "nn": "Norsk",
                    "no": "Norsk",
                },
            )
        ],
        landingPage={"https://testdirektoratet.no"},
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/dcatresource")

    assert parse_dcat_resource(graph, subject) == expected


def test_description_html_cleaner() -> None:
    src = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .

<https://testdirektoratet.no/model/dataset/dcatresource>
        a                         dcat:Dataset ;
        dct:description
            "<p>Beskrivelse av &#60;<a>datasett&nbsp;0</a>&#62;</p>"@nb ,
            "<p>Description of &#60;<a>dataset&nbsp;0</a>&#62;</p>"@en ."""

    expected = PartialDcatResource(
        uri="https://testdirektoratet.no/model/dataset/dcatresource",
        description={
            "nb": "Beskrivelse av datasett0",
            "en": "Description of dataset0",
        },
        descriptionFormatted={
            "nb": "<p>Beskrivelse av &#60;<a>datasett&nbsp;0</a>&#62;</p>",
            "en": "<p>Description of &#60;<a>dataset&nbsp;0</a>&#62;</p>",
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/dcatresource")

    assert parse_dcat_resource(graph, subject) == expected


def test_nb_is_default_language() -> None:
    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dct:title               "Språktest" ;
                dct:description         "De som mangler språk-tag får tildelt bokmål" ;
                dcat:keyword            "test" ."""

    expected = PartialDcatResource(
        uri="https://testdirektoratet.no/model/dataset/0",
        title={"nb": "Språktest"},
        description={"nb": "De som mangler språk-tag får tildelt bokmål"},
        descriptionFormatted={"nb": "De som mangler språk-tag får tildelt bokmål"},
        keyword=[{"nb": "test"}],
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/0")

    assert parse_dcat_resource(graph, subject) == expected
