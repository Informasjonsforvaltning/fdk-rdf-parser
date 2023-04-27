import os
from typing import (
    Dict,
    List,
    Optional,
    Sequence,
    TypeVar,
)

from fdk_rdf_parser.classes import (
    Reference,
    ReferenceDataCode,
)

base_url = os.getenv(
    "FDK_REFERENCE_DATA_BASE_URI",
    "https://www.staging.fellesdatakatalog.digdir.no",
)


def reference_data_url(endpoint: str) -> str:
    return f"{base_url}/reference-data{endpoint}"


def extend_reference_types(
    references: Optional[List[Reference]],
    reference_types: Optional[Dict[str, ReferenceDataCode]],
) -> Optional[List[Reference]]:
    if references is None or reference_types is None:
        return references
    else:
        extended_references = []
        for ref in references:
            ref.referenceType = (
                extend_reference_data_code(ref.referenceType, reference_types)
                if ref.referenceType
                else None
            )
            extended_references.append(ref)
        return extended_references


def extend_reference_data_code(
    ref_data_code: ReferenceDataCode,
    references: Optional[Dict[str, ReferenceDataCode]],
) -> ReferenceDataCode:
    ref_code = None
    if references:
        uri = ref_data_code.uri if ref_data_code else None
        ref_code = references.get(remove_scheme_and_trailing_slash(uri))

    return ref_code if ref_code else ref_data_code


def extend_reference_data_code_list(
    ref_data_codes: Optional[List[ReferenceDataCode]],
    references: Optional[Dict[str, ReferenceDataCode]],
) -> Optional[List[ReferenceDataCode]]:
    if ref_data_codes is None or references is None:
        return ref_data_codes

    extended_codes = []
    for code in ref_data_codes:
        ref_code = (
            references.get(remove_scheme_and_trailing_slash(code.uri))
            if code.uri
            else None
        )
        if ref_code:
            extended_codes.append(ref_code)
        else:
            extended_codes.append(code)
    return extended_codes


def remove_scheme_and_trailing_slash(uri: Optional[str]) -> str:
    if uri is None:
        return ""

    uri = uri.replace("http://", "").replace("https://", "")

    if uri.endswith("/"):
        return uri[:-1]
    else:
        return uri


T = TypeVar("T")


def remove_none_values(lst: Sequence[Optional[T]]) -> List[T]:
    return [item for item in lst if item is not None]
