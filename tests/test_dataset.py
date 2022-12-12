from typing import Dict
from unittest.mock import Mock

from rdflib import Graph, URIRef

from fdk_rdf_parser import parse_datasets
from fdk_rdf_parser.classes import (
    Catalog,
    ConformsTo,
    Dataset,
    Distribution,
    HarvestMetaData,
    MediaTypeOrExtent,
    MediaTypeOrExtentType,
    PartialDataset,
    Publisher,
    QualifiedAttribution,
    QualityAnnotation,
    Reference,
    ReferenceDataCode,
    SkosConcept,
    Subject,
)
from fdk_rdf_parser.parse_functions import parse_dataset


def test_parse_multiple_datasets(mock_reference_data_client: Mock) -> None:

    src = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix fdk:   <https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-reasoning-service/main/src/main/resources/ontology/fdk.owl#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                   dcat:Dataset ;
                fdk:isOpenData      true ;
                fdk:isAuthoritative false ;
                dct:publisher       <https://organizations.fellesdatakatalog.digdir.no/organizations/123456789> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/4667277a>
                a                  dcat:CatalogRecord ;
                dct:identifier     "4667277a" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/1> .

        <https://testdirektoratet.no/model/dataset/1>
                a                   dcat:Dataset ;
                fdk:isAuthoritative true ;
                fdk:isRelatedToTransportportal  true ;
                dct:spatial         [ <http://www.w3.org/ns/locn#geometry> "gmlLiteral"^^<http://www.opengis.net/ont/geosparql#gmlLiteral> ] ;
                dct:accessRights    <http://publications.europa.eu/resource/authority/access-right/PUBLIC> ;
                dct:relation        <https://testdirektoratet.no/model/dataset/0> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca>
                a                  dcat:CatalogRecord ;
                dct:identifier     "a1c680ca" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/123>
                a                  dcat:CatalogRecord ;
                dct:identifier     "123" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime .

        <https://organizations.fellesdatakatalog.digdir.no/organizations/123456789>
            a                      rov:RegisteredOrganization ;
            dct:identifier         "123456789" ;
            rov:legalName          "Digitaliseringsdirektoratet" ;
            foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
            rov:orgType            orgtype:ORGL ;
            br:orgPath             "/STAT/987654321/123456789" ."""

    expected = {
        "https://testdirektoratet.no/model/dataset/0": Dataset(
            id="a1c680ca",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-12T11:52:16Z"],
            ),
            publisher=Publisher(
                uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                id="123456789",
                name="Digitaliseringsdirektoratet",
                orgPath="/STAT/987654321/123456789",
                prefLabel={
                    "nn": "Digitaliseringsdirektoratet",
                    "nb": "Digitaliseringsdirektoratet",
                    "en": "Norwegian Digitalisation Agency",
                },
                organisasjonsform="ORGL",
            ),
            uri="https://testdirektoratet.no/model/dataset/0",
            isOpenData=True,
            isAuthoritative=False,
            isRelatedToTransportportal=False,
        ),
        "https://testdirektoratet.no/model/dataset/1": Dataset(
            id="4667277a",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-12T11:52:16Z"],
            ),
            accessRights=ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/access-right/PUBLIC",
                code="PUBLIC",
                prefLabel={"en": "public"},
            ),
            uri="https://testdirektoratet.no/model/dataset/1",
            isOpenData=False,
            isAuthoritative=True,
            isRelatedToTransportportal=True,
            references=[
                Reference(
                    referenceType=ReferenceDataCode(
                        uri="http://purl.org/dc/terms/relation",
                        code="relation",
                        prefLabel={
                            "nn": "Er relatert til",
                            "nb": "Er relatert til",
                            "en": "Has relation to",
                        },
                    ),
                    source=SkosConcept(
                        uri="https://testdirektoratet.no/model/dataset/0"
                    ),
                )
            ],
        ),
    }

    assert parse_datasets(src) == expected


def test_adds_catalog_to_dataset(
    mock_reference_data_client: Mock,
) -> None:

    src = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

        <https://testdirektoratet.no/model/catalog/0>
                a                dcat:Catalog ;
                dcat:dataset     <https://testdirektoratet.no/model/dataset/0> ;
                dct:title        "Katalog"@nb ;
                dct:description  "Beskrivelse av katalog"@nb ;
                dct:publisher   <https://organizations.fellesdatakatalog.digdir.no/organizations/123456789> .

        <https://datasets.fellesdatakatalog.digdir.no/catalog/abc123>
                a                  dcat:CatalogRecord ;
                dct:identifier     "abc123" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/catalog/0> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca>
                a                  dcat:CatalogRecord ;
                dct:identifier     "a1c680ca" ;
                dct:isPartOf       <https://datasets.fellesdatakatalog.digdir.no/catalog/abc123> ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-13"^^xsd:date ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://testdirektoratet.no/model/dataset/0>
                dct:publisher   <https://organizations.fellesdatakatalog.digdir.no/organizations/123456789> ;
                a                         dcat:Dataset .

        <https://organizations.fellesdatakatalog.digdir.no/organizations/123456789>
            a                      rov:RegisteredOrganization ;
            dct:identifier         "123456789" ;
            rov:legalName          "Digitaliseringsdirektoratet" ;
            foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
            rov:orgType            orgtype:ORGL ;
            br:orgPath             "/STAT/987654321/123456789" ."""

    expected = {
        "https://testdirektoratet.no/model/dataset/0": Dataset(
            id="a1c680ca",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-13"],
            ),
            uri="https://testdirektoratet.no/model/dataset/0",
            publisher=Publisher(
                uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                id="123456789",
                name="Digitaliseringsdirektoratet",
                orgPath="/STAT/987654321/123456789",
                prefLabel={
                    "nn": "Digitaliseringsdirektoratet",
                    "nb": "Digitaliseringsdirektoratet",
                    "en": "Norwegian Digitalisation Agency",
                },
                organisasjonsform="ORGL",
            ),
            catalog=Catalog(
                id="abc123",
                uri="https://testdirektoratet.no/model/catalog/0",
                title={"nb": "Katalog"},
                description={"nb": "Beskrivelse av katalog"},
                publisher=Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                        "en": "Norwegian Digitalisation Agency",
                    },
                    organisasjonsform="ORGL",
                ),
            ),
        )
    }

    assert parse_datasets(src) == expected


def test_does_not_parse_catalog_as_a_dataset(
    mock_reference_data_client: Mock,
) -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

        <https://testdirektoratet.no/model/catalog/0>
                a               dcat:Catalog ;
                dct:publisher   [ a                 vcard:Kind , foaf:Agent ;
                                  dct:identifier    "123456789" ] .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca>
                a                  dcat:CatalogRecord ;
                dct:identifier     "a1c680ca" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/catalog/0> ."""

    expected: Dict = {}

    assert parse_datasets(src) == expected


def test_parse_dataset() -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dct:accrualPeriodicity
                    <http://publications.europa.eu/resource/authority/freq> ;
                dct:identifier
                    "adb4cf00-31c8-460c-9563-55f204cf8221" ;
                dct:publisher
                    <http://data.brreg.no/enhetsregisteret/enhet/987654321> ;
                dct:provenance
                    <http://data.brreg.no/datakatalog/provinens/tredjepart> ;
                dcat:endpointDescription
                    <https://testdirektoratet.no/openapi/dataset/0.yaml> ;
                dct:spatial
                    <https://data.geonorge.no/administrativeEnheter/fylke/id/173142> ;
                dct:subject
                    <https://testdirektoratet.no/model/concept/0> ,
                    <https://testdirektoratet.no/model/concept/1> ;
                foaf:page
                    <https://testdirektoratet.no> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca>
                a                  dcat:CatalogRecord ;
                dct:identifier     "a1c680ca" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-13"^^xsd:date ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> ."""

    expected = PartialDataset(
        id="a1c680ca",
        harvest=HarvestMetaData(
            firstHarvested="2020-03-12T11:52:16Z",
            changed=["2020-03-12T11:52:16Z", "2020-03-13"],
        ),
        identifier={"adb4cf00-31c8-460c-9563-55f204cf8221"},
        uri="https://testdirektoratet.no/model/dataset/0",
        publisher=Publisher(
            uri="http://data.brreg.no/enhetsregisteret/enhet/987654321"
        ),
        page={"https://testdirektoratet.no"},
        subject=[
            Subject(uri="https://testdirektoratet.no/model/concept/0"),
            Subject(uri="https://testdirektoratet.no/model/concept/1"),
        ],
        accrualPeriodicity=ReferenceDataCode(
            "http://publications.europa.eu/resource/authority/freq"
        ),
        provenance=ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/tredjepart"
        ),
        spatial=[
            ReferenceDataCode(
                uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173142"
            )
        ],
    )

    datasets_graph = Graph().parse(data=src, format="turtle")
    dataset_uri = URIRef("https://testdirektoratet.no/model/dataset/0")
    record_uri = URIRef(
        "https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca"
    )

    assert parse_dataset(datasets_graph, record_uri, dataset_uri) == expected


def test_dataset_has_quality_annotations() -> None:

    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dqv:   <http://www.w3.org/ns/dqv#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix oa:    <http://www.w3.org/ns/oa#> .

        <https://testdirektoratet.no/model/dataset/quality>
                a                   dcat:Dataset ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Currentness> ;
                    oa:hasBody     [] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Availability> ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "availability" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Relevance> ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "relevans" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/NOB> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Completeness> ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "Completeness" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ."""

    expected = PartialDataset(
        uri="https://testdirektoratet.no/model/dataset/quality",
        harvest=HarvestMetaData(),
        hasCurrentnessAnnotation=QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Currentness"
        ),
        hasAvailabilityAnnotation=QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Availability",
            hasBody={"en": "availability"},
        ),
        hasRelevanceAnnotation=QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Relevance",
            hasBody={"nb": "relevans"},
        ),
        hasCompletenessAnnotation=QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Completeness",
            hasBody={"en": "Completeness"},
        ),
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/quality")

    assert parse_dataset(graph, URIRef("record"), subject) == expected


def test_legal_basis_fields() -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dcatno:legalBasisForRestriction
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://restriction.no" ;
                  skos:prefLabel  "skjermingshjemmel"@nb
                ] ;
                dcatno:legalBasisForProcessing
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://processing.no" ;
                  skos:prefLabel  "behandlingsgrunnlag"@nb
                ] ;
                dcatno:legalBasisForAccess
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://access.no" ;
                  skos:prefLabel  "utleveringshjemmel"@nb
                ] ."""

    expected = PartialDataset(
        uri="https://testdirektoratet.no/model/dataset/0",
        harvest=HarvestMetaData(),
        legalBasisForRestriction=[
            SkosConcept(
                uri="https://restriction.no",
                prefLabel={"nb": "skjermingshjemmel"},
                extraType="http://purl.org/dc/terms/RightsStatement",
            )
        ],
        legalBasisForProcessing=[
            SkosConcept(
                uri="https://processing.no",
                prefLabel={"nb": "behandlingsgrunnlag"},
                extraType="http://purl.org/dc/terms/RightsStatement",
            )
        ],
        legalBasisForAccess=[
            SkosConcept(
                uri="https://access.no",
                prefLabel={"nb": "utleveringshjemmel"},
                extraType="http://purl.org/dc/terms/RightsStatement",
            )
        ],
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/0")

    assert parse_dataset(graph, URIRef("record"), subject) == expected


def test_informationmodel_and_conformsto() -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dct:conformsTo
                [ a               skos:Concept ;
                  dct:source      "https://conformsto.no" ;
                  dct:title  "conforms to"@en
                ] ;
                dcatno:informationModel
                [ a               skos:Concept , dct:Standard ;
                  dct:source      "https://informationmodel.no" ;
                  skos:prefLabel  "information model"@en
                ] ."""

    expected = PartialDataset(
        uri="https://testdirektoratet.no/model/dataset/0",
        harvest=HarvestMetaData(),
        conformsTo=[
            ConformsTo(
                uri="https://conformsto.no",
                prefLabel={"en": "conforms to"},
            )
        ],
        informationModel=[
            SkosConcept(
                uri="https://informationmodel.no",
                prefLabel={"en": "information model"},
                extraType="http://purl.org/dc/terms/Standard",
            )
        ],
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/0")

    assert parse_dataset(graph, URIRef("record"), subject) == expected


def test_distribution_and_sample() -> None:

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix adms:  <http://www.w3.org/ns/adms#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                adms:sample
                    [ a                dcat:Distribution ;
                      dct:description  "adsgjkv  cghj     dghdh"@nb ;
                      dct:format       "application/ATF" ;
                      dcat:accessURL   <https://application/ATF.com>
                    ] ;
                dcat:distribution
                    [ a                dcat:Distribution ;
                      dct:conformsTo
                        [ a               dct:Standard ;
                          dct:source      "https://hopp.no" ;
                          dct:title  "standard1"@nb
                        ] ;
                      dct:description  "asdadrtyrtydfghdgh  dgh dfgh dh"@nb ;
                      dct:format       "application/ATF" ;
                      dcat:compressFormat   "ZIP" ;
                      dct:license
                        [ a           dct:LicenseDocument , skos:Concept ;
                          dct:source
                            "http://creativecommons.org/publicdomain/zero/1.0/"
                        ] ;
                      dct:type         "Feed" ;
                      dcat:accessURL   <https://distribusjonsentralen.no> , [ ] ;
                      foaf:page        [ a           foaf:Document , skos:Concept ;
                                         dct:source  "https://dokumentsjon.com"
                                       ]
                    ] ."""

    expected = PartialDataset(
        uri="https://testdirektoratet.no/model/dataset/0",
        harvest=HarvestMetaData(),
        sample=[
            Distribution(
                description={"nb": "adsgjkv  cghj     dghdh"},
                format={"application/ATF"},
                fdkFormat=[
                    MediaTypeOrExtent(
                        code="application/ATF", type=MediaTypeOrExtentType.UNKNOWN
                    )
                ],
                accessURL={"https://application/ATF.com"},
            )
        ],
        distribution=[
            Distribution(
                conformsTo=[
                    ConformsTo(
                        uri="https://hopp.no",
                        prefLabel={"nb": "standard1"},
                    )
                ],
                description={"nb": "asdadrtyrtydfghdgh  dgh dfgh dh"},
                format={"application/ATF"},
                fdkFormat=[
                    MediaTypeOrExtent(
                        code="application/ATF", type=MediaTypeOrExtentType.UNKNOWN
                    )
                ],
                compressFormat=MediaTypeOrExtent(code="ZIP"),
                license=[
                    SkosConcept(
                        uri="http://creativecommons.org/publicdomain/zero/1.0/",
                        extraType="http://purl.org/dc/terms/LicenseDocument",
                    )
                ],
                type="Feed",
                accessURL={"https://distribusjonsentralen.no"},
                page=[
                    SkosConcept(
                        uri="https://dokumentsjon.com",
                        extraType="http://xmlns.com/foaf/0.1/Document",
                    )
                ],
            )
        ],
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/0")

    assert parse_dataset(graph, URIRef("record"), subject) == expected


def test_qualified_attributions() -> None:
    src = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                prov:qualifiedAttribution  [ a             prov:Attribution ;
                                             dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor> ;
                                             prov:agent    <https://data.brreg.no/enhetsregisteret/api/enheter/123456789>
                                           ] ;
                prov:qualifiedAttribution  [ a             prov:Attribution ;
                                             dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor> ;
                                             prov:agent    <https://data.brreg.no/enhetsregisteret/api/enheter/111111111>
                                           ] .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca>
            a                  dcat:CatalogRecord ;
            dct:identifier     "a1c680ca" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
            foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://data.brreg.no/enhetsregisteret/api/enheter/123456789>
                a                      rov:RegisteredOrganization ;
                dct:identifier         "123456789" ;
                rov:legalName          "Digitaliseringsdirektoratet" ;
                foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
                rov:orgType            orgtype:ORGL ;
                br:orgPath             "/STAT/987654321/123456789" .

        <https://data.brreg.no/enhetsregisteret/api/enheter/111111111>
                a                      rov:RegisteredOrganization ;
                dct:identifier         "111111111" ;
                rov:legalName          "Pythondirektoratet" ;
                foaf:name              "Pythondirektoratet"@nn , "Pythondirektoratet"@nb , "Norwegian Python Agency"@en ;
                rov:orgType            orgtype:ORGL ;
                br:orgPath             "/STAT/987654321/111111111" ."""

    expected = PartialDataset(
        uri="https://testdirektoratet.no/model/dataset/0",
        qualifiedAttributions=[
            QualifiedAttribution(
                agent=Publisher(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                        "en": "Norwegian Digitalisation Agency",
                    },
                    organisasjonsform="ORGL",
                ),
                role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
            ),
            QualifiedAttribution(
                agent=Publisher(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/111111111",
                    id="111111111",
                    name="Pythondirektoratet",
                    orgPath="/STAT/987654321/111111111",
                    prefLabel={
                        "nn": "Pythondirektoratet",
                        "nb": "Pythondirektoratet",
                        "en": "Norwegian Python Agency",
                    },
                    organisasjonsform="ORGL",
                ),
                role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
            ),
        ],
    )

    actual = parse_datasets(src)["https://testdirektoratet.no/model/dataset/0"]

    if isinstance(actual.qualifiedAttributions, list) and isinstance(
        expected.qualifiedAttributions, list
    ):
        assert all(
            x in actual.qualifiedAttributions for x in expected.qualifiedAttributions
        )


def test_https_uri_open_license(mock_reference_data_client: Mock) -> None:
    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/123>
                a                  dcat:CatalogRecord ;
                dct:identifier     "123" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://testdirektoratet.no/model/dataset/0>
            a                  dcat:Dataset ;
            dct:accessRights   <http://publications.europa.eu/resource/authority/access-right/PUBLIC> ;
            dcat:distribution  <https://example.com/open-distribution> .

        <https://example.com/open-distribution>
            a               dcat:Distribution ;
            dct:format      "HTML" , [ dct:title    "CSV" ] ;
            dct:license     <https://data.norge.no/nlod/> ;
            dcat:accessURL  <http://example.com/access-url> .
    """
    expected = {
        "https://testdirektoratet.no/model/dataset/0": Dataset(
            uri="https://testdirektoratet.no/model/dataset/0",
            accessRights=ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/access-right/PUBLIC",
                code="PUBLIC",
                prefLabel={"en": "public"},
            ),
            id="123",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-12T11:52:16Z"],
            ),
            distribution=[
                Distribution(
                    uri="https://example.com/open-distribution",
                    accessURL={"http://example.com/access-url"},
                    license=[
                        SkosConcept(
                            uri="https://data.norge.no/nlod/",
                            prefLabel={
                                "no": "Norsk lisens for offentlige data",
                                "en": "Norwegian Licence for Open Government Data",
                            },
                        )
                    ],
                    openLicense=True,
                    format={
                        "HTML",
                    },
                    fdkFormat=[
                        MediaTypeOrExtent(
                            code="HTML", type=MediaTypeOrExtentType.UNKNOWN
                        ),
                    ],
                )
            ],
        ),
    }
    assert parse_datasets(src) == expected


def test_dcat_ap_no_2_rules(mock_reference_data_client: Mock) -> None:
    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
        @prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix cpsvno: <https://data.norge.no/vocabulary/cpsvno#> .
        @prefix eli: <http://data.europa.eu/eli/ontology#> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/123>
                a                  dcat:CatalogRecord ;
                dct:identifier     "123" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://testdirektoratet.no/model/dataset/0>
            a                  dcat:Dataset ;
            cpsv:follows [ a cpsv:Rule ;
                    dct:type cpsvno:ruleForNonDisclosure ;
                    cpsv:implements [ a eli:LegalResouce ;
                        rdfs:seeAlso "https://lovdata.no/NL/lov/2016-05-27-14/§3-1" ;
                        dct:type    [ a skos:Concept ;
                            skos:prefLabel  "Skatteforvaltningsloven §3-1"@nb ;
                        ]
                    ] ;
                ] ,
                [ a cpsv:Rule ;
                    dct:type cpsvno:ruleForDisclosure ;
                    cpsv:implements [ a eli:LegalResouce ;
                        rdfs:seeAlso "https://lovdata.no/NL/lov/2016-05-27-14/§3-3" ;
                        dct:type    [ a skos:Concept ;
                            skos:prefLabel  "Skatteforvaltningsloven §§ 3-3 til 3-9"@nb ;
                        ]
                    ] ;
                ] ,
                [ a cpsv:Rule ;
                    dct:type cpsvno:ruleForDataProcessing ;
                    cpsv:implements [ a eli:LegalResouce ;
                        rdfs:seeAlso "https://lovdata.no/NL/lov/2016-05-27-14/§3-3" ;
                    ] ;
                ] ,
                [ a cpsv:Rule ;
                    dct:type cpsvno:ruleForSomethingElse ;
                    cpsv:implements [ a eli:LegalResouce ; ] ;
                ] ,
                [ a cpsv:Rule ; ] ."""
    expected = {
        "https://testdirektoratet.no/model/dataset/0": Dataset(
            uri="https://testdirektoratet.no/model/dataset/0",
            id="123",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-12T11:52:16Z"],
            ),
            legalBasisForRestriction=[
                SkosConcept(
                    uri="https://lovdata.no/NL/lov/2016-05-27-14/§3-1",
                    prefLabel={"nb": "Skatteforvaltningsloven §3-1"},
                    extraType="https://data.norge.no/vocabulary/cpsvno#ruleForNonDisclosure",
                )
            ],
            legalBasisForProcessing=[
                SkosConcept(
                    uri="https://lovdata.no/NL/lov/2016-05-27-14/§3-3",
                    extraType="https://data.norge.no/vocabulary/cpsvno#ruleForDataProcessing",
                )
            ],
            legalBasisForAccess=[
                SkosConcept(
                    uri="https://lovdata.no/NL/lov/2016-05-27-14/§3-3",
                    prefLabel={"nb": "Skatteforvaltningsloven §§ 3-3 til 3-9"},
                    extraType="https://data.norge.no/vocabulary/cpsvno#ruleForDisclosure",
                )
            ],
        ),
    }

    assert parse_datasets(src) == expected


def test_extra_media_types(mock_reference_data_client: Mock) -> None:
    src = """
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/123>
                a                  dcat:CatalogRecord ;
                dct:identifier     "123" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/321>
                a                  dcat:CatalogRecord ;
                dct:identifier     "321" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/1> .

        <https://testdirektoratet.no/model/dataset/0>
            a                  dcat:Dataset ;
            dcat:distribution  <https://example.com/extra-media-types> .

        <https://testdirektoratet.no/model/dataset/1>
            a                  dcat:Dataset ;
            dcat:distribution  <https://example.com/unknown-media-types> .

        <https://example.com/extra-media-types>
            a               dcat:Distribution ;
            dcat:mediaType      <https://www.iana.org/assignments/media-types/text/html> ;
            dcat:compressFormat      <https://www.iana.org/assignments/media-types/application/json> ;
            dcat:packageFormat      <http://publications.europa.eu/resource/authority/file-type/7Z> .

        <https://example.com/unknown-media-types>
            a               dcat:Distribution ;
            dcat:mediaType       <https://www.iana.org/assignments/media-types/text/unknown> ;
            dcat:compressFormat  "text/unknown" ;
            dcat:packageFormat   [ ] .
    """
    expected = {
        "https://testdirektoratet.no/model/dataset/0": Dataset(
            uri="https://testdirektoratet.no/model/dataset/0",
            id="123",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-12T11:52:16Z"],
            ),
            distribution=[
                Distribution(
                    uri="https://example.com/extra-media-types",
                    fdkFormat=[
                        MediaTypeOrExtent(
                            uri="https://www.iana.org/assignments/media-types/text/html",
                            name="html",
                            code="text/html",
                            type=MediaTypeOrExtentType.MEDIA_TYPE,
                        ),
                    ],
                    mediaType=[
                        ReferenceDataCode(
                            uri="https://www.iana.org/assignments/media-types/text/html",
                            code="text/html",
                            prefLabel={"nb": "text/html"},
                        ),
                    ],
                    compressFormat=MediaTypeOrExtent(
                        uri="https://www.iana.org/assignments/media-types/application/json",
                        name="json",
                        code="application/json",
                        type=MediaTypeOrExtentType.MEDIA_TYPE,
                    ),
                    packageFormat=MediaTypeOrExtent(
                        uri="http://publications.europa.eu/resource/authority/file-type/7Z",
                        name="7Z",
                        code="7Z",
                        type=MediaTypeOrExtentType.FILE_TYPE,
                    ),
                )
            ],
        ),
        "https://testdirektoratet.no/model/dataset/1": Dataset(
            uri="https://testdirektoratet.no/model/dataset/1",
            id="321",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z",
                changed=["2020-03-12T11:52:16Z", "2020-03-12T11:52:16Z"],
            ),
            distribution=[
                Distribution(
                    uri="https://example.com/unknown-media-types",
                    compressFormat=MediaTypeOrExtent(
                        code="text/unknown",
                        type=MediaTypeOrExtentType.UNKNOWN,
                    ),
                )
            ],
        ),
    }
    assert parse_datasets(src) == expected
