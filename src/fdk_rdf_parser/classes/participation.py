from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .agent import Agent
from .skos_concept import SkosConcept


@dataclass
class Participation:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    role: Optional[List[SkosConcept]] = None
    agents: Optional[List[Agent]] = None
