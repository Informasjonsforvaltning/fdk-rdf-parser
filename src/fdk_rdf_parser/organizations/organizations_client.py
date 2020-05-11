from typing import Optional
from urllib import error, request

organizationsUrl = (
    "https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations"
)


def getRdfOrgData(orgnr: Optional[str]) -> Optional[str]:

    req = request.Request(
        url=f"{organizationsUrl}/{orgnr}" if orgnr is not None else organizationsUrl,
        headers={"Accept": "text/turtle"},
        method="GET",
    )

    try:
        with request.urlopen(req) as response:
            return response.read()
    except error.HTTPError as err:
        print(f"Error response from organization-catalogue ({err.code})")

    return None
