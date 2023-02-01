from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .reference_data_code import ReferenceDataCode


@dataclass
class Participation:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    role: Optional[List[ReferenceDataCode]] = None
    agent: Optional[str] = None
