from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
)


@dataclass
class ModelCodeElement:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    inScheme: Optional[Set[str]] = None
    subject: Optional[str] = None
    notation: Optional[str] = None
    topConceptOf: Optional[Set[str]] = None
    definition: Optional[Set[str]] = None
    example: Optional[Set[str]] = None
    exclusionNote: Optional[Dict[str, str]] = None
    previousElement: Optional[Set[str]] = None
    hiddenLabel: Optional[Dict[str, str]] = None
    inclusionNote: Optional[Dict[str, str]] = None
    note: Optional[Dict[str, str]] = None
    nextElement: Optional[Set[str]] = None
    scopeNote: Optional[Dict[str, str]] = None
    altLabel: Optional[Dict[str, str]] = None

    def __lt__(self: Any, other: Any) -> bool:
        self_identifier = self.identifier if self.identifier else ""
        other_identifier = other.identifier if other.identifier else ""
        return self_identifier < other_identifier


@dataclass
class ModelElement:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    subject: Optional[str] = None
    hasProperty: Optional[List[str]] = None
    belongsToModule: Optional[str] = None
    elementTypes: Optional[Set[str]] = None
    codeListReference: Optional[str] = None
    codes: Optional[List[ModelCodeElement]] = None
    typeDefinitionReference: Optional[str] = None
    fractionDigits: Optional[int] = None
    length: Optional[int] = None
    maxInclusive: Optional[float] = None
    maxLength: Optional[int] = None
    minInclusive: Optional[float] = None
    minLength: Optional[int] = None
    pattern: Optional[str] = None
    totalDigits: Optional[int] = None
