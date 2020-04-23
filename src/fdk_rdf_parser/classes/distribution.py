from dataclasses import dataclass
from typing import Dict, List

from .data_distribution_service import DataDistributionService
from .skos_concept import SkosConcept

@dataclass
class Distribution:
    uri: str = None
    title: Dict[str, str] = None
    description: Dict[str, str] = None
    downloadURL: List[str] = None
    accessURL: List[str] = None
    license: List[SkosConcept] = None
    conformsTo: List[SkosConcept] = None
    page: List[SkosConcept] = None
    format: List[str] = None
    type: str = None
    accessService: List[DataDistributionService] = None
