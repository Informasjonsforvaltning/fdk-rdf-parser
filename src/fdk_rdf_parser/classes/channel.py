from dataclasses import dataclass
from typing import Optional

from .skos_concept import SkosConcept


@dataclass
class Channel:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    type: Optional[SkosConcept] = None
