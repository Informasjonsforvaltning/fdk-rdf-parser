from dataclasses import dataclass
from typing import Dict


@dataclass
class SkosConcept:
    uri: str = None
    prefLabel: Dict[str, str] = None
    extraType: str = None
