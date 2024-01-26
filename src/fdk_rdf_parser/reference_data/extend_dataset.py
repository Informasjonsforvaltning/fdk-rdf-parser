from fdk_rdf_parser.classes import Dataset
from .reference_data import DatasetReferenceData
from .utils import extend_reference_types


def extend_dataset_with_reference_data(
    dataset: Dataset, ref_data: DatasetReferenceData
) -> Dataset:
    dataset.references = extend_reference_types(
        dataset.references, ref_data.referencetypes
    )

    return dataset
