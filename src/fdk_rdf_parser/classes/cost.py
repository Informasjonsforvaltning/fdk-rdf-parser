from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .channel import Channel
from .publisher import Publisher


@dataclass
class Cost:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    currency: Optional[str] = None
    ifAccessedThrough: Optional[Channel] = None
    isDefinedBy: Optional[List[Publisher]] = None
    value: Optional[str] = None
