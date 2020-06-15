import isodate
from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import PartialDcatResource, PublisherId, SkosCode, ThemeEU
from fdk_rdf_parser.parse_functions import parseDcatResource


def test_dcat_resource_parser() -> None:

    src = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

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
            <http://pubs.europa.eu/resource/authority/language/NOR> ;
        dcat:landingPage          <https://testdirektoratet.no> ;
        dct:temporal              [ a                          dct:PeriodOfTime ;
                                    dcat:startDate
                                        "2019-04-02T00:00:00"^^xsd:dateTime ] ;
        dcat:keyword              "test"@nb ;
        dcat:theme
            <http://pubs.europa.eu/resource/authority/data-theme/GOVE> ,
            <http://pubs.europa.eu/resource/authority/data-theme/TECH> ;
        dct:subject               <https://testdirektoratet.no/model/concept/0> ,
                                  <https://testdirektoratet.no/model/concept/1> ;
        dct:type                  "Kodelister" ;
        foaf:page                 <https://testdirektoratet.no> ."""

    expected = PartialDcatResource(
        identifier=["adb4cf00-31c8-460c-9563-55f204cf8221"],
        title={"nb": "Datasett 0", "en": "Dataset 0"},
        description={
            "nb": "Beskrivelse av datasett 0",
            "en": "Description of dataset 0",
        },
        uri="https://testdirektoratet.no/model/dataset/dcatresource",
        accessRights=SkosCode(
            uri="http://pubs.europa.eu/resource/authority/access-right/PUBLIC"
        ),
        publisher=PublisherId(
            uri="http://data.brreg.no/enhetsregisteret/enhet/987654321"
        ),
        theme=[
            ThemeEU("http://pubs.europa.eu/resource/authority/data-theme/GOVE"),
            ThemeEU("http://pubs.europa.eu/resource/authority/data-theme/TECH"),
        ],
        keyword=[{"nb": "test"}],
        issued=isodate.parse_datetime("2019-03-22T13:11:16.546902"),
        modified=isodate.parse_datetime("2019-03-23T13:11:16.546902"),
        language=[
            SkosCode(uri="http://pubs.europa.eu/resource/authority/language/NOR")
        ],
        landingPage=["https://testdirektoratet.no"],
        type="Kodelister",
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model/dataset/dcatresource")

    assert parseDcatResource(graph, subject) == expected
