from dataclasses import dataclass
from typing import List, Optional

from .skos_code import SkosCode


@dataclass
class OpeningHoursSpecification:
    uri: Optional[str] = None
    dayOfWeek: Optional[List[SkosCode]] = None
    opens: Optional[str] = None
    closes: Optional[str] = None
    validFrom: Optional[str] = None
    validThrough: Optional[str] = None
