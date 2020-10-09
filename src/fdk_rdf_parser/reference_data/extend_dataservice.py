from typing import Dict, List, Optional

from fdk_rdf_parser.classes import DataService, SkosCode
from .reference_data import DataServiceReferenceData


def extend_data_service_with_reference_data(
    data_service: DataService, ref_data: DataServiceReferenceData
) -> DataService:
    data_service.mediaType = extend_media_types(
        data_service.mediaType, ref_data.media_types
    )

    return data_service


def extend_media_types(
    media_types: Optional[List[SkosCode]], references: Optional[Dict[str, SkosCode]]
) -> Optional[List[SkosCode]]:
    extended = []
    if media_types and references:
        for media_type in media_types:
            reference = find_corresponding_reference(media_type.uri, references)
            if reference:
                extended.append(reference)
    return extended if len(extended) > 0 else None


def find_corresponding_reference(
    media_type: Optional[str], references: Optional[Dict[str, SkosCode]]
) -> Optional[SkosCode]:
    if media_type and references:
        for key in references:
            if key in media_type:
                return references[key]
    return None
