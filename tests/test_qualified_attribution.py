from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import (
    Publisher,
    QualifiedAttribution,
)
from fdk_rdf_parser.parse_functions import extract_qualified_attributions
from fdk_rdf_parser.rdf_utils import prov_uri


def test_single_qualified_attribution() -> None:
    src = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix dct:   <http://purl.org/dc/terms/> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .

        <https://testdirektoratet.no/model/dataset/dataset-with-qualified-attribution>
            a                          dcat:Dataset ;
            prov:qualifiedAttribution  [ a             prov:Attribution ;
                                         dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor> ;
                                         prov:agent    <https://data.brreg.no/enhetsregisteret/api/enheter/123456789>
                                       ] .

        <https://data.brreg.no/enhetsregisteret/api/enheter/123456789>
            a                      rov:RegisteredOrganization ;
            dct:identifier         "123456789" ;
            rov:legalName          "Digitaliseringsdirektoratet" ;
            foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
            rov:orgType            orgtype:ORGL ;
            br:orgPath             "/STAT/987654321/123456789" .
      """

    expected = [
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
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://testdirektoratet.no/model/dataset/dataset-with-qualified-attribution"
    )

    actual = extract_qualified_attributions(
        graph, subject, prov_uri("qualifiedAttribution")
    )

    if isinstance(actual, list):
        assert all(x in actual for x in expected)


def test_multiple_qualified_attributions() -> None:
    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .

        <https://testdirektoratet.no/model/dataset/dataset-with-qualified-attributions>
            a                          dcat:Dataset ;
            prov:qualifiedAttribution  [ a             prov:Attribution ;
                                         dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor> ;
                                         prov:agent    <https://data.brreg.no/enhetsregisteret/api/enheter/123456789>
                                       ] ;
            prov:qualifiedAttribution  [ a             prov:Attribution ;
                                         dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor> ;
                                         prov:agent    <https://data.brreg.no/enhetsregisteret/api/enheter/987654321>
                                       ] .
      """

    expected = [
        QualifiedAttribution(
            agent=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/123456789",
            ),
            role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
        ),
        QualifiedAttribution(
            agent=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/987654321",
            ),
            role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://testdirektoratet.no/model/dataset/dataset-with-qualified-attributions"
    )

    actual = extract_qualified_attributions(
        graph, subject, prov_uri("qualifiedAttribution")
    )

    if isinstance(actual, list):
        assert all(x in actual for x in expected)


def test_handles_missing_agent() -> None:
    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .

        <https://testdirektoratet.no/model/dataset/dataset-with-qualified-attribution>
            a                          dcat:Dataset ;
            prov:qualifiedAttribution  [ a             prov:Attribution ;
                                         dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor>
                                       ] .
      """

    expected = [
        QualifiedAttribution(
            role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://testdirektoratet.no/model/dataset/dataset-with-qualified-attribution"
    )

    actual = extract_qualified_attributions(
        graph, subject, prov_uri("qualifiedAttribution")
    )

    if isinstance(actual, list):
        assert all(x in actual for x in expected)
