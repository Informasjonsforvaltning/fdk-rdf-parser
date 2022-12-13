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
    RDF,
)

from fdk_rdf_parser.classes import Agent
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    is_uri_in_list,
    object_value,
    value_list,
    value_translations,
)


def extract_agents_for_participation(
    graph: Graph, participation_ref: URIRef
) -> Optional[List[Agent]]:
    values = []
    agents = graph.subjects(predicate=RDF.type, object=DCTERMS.Agent)
    filtered_agents = filter(
        lambda agent: is_uri_in_list(
            participation_ref, graph, agent, cv_uri("playsRole")
        ),
        agents,
    )
    for resource in filtered_agents:
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None

        values.append(
            Agent(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                title=value_translations(graph, resource, DCTERMS.title),
                name=object_value(graph, resource, FOAF.name),
                playsRole=value_list(graph, resource, cv_uri("playsRole")),
            )
        )

    return values if len(values) > 0 else None
