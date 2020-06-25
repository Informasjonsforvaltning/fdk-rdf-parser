from dataclasses import dataclass
from typing import List, Optional


@dataclass
class HarvestMetaData:
    firstHarvested: Optional[str] = None
    changed: Optional[List[str]] = None
