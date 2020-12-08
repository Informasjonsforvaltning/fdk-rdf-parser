from dataclasses import dataclass
from typing import Dict, Optional

from fdk_rdf_parser.classes import SkosCode, ThemeEU, ThemeLOS
from .reference_data_client import get_reference_data
from .utils import remove_trailing_slash


@dataclass
class DataServiceReferenceData:
    media_types: Optional[Dict[str, SkosCode]] = None


@dataclass
class DatasetReferenceData:
    provenancestatement: Optional[Dict[str, SkosCode]] = None
    rightsstatement: Optional[Dict[str, SkosCode]] = None
    frequency: Optional[Dict[str, SkosCode]] = None
    linguisticsystem: Optional[Dict[str, SkosCode]] = None
    referencetypes: Optional[Dict[str, SkosCode]] = None
    openlicenses: Optional[Dict[str, SkosCode]] = None
    location: Optional[Dict[str, SkosCode]] = None
    eu_themes: Optional[Dict[str, ThemeEU]] = None
    los_themes: Optional[Dict[str, ThemeLOS]] = None


@dataclass
class InformationModelReferenceData:
    linguisticsystem: Optional[Dict[str, SkosCode]] = None
    openlicenses: Optional[Dict[str, SkosCode]] = None
    location: Optional[Dict[str, SkosCode]] = None
    eu_themes: Optional[Dict[str, ThemeEU]] = None
    los_themes: Optional[Dict[str, ThemeLOS]] = None


@dataclass
class PublicServiceReferenceData:
    linguisticsystem: Optional[Dict[str, SkosCode]] = None


def get_data_service_reference_data() -> DataServiceReferenceData:
    return DataServiceReferenceData(media_types=get_and_map_media_types())


def get_dataset_reference_data() -> DatasetReferenceData:
    return DatasetReferenceData(
        provenancestatement=get_and_map_reference_codes("provenancestatement"),
        rightsstatement=get_and_map_reference_codes("rightsstatement"),
        frequency=get_and_map_reference_codes("frequency"),
        linguisticsystem=get_and_map_reference_codes("linguisticsystem"),
        referencetypes=get_and_map_reference_codes("referencetypes"),
        openlicenses=get_and_map_open_licenses(),
        location=get_and_map_reference_codes("location"),
        eu_themes=get_and_map_themes_eu(),
        los_themes=get_and_map_themes_los(),
    )


def get_info_model_reference_data() -> InformationModelReferenceData:
    return InformationModelReferenceData(
        linguisticsystem=get_and_map_reference_codes("linguisticsystem"),
        openlicenses=get_and_map_open_licenses(),
        location=get_and_map_reference_codes("location"),
        eu_themes=get_and_map_themes_eu(),
        los_themes=get_and_map_themes_los(),
    )


def get_public_service_reference_data() -> PublicServiceReferenceData:
    return PublicServiceReferenceData(
        linguisticsystem=get_and_map_reference_codes("linguisticsystem")
    )


def get_and_map_reference_codes(endpoint: str) -> Optional[Dict[str, SkosCode]]:
    codes = get_reference_data(f"/codes/{endpoint}")
    if codes is not None:
        return {
            remove_trailing_slash(str(code.get("uri"))): SkosCode(
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


def get_and_map_themes_eu() -> Optional[Dict[str, ThemeEU]]:
    mapped = {}
    themes = get_reference_data("/themes")
    if themes is not None:
        for theme in themes:
            eu_theme = ThemeEU()
            eu_theme.add_values_from_dict(theme)
            mapped[str(theme.get("id"))] = eu_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_themes_los() -> Optional[Dict[str, ThemeLOS]]:
    mapped = {}
    themes = get_reference_data("/los")
    if themes is not None:
        for theme in themes:
            los_theme = ThemeLOS()
            los_theme.add_values_from_dict(theme)
            mapped[str(theme.get("uri"))] = los_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_media_types() -> Optional[Dict[str, SkosCode]]:
    media_types = {}
    codes = get_reference_data("/codes/mediatypes")
    if codes is not None:
        for code in codes:
            if code.get("code"):
                media_types[str(code.get("code"))] = SkosCode(
                    code=str(code.get("code")),
                    prefLabel={"nb": str(code.get("name"))}
                    if code.get("name")
                    else None,
                )
    return media_types if len(media_types) > 0 else None


def get_and_map_open_licenses() -> Optional[Dict[str, SkosCode]]:
    licenses_with_both_protocols = {}
    licenses = get_and_map_reference_codes("openlicenses")
    if licenses:
        for li in licenses:
            licenses_with_both_protocols[li] = licenses[li]
            if li.startswith("http://"):
                https_uri = "https://" + li.split("http://")[1]
                licenses_with_both_protocols[https_uri] = licenses[li]
            elif li.startswith("https://"):
                http_uri = "http://" + li.split("https://")[1]
                licenses_with_both_protocols[http_uri] = licenses[li]

    return (
        licenses_with_both_protocols if len(licenses_with_both_protocols) > 0 else None
    )
