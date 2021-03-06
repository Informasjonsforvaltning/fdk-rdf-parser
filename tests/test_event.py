from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import Event
from fdk_rdf_parser.parse_functions import extract_events


def test_single_contact_point() -> None:

    src = """
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event>
                a                         cpsv:PublicService ;
                cv:isGroupedBy
                    [ a                          cv:Event ;
                        dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                        dct:identifier   "1" ;
                        dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                        dct:title        "Starte og drive restaurant"@nb ;
                        dct:type         <https://data.norge.no/concpets/livshendelse>
                    ] ."""

    expected = [
        Event(
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            type="https://data.norge.no/concpets/livshendelse",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event"
    )

    assert extract_events(graph, subject) == expected


def test_several_events() -> None:

    src = """
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event>
                a                         cpsv:PublicService ;
                cv:isGroupedBy
                    [ a                          cv:Event ;
                        dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                        dct:identifier   "1" ;
                        dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                        dct:title        "Starte og drive restaurant"@nb ;
                        dct:type         <https://data.norge.no/concpets/livshendelse>
                    ] ;
                cv:isGroupedBy
                    <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>
                a                cv:Event ;
                dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                dct:identifier   "1" ;
                dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                dct:title        "Starte og drive restaurant"@nb ;
                dct:type         <https://data.norge.no/concpets/livshendelse> ."""

    expected = [
        Event(
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            type="https://data.norge.no/concpets/livshendelse",
        ),
        Event(
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            identifier="1",
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
            },
            type="https://data.norge.no/concpets/livshendelse",
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"http://public-service-publisher.fellesdatakatalog.digdir.no/model/public-service/event"
    )

    assert extract_events(graph, subject) == expected
