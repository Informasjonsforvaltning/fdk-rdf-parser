from dataclasses import dataclass
from typing import List, Optional


@dataclass
class OpeningHoursSpecification:
    uri: Optional[str] = None
    dayOfWeek: Optional[List[str]] = None
    opens: Optional[str] = None
    closes: Optional[str] = None
    validFrom: Optional[str] = None
    validThrough: Optional[str] = None
