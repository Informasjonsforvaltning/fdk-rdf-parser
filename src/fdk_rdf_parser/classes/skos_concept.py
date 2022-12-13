from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)


@dataclass
class SkosConcept:
    uri: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    extraType: Optional[str] = None
    broader: Optional[List[str]] = None
    narrower: Optional[List[str]] = None
