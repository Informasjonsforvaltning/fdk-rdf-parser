from dataclasses import dataclass
from enum import Enum
from typing import (
    Any,
    Optional,
)


class MediaTypeOrExtentType(str, Enum):
    UNKNOWN = "UNKNOWN"
    MEDIA_TYPE = "MEDIA_TYPE"
    FILE_TYPE = "FILE_TYPE"


@dataclass
class MediaTypeOrExtent:
    uri: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    type: MediaTypeOrExtentType = MediaTypeOrExtentType.UNKNOWN

    def __hash__(self: Any) -> int:
        return hash((self.uri, self.type, self.code))
