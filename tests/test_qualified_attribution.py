from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import Publisher, QualifiedAttribution
from fdk_rdf_parser.parse_functions import extractQualifiedAttributions
from fdk_rdf_parser.rdf_utils import provURI


def test_single_qualified_attribution() -> None:
    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .

        <https://testdirektoratet.no/model/dataset/dataset-with-qualified-attribution>
            a                          dcat:Dataset ;
            prov:qualifiedAttribution  [ a             prov:Attribution ;
                                         dcat:hadRole  <http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor> ;
                                         prov:agent    <https://data.brreg.no/enhetsregisteret/api/enheter/123456789>
                                       ] .
      """

    expected = [
        QualifiedAttribution(
            agent=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/123456789",
                id="123456789",
            ),
            role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
        )
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"https://testdirektoratet.no/model/dataset/dataset-with-qualified-attribution"
    )

    actual = extractQualifiedAttributions(
        graph, subject, provURI("qualifiedAttribution")
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
                id="123456789",
            ),
            role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
        ),
        QualifiedAttribution(
            agent=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/987654321",
                id="987654321",
            ),
            role="http://registry.it.csiro.au/def/isotc211/CI_RoleCode/contributor",
        ),
    ]

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"https://testdirektoratet.no/model/dataset/dataset-with-qualified-attributions"
    )

    actual = extractQualifiedAttributions(
        graph, subject, provURI("qualifiedAttribution")
    )

    if isinstance(actual, list):
        assert all(x in actual for x in expected)
