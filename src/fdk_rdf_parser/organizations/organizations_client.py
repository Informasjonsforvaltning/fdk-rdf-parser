import logging
from typing import Optional

import requests

from .utils import organizationUrl, orgPathUrl


def getRdfOrgData(orgnr: Optional[str]) -> Optional[str]:

    try:
        response = requests.get(
            organizationUrl(orgnr), headers={"Accept": "text/turtle"},
        )
        response.raise_for_status()

        return response.text
    except requests.HTTPError as err:
        logging.error(f"Error response from organization-catalogue ({err})")

    return None


def getOrgPath(org: str) -> Optional[str]:

    try:
        response = requests.get(orgPathUrl(org), headers={"Accept": "text/plain"},)
        response.raise_for_status()

        return response.text
    except requests.HTTPError as err:

        logging.error(f"Error response from organization-catalogue ({err})")

    return None
