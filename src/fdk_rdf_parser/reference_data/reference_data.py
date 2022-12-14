from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes import (
    EuDataTheme,
    LosNode,
    MediaTypeOrExtent,
    MediaTypeOrExtentType,
    ReferenceDataCode,
)
from .reference_data_client import get_reference_data
from .utils import remove_scheme_and_trailing_slash


@dataclass
class DataServiceReferenceData:
    media_types: Optional[Dict[str, MediaTypeOrExtent]] = None


@dataclass
class DatasetReferenceData:
    provenancestatement: Optional[Dict[str, ReferenceDataCode]] = None
    rightsstatement: Optional[Dict[str, ReferenceDataCode]] = None
    frequency: Optional[Dict[str, ReferenceDataCode]] = None
    linguisticsystem: Optional[Dict[str, ReferenceDataCode]] = None
    referencetypes: Optional[Dict[str, ReferenceDataCode]] = None
    openlicenses: Optional[Dict[str, ReferenceDataCode]] = None
    location: Optional[Dict[str, ReferenceDataCode]] = None
    eu_data_themes: Optional[Dict[str, EuDataTheme]] = None
    los_themes: Optional[Dict[str, LosNode]] = None
    media_types: Optional[Dict[str, MediaTypeOrExtent]] = None


@dataclass
class InformationModelReferenceData:
    linguisticsystem: Optional[Dict[str, ReferenceDataCode]] = None
    openlicenses: Optional[Dict[str, ReferenceDataCode]] = None
    location: Optional[Dict[str, ReferenceDataCode]] = None
    eu_data_themes: Optional[Dict[str, EuDataTheme]] = None
    los_themes: Optional[Dict[str, LosNode]] = None


@dataclass
class PublicServiceReferenceData:
    linguisticsystem: Optional[Dict[str, ReferenceDataCode]] = None
    week_days: Optional[Dict[str, ReferenceDataCode]] = None
    statuses: Optional[Dict[str, ReferenceDataCode]] = None
    types: Optional[Dict[str, ReferenceDataCode]] = None
    evidence_type: Optional[Dict[str, ReferenceDataCode]] = None
    eu_data_themes: Optional[Dict[str, EuDataTheme]] = None
    los_themes: Optional[Dict[str, LosNode]] = None


def get_data_service_reference_data() -> DataServiceReferenceData:
    return DataServiceReferenceData(media_types=get_and_map_media_types())


def get_dataset_reference_data() -> DatasetReferenceData:
    return DatasetReferenceData(
        provenancestatement=get_and_map_provenance_statements(),
        rightsstatement=get_and_map_access_rights(),
        frequency=get_and_map_frequencies(),
        linguisticsystem=get_and_map_linguistic_system(),
        referencetypes=get_and_map_reference_types(),
        openlicenses=get_and_map_open_licenses(),
        location=get_and_map_locations(),
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
        media_types=get_and_map_media_types(),
    )


def get_info_model_reference_data() -> InformationModelReferenceData:
    return InformationModelReferenceData(
        linguisticsystem=get_and_map_linguistic_system(),
        openlicenses=get_and_map_open_licenses(),
        location=get_and_map_locations(),
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
    )


def get_public_service_reference_data() -> PublicServiceReferenceData:
    return PublicServiceReferenceData(
        linguisticsystem=get_and_map_linguistic_system(),
        week_days=get_and_map_week_days(),
        statuses=get_and_map_statuses(),
        evidence_type=get_and_map_evidence_types(),
        types=get_and_map_dct_types(),
        eu_data_themes=get_and_map_eu_data_themes(),
        los_themes=get_and_map_los_themes(),
    )


def parse_reference_codes(
    codes: Optional[List[Dict]],
) -> Optional[Dict[str, ReferenceDataCode]]:
    if codes is not None:
        return {
            remove_scheme_and_trailing_slash(str(code.get("uri"))): ReferenceDataCode(
                uri=str(code.get("uri")) if code.get("uri") is not None else None,
                code=str(code.get("code")) if code.get("code") is not None else None,
                prefLabel=code.get("label") if code.get("label") is not None else None,
            )
            for code in codes
        }
    else:
        return None


def parse_locations(
    nasjoner: Optional[List[Dict]],
    fylker: Optional[List[Dict]],
    kommuner: Optional[List[Dict]],
) -> Optional[Dict[str, ReferenceDataCode]]:
    locations = dict()
    if nasjoner is not None:
        for nasjon in nasjoner:
            locations[
                remove_scheme_and_trailing_slash(str(nasjon.get("uri")))
            ] = ReferenceDataCode(
                uri=str(nasjon.get("uri")) if nasjon.get("uri") is not None else None,
                code=str(nasjon.get("nasjonsnummer"))
                if nasjon.get("nasjonsnummer") is not None
                else None,
                prefLabel={"no": str(nasjon["nasjonsnavn"])}
                if nasjon.get("nasjonsnavn") is not None
                else None,
            )
    if fylker is not None:
        for fylke in fylker:
            locations[
                remove_scheme_and_trailing_slash(str(fylke.get("uri")))
            ] = ReferenceDataCode(
                uri=str(fylke.get("uri")) if fylke.get("uri") is not None else None,
                code=str(fylke.get("fylkesnummer"))
                if fylke.get("fylkesnummer") is not None
                else None,
                prefLabel={"no": str(fylke["fylkesnavn"])}
                if fylke.get("fylkesnavn") is not None
                else None,
            )
    if kommuner is not None:
        for kommune in kommuner:
            locations[
                remove_scheme_and_trailing_slash(str(kommune.get("uri")))
            ] = ReferenceDataCode(
                uri=str(kommune.get("uri")) if kommune.get("uri") is not None else None,
                code=str(kommune.get("kommunenummer"))
                if kommune.get("kommunenummer") is not None
                else None,
                prefLabel={"no": str(kommune["kommunenavnNorsk"])}
                if kommune.get("kommunenavnNorsk") is not None
                else None,
            )

    return locations if len(locations) > 0 else None


def get_and_map_locations() -> Optional[Dict[str, ReferenceDataCode]]:
    nasjoner = get_reference_data("/geonorge/administrative-enheter/nasjoner").get(
        "nasjoner"
    )
    fylker = get_reference_data("/geonorge/administrative-enheter/fylker").get("fylker")
    kommuner = get_reference_data("/geonorge/administrative-enheter/kommuner").get(
        "kommuner"
    )
    return parse_locations(nasjoner, fylker, kommuner)


def get_and_map_frequencies() -> Optional[Dict[str, ReferenceDataCode]]:
    frequencies = get_reference_data("/eu/frequencies").get("frequencies")
    return parse_reference_codes(frequencies)


def get_and_map_provenance_statements() -> Optional[Dict[str, ReferenceDataCode]]:
    provenance_statements = get_reference_data("/provenance-statements").get(
        "provenanceStatements"
    )
    return parse_reference_codes(provenance_statements)


def get_and_map_reference_types() -> Optional[Dict[str, ReferenceDataCode]]:
    reference_types = get_reference_data("/reference-types").get("referenceTypes")
    return parse_reference_codes(reference_types)


def get_and_map_open_licenses() -> Optional[Dict[str, ReferenceDataCode]]:
    open_licenses = get_reference_data("/open-licenses").get("openLicenses")
    return parse_reference_codes(open_licenses)


def get_and_map_linguistic_system() -> Optional[Dict[str, ReferenceDataCode]]:
    linguistic_systems = get_reference_data("/linguistic-systems").get(
        "linguisticSystems"
    )
    return parse_reference_codes(linguistic_systems)


def get_and_map_access_rights() -> Optional[Dict[str, ReferenceDataCode]]:
    access_rights = get_reference_data("/eu/access-rights").get("accessRights")
    return parse_reference_codes(access_rights)


def get_and_map_week_days() -> Optional[Dict[str, ReferenceDataCode]]:
    week_days = get_reference_data("/schema/week-days").get("weekDays")
    return parse_reference_codes(week_days)


def get_and_map_statuses() -> Optional[Dict[str, ReferenceDataCode]]:
    statuses = get_reference_data("/adms/statuses").get("statuses")
    return parse_reference_codes(statuses)


def get_and_map_dct_types() -> Optional[Dict[str, ReferenceDataCode]]:
    dct_types = get_reference_data("/eu/main-activities").get("mainActivities")
    return parse_reference_codes(dct_types)


def get_and_map_evidence_types() -> Optional[Dict[str, ReferenceDataCode]]:
    evidence_types = get_reference_data("/digdir/evidence-types").get("evidenceTypes")
    return parse_reference_codes(evidence_types)


def get_and_map_eu_data_themes() -> Optional[Dict[str, EuDataTheme]]:
    mapped = {}
    themes = get_reference_data("/eu/data-themes").get("dataThemes")
    if themes is not None:
        for theme in themes:
            eu_theme = EuDataTheme()
            eu_theme.add_values_from_dict(theme)
            mapped[remove_scheme_and_trailing_slash(str(theme.get("uri")))] = eu_theme
    return mapped if len(mapped) > 0 else None


def get_and_map_los_themes() -> Optional[Dict[str, LosNode]]:
    mapped = {}
    los_nodes = get_reference_data("/los/themes-and-words").get("losNodes")
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
    iana_codes = get_reference_data("/iana/media-types").get("mediaTypes")
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

    file_types = get_reference_data("/eu/file-types").get("fileTypes")
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
