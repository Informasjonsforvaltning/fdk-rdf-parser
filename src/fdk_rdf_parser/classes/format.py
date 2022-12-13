from dataclasses import dataclass
from typing import (
    Dict,
    Optional,
)

from .skos_code import ReferenceDataCode


@dataclass
class Format:
    uri: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    format: Optional[str] = None
    language: Optional[ReferenceDataCode] = None
    seeAlso: Optional[str] = None
