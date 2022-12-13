import logging
from typing import (
    Dict,
    List,
)

import requests

from .utils import reference_data_url


def get_reference_data(endpoint: str) -> Dict[str, List[Dict]]:

    try:
        response = requests.get(
            reference_data_url(endpoint), headers={"Accept": "application/json"}
        )

        response.raise_for_status()

        return response.json()

    except requests.HTTPError as err:
        logging.error(f"Http error response from reference-data ({err})")
    except Exception as err:
        logging.error(f"Error occurred when getting data from reference-data: {err}")

    return {}
