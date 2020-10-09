import os
import re
from typing import Optional

base_org_url = os.getenv(
    "ORGANIZATION_CATALOGUE_BASE_URI",
    "https://organization-catalogue.staging.fellesdatakatalog.digdir.no",
)


def organization_url(orgnr: Optional[str]) -> str:
    return (
        f"{base_org_url}/organizations/{orgnr}"
        if orgnr is not None
        else f"{base_org_url}/organizations"
    )


def org_path_url(org: str) -> str:
    return f"{base_org_url}/organizations/orgpath/{org}"


def organization_number_from_uri(uri: str) -> Optional[str]:
    match = re.compile(
        "https://data.brreg.no/enhetsregisteret/api/enheter/(\\d{9})$"
    ).match(uri)
    return match.group(1) if match else None
