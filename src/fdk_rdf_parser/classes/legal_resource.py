from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class LegalResource:
    uri: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    url: Optional[str] = None
