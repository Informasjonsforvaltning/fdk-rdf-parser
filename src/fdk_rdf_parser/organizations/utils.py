import os
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
