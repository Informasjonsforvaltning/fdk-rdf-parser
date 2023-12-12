from unittest.mock import Mock

from fdk_rdf_parser import parse_events
from fdk_rdf_parser.classes import (
    BusinessEvent,
    Event,
    HarvestMetaData,
    LifeEvent,
    SkosConcept,
)


def test_parse_events(
    mock_reference_data_client: Mock,
) -> None:
    src = """
            @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
            @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
            @prefix rov:   <http://www.w3.org/ns/regorg#> .
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
                dct:type <https://data.norge.no/concepts/306>, <https://data.norge.no/concepts/312>;
                dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ,
                            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> ;
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/events/2> a cv:LifeEvent ;
                dct:identifier "2" ;
                dct:title "Oppgjør etter dødsfall"@nb ;
                dct:description "Elektronisk prosess for oppgjør etter dødsfall."@nb ;
                dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ;
                cv:hasCompetentAuthority    <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
            .

            <https://data.norge.no/concepts/300> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <https://data.norge.no/concepts/304> a skos:Concept ;
                    skos:broader    <https://data.norge.no/concepts/310> ;
                    skos:narrower   <https://data.norge.no/concepts/306> ;
                    skos:prefLabel  "Drive en bedrift"@nb
            .

            <https://data.norge.no/concepts/306> a skos:Concept ;
                    skos:broader    <https://data.norge.no/concepts/304> ;
                    skos:prefLabel  "Skatt og avgift"@nb
            .

            <https://data.norge.no/concepts/308> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <https://data.norge.no/concepts/310> a skos:Concept ;
                    skos:broader    <https://data.norge.no/concepts/306> ;
                    skos:narrower   <https://data.norge.no/concepts/304> ;
                    skos:prefLabel  "Starte og drive en bedrift"@nb
            .

            <https://data.norge.no/concepts/312> a skos:Concept ;
                    skos:broader    <https://data.norge.no/concepts/313> ;
                    skos:prefLabel  "Test type"@nb
            .

            <https://data.norge.no/concepts/313> a skos:Concept ;
                    skos:prefLabel  "Test type"@nb
            .

            <http://localhost:5000/events/fdk-2>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-2" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/events/2>
            .

            <http://localhost:5000/events/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>
            .

            <http://localhost:5000/events/fdk-4>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-4" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                    cv:isGroupedBy              <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    dct:description             "Dette skjemaet  brukes for å registrere en ny virksomhet, eller søke om godkjenning av en ny næringsmiddelvirksomhet. Skjemaet skal også brukes dersom du vil utvide aktiviteten i en allerede eksisterende virksomhet og starte med en ny aktivitet som ikke er registrert."@nb ;
                    dct:identifier              "4" ;
                    dct:title                   "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"@nb
            .

            <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789>
                    a                      rov:RegisteredOrganization ;
                    dct:identifier         "123456789" ;
                    rov:legalName          "Digitaliseringsdirektoratet" ;
                    foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
                    rov:orgType            orgtype:ORGL ;
                    br:orgPath             "/STAT/987654321/123456789" ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/events/1": BusinessEvent(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            identifier="1",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            title={"nb": "Starte og drive restaurant"},
            description={
                "nb": "Elektronisk prosess for etablering og oppstart av en bedrift."
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/306",
                    prefLabel={"nb": "Skatt og avgift"},
                    broader=["https://data.norge.no/concepts/304"],
                ),
                SkosConcept(
                    uri="https://data.norge.no/concepts/312",
                    prefLabel={"nb": "Test type"},
                    broader=["https://data.norge.no/concepts/313"],
                ),
            ],
            relation=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
                "http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
            ],
            associatedBroaderTypes=[
                "https://data.norge.no/concepts/306",
                "https://data.norge.no/concepts/304",
                "https://data.norge.no/concepts/310",
                "https://data.norge.no/concepts/312",
                "https://data.norge.no/concepts/313",
            ],
            specialized_type="business_event",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/events/2": LifeEvent(
            id="fdk-2",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/2",
            identifier="2",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            title={"nb": "Oppgjør etter dødsfall"},
            description={"nb": "Elektronisk prosess for oppgjør etter dødsfall."},
            relation=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1"
            ],
            specialized_type="life_event",
        ),
    }

    assert parse_events(src) == expected


def test_parse_cv_event(
    mock_reference_data_client: Mock,
) -> None:
    src = """
        @prefix cpsvno:    <https://data.norge.no/vocabulary/cpsvno#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHendelse.ttl>
            a                   cv:Event ;
            dct:description     "Teksten blir vist på nynorsk."@nn , "The text is displayed in English."@en , "Det er fattet vedtak om å gi skjenkebevilling til «Den beste restauranten AS», for servering av alkoholholdig drikk i gruppe 1, jf. Alkoholloven § 4-2"@nb ;
            dct:identifier      "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHendelse.ttl"^^xsd:anyURI ;
            dct:subject         <https://data.norge.no/concepts/ad2ab3f9-17a1-4494-b15e-4ba3967a6424> ;
            dct:title           "Vedtak om skjenkebevilling"@nb ;
            dct:type            <https://data.norge.no/vocabulary/event-type#administrative-decision-made> ;
            dcat:distribution   <https://example.org/example-distribusjon> ;
            cpsvno:mayInitiate  <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl> .

        <https://www.staging.fellesdatakatalog.digdir.no/events/4b75e194-4be7-337c-9950-699d2862c490>
            a                  dcat:CatalogRecord ;
            dct:identifier     "4b75e194-4be7-337c-9950-699d2862c490" ;
            dct:issued         "2022-05-13T13:04:04.942Z"^^xsd:dateTime ;
            dct:modified       "2022-05-13T13:04:04.942Z"^^xsd:dateTime ;
            foaf:primaryTopic  <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHendelse.ttl> ."""

    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHendelse.ttl": Event(
            id="4b75e194-4be7-337c-9950-699d2862c490",
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHendelse.ttl",
            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHendelse.ttl",
            harvest=HarvestMetaData(
                firstHarvested="2022-05-13T13:04:04Z", changed=["2022-05-13T13:04:04Z"]
            ),
            title={"nb": "Vedtak om skjenkebevilling"},
            description={
                "nn": "Teksten blir vist på nynorsk.",
                "en": "The text is displayed in English.",
                "nb": "Det er fattet vedtak om å gi skjenkebevilling til «Den beste restauranten AS», for servering av alkoholholdig drikk i gruppe 1, jf. Alkoholloven § 4-2",
            },
            dctType=[
                SkosConcept(
                    uri="https://data.norge.no/vocabulary/event-type#administrative-decision-made",
                )
            ],
            associatedBroaderTypes=[
                "https://data.norge.no/vocabulary/event-type#administrative-decision-made"
            ],
            mayInitiate=[
                "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl"
            ],
            subject=[
                "https://data.norge.no/concepts/ad2ab3f9-17a1-4494-b15e-4ba3967a6424"
            ],
            distribution=["https://example.org/example-distribusjon"],
        )
    }

    assert parse_events(src) == expected
