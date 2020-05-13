from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class PublisherId:
    uri: Optional[str] = None
    id: Optional[str] = None


@dataclass
class Publisher(PublisherId):
    name: Optional[str] = None
    orgPath: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    organisasjonsform: Optional[str] = None
