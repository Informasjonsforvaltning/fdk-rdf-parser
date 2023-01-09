from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)


@dataclass
class Agent:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    playsRole: Optional[List[str]] = None
