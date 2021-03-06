from fdk_rdf_parser.classes import InformationModel
from .reference_data import InformationModelReferenceData
from .utils import (
    extend_eu_themes,
    extend_los_themes,
    extend_skos_code_list,
    split_los_from_eu_themes,
)


def extend_info_model_with_reference_data(
    info_model: InformationModel, ref_data: InformationModelReferenceData
) -> InformationModel:
    info_model.language = extend_skos_code_list(
        info_model.language, ref_data.linguisticsystem
    )
    info_model.spatial = extend_skos_code_list(info_model.spatial, ref_data.location)
    info_model.license = extend_skos_code_list(
        info_model.license, ref_data.openlicenses
    )

    split_themes = split_los_from_eu_themes(info_model.theme, ref_data.los_themes)
    info_model.losTheme = extend_los_themes(split_themes["los"], ref_data.los_themes)
    info_model.theme = extend_eu_themes(split_themes["eu"], ref_data.eu_themes)

    return info_model
