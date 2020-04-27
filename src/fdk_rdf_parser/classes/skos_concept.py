from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class SkosConcept:
    uri: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    extraType: Optional[str] = None
