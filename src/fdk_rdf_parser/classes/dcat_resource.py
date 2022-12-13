from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
    Set,
)

from .contactpoint import DCATContactPoint
from .publisher import Publisher
from .skos_code import ReferenceDataCode
from .theme import EuDataTheme


@dataclass
class PartialDcatResource:
    identifier: Optional[Set[str]] = None
    publisher: Optional[Publisher] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    descriptionFormatted: Optional[Dict[str, str]] = None
    uri: Optional[str] = None
    accessRights: Optional[ReferenceDataCode] = None
    theme: Optional[List[EuDataTheme]] = None
    keyword: Optional[List[Dict[str, str]]] = None
    contactPoint: Optional[List[DCATContactPoint]] = None
    dctType: Optional[str] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    landingPage: Optional[Set[str]] = None
    language: Optional[List[ReferenceDataCode]] = None
