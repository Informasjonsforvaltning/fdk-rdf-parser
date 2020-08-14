from unittest.mock import Mock

from rdflib import Graph

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.organizations import (
    addOrgPath,
    publisherFromFDKOrgCatalog,
)
from .testdata import org_response_0, org_response_1


def test_publisher_from_get_all() -> None:

    expected = Publisher(
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgsGraph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisherFromFDKOrgCatalog(
            Publisher(uri="https://externalurl.org/123456789", id="123456789"),
            orgsGraph,
        )
        == expected
    )


def test_publisher_not_present_in_get_all(mock_organizations_client: Mock) -> None:

    expected = Publisher(
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgsGraph = Graph().parse(data=org_response_1, format="turtle")

    assert (
        publisherFromFDKOrgCatalog(
            Publisher(uri="https://externalurl.org/123456789", id="123456789"),
            orgsGraph,
        )
        == expected
    )


def test_publisher_not_Found(mock_organizations_error: Mock) -> None:

    expected = Publisher(uri="https://externalurl.org/123456789", id="123456789")

    orgsGraph = Graph().parse(data=org_response_1, format="turtle")

    assert (
        publisherFromFDKOrgCatalog(
            Publisher(uri="https://externalurl.org/123456789", id="123456789"),
            orgsGraph,
        )
        == expected
    )


def test_original_pref_label_is_retained(mock_organizations_client: Mock) -> None:

    expected = Publisher(
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={"en": "Original label"},
        organisasjonsform="ORGL",
    )

    orgsGraph = Graph().parse(data=org_response_1, format="turtle")

    assert (
        publisherFromFDKOrgCatalog(
            Publisher(
                uri="https://externalurl.org/123456789",
                id="123456789",
                prefLabel={"en": "Original label"},
            ),
            orgsGraph,
        )
        == expected
    )


def test_orgpath(mock_orgpath_client: Mock) -> None:
    publisherID = Publisher(id="123456789")
    publisherNB = Publisher(prefLabel={"nb": "nb"})
    publisherNN = Publisher(prefLabel={"nn": "nn"})
    publisherEN = Publisher(prefLabel={"en": "en"})

    expectedID = Publisher(id="123456789", orgPath="/ANNET/orgpath")
    expectedNB = Publisher(prefLabel={"nb": "nb"}, orgPath="/ANNET/orgpath")
    expectedNN = Publisher(prefLabel={"nn": "nn"}, orgPath="/ANNET/orgpath")
    expectedEN = Publisher(prefLabel={"en": "en"}, orgPath="/ANNET/orgpath")

    assert addOrgPath(publisherID) == expectedID
    assert addOrgPath(publisherNB) == expectedNB
    assert addOrgPath(publisherNN) == expectedNN
    assert addOrgPath(publisherEN) == expectedEN


def test_extract_publisher_id_from_uri() -> None:

    expected = Publisher(
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgsGraph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisherFromFDKOrgCatalog(
            Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/123456789"
            ),
            orgsGraph,
        )
        == expected
    )


def test_only_extract_publisher_id_from_brreg_uri() -> None:

    expected = Publisher(uri="https://externalurl.org/123456789")

    orgsGraph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisherFromFDKOrgCatalog(
            Publisher(uri="https://externalurl.org/123456789"), orgsGraph
        )
        == expected
    )


def test_handles_empty_publisher() -> None:

    expected = Publisher()

    orgsGraph = Graph().parse(data=org_response_0, format="turtle")

    assert publisherFromFDKOrgCatalog(Publisher(), orgsGraph) == expected
