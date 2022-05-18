from fdk_rdf_parser.classes import Service
from .reference_data import PublicServiceReferenceData
from .utils import extend_skos_code_list


def extend_cpsvno_service_with_reference_data(
    cpsvno_service: Service, ref_data: PublicServiceReferenceData
) -> Service:
    cpsvno_service.language = extend_skos_code_list(
        cpsvno_service.language, ref_data.linguisticsystem
    )

    return cpsvno_service
