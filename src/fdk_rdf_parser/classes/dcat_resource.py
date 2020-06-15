from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

from .contactpoint import ContactPoint
from .publisher import PublisherId
from .skos_code import SkosCode
from .theme import ThemeEU


@dataclass
class PartialDcatResource:
    identifier: Optional[List[str]] = None
    publisher: Optional[PublisherId] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    uri: Optional[str] = None
    accessRights: Optional[SkosCode] = None
    theme: Optional[List[ThemeEU]] = None
    keyword: Optional[List[Dict[str, str]]] = None
    contactPoint: Optional[List[ContactPoint]] = None
    type: Optional[str] = None
    issued: Optional[datetime] = None
    modified: Optional[datetime] = None
    landingPage: Optional[List[str]] = None
    language: Optional[List[SkosCode]] = None
