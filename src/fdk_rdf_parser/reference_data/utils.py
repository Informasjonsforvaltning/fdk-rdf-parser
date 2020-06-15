import os

baseUrl = os.getenv(
    "REFERENCE_DATA_BASE_URI",
    "http://staging.fellesdatakatalog.digdir.no/reference-data",
)


def referenceDataUrl(endpoint: str) -> str:
    return f"{baseUrl}{endpoint}"
