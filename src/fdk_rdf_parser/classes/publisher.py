from dataclasses import dataclass
from typing import Optional


@dataclass
class PublisherId:
    uri: Optional[str] = None
    id: Optional[str] = None
