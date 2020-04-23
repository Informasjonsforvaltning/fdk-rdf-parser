from dataclasses import dataclass
from typing import List

from .skos_concept import SkosConcept


@dataclass
class DataDistributionService:
    uri: str = None
    title: str = None
    description: str = None
    endpointDescription: List[SkosConcept] = None
