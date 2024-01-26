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
    types={
        "publications.europa.eu/resource/authority/main-activity/defence": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/main-activity/defence",
            code="defence",
            prefLabel={"en": "Defence"},
        ),
    },
)
