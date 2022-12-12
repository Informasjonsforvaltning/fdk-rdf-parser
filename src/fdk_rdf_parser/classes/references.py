from dataclasses import dataclass
from typing import Optional

from .skos_code import ReferenceDataCode
from .skos_concept import SkosConcept


@dataclass
class Reference:
    referenceType: Optional[ReferenceDataCode] = None
    source: Optional[SkosConcept] = None
