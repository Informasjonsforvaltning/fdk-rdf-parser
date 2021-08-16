from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class MediaType:
    uri: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = "UNKNOWN"

    def __hash__(self: Any) -> int:
        return hash((self.uri, self.code, self.name))
