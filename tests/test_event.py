from unittest.mock import Mock

from rdflib import Graph, URIRef

from fdk_rdf_parser import parse_events
from fdk_rdf_parser.classes import BusinessEvent, LifeEvent, Publisher, SkosConcept
from fdk_rdf_parser.parse_functions import extract_events
from fdk_rdf_parser.rdf_utils import cv_uri


def test_parse_events(
    mock_organizations_and_reference_data: Mock,
) -> None:
    src = """
            @prefix cpsv: <http://purl.org/vocab/cpsv#> .
            @prefix dct: <http://purl.org/dc/terms/> .
            @prefix cv: <http://data.europa.eu/m8g/> .
            @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
            @prefix dcat:  <http://www.w3.org/ns/dcat#> .
            @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
            @prefix schema:  <http://schema.org/> .
            @prefix eli: <http://data.europa.eu/eli/ontology#> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> a cv:BusinessEvent ;
                dct:identifier "1" ;
                dct:title "Starte og drive restaurant"@nb ;
                dct:description "Elektronisk prosess for etablering og oppstart av en bedrift."@nb ;
                dct:type <https://data.norge.no/concepts/300> ;
                dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ,
                            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> ;
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/events/2> a cv:LifeEvent ;
                dct:identifier "2" ;
                dct:title "Oppgjør etter dødsfall"@nb ;
                dct:description "Elektronisk prosess for oppgjør etter dødsfall."@nb ;
                dct:type <https://data.norge.no/concepts/308> ;
                dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ;
                cv:hasCompetentAuthority    <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/123456789> ;
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> a cpsv:PublicService ;
                    cv:hasCompetentAuthority    <http://public-service-publisher.fellesdatakatalog.digdir.no/public-organisation/3> ;
                    cv:isGroupedBy              <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    dct:description             "Dette skjemaet  brukes for å registrere en ny virksomhet, eller søke om godkjenning av en ny næringsmiddelvirksomhet. Skjemaet skal også brukes dersom du vil utvide aktiviteten i en allerede eksisterende virksomhet og starte med en ny aktivitet som ikke er registrert."@nb ;
                    dct:identifier              "2" ;
                    dct:title                   "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"@nb
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                    cv:hasCompetentAuthority    <http://public-service-publisher.fellesdatakatalog.digdir.no/public-organisation/3> ;
                    cv:isGroupedBy              <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    dct:description             "Dette skjemaet  brukes for å registrere en ny virksomhet, eller søke om godkjenning av en ny næringsmiddelvirksomhet. Skjemaet skal også brukes dersom du vil utvide aktiviteten i en allerede eksisterende virksomhet og starte med en ny aktivitet som ikke er registrert."@nb ;
                    dct:identifier              "1" ;
                    dct:title                   "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"@nb
            .

            <https://data.norge.no/concepts/300> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <https://data.norge.no/concepts/308> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <http://localhost:5000/services/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
            ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/events/1": BusinessEvent(
            id="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av en bedrift."
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/300",
                    prefLabel={"nb": "Dødsfall og arv"},
                    extraType=None,
                )
            ],
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/events/2": LifeEvent(
            id="http://public-service-publisher.fellesdatakatalog.digdir.no/events/2",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/2",
            identifier="2",
            title={"nb": "Oppgjør etter dødsfall"},
            description={"nb": "Elektronisk prosess for oppgjør etter dødsfall."},
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/308",
                    prefLabel={"nb": "Dødsfall og arv"},
                    extraType=None,
                )
            ],
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/123456789",
                    id=None,
                    name=None,
                    orgPath=None,
                    prefLabel=None,
                    organisasjonsform=None,
                )
            ],
        ),
    }

    assert parse_events(src) == expected


def test_extract_single_event() -> None:

    src = """
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event>
                a                         cpsv:PublicService ;
                cv:isGroupedBy
                    [ a                          cv:BusinessEvent ;
                        dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                        dct:identifier   "1" ;
                        dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                        dct:title        "Starte og drive restaurant"@nb ;
                        dct:type         <https://data.norge.no/concpets/livshendelse>
                    ],
                    [ a                          cv:Event ;
                        dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                        dct:identifier   "1" ;
                        dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                        dct:title        "Starte og drive restaurant"@nb ;
                        dct:type         <https://data.norge.no/concpets/livshendelse>
                    ],
                    [ a                          cv:LifeEvent ;
                        dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                        dct:identifier   "1" ;
                        dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                        dct:title        "Starte og drive restaurant"@nb ;
                        dct:type         <https://data.norge.no/concpets/livshendelse>
                    ]."""

    expected = [
        LifeEvent(
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
        ),
        BusinessEvent(
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event"
    )

    assert extract_events(graph, subject, cv_uri("isGroupedBy")) == expected


def test_extract_several_events() -> None:

    src = """
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event>
                a                         cpsv:PublicService ;
                cv:isGroupedBy
                    [ a                          cv:BusinessEvent ;
                        dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                        dct:identifier   "1" ;
                        dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                        dct:title        "Starte og drive restaurant"@nb ;
                        dct:type         <https://data.norge.no/concpets/livshendelse>
                    ] ;
                cv:isGroupedBy
                    <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>
                a                cv:BusinessEvent ;
                dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                dct:identifier   "1" ;
                dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                dct:title        "Starte og drive restaurant"@nb ;
                dct:type         <https://data.norge.no/concpets/livshendelse> ."""

    expected = [
        BusinessEvent(
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
        ),
        BusinessEvent(
            id="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event"
    )

    assert extract_events(graph, subject, cv_uri("isGroupedBy")) == expected
