from dataclasses import dataclass
from typing import Dict, List, Optional

from .skos_code import SkosCode
from .skos_concept import SkosConcept


@dataclass
class Evidence:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    type: Optional[List[SkosConcept]] = None
    language: Optional[List[SkosCode]] = None
