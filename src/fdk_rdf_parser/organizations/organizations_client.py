import logging
from typing import Optional

import requests

from .utils import org_path_url, organization_url


def get_rdf_org_data(orgnr: Optional[str]) -> Optional[str]:

    try:
        response = requests.get(
            organization_url(orgnr),
            headers={"Accept": "text/turtle"},
        )
        response.raise_for_status()

        return response.text
    except requests.HTTPError as err:
        logging.error(f"Error response from organization-catalogue ({err})")

    return None


def get_org_path(org: str) -> Optional[str]:

    try:
        response = requests.get(
            org_path_url(org),
            headers={"Accept": "text/plain"},
        )
        response.raise_for_status()

        return response.text
    except requests.HTTPError as err:

        logging.error(f"Error response from organization-catalogue ({err})")

    return None
