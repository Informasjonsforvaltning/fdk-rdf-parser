from dataclasses import dataclass
from typing import Dict, List

from .data_distribution_service import DataDistributionService

@dataclass
class Distribution:
    uri: str = None
    title: Dict[str, str] = None
    description: Dict[str, str] = None
    downloadURL: List[str] = None
    accessURL: List[str] = None
    license: str = None
    conformsTo: List[str] = None
    page: List[str] = None
    format: List[str] = None
    type: str = None
    accessService: List[DataDistributionService] = None
