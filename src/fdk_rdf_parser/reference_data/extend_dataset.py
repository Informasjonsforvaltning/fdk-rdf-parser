from typing import Dict, List, Optional

from fdk_rdf_parser.classes import (
    Dataset,
    Distribution,
    Reference,
    SkosCode,
    ThemeEU,
    ThemeLOS,
)
from .reference_data import ReferenceData


def extendDatasetWithReferenceData(dataset: Dataset, refData: ReferenceData) -> Dataset:
    dataset.accessRights = extendSkosCode(dataset.accessRights, refData.rightsstatement)
    dataset.provenance = extendSkosCode(dataset.provenance, refData.provenancestatement)
    dataset.accrualPeriodicity = extendSkosCode(
        dataset.accrualPeriodicity, refData.frequency
    )
    dataset.language = extendSkosCodeList(dataset.language, refData.linguisticsystem)
    dataset.spatial = extendSkosCodeList(dataset.spatial, refData.location)
    dataset.distribution = extendDistributions(
        dataset.distribution, refData.openlicenses
    )
    dataset.references = extendReferenceTypes(
        dataset.references, refData.referencetypes
    )

    splitThemes = splitLOSFromEUThemes(dataset.theme, refData.losThemes)
    dataset.losTheme = extendLOSThemes(splitThemes["los"], refData.losThemes)
    dataset.theme = extendEUThemes(splitThemes["eu"], refData.euThemes)

    return dataset


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


def extendDistributions(
    distributions: Optional[List[Distribution]],
    openLicenses: Optional[Dict[str, SkosCode]],
) -> Optional[List[Distribution]]:
    if distributions is None or openLicenses is None:
        return distributions
    else:
        extendedDistributions = []
        for dist in distributions:
            if dist.license is not None:
                extendedLicenses = []
                for lic in dist.license:
                    refCode = openLicenses.get(lic.uri) if lic.uri is not None else None
                    if refCode is not None:
                        dist.openLicense = True
                        if lic.prefLabel is None:
                            lic.prefLabel = refCode.prefLabel
                    extendedLicenses.append(lic)
                dist.license = extendedLicenses
            extendedDistributions.append(dist)
        return extendedDistributions


def extendReferenceTypes(
    references: Optional[List[Reference]], referenceTypes: Optional[Dict[str, SkosCode]]
) -> Optional[List[Reference]]:
    if references is None or referenceTypes is None:
        return references
    else:
        extendedReferences = []
        for ref in references:
            ref.referenceType = extendSkosCode(ref.referenceType, referenceTypes)
            extendedReferences.append(ref)
        return extendedReferences


def splitLOSFromEUThemes(
    themes: Optional[List[ThemeEU]], los: Optional[Dict[str, ThemeLOS]],
) -> Dict[str, List[ThemeEU]]:
    splitThemes: Dict[str, List[ThemeEU]] = {}
    splitThemes["los"] = []
    splitThemes["eu"] = []
    if themes is None:
        return splitThemes
    elif los is None:
        splitThemes["eu"] = themes
        return splitThemes
    else:
        for theme in themes:
            if theme.id in los:
                splitThemes["los"].append(theme)
            else:
                splitThemes["eu"].append(theme)
        return splitThemes


def extendLOSThemes(
    themes: List[ThemeEU], los: Optional[Dict[str, ThemeLOS]]
) -> Optional[List[ThemeLOS]]:
    extended = []
    if los is not None:
        for theme in themes:
            extended.append(los[str(theme.id)])
    return extended if len(extended) > 0 else None


def extendEUThemes(
    themes: List[ThemeEU], euThemes: Optional[Dict[str, ThemeEU]]
) -> Optional[List[ThemeEU]]:
    extended = []
    if euThemes is not None:
        for theme in themes:
            euTheme = euThemes.get(theme.id) if theme.id is not None else None
            if euTheme is None:
                extended.append(theme)
            else:
                extended.append(euTheme)
    return extended if len(extended) > 0 else None
