from dataclasses import dataclass
from typing import (
    Dict,
    Optional,
)


@dataclass
class ConformsTo:
    uri: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
