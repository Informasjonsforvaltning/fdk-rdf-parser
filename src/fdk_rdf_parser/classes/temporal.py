from dataclasses import dataclass
from typing import Optional


@dataclass
class Temporal:
    uri: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
