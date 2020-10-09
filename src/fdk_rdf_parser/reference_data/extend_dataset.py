from typing import Dict, List, Optional

from fdk_rdf_parser.classes import (
    Dataset,
    Distribution,
    Reference,
    SkosCode,
    ThemeEU,
    ThemeLOS,
)
from .reference_data import DatasetReferenceData
from .utils import extend_skos_code, extend_skos_code_list, remove_trailing_slash


def extend_dataset_with_reference_data(
    dataset: Dataset, ref_data: DatasetReferenceData
) -> Dataset:
    dataset.accessRights = extend_skos_code(
        dataset.accessRights, ref_data.rightsstatement
    )
    dataset.provenance = extend_skos_code(
        dataset.provenance, ref_data.provenancestatement
    )
    dataset.accrualPeriodicity = extend_skos_code(
        dataset.accrualPeriodicity, ref_data.frequency
    )
    dataset.language = extend_skos_code_list(
        dataset.language, ref_data.linguisticsystem
    )
    dataset.spatial = extend_skos_code_list(dataset.spatial, ref_data.location)
    dataset.distribution = extend_distributions(
        dataset.distribution, ref_data.openlicenses
    )
    dataset.references = extend_reference_types(
        dataset.references, ref_data.referencetypes
    )

    split_themes = split_los_from_eu_themes(dataset.theme, ref_data.los_themes)
    dataset.losTheme = extend_los_themes(split_themes["los"], ref_data.los_themes)
    dataset.theme = extend_eu_themes(split_themes["eu"], ref_data.eu_themes)

    return dataset


def extend_distributions(
    distributions: Optional[List[Distribution]],
    open_licenses: Optional[Dict[str, SkosCode]],
) -> Optional[List[Distribution]]:
    if distributions is None or open_licenses is None:
        return distributions
    else:
        extended_distributions = []
        for dist in distributions:
            if dist.license is not None:
                extended_licenses = []
                for lic in dist.license:
                    ref_code = (
                        open_licenses.get(remove_trailing_slash(lic.uri))
                        if lic.uri is not None
                        else None
                    )
                    if ref_code is not None:
                        dist.openLicense = True
                        if lic.prefLabel is None:
                            lic.prefLabel = ref_code.prefLabel
                    extended_licenses.append(lic)
                dist.license = extended_licenses
            extended_distributions.append(dist)
        return extended_distributions


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
    themes: Optional[List[ThemeEU]], los: Optional[Dict[str, ThemeLOS]],
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
