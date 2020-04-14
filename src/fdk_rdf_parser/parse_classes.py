from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class HarvestMetaData:
    firstHarvested: datetime
    changed: List[str] = field(default_factory=list)

@dataclass
class ContactPoint:
    uri: str = None
    fullname: str = None
    email: str = None
    organizationName: str = None
    organizationUnit: str = None
    hasURL: str = None
    hasTelephone: str = None

@dataclass
class Distribution:
    uri: str = None
    title: Dict[str, str] = field(default_factory=dict)
    description: Dict[str, str] = field(default_factory=dict)
    downloadURL: List[str] = field(default_factory=list)
    accessURL: List[str] = field(default_factory=list)
    license: str = None
    conformsTo: List[str] = field(default_factory=list)
    page: List[str] = field(default_factory=list)
    format: List[str] = field(default_factory=list)
    type: str = None
    accessService: str = None

@dataclass
class Dataset:
    id: str
    harvest: HarvestMetaData
    identifier: List[str] = field(default_factory=list)
    publisher: str = None
    title: Dict[str, str] = field(default_factory=dict)
    description: Dict[str, str] = field(default_factory=dict)
    uri: str = None
    accessRights: str = None
    accessRightsComment: List[str] = field(default_factory=list)
    theme: List[str] = field(default_factory=list)
    keyword: List[str] = field(default_factory=list)
    contactPoint: List[ContactPoint] = field(default_factory=list)
    distribution: List[Distribution] = field(default_factory=list)
    spatial: List[str] = field(default_factory=list)
    source: str = None
    objective: Dict[str, str] = field(default_factory=dict)
    type: str = None
    page: List[str] = field(default_factory=list)
    admsIdentifier: List[str] = field(default_factory=list)
