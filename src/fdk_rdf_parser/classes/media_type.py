from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class MediaType:
    uri: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = "unknown"
    subType: Optional[str] = None

    def __hash__(self: Any) -> int:
        return hash((self.uri, self.name, self.type, self.subType))
