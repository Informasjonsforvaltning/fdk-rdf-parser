from dataclasses import dataclass
from datetime import datetime

@dataclass
class HarvestMetaData:
    firstHarvested: datetime
    """changed: List[str]"""