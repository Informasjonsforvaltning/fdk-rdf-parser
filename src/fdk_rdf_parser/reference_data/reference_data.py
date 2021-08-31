from dataclasses import dataclass
from typing import Dict, Optional

from fdk_rdf_parser.classes import EuDataTheme, LosNode, MediaType, SkosCode
from .reference_data_client import get_new_reference_data, get_reference_data
from .utils import remove_trailing_slash


@dataclass
class DataServiceReferenceData:
    media_types: Optional[Dict[str, MediaType]] = None


@dataclass
class DatasetReferenceData:
    provenancestatement: Optional[Dict[str, SkosCode]] = None
    rightsstatement: Optional[Dict[str, SkosCode]] = None
    frequency: Optional[Dict[str, SkosCode]] = None
    linguisticsystem: Optional[Dict[str, SkosCode]] = None
    referencetypes: Optional[Dict[str, SkosCode]] = None
    openlicenses: Optional[Dict[str, SkosCode]] = None
    location: Optional[Dict[str, SkosCode]] = None
    eu_data_themes: Optional[Dict[str, EuDataTheme]] = None
    los_themes: Optional[Dict[str, LosNode]] = None
    media_types: Optional[Dict[str, MediaType]] = None


@dataclass
class InformationModelReferenceData:
    linguisticsystem: Optional[Dict[str, SkosCode]] = None
    openlicenses: Optional[Dict[str, SkosCode]] = None
    location: Optional[Dict[str, SkosCode]] = None
    eu_data_themes: Optional[Dict[str, EuDataTheme]] = None
    los_themes: Optional[Dict[str, LosNode]] = None


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
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
        media_types=get_and_map_media_types(),
    )


def get_info_model_reference_data() -> InformationModelReferenceData:
    return InformationModelReferenceData(
        linguisticsystem=get_and_map_reference_codes("linguisticsystem"),
        openlicenses=get_and_map_open_licenses(),
        location=get_and_map_reference_codes("location"),
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
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


def get_and_map_eu_data_themes() -> Optional[Dict[str, EuDataTheme]]:
    mapped = {}
    themes = get_new_reference_data("/eu/data-themes").get("dataThemes")
    if themes is not None:
        for theme in themes:
            eu_theme = EuDataTheme()
            eu_theme.add_values_from_dict(theme)
            mapped[str(theme.get("uri"))] = eu_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_los_themes() -> Optional[Dict[str, LosNode]]:
    mapped = {}
    los_nodes = get_new_reference_data("/los/themes-and-words").get("losNodes")
    if los_nodes is not None:
        for los_node in los_nodes:
            los_theme = LosNode()
            los_theme.add_values_from_dict(los_node)
            mapped[str(los_node.get("uri"))] = los_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_media_types() -> Optional[Dict[str, MediaType]]:
    media_types = {}
    codes = get_new_reference_data("/iana/media-types").get("mediaTypes")
    if codes is not None:
        for code in codes:
            media_type = MediaType(
                uri=str(code["uri"]) if code.get("uri") else None,
                type=str(code["type"]) if code.get("type") else None,
                subType=str(code["subType"]) if code.get("subType") else None,
                name=str(code["name"]) if code.get("name") else None,
            )
            if media_type.uri:
                media_types[media_type.uri] = media_type

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
