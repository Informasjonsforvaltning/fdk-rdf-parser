from fdk_rdf_parser.classes import InformationModel
from .reference_data import InformationModelReferenceData
from .utils import extend_reference_data_code_list


def extend_info_model_with_reference_data(
    info_model: InformationModel, ref_data: InformationModelReferenceData
) -> InformationModel:
    info_model.language = extend_reference_data_code_list(
        info_model.language, ref_data.linguisticsystem
    )

    return info_model
