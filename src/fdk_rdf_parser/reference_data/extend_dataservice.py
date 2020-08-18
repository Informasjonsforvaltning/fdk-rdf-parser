from typing import Dict, List, Optional

from fdk_rdf_parser.classes import DataService, SkosCode
from .reference_data import DataServiceReferenceData


def extendDataServiceWithReferenceData(
    dataService: DataService, refData: DataServiceReferenceData
) -> DataService:
    dataService.mediaType = extendMediaTypes(dataService.mediaType, refData.mediaTypes)

    return dataService


def extendMediaTypes(
    mediaTypes: Optional[List[SkosCode]], references: Optional[Dict[str, SkosCode]]
) -> Optional[List[SkosCode]]:
    extended = []
    if mediaTypes and references:
        for mediaType in mediaTypes:
            reference = findCorrespondingReference(mediaType.uri, references)
            if reference:
                extended.append(reference)
    return extended if len(extended) > 0 else None


def findCorrespondingReference(
    mediaType: Optional[str], references: Optional[Dict[str, SkosCode]]
) -> Optional[SkosCode]:
    if mediaType and references:
        for key in references:
            if key in mediaType:
                return references[key]
    return None
