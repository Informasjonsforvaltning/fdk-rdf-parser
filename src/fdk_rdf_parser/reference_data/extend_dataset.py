from typing import Dict, List, Optional, Set

from fdk_rdf_parser.classes import Dataset, Distribution, MediaType, SkosCode
from .reference_data import DatasetReferenceData
from .utils import (
    extend_eu_themes,
    extend_los_themes,
    extend_reference_types,
    extend_skos_code,
    extend_skos_code_list,
    map_media_type_to_skos_code,
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
        dataset.distribution, ref_data.openlicenses, ref_data.media_types
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
    ref_media_types: Optional[Dict[str, MediaType]],
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

            if ref_media_types:
                fdk_formats: Set[MediaType] = set()

                if dist.format:
                    extended_formats = []
                    for fmt in dist.format:
                        ref_media_type = ref_media_types.get(fmt)
                        if ref_media_type:
                            extended_formats.append(
                                map_media_type_to_skos_code(ref_media_type)
                            )
                            fdk_formats.add(ref_media_type)
                        else:
                            fdk_formats.add(MediaType(name=fmt))
                    dist.mediaType = (
                        extended_formats if len(extended_formats) > 0 else None
                    )

                if dist.dcatMediaType:
                    extended_dcat_types = []
                    for media_type in dist.dcatMediaType:
                        extended = (
                            ref_media_types.get(media_type.uri)
                            if media_type.uri
                            else None
                        )
                        if extended:
                            extended_dcat_types.append(extended)
                            fdk_formats.add(extended)
                        else:
                            extended_dcat_types.append(media_type)
                            fdk_formats.add(media_type)
                    dist.dcatMediaType = extended_dcat_types

                if len(fdk_formats) > 0:
                    dist.fdkFormat = list(fdk_formats)

                if (
                    dist.compressFormat
                    and dist.compressFormat.uri
                    and ref_media_types.get(dist.compressFormat.uri)
                ):
                    dist.compressFormat = ref_media_types[dist.compressFormat.uri]

                if (
                    dist.packageFormat
                    and dist.packageFormat.uri
                    and ref_media_types.get(dist.packageFormat.uri)
                ):
                    dist.packageFormat = ref_media_types[dist.packageFormat.uri]

            extended_distributions.append(dist)
        return extended_distributions
