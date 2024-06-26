from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
)
from rdflib.term import Node

from fdk_rdf_parser.classes import (
    PublicService,
    Service,
)
from fdk_rdf_parser.rdf_utils import (
    cpsv_uri,
    cv_uri,
    duration_string_value,
    is_type,
    object_value,
    resource_list,
    resource_uri_value,
    value_list,
    value_translations,
)
from .agent import extract_participating_agents
from .catalog import parse_catalog
from .channel import extract_channels
from .contactpoint import extract_cv_contact_point
from .cost import extract_costs
from .dcat_resource import extract_key_words
from .evidence import extract_evidences
from .harvest_meta_data import extract_meta_data
from .legal_resource import extract_legal_resources
from .organization import extract_organizations
from .output import extract_outputs
from .reference_data_code import (
    extract_reference_adms_status,
    extract_reference_language_list,
    extract_reference_main_activities,
)
from .requirement import extract_requirements
from .rule import extract_rules
from .skos_concept import extract_skos_concept
from .theme import (
    map_data_themes,
    map_eurovoc_themes,
    map_los_themes,
    split_theme_refs,
)


def extract_cpsvno_services(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Service]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        values.append(
            Service(
                uri=resource_uri_value(resource),
                identifier=object_value(graph, resource, DCTERMS.identifier),
                id=object_value(graph, resource, DCTERMS.identifier),
                title=value_translations(graph, resource, DCTERMS.title),
            )
        )

    return values if len(values) > 0 else None


def _parse_cpsvno_service(
    services_graph: Graph, catalog_record_uri: Node, cpsvno_service_uri: URIRef
) -> Service:
    theme_refs = split_theme_refs(
        services_graph, cpsvno_service_uri, cv_uri("thematicArea")
    )

    service = Service(
        id=object_value(services_graph, catalog_record_uri, DCTERMS.identifier),
        uri=resource_uri_value(cpsvno_service_uri),
        identifier=object_value(services_graph, cpsvno_service_uri, DCTERMS.identifier),
        title=value_translations(services_graph, cpsvno_service_uri, DCTERMS.title),
        description=value_translations(
            services_graph, cpsvno_service_uri, DCTERMS.description
        ),
        ownedBy=extract_organizations(
            services_graph, cpsvno_service_uri, cv_uri("ownedBy")
        ),
        contactPoint=extract_cv_contact_point(services_graph, cpsvno_service_uri),
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
        language=extract_reference_language_list(
            services_graph, cpsvno_service_uri, DCTERMS.language
        ),
        holdsRequirement=extract_requirements(services_graph, cpsvno_service_uri),
        hasParticipation=value_list(
            services_graph, cpsvno_service_uri, cv_uri("hasParticipation")
        ),
        hasInput=extract_evidences(services_graph, cpsvno_service_uri),
        produces=extract_outputs(services_graph, cpsvno_service_uri),
        requires=extract_cpsvno_services(
            services_graph, cpsvno_service_uri, DCTERMS.requires
        ),
        follows=extract_rules(services_graph, cpsvno_service_uri),
        hasLegalResource=extract_legal_resources(
            services_graph, cpsvno_service_uri, cv_uri("hasLegalResource")
        ),
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
        admsStatus=extract_reference_adms_status(services_graph, cpsvno_service_uri),
        subject=extract_skos_concept(
            services_graph, cpsvno_service_uri, DCTERMS.subject
        ),
        homepage=value_list(services_graph, cpsvno_service_uri, FOAF.homepage),
        dctType=extract_reference_main_activities(services_graph, cpsvno_service_uri),
        thematicAreaUris=value_list(
            services_graph, cpsvno_service_uri, cv_uri("thematicArea")
        ),
        euDataThemes=map_data_themes(services_graph, theme_refs["data-themes"]),
        losThemes=map_los_themes(services_graph, theme_refs["los"]),
        eurovocThemes=map_eurovoc_themes(services_graph, theme_refs["eurovocs"]),
        participatingAgents=extract_participating_agents(
            services_graph, cpsvno_service_uri
        ),
        catalog=parse_catalog(services_graph, catalog_record_uri),
    )

    if is_type(cpsv_uri("PublicService"), services_graph, cpsvno_service_uri):
        public_service = PublicService(
            hasCompetentAuthority=extract_organizations(
                services_graph, cpsvno_service_uri, cv_uri("hasCompetentAuthority")
            ),
        )
        public_service.add_cpsvno_service_values(service)
        return public_service
    else:
        return service
