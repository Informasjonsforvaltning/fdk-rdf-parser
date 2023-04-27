from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import (
    Organization,
    ReferenceDataCode,
)
from fdk_rdf_parser.parse_functions.organization import (
    extract_organizations,
    parse_organization,
    set_organization_name_from_pref_label_if_missing,
)
from fdk_rdf_parser.rdf_utils.ns import cv_uri


def test_parse_organization() -> None:
    src = """
        @prefix dct:   <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
        @prefix org:   <http://www.w3.org/ns/org#> .

        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123>
            a                      org:Organization ;
            dct:identifier         "123" ;
            dct:title              "Digitaliseringsdirektoratet"@nb ;
            skos:prefLabel         "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
            dct:type               <http://purl.org/adms/publishertype/NationalAuthority> ;
            foaf:homepage          "https://www.digdir.no" ;
            dct:spatial            <http://publications.europa.eu/resource/authority/country/NOR> .
    """

    expected = Organization(
        uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123",
        identifier="123",
        name={"nb": "Digitaliseringsdirektoratet"},
        title={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        orgType=ReferenceDataCode(
            uri="http://purl.org/adms/publishertype/NationalAuthority",
        ),
        homepage=["https://www.digdir.no"],
        spatial=["http://publications.europa.eu/resource/authority/country/NOR"],
    )
    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123"
    )

    assert parse_organization(graph, subject) == expected


def test_extract_organizations() -> None:
    src = """
        @prefix br:      <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix cv:      <http://data.europa.eu/m8g/> .
        @prefix cpsv:    <http://purl.org/vocab/cpsv#> .
        @prefix cpsvno:   <https://data.norge.no/vocabulary/cpsvno#> .
        @prefix dct:     <http://purl.org/dc/terms/> .
        @prefix foaf:    <http://xmlns.com/foaf/0.1/> .
        @prefix org:     <http://www.w3.org/ns/org#> .
        @prefix orgtype: <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix rov:     <http://www.w3.org/ns/regorg#> .
        @prefix skos:    <http://www.w3.org/2004/02/skos/core#> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
            a cpsvno:Service ;
            cv:ownedBy  <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123> ,
                        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
            dct:identifier  "1" .

        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123>
            a                      org:Organization ;
            dct:identifier         "123" ;
            dct:title              "Sivil organisasjon"@nb ;
            skos:prefLabel         "SO"@nn , "SO"@nb , "SO"@en ;
            dct:type               <http://purl.org/adms/publishertype/NonGovernmentalOrganisation> ;
            foaf:homepage          "https://www.sivilorg.no" ;
            dct:spatial            <http://publications.europa.eu/resource/authority/country/NOR> .

        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789>
            a                      rov:RegisteredOrganization ;
            dct:identifier         "123456789" ;
            rov:legalName          "Stor registrert organisasjon"@nb ;
            foaf:name              "SRO"@nn , "SRO"@nb , "SRO"@en ;
            rov:orgType            orgtype:FLI ;
            br:orgPath             "/PRIVAT/123456789" ;
            foaf:homepage          <https://www.storregorg.no> . """

    expected = [
        Organization(
            uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123",
            identifier="123",
            name={"nb": "Sivil organisasjon"},
            title={
                "nn": "SO",
                "nb": "SO",
                "en": "SO",
            },
            orgType=ReferenceDataCode(
                uri="http://purl.org/adms/publishertype/NonGovernmentalOrganisation",
            ),
            homepage=["https://www.sivilorg.no"],
            spatial=["http://publications.europa.eu/resource/authority/country/NOR"],
        ),
        Organization(
            uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
            identifier="123456789",
            orgPath="/PRIVAT/123456789",
            name={"nb": "Stor registrert organisasjon"},
            title={
                "nn": "SRO",
                "nb": "SRO",
                "en": "SRO",
            },
            homepage=["https://www.storregorg.no"],
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1"
    )

    assert extract_organizations(graph, subject, cv_uri("ownedBy")) == expected


def test_extract_public_organisation() -> None:
    src = """
        @prefix cv:      <http://data.europa.eu/m8g/> .
        @prefix cpsv:    <http://purl.org/vocab/cpsv#> .
        @prefix dct:     <http://purl.org/dc/terms/> .
        @prefix foaf:    <http://xmlns.com/foaf/0.1/> .
        @prefix skos:    <http://www.w3.org/2004/02/skos/core#> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
            a cpsv:PublicService ;
            cv:hasCompetentAuthority  <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321> ;
            dct:identifier  "1" .

        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321>
            a                      cv:PublicOrganisation ;
            dct:identifier         "987654321" ;
            dct:title              "Offentlig organisasjon"@nb ;
            skos:prefLabel         "OO"@nn , "OO"@nb , "OO"@en ;
            dct:type               <http://purl.org/adms/publishertype/NationalAuthority> ;
            foaf:homepage          "https://www.sivilorg.no" ;
            dct:spatial            <http://publications.europa.eu/resource/authority/country/NOR> . """

    expected = [
        Organization(
            uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321",
            identifier="987654321",
            name={"nb": "Offentlig organisasjon"},
            title={
                "nn": "OO",
                "nb": "OO",
                "en": "OO",
            },
            orgType=ReferenceDataCode(
                uri="http://purl.org/adms/publishertype/NationalAuthority",
            ),
            homepage=["https://www.sivilorg.no"],
            spatial=["http://publications.europa.eu/resource/authority/country/NOR"],
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1"
    )

    assert (
        extract_organizations(graph, subject, cv_uri("hasCompetentAuthority"))
        == expected
    )


def test_bnode_organization() -> None:
    src = """
        @prefix cv:      <http://data.europa.eu/m8g/> .
        @prefix cpsv:    <http://purl.org/vocab/cpsv#> .
        @prefix dct:     <http://purl.org/dc/terms/> .
        @prefix org:     <http://www.w3.org/ns/org#> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
            a                      cpsv:Service ;
            cv:ownedBy             [
                a   org:Organization ;
                dct:identifier         "123" ] . """

    expected = [
        Organization(identifier="123"),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1"
    )

    assert extract_organizations(graph, subject, cv_uri("ownedBy")) == expected


def test_parse_invalid_organization_type() -> None:
    src = """
        @prefix dct:     <http://purl.org/dc/terms/> .
        @prefix custom:  <http://staging.fellesdatakatalog.digdir.no/custom-prefix> .

        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123>
            a                custom:InvalidType ;
            dct:identifier   "123" .
    """

    expected = Organization(
        uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123",
        identifier="123",
    )
    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123"
    )

    assert parse_organization(graph, subject) == expected


def test_set_name_from_label() -> None:
    input_0 = Organization(identifier="123456789")
    expected_0 = Organization(identifier="123456789")
    input_1 = Organization(
        identifier="123456789", name={"nb": "Original"}, title={"nb": "Bokmål"}
    )
    expected_1 = Organization(
        identifier="123456789", name={"nb": "Original"}, title={"nb": "Bokmål"}
    )
    input_2 = Organization(
        identifier="123456789", title={"nb": "Bokmål", "nn": "Nynorsk"}
    )
    expected_2 = Organization(
        identifier="123456789",
        name={"nb": "Bokmål", "nn": "Nynorsk"},
        title={"nb": "Bokmål", "nn": "Nynorsk"},
    )
    input_3 = Organization(identifier="123456789", title={})
    expected_3 = Organization(identifier="123456789", name={}, title={})

    assert set_organization_name_from_pref_label_if_missing(input_0) == expected_0
    assert set_organization_name_from_pref_label_if_missing(input_1) == expected_1
    assert set_organization_name_from_pref_label_if_missing(input_2) == expected_2
    assert set_organization_name_from_pref_label_if_missing(input_3) == expected_3
