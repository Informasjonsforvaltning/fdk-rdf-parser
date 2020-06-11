from dataclasses import dataclass
from typing import Dict, Optional

from fdk_rdf_parser.classes import SkosCode, ThemeEU, ThemeLOS
from .reference_data_client import getReferenceData


@dataclass
class ReferenceData:
    provenancestatement: Optional[Dict[str, SkosCode]] = None
    rightsstatement: Optional[Dict[str, SkosCode]] = None
    frequency: Optional[Dict[str, SkosCode]] = None
    linguisticsystem: Optional[Dict[str, SkosCode]] = None
    referencetypes: Optional[Dict[str, SkosCode]] = None
    openlicenses: Optional[Dict[str, SkosCode]] = None
    location: Optional[Dict[str, SkosCode]] = None
    euThemes: Optional[Dict[str, ThemeEU]] = None
    losThemes: Optional[Dict[str, ThemeLOS]] = None


def getAllReferenceData() -> ReferenceData:
    return ReferenceData(
        provenancestatement=getAndMapReferenceCodes("provenancestatement"),
        rightsstatement=getAndMapReferenceCodes("rightsstatement"),
        frequency=getAndMapReferenceCodes("frequency"),
        linguisticsystem=getAndMapReferenceCodes("linguisticsystem"),
        referencetypes=getAndMapReferenceCodes("referencetypes"),
        openlicenses=getAndMapReferenceCodes("openlicenses"),
        location=getAndMapReferenceCodes("location"),
        euThemes=getAndMapThemesEU(),
        losThemes=getAndMapThemesLOS(),
    )


def getAndMapReferenceCodes(endpoint: str) -> Optional[Dict[str, SkosCode]]:
    codes = getReferenceData(f"/codes/{endpoint}")
    if codes is not None:
        return {
            str(code.get("uri")): SkosCode(
                uri=str(code.get("uri")) if code.get("uri") is not None else None,
                code=str(code.get("code")) if code.get("code") is not None else None,
                prefLabel=code.get("prefLabel")
                if code.get("prefLabel") is not None
                else None,
            )
            for code in codes
        }
    else:
        return None


def getAndMapThemesEU() -> Optional[Dict[str, ThemeEU]]:
    mapped = {}
    themes = getReferenceData("/themes")
    if themes is not None:
        for theme in themes:
            euTheme = ThemeEU()
            euTheme.addValuesFromDict(theme)
            mapped[str(theme.get("id"))] = euTheme
    return mapped if len(mapped) > 0 else None


def getAndMapThemesLOS() -> Optional[Dict[str, ThemeLOS]]:
    mapped = {}
    themes = getReferenceData("/los")
    if themes is not None:
        for theme in themes:
            losTheme = ThemeLOS()
            losTheme.addValuesFromDict(theme)
            mapped[str(theme.get("uri"))] = losTheme
    return mapped if len(mapped) > 0 else None
