from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .address import Address
from .reference_data_code import ReferenceDataCode


@dataclass
class Channel:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    channelType: Optional[ReferenceDataCode] = None
    description: Optional[Dict[str, str]] = None
    address: Optional[List[Address]] = None
    processingTime: Optional[str] = None
    hasInput: Optional[List[str]] = None
    email: Optional[List[str]] = None
    url: Optional[List[str]] = None
    telephone: Optional[List[str]] = None
