from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Temporal:
    uri: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
