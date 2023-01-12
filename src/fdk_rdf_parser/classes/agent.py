from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes.participation import Participation


@dataclass
class Agent:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    playsRole: Optional[List[Participation]] = None
