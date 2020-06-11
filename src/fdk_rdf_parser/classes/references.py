from dataclasses import dataclass
from typing import Optional

from .skos_code import SkosCode
from .skos_concept import SkosConcept


@dataclass
class Reference:
    referenceType: Optional[SkosCode] = None
    source: Optional[SkosConcept] = None
