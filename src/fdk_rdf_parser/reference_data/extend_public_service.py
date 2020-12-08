from fdk_rdf_parser.classes import PublicService
from .reference_data import PublicServiceReferenceData
from .utils import extend_skos_code_list


def extend_public_service_with_reference_data(
    public_service: PublicService, ref_data: PublicServiceReferenceData
) -> PublicService:
    public_service.language = extend_skos_code_list(
        public_service.language, ref_data.linguisticsystem
    )

    return public_service
