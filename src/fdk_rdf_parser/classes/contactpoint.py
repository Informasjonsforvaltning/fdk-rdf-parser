from dataclasses import dataclass

@dataclass
class ContactPoint:
    uri: str = None
    fullname: str = None
    email: str = None
    organizationName: str = None
    organizationUnit: str = None
    hasURL: str = None
    hasTelephone: str = None
