from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .skos_concept import SkosConcept


@dataclass
class DataDistributionService:
    uri: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    endpointDescription: Optional[List[SkosConcept]] = None
