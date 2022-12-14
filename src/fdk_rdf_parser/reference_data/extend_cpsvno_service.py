from typing import (
    List,
    Optional,
)

from fdk_rdf_parser.classes import (
    CVContactPoint,
    Evidence,
    OpeningHoursSpecification,
    Output,
    Service,
)
from .reference_data import PublicServiceReferenceData
from .utils import (
    collect_eu_data_themes,
    collect_los_themes,
    extend_skos_code,
    extend_skos_code_list,
)


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
    cpsvno_service.hasInput = extend_cv_evidence(cpsvno_service.hasInput, ref_data)
    cpsvno_service.dctType = extend_skos_code_list(
        cpsvno_service.dctType, ref_data.types
    )

    cpsvno_service.losThemes = collect_los_themes(
        cpsvno_service.thematicAreaUris, ref_data.los_themes
    )
    cpsvno_service.euDataThemes = collect_eu_data_themes(
        cpsvno_service.thematicAreaUris, ref_data.eu_data_themes
    )

    return cpsvno_service


def extend_cv_contact_points(
    contact_points: Optional[List[CVContactPoint]], ref_data: PublicServiceReferenceData
) -> Optional[List[CVContactPoint]]:
    if contact_points is None:
        return contact_points

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
    return contact_points


def extend_opening_hours_spec(
    opening_hours: Optional[List[OpeningHoursSpecification]],
    ref_data: PublicServiceReferenceData,
) -> Optional[List[OpeningHoursSpecification]]:
    if opening_hours is None:
        return opening_hours

    for item in opening_hours:
        item.dayOfWeek = extend_skos_code_list(item.dayOfWeek, ref_data.week_days)
    return opening_hours


def extend_cv_output(
    outputs: Optional[List[Output]], ref_data: PublicServiceReferenceData
) -> Optional[List[Output]]:
    if outputs is None:
        return outputs

    for output in outputs:
        output.language = extend_skos_code_list(
            output.language, ref_data.linguisticsystem
        )
    return outputs


def extend_cv_evidence(
    evidences: Optional[List[Evidence]], ref_data: PublicServiceReferenceData
) -> Optional[List[Evidence]]:
    if evidences is None:
        return None

    for evidence in evidences:
        evidence.dctType = extend_skos_code_list(
            evidence.dctType, ref_data.evidence_type
        )
        evidence.language = extend_skos_code_list(
            evidence.language, ref_data.linguisticsystem
        )
    return evidences
