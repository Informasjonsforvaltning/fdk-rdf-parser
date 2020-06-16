from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Subject:
    identifier: Optional[str] = None
    uri: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    definition: Optional[Dict[str, str]] = None
