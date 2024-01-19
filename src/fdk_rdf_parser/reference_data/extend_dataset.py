from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes import (
    Dataset,
    Distribution,
    ReferenceDataCode,
)
from .reference_data import DatasetReferenceData
from .utils import (
    extend_reference_data_code,
    extend_reference_data_code_list,
    extend_reference_types,
    remove_scheme_and_trailing_slash,
)


def extend_dataset_with_reference_data(
    dataset: Dataset, ref_data: DatasetReferenceData
) -> Dataset:
    dataset.accessRights = (
        extend_reference_data_code(dataset.accessRights, ref_data.rightsstatement)
        if dataset.accessRights
        else None
    )
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
    dataset.language = extend_reference_data_code_list(
        dataset.language, ref_data.linguisticsystem
    )
    dataset.distribution = extend_distributions(
        dataset.distribution, ref_data.openlicenses
    )
    dataset.references = extend_reference_types(
        dataset.references, ref_data.referencetypes
    )

    return dataset


def extend_distributions(
    distributions: Optional[List[Distribution]],
    open_licenses: Optional[Dict[str, ReferenceDataCode]],
) -> Optional[List[Distribution]]:
    if distributions is None:
        return distributions
    else:
        extended_distributions = []
        for dist in distributions:
            if open_licenses is not None:
                if dist.license is not None:
                    extended_licenses = []
                    for lic in dist.license:
                        ref_code = (
                            open_licenses.get(remove_scheme_and_trailing_slash(lic.uri))
                            if lic.uri is not None
                            else None
                        )
                        if ref_code is not None:
                            dist.openLicense = True
                            if lic.prefLabel is None:
                                lic.prefLabel = ref_code.prefLabel
                        extended_licenses.append(lic)
                    dist.license = extended_licenses

            extended_distributions.append(dist)
        return extended_distributions
