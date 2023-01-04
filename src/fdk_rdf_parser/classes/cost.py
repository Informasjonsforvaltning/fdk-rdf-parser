from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .organization import Organization


@dataclass
class Cost:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    currency: Optional[str] = None
    ifAccessedThrough: Optional[str] = None
    isDefinedBy: Optional[List[Organization]] = None
    value: Optional[str] = None
