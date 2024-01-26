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
