from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class HarvestMetaData:
    firstHarvested: datetime = None
    changed: List[str] = None
