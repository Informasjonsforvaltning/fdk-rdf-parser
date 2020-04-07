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
    harvest: HarvestMetaData
    title: Dict[str, str]
    description: Dict[str, str]
    uri: str
    accessRights: str
    accessRightsComment: str