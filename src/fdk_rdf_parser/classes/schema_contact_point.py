from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class SchemaContactPoint:
    uri: Optional[str] = None
    contactType: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    email: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    telephone: Optional[str] = None
    url: Optional[str] = None
