from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .skos_concept import SkosConcept


@dataclass
class Requirement:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    dctTitle: Optional[Dict[str, str]] = None
    dctType: Optional[List[SkosConcept]] = None
    description: Optional[Dict[str, str]] = None
    fulfils: Optional[List[str]] = None
