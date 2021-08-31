from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class FDKFormatType(str, Enum):
    UNKNOWN = "UNKNOWN"
    IANA = "IANA"
    FILE = "FILE"


@dataclass
class MediaType:
    fdkType: FDKFormatType = FDKFormatType.UNKNOWN
    code: Optional[str] = None

    def __hash__(self: Any) -> int:
        return hash((self.fdkType, self.code))
