from dataclasses import dataclass
from typing import Dict, List, Optional

from .skos_code import SkosCode


@dataclass
class Format:
    uri: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    format: Optional[str] = None
    language: Optional[SkosCode] = None
    seeAlso: Optional[List[str]] = None
