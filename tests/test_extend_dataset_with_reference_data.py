from fdk_rdf_parser.classes import (
    Dataset,
    Reference,
    ReferenceDataCode,
    SkosConcept,
)
from fdk_rdf_parser.reference_data import (
    DatasetReferenceData,
    extend_dataset_with_reference_data,
)
from .testdata import dataset_reference_data


def test_handles_missing_reference_data() -> None:
    parsed_dataset = Dataset(
        accessRights=ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED"
        ),
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, DatasetReferenceData())
        == parsed_dataset
    )


def test_uri_not_present_in_reference_data() -> None:
    parsed_dataset = Dataset(
        accessRights=ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/MISSING"
        ),
        language=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/language/JAP"
            )
        ],
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == parsed_dataset
    )


def test_extend_access_rights() -> None:
    parsed_dataset = Dataset(
        accessRights=ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED"
        )
    )

    expected = Dataset(
        accessRights=ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED",
            code="RESTRICTED",
            prefLabel={"en": "restricted"},
        )
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_provenance() -> None:
    parsed_dataset = Dataset(
        provenance=ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker"
        )
    )

    expected = Dataset(
        provenance=ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker",
            code="BRUKER",
            prefLabel={
                "nb": "Brukerinnsamlede data",
                "nn": "Brukerinnsamlede data",
                "en": "User collection",
            },
        )
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_accrual_periodicity() -> None:
    parsed_dataset = Dataset(
        accrualPeriodicity=ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL"
        )
    )

    expected = Dataset(
        accrualPeriodicity=ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL",
            code="ANNUAL",
            prefLabel={"nn": "årleg", "no": "årlig", "nb": "årlig", "en": "annual"},
        )
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_language() -> None:
    parsed_dataset = Dataset(
        language=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/language/ENG"
            )
        ]
    )

    expected = Dataset(
        language=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/language/ENG",
                code="ENG",
                prefLabel={
                    "en": "English",
                    "nb": "Engelsk",
                    "nn": "Engelsk",
                    "no": "Engelsk",
                },
            )
        ]
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_references() -> None:
    parsed_dataset = Dataset(
        references=[
            Reference(
                referenceType=ReferenceDataCode(
                    uri="http://purl.org/dc/terms/hasVersion"
                ),
                source=SkosConcept(
                    uri="https://testdirektoratet.no/model/dataset/hasVersion"
                ),
            )
        ]
    )

    expected = Dataset(
        references=[
            Reference(
                referenceType=ReferenceDataCode(
                    uri="http://purl.org/dc/terms/hasVersion",
                    code="hasVersion",
                    prefLabel={
                        "nn": "Har versjon",
                        "nb": "Har versjon",
                        "en": "Has version",
                    },
                ),
                source=SkosConcept(
                    uri="https://testdirektoratet.no/model/dataset/hasVersion"
                ),
            )
        ]
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )
