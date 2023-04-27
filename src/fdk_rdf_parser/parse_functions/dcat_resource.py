import re
from typing import (
    Dict,
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import PartialDcatResource
from fdk_rdf_parser.rdf_utils import (
    date_value,
    dcat_uri,
    object_value,
    value_list,
    value_set,
    value_translations,
)
from .contactpoint import extract_contact_points
from .publisher import extract_publisher
from .reference_data_code import (
    extract_reference_data_code,
    extract_reference_data_code_list,
)
from .theme import (
    map_data_themes,
    map_eurovoc_themes,
    map_los_themes,
    split_theme_refs,
)


def parse_dcat_resource(graph: Graph, subject: URIRef) -> PartialDcatResource:
    formatted_description = value_translations(graph, subject, DCTERMS.description)
    theme_refs = split_theme_refs(graph, subject, dcat_uri("theme"))
    return PartialDcatResource(
        identifier=value_set(graph, subject, DCTERMS.identifier),
        publisher=extract_publisher(graph, subject),
        title=value_translations(graph, subject, DCTERMS.title),
        description=description_html_cleaner(formatted_description)
        if formatted_description
        else None,
        descriptionFormatted=formatted_description,
        uri=subject.toPython(),
        accessRights=extract_reference_data_code(graph, subject, DCTERMS.accessRights),
        themeUris=value_list(graph, subject, dcat_uri("theme")),
        theme=map_data_themes(graph, theme_refs["data-themes"]),
        losTheme=map_los_themes(graph, theme_refs["los"]),
        eurovocThemes=map_eurovoc_themes(graph, theme_refs["eurovocs"]),
        keyword=extract_key_words(graph, subject),
        contactPoint=extract_contact_points(graph, subject),
        dctType=object_value(graph, subject, DCTERMS.type),
        issued=date_value(graph, subject, DCTERMS.issued),
        modified=date_value(graph, subject, DCTERMS.modified),
        landingPage=value_set(graph, subject, dcat_uri("landingPage")),
        language=extract_reference_data_code_list(graph, subject, DCTERMS.language),
    )


def extract_key_words(graph: Graph, subject: URIRef) -> Optional[List[Dict[str, str]]]:
    values = []
    for keyword in graph.objects(subject, dcat_uri("keyword")):
        translation = {}
        if keyword.language:
            translation[keyword.language] = keyword.toPython()
        else:
            translation["nb"] = keyword.toPython()
        values.append(translation)
    return values if len(values) > 0 else None


def description_html_cleaner(formatted: Dict[str, str]) -> Optional[Dict[str, str]]:
    cleaner_regex = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
    description = {}
    for language in formatted:
        description[language] = re.sub(cleaner_regex, "", formatted[language])

    return description if len(description) > 0 else None
