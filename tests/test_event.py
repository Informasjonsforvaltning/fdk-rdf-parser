from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import BusinessEvent, LifeEvent, SkosConcept
from fdk_rdf_parser.parse_functions import extract_events
from fdk_rdf_parser.rdf_utils import cv_uri


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
            type=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
            event_type="life_event",
        ),
        BusinessEvent(
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            type=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
            event_type="business_event",
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
            type=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
            event_type="business_event",
        ),
        BusinessEvent(
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            type=[
                SkosConcept(
                    uri="https://data.norge.no/concpets/livshendelse",
                )
            ],
            event_type="business_event",
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event"
    )

    assert extract_events(graph, subject, cv_uri("isGroupedBy")) == expected
