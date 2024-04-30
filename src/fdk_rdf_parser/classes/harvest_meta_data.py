from dataclasses import dataclass
from typing import Optional


@dataclass
class HarvestMetaData:
    firstHarvested: Optional[str] = None
    modified: Optional[str] = None
