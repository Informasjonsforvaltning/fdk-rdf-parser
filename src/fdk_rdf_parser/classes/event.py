from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Event:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    type: Optional[str] = None
