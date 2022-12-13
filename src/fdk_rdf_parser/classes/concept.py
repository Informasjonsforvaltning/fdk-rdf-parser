from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
    Set,
)

from .contactpoint import DCATContactPoint
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
class AssociativeRelation:
    description: Optional[Dict[str, str]] = None
    related: Optional[str] = None


@dataclass
class PartitiveRelation:
    description: Optional[Dict[str, str]] = None
    hasPart: Optional[str] = None
    isPartOf: Optional[str] = None


@dataclass
class GenericRelation:
    divisioncriterion: Optional[Dict[str, str]] = None
    generalizes: Optional[str] = None
    specializes: Optional[str] = None


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
    contactPoint: Optional[DCATContactPoint] = None
    definition: Optional[Definition] = None
    seeAlso: Optional[Set[str]] = None
    isReplacedBy: Optional[Set[str]] = None
    replaces: Optional[Set[str]] = None
    validFromIncluding: Optional[str] = None
    validToIncluding: Optional[str] = None
    associativeRelation: Optional[List[AssociativeRelation]] = None
    partitiveRelation: Optional[List[PartitiveRelation]] = None
    genericRelation: Optional[List[GenericRelation]] = None
    type: str = "concept"
