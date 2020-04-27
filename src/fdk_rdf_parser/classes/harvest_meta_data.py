from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class HarvestMetaData:
    firstHarvested: Optional[datetime] = None
    changed: Optional[List[str]] = None
