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
    if "data.brreg.no/" in uri or "fellesdatakatalog.digdir.no/organizations/" in uri:
        matches = re.findall("[0-9]{9}", uri)
        return matches[0] if len(matches) == 1 else None
    return None
