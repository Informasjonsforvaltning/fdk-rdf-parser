from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import PublicService
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    value_list,
    value_translations,
)
from .channel import extract_channels
from .cost import extract_costs
from .criterion_requirement import extract_criterion_requirements
from .dcat_resource import extract_key_words, extract_skos_code_list
from .event import extract_events
from .evidence import extract_evidences
from .harvest_meta_data import extract_meta_data
from .legal_resource import extract_legal_resources
from .output import extract_outputs
from .participation import extract_participations
from .publisher import Publisher
from .rule import extract_rules
from .schema_contact_point import extract_schema_contact_points
from .skos_concept import extract_skos_concept


def extract_publishers(
    public_services_graph: Graph, public_service_uri: URIRef
) -> Optional[List[Publisher]]:
    authorities = value_list(
        public_services_graph, public_service_uri, cv_uri("hasCompetentAuthority")
    )
    if authorities is not None and len(authorities) > 0:
        return list(
            map(
                lambda hasCompetentAuthority: Publisher(uri=hasCompetentAuthority),
                authorities,
            )
        )
    else:
        return None


def extract_public_services(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[PublicService]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            PublicService(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                id=object_value(graph, resource, DCTERMS.identifier),
                title=value_translations(graph, resource, DCTERMS.title),
            )
        )

    return values if len(values) > 0 else None


def parse_public_service(
    public_services_graph: Graph, catalog_record_uri: URIRef, public_service_uri: URIRef
) -> PublicService:

    public_service = PublicService(
        id=object_value(public_services_graph, catalog_record_uri, DCTERMS.identifier),
        uri=public_service_uri.toPython(),
        identifier=object_value(
            public_services_graph, public_service_uri, DCTERMS.identifier
        ),
        title=value_translations(
            public_services_graph, public_service_uri, DCTERMS.title
        ),
        description=value_translations(
            public_services_graph, public_service_uri, DCTERMS.description
        ),
        isGroupedBy=extract_events(public_services_graph, public_service_uri),
        hasCompetentAuthority=extract_publishers(
            public_services_graph, public_service_uri
        ),
        harvest=extract_meta_data(public_services_graph, catalog_record_uri),
        keyword=extract_key_words(public_services_graph, public_service_uri),
        sector=extract_skos_concept(
            public_services_graph, public_service_uri, cv_uri("sector")
        ),
        isClassifiedBy=extract_skos_concept(
            public_services_graph, public_service_uri, cv_uri("isClassifiedBy")
        ),
        language=extract_skos_code_list(
            public_services_graph, public_service_uri, DCTERMS.language
        ),
        hasCriterion=extract_criterion_requirements(
            public_services_graph, public_service_uri
        ),
        hasParticipation=extract_participations(
            public_services_graph, public_service_uri
        ),
        hasInput=extract_evidences(public_services_graph, public_service_uri),
        produces=extract_outputs(public_services_graph, public_service_uri),
        requires=extract_public_services(
            public_services_graph, public_service_uri, DCTERMS.requires
        ),
        hasContactPoint=extract_schema_contact_points(
            public_services_graph, public_service_uri
        ),
        follows=extract_rules(public_services_graph, public_service_uri),
        hasLegalResource=extract_legal_resources(
            public_services_graph, public_service_uri
        ),
        hasChannel=extract_channels(public_services_graph, public_service_uri),
        processingTime=object_value(
            public_services_graph, public_service_uri, cv_uri("processingTime")
        ),
        hasCost=extract_costs(public_services_graph, public_service_uri),
        relation=extract_public_services(
            public_services_graph, public_service_uri, DCTERMS.relation
        ),
    )
    return public_service
