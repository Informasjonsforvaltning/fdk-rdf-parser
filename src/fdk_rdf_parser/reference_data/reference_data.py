from dataclasses import dataclass
from typing import Dict, List, Optional

from fdk_rdf_parser.classes import (
    EuDataTheme,
    LosNode,
    MediaTypeOrExtent,
    MediaTypeOrExtentType,
    SkosCode,
)
from .reference_data_client import get_new_reference_data, get_reference_data
from .utils import remove_scheme_and_trailing_slash


@dataclass
class DataServiceReferenceData:
    media_types: Optional[Dict[str, MediaTypeOrExtent]] = None


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
    media_types: Optional[Dict[str, MediaTypeOrExtent]] = None


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
        rightsstatement=get_and_map_access_rights(),
        frequency=get_and_map_reference_codes("frequency"),
        linguisticsystem=get_and_map_reference_codes("linguisticsystem"),
        referencetypes=get_and_map_reference_codes("referencetypes"),
        openlicenses=get_and_map_reference_codes("openlicenses"),
        location=get_and_map_reference_codes("location"),
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
        media_types=get_and_map_media_types(),
    )


def get_info_model_reference_data() -> InformationModelReferenceData:
    return InformationModelReferenceData(
        linguisticsystem=get_and_map_reference_codes("linguisticsystem"),
        openlicenses=get_and_map_reference_codes("openlicenses"),
        location=get_and_map_reference_codes("location"),
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
    )


def get_public_service_reference_data() -> PublicServiceReferenceData:
    return PublicServiceReferenceData(
        linguisticsystem=get_and_map_reference_codes("linguisticsystem")
    )


def parse_reference_codes(codes: Optional[List[Dict]]) -> Optional[Dict[str, SkosCode]]:
    if codes is not None:
        return {
            remove_scheme_and_trailing_slash(str(code.get("uri"))): SkosCode(
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


def get_and_map_reference_codes(endpoint: str) -> Optional[Dict[str, SkosCode]]:
    codes = get_reference_data(f"/codes/{endpoint}")
    return parse_reference_codes(codes)


def get_and_map_access_rights() -> Optional[Dict[str, SkosCode]]:
    access_rights = get_new_reference_data("/eu/access-rights").get("accessRights")
    return parse_reference_codes(access_rights)


def get_and_map_eu_data_themes() -> Optional[Dict[str, EuDataTheme]]:
    mapped = {}
    themes = get_new_reference_data("/eu/data-themes").get("dataThemes")
    if themes is not None:
        for theme in themes:
            eu_theme = EuDataTheme()
            eu_theme.add_values_from_dict(theme)
            mapped[remove_scheme_and_trailing_slash(str(theme.get("uri")))] = eu_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_los_themes() -> Optional[Dict[str, LosNode]]:
    mapped = {}
    los_nodes = get_new_reference_data("/los/themes-and-words").get("losNodes")
    if los_nodes is not None:
        for los_node in los_nodes:
            los_theme = LosNode()
            los_theme.add_values_from_dict(los_node)
            mapped[
                remove_scheme_and_trailing_slash(str(los_node.get("uri")))
            ] = los_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_media_types() -> Optional[Dict[str, MediaTypeOrExtent]]:
    media_types = {}
    iana_codes = get_new_reference_data("/iana/media-types").get("mediaTypes")
    if iana_codes is not None:
        for code in iana_codes:
            media_type_uri = str(code["uri"]) if code.get("uri") else None
            if media_type_uri:
                media_types[
                    remove_scheme_and_trailing_slash(media_type_uri)
                ] = MediaTypeOrExtent(
                    uri=code.get("uri"),
                    name=f"{code.get('name')}",
                    code=f"{code.get('type')}/{code.get('subType')}",
                    type=MediaTypeOrExtentType.MEDIA_TYPE,
                )

    file_types = get_new_reference_data("/eu/file-types").get("fileTypes")
    if file_types is not None:
        for file_type in file_types:
            file_type_uri = str(file_type["uri"]) if file_type.get("uri") else None
            if file_type_uri:
                media_types[
                    remove_scheme_and_trailing_slash(file_type_uri)
                ] = MediaTypeOrExtent(
                    uri=file_type.get("uri"),
                    name=f"{file_type.get('code')}",
                    code=f"{file_type.get('code')}",
                    type=MediaTypeOrExtentType.FILE_TYPE,
                )

    return media_types if len(media_types) > 0 else None
