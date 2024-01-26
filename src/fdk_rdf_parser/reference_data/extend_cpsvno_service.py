from typing import (
    List,
    Optional,
)

from fdk_rdf_parser.classes import (
    Channel,
    Organization,
    PublicService,
    Service,
)
from .reference_data import PublicServiceReferenceData
from .utils import (
    extend_reference_data_code,
    extend_reference_data_code_list,
)


def extend_cpsvno_service_with_reference_data(
    cpsvno_service: Service, ref_data: PublicServiceReferenceData
) -> Service:
    cpsvno_service.dctType = extend_reference_data_code_list(
        cpsvno_service.dctType, ref_data.types
    )
    cpsvno_service.hasChannel = extend_channels(cpsvno_service.hasChannel, ref_data)
    cpsvno_service.ownedBy = extend_organizations(cpsvno_service.ownedBy, ref_data)

    if isinstance(cpsvno_service, PublicService):
        cpsvno_service.hasCompetentAuthority = extend_organizations(
            cpsvno_service.hasCompetentAuthority, ref_data
        )

    return cpsvno_service


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
