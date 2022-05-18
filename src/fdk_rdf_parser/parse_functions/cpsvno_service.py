from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import PublicService, Service
from fdk_rdf_parser.rdf_utils import (
    cpsv_uri,
    cv_uri,
    duration_string_value,
    is_type,
    object_value,
    resource_list,
    value_list,
    value_translations,
)
from .channel import extract_channels
from .contactpoint import extract_contact_points
from .cost import extract_costs
from .criterion_requirement import extract_criterion_requirements
from .dcat_resource import extract_key_words, extract_skos_code_list
from .evidence import extract_evidences
from .harvest_meta_data import extract_meta_data
from .legal_resource import extract_legal_resources
from .output import extract_outputs
from .participation import extract_participations
from .publisher import extract_list_of_publishers
from .rule import extract_rules
from .schema_contact_point import extract_schema_contact_points
from .skos_concept import extract_skos_concept


def extract_cpsvno_services(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Service]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            Service(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                id=object_value(graph, resource, DCTERMS.identifier),
                title=value_translations(graph, resource, DCTERMS.title),
            )
        )

    return values if len(values) > 0 else None


def parse_cpsvno_service(
    services_graph: Graph, catalog_record_uri: URIRef, cpsvno_service_uri: URIRef
) -> Service:

    service = Service(
        id=object_value(services_graph, catalog_record_uri, DCTERMS.identifier),
        uri=cpsvno_service_uri.toPython(),
        identifier=object_value(services_graph, cpsvno_service_uri, DCTERMS.identifier),
        title=value_translations(services_graph, cpsvno_service_uri, DCTERMS.title),
        description=value_translations(
            services_graph, cpsvno_service_uri, DCTERMS.description
        ),
        ownedBy=extract_list_of_publishers(
            services_graph, cpsvno_service_uri, cv_uri("ownedBy")
        ),
        contactPoint=extract_contact_points(services_graph, cpsvno_service_uri),
        isGroupedBy=value_list(
            services_graph, cpsvno_service_uri, cv_uri("isGroupedBy")
        ),
        harvest=extract_meta_data(services_graph, catalog_record_uri),
        keyword=extract_key_words(services_graph, cpsvno_service_uri),
        sector=extract_skos_concept(
            services_graph, cpsvno_service_uri, cv_uri("sector")
        ),
        isClassifiedBy=extract_skos_concept(
            services_graph, cpsvno_service_uri, cv_uri("isClassifiedBy")
        ),
        isDescribedAt=extract_skos_concept(
            services_graph, cpsvno_service_uri, cv_uri("isDescribedAt")
        ),
        language=extract_skos_code_list(
            services_graph, cpsvno_service_uri, DCTERMS.language
        ),
        hasCriterion=extract_criterion_requirements(services_graph, cpsvno_service_uri),
        hasParticipation=extract_participations(services_graph, cpsvno_service_uri),
        hasInput=extract_evidences(services_graph, cpsvno_service_uri),
        produces=extract_outputs(services_graph, cpsvno_service_uri),
        requires=extract_cpsvno_services(
            services_graph, cpsvno_service_uri, DCTERMS.requires
        ),
        follows=extract_rules(services_graph, cpsvno_service_uri),
        hasLegalResource=extract_legal_resources(services_graph, cpsvno_service_uri),
        hasChannel=extract_channels(
            services_graph, cpsvno_service_uri, cv_uri("hasChannel")
        ),
        processingTime=duration_string_value(
            services_graph, cpsvno_service_uri, cv_uri("processingTime")
        ),
        hasCost=extract_costs(services_graph, cpsvno_service_uri),
        relation=extract_cpsvno_services(
            services_graph, cpsvno_service_uri, DCTERMS.relation
        ),
        spatial=value_list(services_graph, cpsvno_service_uri, DCTERMS.spatial),
    )

    if is_type(cpsv_uri("PublicService"), services_graph, cpsvno_service_uri):
        public_service = PublicService(
            hasCompetentAuthority=extract_list_of_publishers(
                services_graph, cpsvno_service_uri, cv_uri("hasCompetentAuthority")
            ),
            hasContactPoint=extract_schema_contact_points(
                services_graph, cpsvno_service_uri
            ),
        )
        public_service.add_cpsvno_service_values(service)
        return public_service
    else:
        return service
