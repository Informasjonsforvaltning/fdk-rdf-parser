import logging
from typing import Optional

import requests

from .utils import organizationUrl


def getRdfOrgData(orgnr: Optional[str]) -> Optional[str]:

    try:
        req = requests.get(organizationUrl(orgnr), headers={"Accept": "text/turtle"},)

        return req.text
    except requests.HTTPError as err:
        logging.error(f"Error response from organization-catalogue ({err})")

    return None
