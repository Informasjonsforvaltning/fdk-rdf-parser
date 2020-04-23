from dataclasses import dataclass
from typing import Dict


@dataclass
class QualityAnnotation:
    inDimension: str = None
    hasBody: Dict[str, str] = None
