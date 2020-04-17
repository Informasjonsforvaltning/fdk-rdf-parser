from dataclasses import dataclass, field
from typing import Dict

@dataclass
class QualityAnnotation:
    inDimension: str = None
    hasBody: Dict[str, str] = None
