from dataclasses import dataclass
from typing import (
    List,
    Optional,
)

from .reference_data_code import ReferenceDataCode


@dataclass
class OpeningHoursSpecification:
    uri: Optional[str] = None
    dayOfWeek: Optional[List[ReferenceDataCode]] = None
    opens: Optional[str] = None
    closes: Optional[str] = None
    validFrom: Optional[str] = None
    validThrough: Optional[str] = None
