from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from .contactpoint import ContactPoint
from .publisher import Publisher


@dataclass
class DcatResource:
    identifier: List[str] = None
    publisher: Publisher = None
    title: Dict[str, str] = None
    description: Dict[str, str] = None
    uri: str = None
    accessRights: str = None
    theme: List[str] = None
    keyword: List[str] = None
    contactPoint: List[ContactPoint] = None
    type: str = None
    issued: datetime = None
    modified: datetime = None
    landingPage: List[str] = None
    language: List[str] = None
