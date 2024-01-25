from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.reference_data import (
    DatasetReferenceData,
    PublicServiceReferenceData,
)

public_service_reference_data = PublicServiceReferenceData(
    organization_types={
        "purl.org/adms/publishertype/IndustryConsortium": ReferenceDataCode(
            uri="http://purl.org/adms/publishertype/IndustryConsortium",
            code="IndustryConsortium",
            prefLabel={
                "nn": "Industrikonsortium",
                "nb": "Industrikonsortium",
                "en": "Industry consortium",
            },
        ),
        "purl.org/adms/publishertype/NationalAuthority": ReferenceDataCode(
            uri="http://purl.org/adms/publishertype/NationalAuthority",
            code="NationalAuthority",
            prefLabel={
                "nn": "Nasjonal myndigheit",
                "nb": "Nasjonal myndighet",
                "en": "National authority",
            },
        ),
    },
    role_types={
        "data.norge.no/vocabulary/role-type#data-consumer": ReferenceDataCode(
            uri="https://data.norge.no/vocabulary/role-type#data-consumer",
            code="data-consumer",
            prefLabel={
                "nb": "datakonsument",
                "en": "data consumer",
            },
        ),
        "data.norge.no/vocabulary/role-type#data-provider": ReferenceDataCode(
            uri="https://data.norge.no/vocabulary/role-type#data-provider",
            code="data-provider",
            prefLabel={"nb": "dataleverandør", "en": "data provider"},
        ),
    },
    types={
        "publications.europa.eu/resource/authority/main-activity/defence": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/main-activity/defence",
            code="defence",
            prefLabel={"en": "Defence"},
        ),
    },
)

dataset_reference_data = DatasetReferenceData(
    provenancestatement={
        "data.brreg.no/datakatalog/provinens/bruker": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker",
            code="BRUKER",
            prefLabel={
                "nn": "Brukerinnsamlede data",
                "nb": "Brukerinnsamlede data",
                "en": "User collection",
            },
        ),
        "data.brreg.no/datakatalog/provinens/nasjonal": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/nasjonal",
            code="NASJONAL",
            prefLabel={
                "nn": "Autoritativ kilde",
                "nb": "Autoritativ kilde",
                "en": "Authoritativ source",
            },
        ),
        "data.brreg.no/datakatalog/provinens/tredjepart": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/tredjepart",
            code="TREDJEPART",
            prefLabel={"nn": "Tredjepart", "nb": "Tredjepart", "en": "Third party"},
        ),
        "data.brreg.no/datakatalog/provinens/vedtak": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/vedtak",
            code="VEDTAK",
            prefLabel={"nn": "Vedtak", "nb": "Vedtak", "en": "Governmental decisions"},
        ),
    },
    referencetypes={
        "purl.org/dc/terms/hasVersion": ReferenceDataCode(
            uri="http://purl.org/dc/terms/hasVersion",
            code="hasVersion",
            prefLabel={"nn": "Har versjon", "nb": "Har versjon", "en": "Has version"},
        ),
        "purl.org/dc/terms/isPartOf": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isPartOf",
            code="isPartOf",
            prefLabel={"nn": "Er del av", "nb": "Er en del av", "en": "Is Part Of"},
        ),
        "purl.org/dc/terms/isReferencedBy": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isReferencedBy",
            code="isReferencedBy",
            prefLabel={
                "nn": "Er referert av",
                "nb": "Er referert av",
                "en": "Is Referenced By",
            },
        ),
        "purl.org/dc/terms/isReplacedBy": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isReplacedBy",
            code="isReplacedBy",
            prefLabel={
                "nn": "Er erstatta av",
                "nb": "Er erstattet av",
                "en": "Is replaced by",
            },
        ),
        "purl.org/dc/terms/isRequiredBy": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isRequiredBy",
            code="isRequiredBy",
            prefLabel={
                "nn": "Er påkravd av",
                "nb": "Er påkrevd av",
                "en": "Is required by",
            },
        ),
        "purl.org/dc/terms/isVersionOf": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isVersionOf",
            code="isVersionOf",
            prefLabel={
                "nn": "Er versjon av",
                "nb": "Er versjon av",
                "en": "Is version of",
            },
        ),
        "purl.org/dc/terms/references": ReferenceDataCode(
            uri="http://purl.org/dc/terms/references",
            code="references",
            prefLabel={"nn": "Refererar", "nb": "Refererer", "en": "References"},
        ),
        "purl.org/dc/terms/relation": ReferenceDataCode(
            uri="http://purl.org/dc/terms/relation",
            code="relation",
            prefLabel={
                "nn": "Er relatert til",
                "nb": "Er relatert til",
                "en": "Has relation to",
            },
        ),
        "purl.org/dc/terms/replaces": ReferenceDataCode(
            uri="http://purl.org/dc/terms/replaces",
            code="replaces",
            prefLabel={"nn": "Erstatter", "nb": "Erstatter", "en": "Replaces"},
        ),
        "purl.org/dc/terms/requires": ReferenceDataCode(
            uri="http://purl.org/dc/terms/requires",
            code="requires",
            prefLabel={"nn": "Krevjar", "nb": "Krever", "en": "Requires"},
        ),
        "purl.org/dc/terms/source": ReferenceDataCode(
            uri="http://purl.org/dc/terms/source",
            code="source",
            prefLabel={
                "nn": "Er avleda frå (kjelde)",
                "nb": "Er avledet fra (kilde)",
                "en": "Source",
            },
        ),
    },
)
