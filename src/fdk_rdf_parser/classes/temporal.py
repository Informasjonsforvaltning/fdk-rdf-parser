from dataclasses import dataclass
from datetime import datetime

@dataclass
class Temporal:
    uri: str = None
    startDate: datetime = None
    endDate: datetime = None
