from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class HarvestMetaData:
    firstHarvested: datetime
    changed: List[str]

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
    contactPoint: List

@dataclass
class ContactPoint:
    uri: str = None
    fullname: str = None
    email: str = None
    organizationName: str = None
    organizationUnit: str = None
    hasURL: str = None
    hasTelephone: str = None
