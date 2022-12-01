from typing import List, Optional

from fdk_rdf_parser.classes import CVContactPoint, Service
from .reference_data import PublicServiceReferenceData
from .utils import extend_skos_code_list


def extend_cpsvno_service_with_reference_data(
    cpsvno_service: Service, ref_data: PublicServiceReferenceData
) -> Service:
    cpsvno_service.language = extend_skos_code_list(
        cpsvno_service.language, ref_data.linguisticsystem
    )
    cpsvno_service.contactPoint = extend_cv_contact_points(
        cpsvno_service.contactPoint, ref_data
    )

    return cpsvno_service


def extend_cv_contact_points(
    contact_points: Optional[List[CVContactPoint]], ref_data: PublicServiceReferenceData
) -> Optional[List[CVContactPoint]]:
    if contact_points is None:
        return contact_points
    else:
        extended: List[CVContactPoint] = list()
        for contact_point in contact_points:
            contact_point.language = extend_skos_code_list(
                contact_point.language, ref_data.linguisticsystem
            )
            extended.append(contact_point)
        return extended
