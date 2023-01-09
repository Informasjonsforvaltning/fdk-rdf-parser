from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes import Agent


@dataclass
class Organization(Agent):
    title: Optional[Dict[str, str]] = None
    orgPath: Optional[str] = None
    orgType: Optional[str] = None
    spatial: Optional[List[str]] = None
    homepage: Optional[List[str]] = None
