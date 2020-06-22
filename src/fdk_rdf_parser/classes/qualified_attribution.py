from dataclasses import dataclass
from typing import Optional

from .publisher import Publisher


@dataclass
class QualifiedAttribution:
    agent: Optional[Publisher] = None
    role: Optional[str] = None
