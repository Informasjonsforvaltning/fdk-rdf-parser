from unittest.mock import Mock

from fdk_rdf_parser import parse_public_services
from fdk_rdf_parser.classes import (
    CriterionRequirement,
    Event,
    Evidence,
    HarvestMetaData,
    Output,
    Participation,
    PublicService,
    Publisher,
    SkosCode,
    SkosConcept,
)


def test_complete_public_services(
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

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> a cpsv:PublicService ;
                    cv:hasCompetentAuthority    <http://public-service-publisher.fellesdatakatalog.digdir.no/public-organisation/3> ;
                    cv:isGroupedBy              <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    dct:description             "Dette skjemaet  brukes for å registrere en ny virksomhet, eller søke om godkjenning av en ny næringsmiddelvirksomhet. Skjemaet skal også brukes dersom du vil utvide aktiviteten i en allerede eksisterende virksomhet og starte med en ny aktivitet som ikke er registrert."@nb ;
                    dct:identifier              "4" ;
                    dct:title                   "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                    cv:hasCompetentAuthority    <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/123456789> ;
                    cv:hasCriterion <http://public-service-publisher.fellesdatakatalog.digdir.no/criterion-requirement/5>  ;
                    cv:hasParticipation <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6> ;
                    cv:isClassifiedBy <https://data.norge.no/concepts/17> , <https://data.norge.no/concepts/16> ;
                    cv:isGroupedBy <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>;
                    cv:sector <https://data.norge.no/concepts/2> ;
                    dct:description "Ei offentleg teneste som tener som døme til bruk i utvikling"@nn ;
                    dct:identifier "1" ;
                    dct:language <http://publications.europa.eu/resource/authority/language/NOB>;
                    dct:requires <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> ;
                    dct:title "Ei offentleg teneste"@nb ;
                    cpsv:hasInput <http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1> ;
                    cpsv:produces <http://public-service-publisher.fellesdatakatalog.digdir.no/output/4> ;
                    dcat:keyword "Serveringsbevilling"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>
                    a                cv:BusinessEvent ;
                    dct:description  "Elektronisk prosess for etablering og oppstart av en bedrift."@nb ;
                    dct:identifier   "1" ;
                    dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                    dct:title        "Starte og drive bedrift"@nb ;
                    dct:type         <https://data.norge.no/concepts/1> .

            <https://data.norge.no/concepts/1>
                    a               skos:Concept ;
                    skos:prefLabel  "Starting business"@nb .

            <https://data.norge.no/concepts/15>
                    a               skos:Concept ;
                    skos:prefLabel  "Daglig leder"@nb .

            <https://data.norge.no/concepts/16>
                    a               skos:Concept ;
                    skos:prefLabel  "Kafé"@nb .

            <https://data.norge.no/concepts/17>
                    a               skos:Concept ;
                    skos:prefLabel  "Spiserestaurant"@nb .

            <https://data.norge.no/concepts/2>
                    a               skos:Concept ;
                    skos:prefLabel  "Nacekode: 56.1"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/criterion-requirement/5>
                    a               cv:CriterionRequirement ;
                    dct:identifier  "5" ;
                    dct:title       "Krav om vandel"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6>
                    a                cv:Participation ;
                    cv:role          <https://data.norge.no/concepts/15> ;
                    dct:description  "Mattilsynet"@nb ;
                    dct:identifier   "6" .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1>
                    a                cv:Evidence ;
                    dct:description  "Vandelsattest"@nb ;
                    dct:identifier   "1" ;
                    dct:title        "Vandelsattest"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/output/4>
                    a                cv:Output ;
                    dct:description  "Serveringsbevilling"@nb ;
                    dct:identifier   "4" ;
                    dct:title        "Serveringsbevilling"@nb .

            <http://localhost:5000/services/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            isGroupedBy=[
                Event(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
                    identifier="1",
                    title={"nb": "Starte og drive bedrift"},
                    description={
                        "nb": "Elektronisk prosess for etablering og oppstart av en bedrift."
                    },
                    type="https://data.norge.no/concepts/1",
                )
            ],
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "en": "Norwegian Digitalisation Agency",
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                    },
                    organisasjonsform="ORGL",
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            keyword=[{"nb": "Serveringsbevilling"}],
            sector=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/2",
                    prefLabel={"nb": "Nacekode: 56.1"},
                    extraType=None,
                )
            ],
            isClassifiedBy=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/16",
                    prefLabel={"nb": "Kafé"},
                    extraType=None,
                ),
                SkosConcept(
                    uri="https://data.norge.no/concepts/17",
                    prefLabel={"nb": "Spiserestaurant"},
                    extraType=None,
                ),
            ],
            language=[
                SkosCode(
                    uri="http://publications.europa.eu/resource/authority/language/NOB",
                    code="NOB",
                    prefLabel={
                        "en": "Norwegian Bokmål",
                        "nb": "Norsk Bokmål",
                        "nn": "Norsk Bokmål",
                        "no": "Norsk Bokmål",
                    },
                ),
            ],
            hasCriterion=[
                CriterionRequirement(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/criterion-requirement/5",
                    identifier="5",
                    name={"nb": "Krav om vandel"},
                    type=None,
                ),
            ],
            hasParticipation=[
                Participation(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6",
                    identifier="6",
                    description={"nb": "Mattilsynet"},
                    role=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/15",
                            prefLabel={"nb": "Daglig leder"},
                            extraType=None,
                        )
                    ],
                ),
            ],
            hasInput=[
                Evidence(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1",
                    identifier="1",
                    name={"nb": "Vandelsattest"},
                    description={"nb": "Vandelsattest"},
                    type=None,
                    language=None,
                ),
            ],
            produces=[
                Output(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/output/4",
                    identifier="4",
                    name={"nb": "Serveringsbevilling"},
                    description={"nb": "Serveringsbevilling"},
                ),
            ],
            requires=[
                PublicService(
                    id="4",
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
                    identifier="4",
                    title={
                        "nb": "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"
                    },
                )
            ],
            type="publicservices",
        ),
    }

    assert parse_public_services(src) == expected


def test_parse_multiple_public_services(
    mock_organizations_and_reference_data: Mock,
) -> None:
    src = """
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                dct:identifier "1" ;
                dct:title "Ei offentleg teneste"@nb ;
                dct:description "Ei offentleg teneste som tener som døme til bruk i utvikling"@nn ;
                cv:hasCompetentAuthority <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/123456789> ;
                cv:isGroupedBy <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>
                a                cv:Event ;
                dct:description  "Elektronisk prosess for etablering og oppstart av restaurantdrift."@nb ;
                dct:identifier   "1" ;
                dct:relation     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> ;
                dct:title        "Starte og drive restaurant"@nb ;
                dct:type         <https://data.norge.no/concpets/livshendelse> .

        <http://localhost:5000/services/fdk-1>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-1" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> a cpsv:PublicService ;
                dct:identifier "2" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ;
                cv:hasCompetentAuthority <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/991825827> .

        <http://localhost:5000/services/fdk-2>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-2" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> a cpsv:PublicService ;
                dct:identifier "3" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ; .

        <http://localhost:5000/services/fdk-3>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-3" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/4> a cpsv:PublicService ;
                dct:identifier "4" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ; .

        <http://localhost:5000/services/fdk-4>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-4" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            isGroupedBy=[
                Event(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
                    identifier="1",
                    title={"nb": "Starte og drive restaurant"},
                    description={
                        "nb": "Elektronisk prosess for etablering og oppstart av restaurantdrift."
                    },
                    type="https://data.norge.no/concpets/livshendelse",
                )
            ],
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "en": "Norwegian Digitalisation Agency",
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                    },
                    organisasjonsform="ORGL",
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/2": PublicService(
            id="fdk-2",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
            identifier="2",
            title={"nn": "Ei anna offentleg teneste"},
            description={
                "nb": "Ei anna offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/991825827",
                    id=None,
                    name=None,
                    orgPath=None,
                    prefLabel=None,
                    organisasjonsform=None,
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/3": PublicService(
            id="fdk-3",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/3",
            identifier="3",
            title={"nn": "Ei anna offentleg teneste"},
            description={
                "nb": "Ei anna offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=None,
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
    }

    assert parse_public_services(src) == expected
