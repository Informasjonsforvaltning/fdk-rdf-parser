from typing import Dict, List, Optional

from fdk_rdf_parser.classes import DataService, MediaType, SkosCode
from .reference_data import DataServiceReferenceData


def extend_data_service_with_reference_data(
    data_service: DataService, ref_data: DataServiceReferenceData
) -> DataService:
    data_service.mediaType = extend_media_type_skos_codes(
        data_service.mediaType, ref_data.media_types
    )
    data_service.fdkFormat = extend_fdk_format(
        data_service.fdkFormat, ref_data.media_types
    )

    return data_service


def extend_media_type_skos_codes(
    media_types: Optional[List[SkosCode]], references: Optional[Dict[str, MediaType]]
) -> Optional[List[SkosCode]]:
    extended = []
    if media_types and references:
        for media_type in media_types:
            reference = find_corresponding_media_type_reference(
                media_type.uri, references
            )
            if reference:
                extended.append(
                    SkosCode(
                        uri=media_type.uri,
                        code=reference.code,
                        prefLabel={"nb": reference.code} if reference.code else None,
                    )
                )
    return extended if len(extended) > 0 else None


def extend_fdk_format(
    formats: Optional[List[MediaType]], references: Optional[Dict[str, MediaType]]
) -> Optional[List[MediaType]]:
    extended = []
    if formats and references:
        for fmt in formats:
            reference = find_corresponding_media_type_reference(fmt.uri, references)
            if reference:
                extended.append(reference)
            elif fmt.code:
                extended.append(fmt)
    return extended if len(extended) > 0 else None


def find_corresponding_media_type_reference(
    media_type: Optional[str], references: Optional[Dict[str, MediaType]]
) -> Optional[MediaType]:
    if media_type and references:
        return references.get(media_type)
    return None
