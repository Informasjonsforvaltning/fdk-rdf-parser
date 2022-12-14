import os
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes import (
    EuDataTheme,
    LosNode,
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
            ref.referenceType = extend_skos_code(ref.referenceType, reference_types)
            extended_references.append(ref)
        return extended_references


def collect_los_themes(
    theme_uris: Optional[List[str]],
    los: Optional[Dict[str, LosNode]],
) -> Optional[List[LosNode]]:
    if los is None or theme_uris is None:
        return None

    collected_los_themes: List[LosNode] = list()
    for uri in theme_uris:
        uri = remove_scheme_and_trailing_slash(uri)
        if uri in los:
            collected_los_themes.append(los[uri])

    return collected_los_themes if len(collected_los_themes) > 0 else None


def collect_eu_data_themes(
    theme_uris: Optional[List[str]],
    eu_data_themes: Optional[Dict[str, EuDataTheme]],
) -> Optional[List[EuDataTheme]]:
    if eu_data_themes is None or theme_uris is None:
        return None

    collected_eu_data_themes: List[EuDataTheme] = list()
    for uri in theme_uris:
        uri = remove_scheme_and_trailing_slash(uri)
        if uri in eu_data_themes:
            collected_eu_data_themes.append(eu_data_themes[uri])

    return collected_eu_data_themes if len(collected_eu_data_themes) > 0 else None


def split_themes(
    themes: Optional[List[EuDataTheme]],
    los: Optional[Dict[str, LosNode]],
) -> Dict[str, List[EuDataTheme]]:
    splitted_themes: Dict[str, List[EuDataTheme]] = {"los": [], "eu_data_themes": []}
    if themes is None:
        return splitted_themes
    elif los is None:
        splitted_themes["eu_data_themes"] = themes
        return splitted_themes
    else:
        for theme in themes:
            if remove_scheme_and_trailing_slash(theme.id) in los:
                splitted_themes["los"].append(theme)
            else:
                splitted_themes["eu_data_themes"].append(theme)
        return splitted_themes


def extend_los_themes(
    themes: List[EuDataTheme], los: Optional[Dict[str, LosNode]]
) -> Optional[List[LosNode]]:
    extended = []
    if los is not None:
        for theme in themes:
            extended.append(los[remove_scheme_and_trailing_slash(str(theme.id))])
    return extended if len(extended) > 0 else None


def extend_eu_data_themes(
    themes: List[EuDataTheme], eu_data_themes: Optional[Dict[str, EuDataTheme]]
) -> Optional[List[EuDataTheme]]:
    extended = []
    if eu_data_themes is not None:
        for theme in themes:
            eu_theme = (
                eu_data_themes.get(remove_scheme_and_trailing_slash(theme.id))
                if theme.id is not None
                else None
            )
            if eu_theme is None:
                extended.append(theme)
            else:
                extended.append(eu_theme)
    return extended if len(extended) > 0 else None


def extend_skos_code(
    skos_code: Optional[ReferenceDataCode],
    references: Optional[Dict[str, ReferenceDataCode]],
) -> Optional[ReferenceDataCode]:
    ref_code = None
    if references is not None:
        uri = skos_code.uri if skos_code is not None else None
        if uri is not None:
            ref_code = (
                references.get(remove_scheme_and_trailing_slash(uri))
                if references is not None
                else None
            )

    return ref_code if ref_code is not None else skos_code


def extend_skos_code_list(
    skos_codes: Optional[List[ReferenceDataCode]],
    references: Optional[Dict[str, ReferenceDataCode]],
) -> Optional[List[ReferenceDataCode]]:
    if skos_codes is None or references is None:
        return skos_codes
    else:
        extended_codes = []
        for code in skos_codes:
            ref_code = (
                references.get(remove_scheme_and_trailing_slash(code.uri))
                if code.uri is not None
                else None
            )
            if ref_code is not None:
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
