from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .skos_code import ReferenceDataCode
from .skos_concept import SkosConcept


@dataclass
class Output:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    language: Optional[List[ReferenceDataCode]] = None
    type: Optional[List[SkosConcept]] = None
