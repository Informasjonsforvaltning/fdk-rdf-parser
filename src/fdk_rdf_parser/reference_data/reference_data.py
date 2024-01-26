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
class PublicServiceReferenceData:
    types: Optional[Dict[str, ReferenceDataCode]] = None
    organization_types: Optional[Dict[str, ReferenceDataCode]] = None


def get_public_service_reference_data() -> PublicServiceReferenceData:
    return PublicServiceReferenceData(
        types=get_and_map_dct_types(),
        organization_types=get_and_map_organization_types(),
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


def get_and_map_dct_types() -> Optional[Dict[str, ReferenceDataCode]]:
    dct_types = get_reference_data("/eu/main-activities").get("mainActivities")
    return parse_reference_codes(dct_types)


def get_and_map_organization_types() -> Optional[Dict[str, ReferenceDataCode]]:
    organization_types = get_reference_data("/adms/publisher-types").get(
        "publisherTypes"
    )
    return parse_reference_codes(organization_types)
