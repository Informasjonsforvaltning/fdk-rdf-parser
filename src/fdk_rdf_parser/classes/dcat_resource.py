from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime

from .contactpoint import ContactPoint

@dataclass
class DcatResource:
    identifier: List[str] = field(default_factory=list)
    publisher: str = None
    title: Dict[str, str] = None
    description: Dict[str, str] = None
    uri: str = None
    accessRights: str = None
    theme: List[str] = field(default_factory=list)
    keyword: List[str] = field(default_factory=list)
    contactPoint: List[ContactPoint] = field(default_factory=list)
    type: str = None
    issued: datetime = None
    modified: datetime = None
    landingPage: List[str] = field(default_factory=list)
    language: List[str] = field(default_factory=list)
