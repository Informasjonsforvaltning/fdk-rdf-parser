from dataclasses import dataclass
from typing import Optional


@dataclass
class Publisher:
    uri: Optional[str] = None
    id: Optional[str] = None
