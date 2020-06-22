import os
import re
from typing import Optional

baseOrgUrl = os.getenv(
    "ORGANIZATION_CATALOGUE_BASE_URI",
    "https://organization-catalogue.staging.fellesdatakatalog.digdir.no",
)


def organizationUrl(orgnr: Optional[str]) -> str:
    return (
        f"{baseOrgUrl}/organizations/{orgnr}"
        if orgnr is not None
        else f"{baseOrgUrl}/organizations"
    )


def organisationNumberFromUri(uri: str) -> Optional[str]:
    match = re.compile(
        "https://data.brreg.no/enhetsregisteret/api/enheter/(\\d{9})$"
    ).match(uri)
    return match.group(1) if match else None
