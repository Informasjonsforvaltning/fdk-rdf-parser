from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ModelCodeElement:
    identifier: Optional[str] = None
    prefLabel: Optional[Dict[str, str]] = None
    inScheme: Optional[List[str]] = None
    subject: Optional[str] = None
    notation: Optional[str] = None
    topConceptOf: Optional[List[str]] = None
    definition: Optional[List[str]] = None
    example: Optional[List[str]] = None
    exclusionNote: Optional[Dict[str, str]] = None
    previousElement: Optional[List[str]] = None
    hiddenLabel: Optional[Dict[str, str]] = None
    inclusionNote: Optional[Dict[str, str]] = None
    note: Optional[Dict[str, str]] = None
    nextElement: Optional[List[str]] = None
    scopeNote: Optional[Dict[str, str]] = None
    altLabel: Optional[Dict[str, str]] = None

    def __lt__(self: Any, other: Any) -> bool:
        return self.identifier < other.identifier


@dataclass
class ModelElement:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    subject: Optional[str] = None
    hasProperty: Optional[List[str]] = None
    belongsToModule: Optional[str] = None
    elementTypes: Optional[List[str]] = None
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
