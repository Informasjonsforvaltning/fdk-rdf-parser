from typing import Optional
from urllib import error, request

from .utils import organizationUrl


def getRdfOrgData(orgnr: Optional[str]) -> Optional[str]:

    req = request.Request(
        url=organizationUrl(orgnr), headers={"Accept": "text/turtle"}, method="GET",
    )

    try:
        with request.urlopen(req) as response:
            return response.read()
    except error.HTTPError as err:
        print(f"Error response from organization-catalogue ({err.code})")

    return None
