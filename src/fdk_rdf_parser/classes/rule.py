from dataclasses import dataclass
from typing import Dict, List, Optional

from .skos_code import SkosCode


@dataclass
class Rule:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    language: Optional[List[SkosCode]] = None
    name: Optional[Dict[str, str]] = None
