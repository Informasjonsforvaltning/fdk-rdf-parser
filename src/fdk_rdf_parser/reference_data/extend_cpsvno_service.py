from typing import (
    List,
    Optional,
)

from fdk_rdf_parser.classes import (
    Agent,
    Channel,
    CVContactPoint,
    Evidence,
    Organization,
    Output,
    Participation,
    PublicService,
    Service,
)
from .reference_data import PublicServiceReferenceData
from .utils import (
    extend_reference_data_code,
    extend_reference_data_code_list,
    remove_none_values,
)


def extend_cpsvno_service_with_reference_data(
    cpsvno_service: Service, ref_data: PublicServiceReferenceData
) -> Service:
    cpsvno_service.language = extend_reference_data_code_list(
        cpsvno_service.language, ref_data.linguisticsystem
    )
    cpsvno_service.contactPoint = extend_cv_contact_points(
        cpsvno_service.contactPoint, ref_data
    )
    cpsvno_service.produces = extend_cv_output(cpsvno_service.produces, ref_data)
    cpsvno_service.admsStatus = (
        extend_reference_data_code(cpsvno_service.admsStatus, ref_data.statuses)
        if cpsvno_service.admsStatus
        else None
    )
    cpsvno_service.hasInput = extend_cv_evidence(cpsvno_service.hasInput, ref_data)
    cpsvno_service.dctType = extend_reference_data_code_list(
        cpsvno_service.dctType, ref_data.types
    )
    cpsvno_service.hasChannel = extend_channels(cpsvno_service.hasChannel, ref_data)
    cpsvno_service.ownedBy = extend_organizations(cpsvno_service.ownedBy, ref_data)

    cpsvno_service.participatingAgents = extend_participations_of_agents(
        cpsvno_service.participatingAgents, ref_data
    )

    if isinstance(cpsvno_service, PublicService):
        cpsvno_service.hasCompetentAuthority = extend_organizations(
            cpsvno_service.hasCompetentAuthority, ref_data
        )

    return cpsvno_service


def extend_cv_contact_points(
    contact_points: Optional[List[CVContactPoint]], ref_data: PublicServiceReferenceData
) -> Optional[List[CVContactPoint]]:
    if contact_points is None:
        return contact_points

    for contact_point in contact_points:
        contact_point.language = extend_reference_data_code_list(
            contact_point.language, ref_data.linguisticsystem
        )
    return contact_points


def extend_cv_output(
    outputs: Optional[List[Output]], ref_data: PublicServiceReferenceData
) -> Optional[List[Output]]:
    if outputs is None:
        return outputs

    for output in outputs:
        output.language = extend_reference_data_code_list(
            output.language, ref_data.linguisticsystem
        )
    return outputs


def extend_cv_evidence(
    evidences: Optional[List[Evidence]], ref_data: PublicServiceReferenceData
) -> Optional[List[Evidence]]:
    if evidences is None:
        return None

    for evidence in evidences:
        evidence.dctType = extend_reference_data_code_list(
            evidence.dctType, ref_data.evidence_type
        )
        evidence.language = extend_reference_data_code_list(
            evidence.language, ref_data.linguisticsystem
        )
    return evidences


def extend_channels(
    channels: Optional[List[Channel]], ref_data: PublicServiceReferenceData
) -> Optional[List[Channel]]:
    if channels is None:
        return None

    for channel in channels:
        channel.channelType = (
            extend_reference_data_code(channel.channelType, ref_data.channel_type)
            if channel.channelType
            else None
        )
    return channels


def extend_organizations(
    organizations: Optional[List[Organization]], ref_data: PublicServiceReferenceData
) -> Optional[List[Organization]]:
    if organizations is None:
        return None

    for organization in organizations:
        organization.orgType = (
            extend_reference_data_code(
                organization.orgType, ref_data.organization_types
            )
            if organization.orgType
            else None
        )
    return organizations


def extend_participations_of_agents(
    participating_agents: Optional[List[Agent]], ref_data: PublicServiceReferenceData
) -> Optional[List[Agent]]:
    if participating_agents is None:
        return None

    for agent in participating_agents:
        agent.playsRole = extend_participations(agent.playsRole, ref_data)

    return participating_agents


def extend_participations(
    participations: Optional[List[Participation]], ref_data: PublicServiceReferenceData
) -> Optional[List[Participation]]:
    if participations is None:
        return None

    for participation in participations:
        extended_roles = []
        if participation.role:
            for role in participation.role:
                extended_roles.append(
                    extend_reference_data_code(role, ref_data.role_types)
                )
        filtered_extended_roles = remove_none_values(extended_roles)
        participation.role = (
            filtered_extended_roles if len(filtered_extended_roles) > 0 else None
        )

    return participations
