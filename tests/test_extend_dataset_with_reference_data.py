from fdk_rdf_parser.classes import (
    ConceptSchema,
    Dataset,
    Distribution,
    EuDataTheme,
    FDKFormatType,
    LosNode,
    MediaType,
    Reference,
    SkosCode,
    SkosConcept,
)
from fdk_rdf_parser.reference_data import (
    DatasetReferenceData,
    extend_dataset_with_reference_data,
)
from .testdata import dataset_reference_data


def test_handles_missing_reference_data() -> None:
    parsed_dataset = Dataset(
        accessRights=SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED"
        ),
        theme=[EuDataTheme(id="https://psi.norge.no/los/tema/grunnskole")],
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, DatasetReferenceData())
        == parsed_dataset
    )


def test_uri_not_present_in_reference_data() -> None:
    parsed_dataset = Dataset(
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
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == parsed_dataset
    )


def test_extend_access_rights() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_provenance() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_accrual_periodicity() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_language() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_spatial() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_handles_open_licenses_with_missing_reference_data() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, DatasetReferenceData())
        == parsed_dataset
    )


def test_extend_open_licenses() -> None:
    parsed_dataset = Dataset(
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_handles_media_types_with_missing_reference_data() -> None:
    parsed_dataset = Dataset(
        distribution=[
            Distribution(format={"application/xml"}),
            Distribution(format={"CSV"}),
            Distribution(format={"json"}),
            Distribution(format={"geo+json"}),
            Distribution(format={"text/turtle"}),
            Distribution(),
        ]
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, DatasetReferenceData())
        == parsed_dataset
    )


def test_extend_media_types() -> None:
    parsed_dataset = Dataset(
        distribution=[
            Distribution(
                fdkFormat=[
                    MediaType(
                        uri="https://www.iana.org/assignments/media-types/application/xml"
                    ),
                ]
            ),
            Distribution(
                fdkFormat=[
                    MediaType(
                        uri="http://publications.europa.eu/resource/authority/file-type/XML"
                    ),
                ]
            ),
            Distribution(fdkFormat=[MediaType(code="CSV")]),
            Distribution(fdkFormat=[MediaType(code="json")]),
            Distribution(fdkFormat=[MediaType(code="geo+json")]),
            Distribution(
                fdkFormat=[
                    MediaType(
                        uri="https://www.iana.org/assignments/media-types/text/turtle"
                    )
                ]
            ),
            Distribution(fdkFormat=[MediaType(code="Rubbish")]),
            Distribution(),
        ]
    )

    expected = Dataset(
        distribution=[
            Distribution(
                mediaType=[
                    SkosCode(
                        uri="https://www.iana.org/assignments/media-types/application/xml",
                        code="application/xml",
                        prefLabel={"nb": "application/xml"},
                    ),
                ],
                fdkFormat=[
                    MediaType(
                        uri="https://www.iana.org/assignments/media-types/application/xml",
                        fdkType=FDKFormatType.MEDIA_TYPE,
                        code="application/xml",
                    ),
                ],
            ),
            Distribution(
                mediaType=[
                    SkosCode(
                        uri="http://publications.europa.eu/resource/authority/file-type/XML",
                        code="XML",
                        prefLabel={"nb": "XML"},
                    ),
                ],
                fdkFormat=[
                    MediaType(
                        uri="http://publications.europa.eu/resource/authority/file-type/XML",
                        fdkType=FDKFormatType.FILE_TYPE,
                        code="XML",
                    ),
                ],
            ),
            Distribution(
                fdkFormat=[MediaType(code="CSV", fdkType=FDKFormatType.UNKNOWN)],
            ),
            Distribution(
                fdkFormat=[MediaType(code="json", fdkType=FDKFormatType.UNKNOWN)],
            ),
            Distribution(
                fdkFormat=[MediaType(code="geo+json", fdkType=FDKFormatType.UNKNOWN)],
            ),
            Distribution(
                mediaType=[
                    SkosCode(
                        uri="https://www.iana.org/assignments/media-types/text/turtle",
                        code="text/turtle",
                        prefLabel={"nb": "text/turtle"},
                    ),
                ],
                fdkFormat=[
                    MediaType(
                        uri="https://www.iana.org/assignments/media-types/text/turtle",
                        code="text/turtle",
                        fdkType=FDKFormatType.MEDIA_TYPE,
                    ),
                ],
            ),
            Distribution(
                fdkFormat=[MediaType(code="Rubbish", fdkType=FDKFormatType.UNKNOWN)],
            ),
            Distribution(),
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

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )


def test_extend_themes() -> None:
    parsed_dataset = Dataset(
        theme=[
            EuDataTheme(
                id="http://publications.europa.eu/resource/authority/data-theme/ECON"
            ),
            EuDataTheme(id="https://psi.norge.no/los/tema/kultur"),
            EuDataTheme(id="https://psi.norge.no/not/in/los/or/eu"),
        ]
    )

    expected = Dataset(
        theme=[
            EuDataTheme(
                id="http://publications.europa.eu/resource/authority/data-theme/ECON",
                code="ECON",
                startUse="2015-10-01",
                title={"nb": "Økonomi og finans", "en": "Economy and finance"},
                conceptSchema=ConceptSchema(
                    id="http://publications.europa.eu/resource/authority/data-theme",
                    title={"en": "Dataset types Named Authority List"},
                    versioninfo="20160921-0",
                    versionnumber="20160921-0",
                ),
            ),
            EuDataTheme(id="https://psi.norge.no/not/in/los/or/eu"),
        ],
        losTheme=[
            LosNode(
                children=[
                    "https://psi.norge.no/los/ord/film-og-kino",
                    "https://psi.norge.no/los/ord/kulturtilbud",
                ],
                parents=["https://psi.norge.no/los/tema/kultur-idrett-og-fritid"],
                isTema=True,
                losPaths=["kultur-idrett-og-fritid/kultur"],
                name={"nn": "Kultur", "nb": "Kultur", "en": "Culture"},
                definition=None,
                uri="https://psi.norge.no/los/tema/kultur",
                synonyms=[],
                relatedTerms=None,
            )
        ],
    )

    assert (
        extend_dataset_with_reference_data(parsed_dataset, dataset_reference_data)
        == expected
    )
