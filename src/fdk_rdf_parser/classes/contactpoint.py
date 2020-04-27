from dataclasses import dataclass
from typing import Optional


@dataclass
class ContactPoint:
    uri: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    organizationName: Optional[str] = None
    organizationUnit: Optional[str] = None
    hasURL: Optional[str] = None
    hasTelephone: Optional[str] = None
