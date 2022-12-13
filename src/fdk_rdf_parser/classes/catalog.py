from dataclasses import dataclass
from typing import (
    Dict,
    Optional,
)

from .publisher import Publisher


@dataclass
class Catalog:
    id: Optional[str] = None
    publisher: Optional[Publisher] = None
    title: Optional[Dict[str, str]] = None
    uri: Optional[str] = None
    description: Optional[Dict[str, str]] = None
