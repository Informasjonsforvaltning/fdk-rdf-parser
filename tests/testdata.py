from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.reference_data import PublicServiceReferenceData

public_service_reference_data = PublicServiceReferenceData(
    types={
        "publications.europa.eu/resource/authority/main-activity/defence": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/main-activity/defence",
            code="defence",
            prefLabel={"en": "Defence"},
        ),
    },
)
