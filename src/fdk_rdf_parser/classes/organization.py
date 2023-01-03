from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)


@dataclass
class Organization:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    name: Optional[Dict[str, str]] = None
    orgPath: Optional[str] = None
    orgType: Optional[str] = None
    spatial: Optional[List[str]] = None
    homepage: Optional[List[str]] = None
