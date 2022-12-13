from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
    Set,
)

from .conforms_to import ConformsTo
from .data_distribution_service import DataDistributionService
from .media_type import MediaTypeOrExtent
from .skos_code import ReferenceDataCode
from .skos_concept import SkosConcept


@dataclass
class Distribution:
    uri: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    downloadURL: Optional[Set[str]] = None
    accessURL: Optional[Set[str]] = None
    license: Optional[List[SkosConcept]] = None
    openLicense: bool = False
    conformsTo: Optional[List[ConformsTo]] = None
    page: Optional[List[SkosConcept]] = None
    mediaType: Optional[List[ReferenceDataCode]] = None
    format: Optional[Set[str]] = None
    fdkFormat: Optional[List[MediaTypeOrExtent]] = None
    compressFormat: Optional[MediaTypeOrExtent] = None
    packageFormat: Optional[MediaTypeOrExtent] = None
    type: Optional[str] = None
    accessService: Optional[List[DataDistributionService]] = None
