import os
from typing import Dict, List, Optional

from fdk_rdf_parser.classes import Reference, SkosCode, ThemeEU, ThemeLOS

base_url = os.getenv(
    "REFERENCE_DATA_BASE_URI",
    "http://staging.fellesdatakatalog.digdir.no/reference-data",
)


def reference_data_url(endpoint: str) -> str:
    return f"{base_url}{endpoint}"


def extend_reference_types(
    references: Optional[List[Reference]],
    reference_types: Optional[Dict[str, SkosCode]],
) -> Optional[List[Reference]]:
    if references is None or reference_types is None:
        return references
    else:
        extended_references = []
        for ref in references:
            ref.referenceType = extend_skos_code(ref.referenceType, reference_types)
            extended_references.append(ref)
        return extended_references


def split_los_from_eu_themes(
    themes: Optional[List[ThemeEU]],
    los: Optional[Dict[str, ThemeLOS]],
) -> Dict[str, List[ThemeEU]]:
    split_themes: Dict[str, List[ThemeEU]] = {"los": [], "eu": []}
    if themes is None:
        return split_themes
    elif los is None:
        split_themes["eu"] = themes
        return split_themes
    else:
        for theme in themes:
            if theme.id in los:
                split_themes["los"].append(theme)
            else:
                split_themes["eu"].append(theme)
        return split_themes


def extend_los_themes(
    themes: List[ThemeEU], los: Optional[Dict[str, ThemeLOS]]
) -> Optional[List[ThemeLOS]]:
    extended = []
    if los is not None:
        for theme in themes:
            extended.append(los[str(theme.id)])
    return extended if len(extended) > 0 else None


def extend_eu_themes(
    themes: List[ThemeEU], eu_themes: Optional[Dict[str, ThemeEU]]
) -> Optional[List[ThemeEU]]:
    extended = []
    if eu_themes is not None:
        for theme in themes:
            eu_theme = eu_themes.get(theme.id) if theme.id is not None else None
            if eu_theme is None:
                extended.append(theme)
            else:
                extended.append(eu_theme)
    return extended if len(extended) > 0 else None


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
