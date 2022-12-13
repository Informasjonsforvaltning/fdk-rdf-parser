from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .skos_concept import SkosConcept


@dataclass
class CriterionRequirement:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    type: Optional[List[SkosConcept]] = None
