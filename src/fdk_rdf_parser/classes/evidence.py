from dataclasses import dataclass
from enum import Enum
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    dcat_uri,
)
from .skos_code import ReferenceDataCode


class EvidenceRdfType(str, Enum):
    UNKNOWN = "UNKNOWN"
    DATASET_TYPE = dcat_uri("Dataset")
    EVIDENCE_TYPE = cv_uri("Evidence")


@dataclass
class Evidence:
    rdfType: EvidenceRdfType = EvidenceRdfType.UNKNOWN
    uri: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    dctType: Optional[List[ReferenceDataCode]] = None
    language: Optional[List[ReferenceDataCode]] = None
    page: Optional[List[str]] = None
