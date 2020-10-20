from typing import Dict, List, Optional

from fdk_rdf_parser.classes import Dataset, Distribution, SkosCode
from .reference_data import DatasetReferenceData
from .utils import (
    extend_eu_themes,
    extend_los_themes,
    extend_reference_types,
    extend_skos_code,
    extend_skos_code_list,
    remove_trailing_slash,
    split_los_from_eu_themes,
)


def extend_dataset_with_reference_data(
    dataset: Dataset, ref_data: DatasetReferenceData
) -> Dataset:
    dataset.accessRights = extend_skos_code(
        dataset.accessRights, ref_data.rightsstatement
    )
    dataset.provenance = extend_skos_code(
        dataset.provenance, ref_data.provenancestatement
    )
    dataset.accrualPeriodicity = extend_skos_code(
        dataset.accrualPeriodicity, ref_data.frequency
    )
    dataset.language = extend_skos_code_list(
        dataset.language, ref_data.linguisticsystem
    )
    dataset.spatial = extend_skos_code_list(dataset.spatial, ref_data.location)
    dataset.distribution = extend_distributions(
        dataset.distribution, ref_data.openlicenses
    )
    dataset.references = extend_reference_types(
        dataset.references, ref_data.referencetypes
    )

    split_themes = split_los_from_eu_themes(dataset.theme, ref_data.los_themes)
    dataset.losTheme = extend_los_themes(split_themes["los"], ref_data.los_themes)
    dataset.theme = extend_eu_themes(split_themes["eu"], ref_data.eu_themes)

    return dataset


def extend_distributions(
    distributions: Optional[List[Distribution]],
    open_licenses: Optional[Dict[str, SkosCode]],
) -> Optional[List[Distribution]]:
    if distributions is None or open_licenses is None:
        return distributions
    else:
        extended_distributions = []
        for dist in distributions:
            if dist.license is not None:
                extended_licenses = []
                for lic in dist.license:
                    ref_code = (
                        open_licenses.get(remove_trailing_slash(lic.uri))
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
