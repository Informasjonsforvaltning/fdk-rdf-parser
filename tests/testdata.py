from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.reference_data import PublicServiceReferenceData

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
