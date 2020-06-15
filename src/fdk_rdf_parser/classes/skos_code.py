from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class SkosCode:
    uri: Optional[str] = None
    code: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
