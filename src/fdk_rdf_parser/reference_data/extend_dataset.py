from typing import (
    Dict,
    List,
    Optional,
    Set,
)

from fdk_rdf_parser.classes import (
    Dataset,
    Distribution,
    MediaTypeOrExtent,
    ReferenceDataCode,
)
from .reference_data import DatasetReferenceData
from .utils import (
    extend_eu_data_themes,
    extend_los_themes,
    extend_reference_types,
    extend_skos_code,
    extend_skos_code_list,
    remove_scheme_and_trailing_slash,
    split_themes,
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
        dataset.distribution, ref_data.openlicenses, ref_data.media_types
    )
    dataset.references = extend_reference_types(
        dataset.references, ref_data.referencetypes
    )

    splitted_themes = split_themes(dataset.theme, ref_data.los_themes)
    dataset.losTheme = extend_los_themes(splitted_themes["los"], ref_data.los_themes)
    dataset.theme = extend_eu_data_themes(
        splitted_themes["eu_data_themes"], ref_data.eu_data_themes
    )

    return dataset


def extend_distributions(
    distributions: Optional[List[Distribution]],
    open_licenses: Optional[Dict[str, ReferenceDataCode]],
    ref_media_types: Optional[Dict[str, MediaTypeOrExtent]],
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

            if ref_media_types:
                fdk_formats: Set[MediaTypeOrExtent] = set()

                if dist.fdkFormat:
                    skos_code_formats = []
                    for fmt in dist.fdkFormat:
                        ref_media_type = (
                            ref_media_types.get(
                                remove_scheme_and_trailing_slash(fmt.uri)
                            )
                            if fmt.uri
                            else None
                        )
                        if ref_media_type:
                            skos_code_formats.append(
                                ReferenceDataCode(
                                    uri=ref_media_type.uri,
                                    code=ref_media_type.code,
                                    prefLabel={"nb": ref_media_type.code}
                                    if ref_media_type.code
                                    else None,
                                )
                            )
                            fdk_formats.add(ref_media_type)
                        elif fmt.code:
                            fdk_formats.add(fmt)
                    dist.fdkFormat = list(fdk_formats) if len(fdk_formats) > 0 else None
                    dist.mediaType = (
                        skos_code_formats if len(skos_code_formats) > 0 else None
                    )

                if (
                    dist.compressFormat
                    and dist.compressFormat.uri
                    and ref_media_types.get(
                        remove_scheme_and_trailing_slash(dist.compressFormat.uri)
                    )
                ):
                    dist.compressFormat = ref_media_types[
                        remove_scheme_and_trailing_slash(dist.compressFormat.uri)
                    ]

                if (
                    dist.packageFormat
                    and dist.packageFormat.uri
                    and ref_media_types.get(
                        remove_scheme_and_trailing_slash(dist.packageFormat.uri)
                    )
                ):
                    dist.packageFormat = ref_media_types[
                        remove_scheme_and_trailing_slash(dist.packageFormat.uri)
                    ]

            extended_distributions.append(dist)
        return extended_distributions
