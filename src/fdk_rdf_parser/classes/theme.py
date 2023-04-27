from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)


@dataclass
class EuDataTheme:
    uri: Optional[str] = None
    code: Optional[str] = None
    title: Optional[Dict[str, str]] = None


@dataclass
class LosNode:
    isTema: Optional[bool] = None
    losPaths: Optional[List[str]] = None
    name: Optional[Dict[str, str]] = None
    uri: Optional[str] = None
    code: Optional[str] = None


@dataclass
class Eurovoc:
    uri: Optional[str] = None
    code: Optional[str] = None
    label: Optional[Dict[str, str]] = None
    eurovocPaths: Optional[List[str]] = None
