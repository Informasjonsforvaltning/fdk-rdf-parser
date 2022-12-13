from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
    Set,
)


@dataclass
class ModelProperty:
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    subject: Optional[str] = None
    propertyTypes: Optional[Set[str]] = None
    minOccurs: Optional[int] = None
    maxOccurs: Optional[int] = None
    hasType: Optional[List[str]] = None
    relationPropertyLabel: Optional[Dict[str, str]] = None
    sequenceNumber: Optional[int] = None
    belongsToModule: Optional[str] = None
    formsSymmetryWith: Optional[str] = None
    isAbstractionOf: Optional[str] = None
    refersTo: Optional[str] = None
    hasDataType: Optional[str] = None
    hasSimpleType: Optional[str] = None
    hasObjectType: Optional[str] = None
    hasValueFrom: Optional[str] = None
    hasSome: Optional[List[str]] = None
    hasMember: Optional[str] = None
    contains: Optional[str] = None
    hasSupplier: Optional[str] = None
    hasGeneralConcept: Optional[str] = None
    notification: Optional[Dict[str, str]] = None
