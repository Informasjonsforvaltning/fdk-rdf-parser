from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class HarvestMetaData:
    firstHarvested: datetime
    changed: List[str]

@dataclass
class Dataset:
    id: str
    harvest: HarvestMetaData