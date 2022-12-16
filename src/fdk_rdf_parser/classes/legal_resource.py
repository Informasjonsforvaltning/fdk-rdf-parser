from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)


@dataclass
class LegalResource:
    uri: Optional[str] = None
    dctTitle: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    seeAlso: Optional[List[str]] = None
    relation: Optional[List[str]] = None
