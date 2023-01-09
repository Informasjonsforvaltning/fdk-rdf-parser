from dataclasses import dataclass
from typing import (
    Dict,
    Optional,
)


@dataclass
class Address:
    streetAddress: Optional[str] = None
    locality: Optional[str] = None
    postalCode: Optional[str] = None
    countryName: Optional[Dict[str, str]] = None
