from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class HarvestMetaData:
    firstHarvested: datetime = None
    changed: List[str] = field(default_factory=list)
