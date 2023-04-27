from typing import (
    Dict,
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import SKOS

from fdk_rdf_parser.classes import (
    EuDataTheme,
    Eurovoc,
    LosNode,
)
from fdk_rdf_parser.rdf_utils import (
    fdk_internal_uri,
    resource_list,
    value_list,
    value_translations,
)

data_theme_base = "http://publications.europa.eu/resource/authority/data-theme"
eurovoc_base = "http://eurovoc.europa.eu"
los_base = "https://psi.norge.no/los"
los_theme_url_part = "/tema/"


def code_from_theme_uri(uri: str) -> str:
    return uri.split("/")[-1]


def split_theme_refs(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Dict[str, List[URIRef]]:
    los: List[URIRef] = list()
    data_themes: List[URIRef] = list()
    eurovocs: List[URIRef] = list()
    for resource in resource_list(graph, subject, predicate):
        theme_uri = resource.toPython() if isinstance(resource, URIRef) else None
        if los_base in theme_uri:
            los.append(resource)
        elif data_theme_base in theme_uri:
            data_themes.append(resource)
        elif eurovoc_base in theme_uri:
            eurovocs.append(resource)

    return {"los": los, "data-themes": data_themes, "eurovocs": eurovocs}


def map_los_themes(graph: Graph, theme_refs: List[URIRef]) -> Optional[List[LosNode]]:
    values = []
    for resource in theme_refs:
        los_uri = resource.toPython()

        values.append(
            LosNode(
                uri=los_uri,
                isTema=True if los_theme_url_part in los_uri else False,
                code=code_from_theme_uri(los_uri),
                name=value_translations(graph, resource, SKOS.prefLabel),
                losPaths=value_list(graph, resource, fdk_internal_uri("themePath")),
            )
        )

    return values if len(values) > 0 else None


def map_data_themes(
    graph: Graph, theme_refs: List[URIRef]
) -> Optional[List[EuDataTheme]]:
    values = []
    for resource in theme_refs:
        theme_uri = resource.toPython()
        values.append(
            EuDataTheme(
                uri=theme_uri,
                code=code_from_theme_uri(theme_uri),
                title=value_translations(graph, resource, SKOS.prefLabel),
            )
        )

    return values if len(values) > 0 else None


def map_eurovoc_themes(
    graph: Graph, theme_refs: List[URIRef]
) -> Optional[List[Eurovoc]]:
    values = []
    for resource in theme_refs:
        theme_uri = resource.toPython()
        values.append(
            Eurovoc(
                uri=theme_uri,
                code=code_from_theme_uri(theme_uri),
                label=value_translations(graph, resource, SKOS.prefLabel),
                eurovocPaths=value_list(graph, resource, fdk_internal_uri("themePath")),
            )
        )

    return values if len(values) > 0 else None
