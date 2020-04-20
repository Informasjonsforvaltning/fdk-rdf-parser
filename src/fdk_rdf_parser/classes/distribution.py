from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Distribution:
    uri: str = None
    title: Dict[str, str] = None
    description: Dict[str, str] = None
    downloadURL: List[str] = field(default_factory=list)
    accessURL: List[str] = field(default_factory=list)
    license: str = None
    conformsTo: List[str] = field(default_factory=list)
    page: List[str] = field(default_factory=list)
    format: List[str] = field(default_factory=list)
    type: str = None
    accessService: str = None
