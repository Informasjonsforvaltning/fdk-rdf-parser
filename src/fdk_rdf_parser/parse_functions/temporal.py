from typing import (
    Any,
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Temporal
from fdk_rdf_parser.rdf_utils import (
    date_value,
    dcat_uri,
    owl_time_uri,
    resource_list,
    schema_uri,
)


def extract_temporal(graph: Graph, subject: URIRef) -> Optional[List[Temporal]]:
    values = []
    for temporal_resource in resource_list(graph, subject, DCTERMS.temporal):
        temporal_uri = None
        if isinstance(temporal_resource, URIRef):
            temporal_uri = temporal_resource.toPython()

        start_value = date_value(graph, temporal_resource, dcat_uri("startDate"))
        end_value = date_value(graph, temporal_resource, dcat_uri("endDate"))

        start_value = (
            date_value(graph, temporal_resource, schema_uri("startDate"))
            if start_value is None
            else start_value
        )
        end_value = (
            date_value(graph, temporal_resource, schema_uri("endDate"))
            if end_value is None
            else end_value
        )

        start_value = (
            extract_owl_time_start(graph, temporal_resource)
            if start_value is None
            else start_value
        )
        end_value = (
            extract_owl_time_end(graph, temporal_resource)
            if end_value is None
            else end_value
        )

        values.append(
            Temporal(uri=temporal_uri, startDate=start_value, endDate=end_value)
        )

    return values if len(values) > 0 else None


def extract_owl_time_instant(graph: Graph, subject: Any) -> Optional[str]:
    owl_date = date_value(graph, subject, owl_time_uri("inXSDDateTime"))
    owl_date = (
        date_value(graph, subject, owl_time_uri("inXSDDateTimeStamp"))
        if owl_date is None
        else owl_date
    )
    owl_date = (
        date_value(graph, subject, owl_time_uri("inXSDDate"))
        if owl_date is None
        else owl_date
    )

    return owl_date


def extract_owl_time_start(graph: Graph, subject: Any) -> Any:
    has_beginning = graph.value(subject, owl_time_uri("hasBeginning"))
    if has_beginning is not None:
        return extract_owl_time_instant(graph, has_beginning)
    else:
        return None


def extract_owl_time_end(graph: Graph, subject: Any) -> Any:
    has_end = graph.value(subject, owl_time_uri("hasEnd"))
    if has_end is not None:
        return extract_owl_time_instant(graph, has_end)
    else:
        return None
