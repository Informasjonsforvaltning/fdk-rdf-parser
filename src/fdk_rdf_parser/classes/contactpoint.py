from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ContactPoint:
    uri: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    organizationName: Optional[Dict[str, str]] = None
    organizationUnit: Optional[Dict[str, str]] = None
    hasURL: Optional[str] = None
    hasTelephone: Optional[str] = None
