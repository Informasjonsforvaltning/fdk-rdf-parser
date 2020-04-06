from dataclasses import dataclass
import isodate

@dataclass
class HarvestMetaData:
    firstHarvested: isodate
    """changed: List[str]"""