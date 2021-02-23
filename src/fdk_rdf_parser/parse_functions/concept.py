from typing import Dict, List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF, RDFS, SKOS

from fdk_rdf_parser.classes import Concept, Temporal
from fdk_rdf_parser.classes.concept import Collection, Definition, TextAndURI
from fdk_rdf_parser.rdf_utils import (
    date_value,
    dcat_uri,
    is_type,
    object_value,
    skosno_uri,
    skosxl_uri,
    value_set,
    value_translations,
)
from .contactpoint import extract_contact_points
from .harvest_meta_data import extract_meta_data
from .publisher import extract_publisher
from .temporal import extract_temporal


def parse_text_and_uri(graph: Graph, subject: URIRef) -> TextAndURI:
    return TextAndURI(
        text=value_translations(graph, subject, RDFS.label),
        uri=object_value(graph, subject, RDFS.seeAlso),
    )


def extract_range(graph: Graph, definition_ref: URIRef) -> Optional[TextAndURI]:
    range_list = []
    for range_ref in graph.objects(definition_ref, skosno_uri("omfang")):
        range_list.append(parse_text_and_uri(graph, range_ref))
    return range_list[0] if len(range_list) == 1 else None


def extract_sources(graph: Graph, definition_ref: URIRef) -> Optional[List[TextAndURI]]:
    sources = []
    for source_ref in graph.objects(definition_ref, DCTERMS.source):
        sources.append(parse_text_and_uri(graph, source_ref))
    return sources if len(sources) > 0 else None


def extract_target_group(graph: Graph, definition_ref: URIRef) -> Optional[str]:
    uri = object_value(graph, definition_ref, DCTERMS.audience)
    if not uri:
        return None
    if "allmennheten" in uri:
        return "allmennheten"
    elif "fagspesialist" in uri:
        return "fagspesialist"
    else:
        return None


def extract_source_relationship(graph: Graph, definition_ref: URIRef) -> Optional[str]:
    uri = object_value(graph, definition_ref, skosno_uri("forholdTilKilde"))
    if not uri:
        return None
    if "sitatFraKilde" in uri:
        return "sitatFraKilde"
    elif "basertPåKilde" in uri:
        return "basertPåKilde"
    elif "egendefinert" in uri:
        return "egendefinert"
    else:
        return None


def extract_definitions(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[Definition]]:
    definitions = []
    for definition_ref in graph.objects(concept_uri, skosno_uri("definisjon")):
        definitions.append(
            Definition(
                text=value_translations(graph, definition_ref, RDFS.label),
                remark=value_translations(graph, definition_ref, SKOS.scopeNote),
                targetGroup=extract_target_group(graph, definition_ref),
                sourceRelationship=extract_source_relationship(graph, definition_ref),
                range=extract_range(graph, definition_ref),
                sources=extract_sources(graph, definition_ref),
                lastUpdated=date_value(graph, definition_ref, DCTERMS.modified),
            )
        )
    return definitions if len(definitions) > 0 else None


def parse_collection(graph: Graph, concept_record_uri: URIRef) -> Optional[Collection]:
    collection_record_uri = graph.value(concept_record_uri, DCTERMS.isPartOf)

    if collection_record_uri and is_type(
        dcat_uri("CatalogRecord"), graph, collection_record_uri
    ):
        collection_uri = graph.value(collection_record_uri, FOAF.primaryTopic)

        if collection_uri and is_type(SKOS.Collection, graph, collection_uri):
            return Collection(
                id=object_value(graph, collection_record_uri, DCTERMS.identifier),
                publisher=extract_publisher(graph, collection_uri, collection_uri),
                label=value_translations(graph, collection_uri, RDFS.label),
                uri=collection_uri.toPython(),
                description=value_translations(
                    graph, collection_uri, DCTERMS.description
                ),
            )
    return None


def parse_applications(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[Dict[str, str]]]:
    applications = []
    for application in graph.objects(concept_uri, skosno_uri("bruksområde")):
        dict = {}
        if application.language:
            dict[application.language] = application.toPython()
        else:
            dict["nb"] = application.toPython()
        applications.append(dict)
    return applications if len(applications) > 0 else None


def parse_label_set(
    graph: Graph, concept_uri: URIRef, predicate: URIRef
) -> Optional[List[Dict[str, str]]]:
    values = []
    for label in graph.objects(concept_uri, predicate):
        literal_form = value_translations(graph, label, skosxl_uri("literalForm"))
        if literal_form:
            values.append(literal_form)
    values.sort()
    return values if len(values) > 0 else None


def parse_concept(graph: Graph, fdk_record_uri: URIRef, concept_uri: URIRef) -> Concept:

    concept_temporal_list = extract_temporal(graph, concept_uri)
    concept_temporal = concept_temporal_list[0] if concept_temporal_list else Temporal()

    pref_label_list = parse_label_set(graph, concept_uri, skosxl_uri("prefLabel"))

    return Concept(
        id=object_value(graph, fdk_record_uri, DCTERMS.identifier),
        uri=concept_uri.toPython(),
        harvest=extract_meta_data(graph, fdk_record_uri),
        collection=parse_collection(graph, fdk_record_uri),
        publisher=extract_publisher(
            graph, concept_uri, graph.value(fdk_record_uri, DCTERMS.isPartOf)
        ),
        subject=value_translations(graph, concept_uri, DCTERMS.subject),
        application=parse_applications(graph, concept_uri),
        example=value_translations(graph, concept_uri, DCTERMS.example),
        prefLabel=pref_label_list[0]
        if pref_label_list and len(pref_label_list) > 0
        else None,
        hiddenLabel=parse_label_set(graph, concept_uri, skosxl_uri("hiddenLabel")),
        altLabel=parse_label_set(graph, concept_uri, skosxl_uri("altLabel")),
        contactPoint=extract_contact_points(graph, concept_uri),
        definition=extract_definitions(graph, concept_uri),
        seeAlso=value_set(graph, concept_uri, RDFS.seeAlso),
        validFromIncluding=concept_temporal.startDate,
        validToIncluding=concept_temporal.endDate,
    )
