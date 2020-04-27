from dataclasses import dataclass
from typing import Optional


@dataclass
class Reference:
    referenceType: Optional[str] = None
    source: Optional[str] = None
