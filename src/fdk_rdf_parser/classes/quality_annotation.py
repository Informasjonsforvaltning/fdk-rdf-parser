from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class QualityAnnotation:
    inDimension: Optional[str] = None
    hasBody: Optional[Dict[str, str]] = None
