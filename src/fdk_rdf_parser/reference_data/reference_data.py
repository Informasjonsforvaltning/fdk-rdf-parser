from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes import ReferenceDataCode
from .reference_data_client import get_reference_data
from .utils import remove_scheme_and_trailing_slash


@dataclass
class DatasetReferenceData:
    provenancestatement: Optional[Dict[str, ReferenceDataCode]] = None
    frequency: Optional[Dict[str, ReferenceDataCode]] = None
    referencetypes: Optional[Dict[str, ReferenceDataCode]] = None


@dataclass
class PublicServiceReferenceData:
    week_days: Optional[Dict[str, ReferenceDataCode]] = None
    statuses: Optional[Dict[str, ReferenceDataCode]] = None
    types: Optional[Dict[str, ReferenceDataCode]] = None
    evidence_type: Optional[Dict[str, ReferenceDataCode]] = None
    channel_type: Optional[Dict[str, ReferenceDataCode]] = None
    organization_types: Optional[Dict[str, ReferenceDataCode]] = None
    role_types: Optional[Dict[str, ReferenceDataCode]] = None


def get_dataset_reference_data() -> DatasetReferenceData:
    return DatasetReferenceData(
        provenancestatement=get_and_map_provenance_statements(),
        frequency=get_and_map_frequencies(),
        referencetypes=get_and_map_reference_types(),
    )


def get_public_service_reference_data() -> PublicServiceReferenceData:
    return PublicServiceReferenceData(
        week_days=get_and_map_week_days(),
        statuses=get_and_map_statuses(),
        evidence_type=get_and_map_evidence_types(),
        types=get_and_map_dct_types(),
        channel_type=get_and_map_channel_types(),
        organization_types=get_and_map_organization_types(),
        role_types=get_and_map_role_types(),
    )


def parse_reference_codes(
    codes: Optional[List[Dict]],
) -> Optional[Dict[str, ReferenceDataCode]]:
    if codes is not None:
        return {
            remove_scheme_and_trailing_slash(str(code.get("uri"))): ReferenceDataCode(
                uri=str(code.get("uri")) if code.get("uri") is not None else None,
                code=str(code.get("code")) if code.get("code") is not None else None,
                prefLabel=code.get("label") if code.get("label") is not None else None,
            )
            for code in codes
        }
    else:
        return None


def get_and_map_frequencies() -> Optional[Dict[str, ReferenceDataCode]]:
    frequencies = get_reference_data("/eu/frequencies").get("frequencies")
    return parse_reference_codes(frequencies)


def get_and_map_provenance_statements() -> Optional[Dict[str, ReferenceDataCode]]:
    provenance_statements = get_reference_data("/provenance-statements").get(
        "provenanceStatements"
    )
    return parse_reference_codes(provenance_statements)


def get_and_map_reference_types() -> Optional[Dict[str, ReferenceDataCode]]:
    reference_types = get_reference_data("/reference-types").get("referenceTypes")
    return parse_reference_codes(reference_types)


def get_and_map_week_days() -> Optional[Dict[str, ReferenceDataCode]]:
    week_days = get_reference_data("/schema/week-days").get("weekDays")
    return parse_reference_codes(week_days)


def get_and_map_statuses() -> Optional[Dict[str, ReferenceDataCode]]:
    statuses = get_reference_data("/adms/statuses").get("statuses")
    return parse_reference_codes(statuses)


def get_and_map_dct_types() -> Optional[Dict[str, ReferenceDataCode]]:
    dct_types = get_reference_data("/eu/main-activities").get("mainActivities")
    return parse_reference_codes(dct_types)


def get_and_map_channel_types() -> Optional[Dict[str, ReferenceDataCode]]:
    channels = get_reference_data("/digdir/service-channel-types").get(
        "serviceChannelTypes"
    )
    return parse_reference_codes(channels)


def get_and_map_organization_types() -> Optional[Dict[str, ReferenceDataCode]]:
    organization_types = get_reference_data("/adms/publisher-types").get(
        "publisherTypes"
    )
    return parse_reference_codes(organization_types)


def get_and_map_evidence_types() -> Optional[Dict[str, ReferenceDataCode]]:
    evidence_types = get_reference_data("/digdir/evidence-types").get("evidenceTypes")
    return parse_reference_codes(evidence_types)


def get_and_map_role_types() -> Optional[Dict[str, ReferenceDataCode]]:
    role_types = get_reference_data("/digdir/role-types").get("roleTypes")
    return parse_reference_codes(role_types)
