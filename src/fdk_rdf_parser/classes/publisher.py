from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Publisher:
    uri: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    orgPath: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    organisasjonsform: Optional[str] = None
