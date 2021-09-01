from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class FDKFormatType(str, Enum):
    UNKNOWN = "UNKNOWN"
    MEDIA_TYPE = "MEDIA_TYPE"
    FILE_TYPE = "FILE_TYPE"


@dataclass
class MediaType:
    uri: Optional[str] = None
    fdkType: FDKFormatType = FDKFormatType.UNKNOWN
    code: Optional[str] = None

    def __hash__(self: Any) -> int:
        return hash((self.uri, self.fdkType, self.code))
