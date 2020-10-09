import os
from typing import Dict, List, Optional

from fdk_rdf_parser.classes import SkosCode

base_url = os.getenv(
    "REFERENCE_DATA_BASE_URI",
    "http://staging.fellesdatakatalog.digdir.no/reference-data",
)


def reference_data_url(endpoint: str) -> str:
    return f"{base_url}{endpoint}"


def extend_skos_code(
    skos_code: Optional[SkosCode], references: Optional[Dict[str, SkosCode]]
) -> Optional[SkosCode]:
    ref_code = None
    if references is not None:
        uri = skos_code.uri if skos_code is not None else None
        if uri is not None:
            ref_code = (
                references.get(remove_trailing_slash(uri))
                if references is not None
                else None
            )
            if ref_code is not None:
                return ref_code

    return ref_code


def extend_skos_code_list(
    skos_codes: Optional[List[SkosCode]], references: Optional[Dict[str, SkosCode]]
) -> Optional[List[SkosCode]]:
    if skos_codes is None or references is None:
        return skos_codes
    else:
        extended_codes = []
        for code in skos_codes:
            ref_code = (
                references.get(remove_trailing_slash(code.uri))
                if code.uri is not None
                else None
            )
            if ref_code is not None:
                extended_codes.append(ref_code)
            else:
                extended_codes.append(code)
        return extended_codes


def remove_trailing_slash(uri: str) -> str:
    if uri.endswith("/"):
        return uri[:-1]
    else:
        return uri
