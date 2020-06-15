import logging
from typing import Dict, List, Optional

import requests

from .utils import referenceDataUrl


def getReferenceData(endpoint: str) -> Optional[List[Dict]]:

    try:
        response = requests.get(
            referenceDataUrl(endpoint), headers={"Accept": "application/json"}
        )

        response.raise_for_status()

        return response.json()

    except requests.HTTPError as err:
        logging.error(f"Http error response from reference-data ({err})")
    except Exception as err:
        logging.error(f"Error occurred when getting data from reference-data: {err}")

    return None
