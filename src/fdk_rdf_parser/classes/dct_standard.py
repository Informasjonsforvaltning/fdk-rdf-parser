from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)


@dataclass
class DctStandard:
    uri: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    seeAlso: Optional[List[str]] = None
    versionInfo: Optional[str] = None
