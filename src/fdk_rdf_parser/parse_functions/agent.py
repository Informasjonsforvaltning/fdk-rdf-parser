from typing import (
    Dict,
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

from fdk_rdf_parser.classes import Agent
from fdk_rdf_parser.parse_functions.organization import parse_organization
from fdk_rdf_parser.parse_functions.participation import parse_participation
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    org_uri,
    resource_list,
    rov_uri,
    uri_or_identifier,
    value_translations,
)
from fdk_rdf_parser.rdf_utils.utils import is_type


def parse_agent_or_organization(graph: Graph, subject: URIRef) -> Optional[Agent]:
    if (
        is_type(org_uri("Organization"), graph, subject)
        or is_type(rov_uri("RegisteredOrganization"), graph, subject)
        or is_type(cv_uri("PublicOrganisation"), graph, subject)
    ):
        return parse_organization(graph, subject)
    elif is_type(FOAF.Agent, graph, subject) or is_type(DCTERMS.Agent, graph, subject):
        return Agent(
            uri=uri_or_identifier(graph, subject),
            identifier=object_value(graph, subject, DCTERMS.identifier),
            name=value_translations(graph, subject, DCTERMS.title),
        )
    else:
        return None


def extract_participating_agents(
    graph: Graph, service_uri: URIRef
) -> Optional[List[Agent]]:
    agents: Dict[str, Agent] = {}
    for participation in resource_list(graph, service_uri, cv_uri("hasParticipation")):
        agent_uri = object_value(graph, participation, cv_uri("hasParticipant"))
        if agent_uri and agent_uri not in agents:
            agent = parse_agent_or_organization(graph, URIRef(agent_uri))
            if agent:
                agents[agent_uri] = agent

        parsed_participation = parse_participation(graph, participation)
        agent = agents.get(agent_uri) if agent_uri else None
        if parsed_participation and agent:
            if agent.playsRole:
                agent.playsRole.append(parsed_participation)
            else:
                agent.playsRole = [parsed_participation]

    values = list(agents.values())
    return values if len(values) > 0 else None
