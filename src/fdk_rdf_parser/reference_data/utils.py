import os
from typing import Dict, List, Optional

from fdk_rdf_parser.classes import SkosCode

baseUrl = os.getenv(
    "REFERENCE_DATA_BASE_URI",
    "http://staging.fellesdatakatalog.digdir.no/reference-data",
)


def referenceDataUrl(endpoint: str) -> str:
    return f"{baseUrl}{endpoint}"


def extendSkosCode(
    skosCode: Optional[SkosCode], references: Optional[Dict[str, SkosCode]]
) -> Optional[SkosCode]:
    if references is not None:
        uri = skosCode.uri if skosCode is not None else None
        if uri is not None:
            refCode = references.get(uri) if references is not None else None
            if refCode is not None:
                return refCode

    return skosCode


def extendSkosCodeList(
    skosCodes: Optional[List[SkosCode]], references: Optional[Dict[str, SkosCode]]
) -> Optional[List[SkosCode]]:
    if skosCodes is None or references is None:
        return skosCodes
    else:
        extendedCodes = []
        for code in skosCodes:
            refCode = references.get(code.uri) if code.uri is not None else None
            if refCode is not None:
                extendedCodes.append(refCode)
            else:
                extendedCodes.append(code)
        return extendedCodes
