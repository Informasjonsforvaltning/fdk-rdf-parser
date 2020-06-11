from fdk_rdf_parser.classes import (
    Dataset,
    Distribution,
    Reference,
    SkosCode,
    SkosConcept,
)
from fdk_rdf_parser.reference_data import extendDatasetWithReferenceData, ReferenceData
from .testdata import reference_data


def test_handles_missing_reference_data() -> None:
    parsedDataset = Dataset(
        accessRights=SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED"
        )
    )

    assert (
        extendDatasetWithReferenceData(parsedDataset, ReferenceData()) == parsedDataset
    )


def test_uri_not_present_in_reference_data() -> None:
    parsedDataset = Dataset(
        accessRights=SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/MISSING"
        ),
        language=[
            SkosCode(
                uri="http://publications.europa.eu/resource/authority/language/JAP"
            )
        ],
    )

    assert (
        extendDatasetWithReferenceData(parsedDataset, reference_data) == parsedDataset
    )


def test_extend_access_rights() -> None:
    parsedDataset = Dataset(
        accessRights=SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED"
        )
    )

    expected = Dataset(
        accessRights=SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED",
            code="RESTRICTED",
            prefLabel={"en": "Restricted"},
        )
    )

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected


def test_extend_provenance() -> None:
    parsedDataset = Dataset(
        provenance=SkosCode(uri="http://data.brreg.no/datakatalog/provinens/bruker")
    )

    expected = Dataset(
        provenance=SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker",
            code="BRUKER",
            prefLabel={
                "nb": "Brukerinnsamlede data",
                "nn": "Brukerinnsamlede data",
                "en": "User collection",
            },
        )
    )

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected


def test_extend_accrual_periodicity() -> None:
    parsedDataset = Dataset(
        accrualPeriodicity=SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL"
        )
    )

    expected = Dataset(
        accrualPeriodicity=SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL",
            code="ANNUAL",
            prefLabel={"en": "annual"},
        )
    )

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected


def test_extend_language() -> None:
    parsedDataset = Dataset(
        language=[
            SkosCode(
                uri="http://publications.europa.eu/resource/authority/language/ENG"
            )
        ]
    )

    expected = Dataset(
        language=[
            SkosCode(
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

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected


def test_extend_spatial() -> None:
    parsedDataset = Dataset(
        spatial=[
            SkosCode(
                uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173142"
            )
        ]
    )

    expected = Dataset(
        spatial=[
            SkosCode(
                uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173142",
                code="https://data.geonorge.no/administrativeEnheter/fylke/id/173142",
                prefLabel={"no": "Finnmárku"},
            )
        ]
    )

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected


def test_extend_open_licenses() -> None:
    parsedDataset = Dataset(
        distribution=[
            Distribution(
                license=[
                    SkosConcept(uri="http://data.norge.no/nlod/"),
                    SkosConcept(
                        uri="http://creativecommons.org/licenses/by/4.0/",
                        prefLabel={"en": "Is not overwritten"},
                    ),
                ]
            ),
            Distribution(
                license=[
                    SkosConcept(
                        uri="http://creativesnobs.org/licenses/",
                        prefLabel={"en": "Is not open"},
                    )
                ]
            ),
            Distribution(),
        ]
    )

    expected = Dataset(
        distribution=[
            Distribution(
                license=[
                    SkosConcept(
                        uri="http://data.norge.no/nlod/",
                        prefLabel={"en": "Norwegian Licence for Open Government Data"},
                    ),
                    SkosConcept(
                        uri="http://creativecommons.org/licenses/by/4.0/",
                        prefLabel={"en": "Is not overwritten"},
                    ),
                ],
                openLicense=True,
            ),
            Distribution(
                license=[
                    SkosConcept(
                        uri="http://creativesnobs.org/licenses/",
                        prefLabel={"en": "Is not open"},
                    )
                ],
                openLicense=False,
            ),
            Distribution(),
        ]
    )

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected


def test_extend_references() -> None:
    parsedDataset = Dataset(
        references=[
            Reference(
                referenceType=SkosCode(uri="http://purl.org/dc/terms/hasVersion"),
                source=SkosConcept(
                    uri="https://testdirektoratet.no/model/dataset/hasVersion"
                ),
            )
        ]
    )

    expected = Dataset(
        references=[
            Reference(
                referenceType=SkosCode(
                    uri="http://purl.org/dc/terms/hasVersion",
                    code="hasVersion",
                    prefLabel={"en": "Has version"},
                ),
                source=SkosConcept(
                    uri="https://testdirektoratet.no/model/dataset/hasVersion"
                ),
            )
        ]
    )

    assert extendDatasetWithReferenceData(parsedDataset, reference_data) == expected
