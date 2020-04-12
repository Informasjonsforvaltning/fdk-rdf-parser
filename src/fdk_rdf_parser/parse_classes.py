from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class HarvestMetaData:
    firstHarvested: datetime
    changed: List[str]

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
    publisher: str
    harvest: HarvestMetaData
    title: Dict[str, str]
    description: Dict[str, str]
    uri: str
    accessRights: str
    accessRightsComment: str
    theme: List[str]
    keyword: List[str]
    contactPoint: List[ContactPoint]
    distribution: List[Distribution]
