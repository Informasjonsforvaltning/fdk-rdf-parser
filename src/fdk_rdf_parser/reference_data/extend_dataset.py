from fdk_rdf_parser.classes import Dataset
from .reference_data import DatasetReferenceData
from .utils import (
    extend_reference_data_code,
    extend_reference_types,
)


def extend_dataset_with_reference_data(
    dataset: Dataset, ref_data: DatasetReferenceData
) -> Dataset:
    dataset.provenance = (
        extend_reference_data_code(dataset.provenance, ref_data.provenancestatement)
        if dataset.provenance
        else None
    )
    dataset.accrualPeriodicity = (
        extend_reference_data_code(dataset.accrualPeriodicity, ref_data.frequency)
        if dataset.accrualPeriodicity
        else None
    )
    dataset.references = extend_reference_types(
        dataset.references, ref_data.referencetypes
    )

    return dataset
