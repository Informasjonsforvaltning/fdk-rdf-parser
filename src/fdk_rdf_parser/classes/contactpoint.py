from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .reference_data_code import ReferenceDataCode


@dataclass
class DCATContactPoint:
    uri: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    organizationName: Optional[Dict[str, str]] = None
    organizationUnit: Optional[Dict[str, str]] = None
    hasURL: Optional[str] = None
    hasTelephone: Optional[str] = None


@dataclass
class CVContactPoint:
    uri: Optional[str] = None
    contactType: Optional[Dict[str, str]] = None
    email: Optional[List[str]] = None
    telephone: Optional[List[str]] = None
    contactPage: Optional[List[str]] = None
    language: Optional[List[ReferenceDataCode]] = None
