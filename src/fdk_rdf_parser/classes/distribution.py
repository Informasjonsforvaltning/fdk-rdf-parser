from dataclasses import dataclass
from typing import Dict, List, Optional

from .data_distribution_service import DataDistributionService
from .skos_concept import SkosConcept


@dataclass
class Distribution:
    uri: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    downloadURL: Optional[List[str]] = None
    accessURL: Optional[List[str]] = None
    license: Optional[List[SkosConcept]] = None
    openLicense: bool = False
    conformsTo: Optional[List[SkosConcept]] = None
    page: Optional[List[SkosConcept]] = None
    format: Optional[List[str]] = None
    type: Optional[str] = None
    accessService: Optional[List[DataDistributionService]] = None
