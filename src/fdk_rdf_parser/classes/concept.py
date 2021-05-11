from dataclasses import dataclass
from typing import Dict, List, Optional, Set

from .contactpoint import ContactPoint
from .harvest_meta_data import HarvestMetaData
from .publisher import Publisher


@dataclass
class Collection:
    id: Optional[str] = None
    uri: Optional[str] = None
    label: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    publisher: Optional[Publisher] = None


@dataclass
class TextAndURI:
    uri: Optional[str] = None
    text: Optional[Dict[str, str]] = None


@dataclass
class Definition:
    text: Optional[Dict[str, str]] = None
    remark: Optional[Dict[str, str]] = None
    targetGroup: Optional[str] = None
    sourceRelationship: Optional[str] = None
    range: Optional[TextAndURI] = None
    sources: Optional[List[TextAndURI]] = None
    lastUpdated: Optional[str] = None


@dataclass
class Concept:
    id: Optional[str] = None
    uri: Optional[str] = None
    identifier: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    collection: Optional[Collection] = None
    publisher: Optional[Publisher] = None
    subject: Optional[Dict[str, str]] = None
    application: Optional[List[Dict[str, str]]] = None
    example: Optional[Dict[str, str]] = None
    prefLabel: Optional[Dict[str, str]] = None
    hiddenLabel: Optional[List[Dict[str, str]]] = None
    altLabel: Optional[List[Dict[str, str]]] = None
    contactPoint: Optional[ContactPoint] = None
    definition: Optional[Definition] = None
    seeAlso: Optional[Set[str]] = None
    validFromIncluding: Optional[str] = None
    validToIncluding: Optional[str] = None
    type: str = "concept"
