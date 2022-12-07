from typing import List, Optional

from fdk_rdf_parser.classes import (
    CVContactPoint,
    OpeningHoursSpecification,
    Output,
    Service,
)
from .reference_data import PublicServiceReferenceData
from .utils import extend_skos_code, extend_skos_code_list


def extend_cpsvno_service_with_reference_data(
    cpsvno_service: Service, ref_data: PublicServiceReferenceData
) -> Service:
    cpsvno_service.language = extend_skos_code_list(
        cpsvno_service.language, ref_data.linguisticsystem
    )
    cpsvno_service.contactPoint = extend_cv_contact_points(
        cpsvno_service.contactPoint, ref_data
    )
    cpsvno_service.produces = extend_cv_output(cpsvno_service.produces, ref_data)
    cpsvno_service.admsStatus = extend_skos_code(
        cpsvno_service.admsStatus, ref_data.statuses
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
            contact_point.hoursAvailable = extend_opening_hours_spec(
                contact_point.hoursAvailable, ref_data=ref_data
            )
            contact_point.specialOpeningHours = extend_opening_hours_spec(
                contact_point.specialOpeningHours, ref_data=ref_data
            )
            extended.append(contact_point)
        return extended


def extend_opening_hours_spec(
    opening_hours: Optional[List[OpeningHoursSpecification]],
    ref_data: PublicServiceReferenceData,
) -> Optional[List[OpeningHoursSpecification]]:
    if opening_hours is None:
        return opening_hours
    else:
        extended: List[OpeningHoursSpecification] = list()
        for item in opening_hours:
            item.dayOfWeek = extend_skos_code_list(item.dayOfWeek, ref_data.week_days)
            extended.append(item)
        return extended


def extend_cv_output(
    outputs: Optional[List[Output]], ref_data: PublicServiceReferenceData
) -> Optional[List[Output]]:
    if outputs is None:
        return outputs
    else:
        extended: List[Output] = list()
        for output in outputs:
            output.language = extend_skos_code_list(
                output.language, ref_data.linguisticsystem
            )
            extended.append(output)
        return extended
