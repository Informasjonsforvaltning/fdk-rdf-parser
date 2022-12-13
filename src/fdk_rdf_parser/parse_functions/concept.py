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
    RDFS,
    SKOS,
)

from fdk_rdf_parser.classes import (
    Concept,
    Temporal,
)
from fdk_rdf_parser.classes.concept import (
    AssociativeRelation,
    Collection,
    Definition,
    GenericRelation,
    PartitiveRelation,
    TextAndURI,
)
from fdk_rdf_parser.rdf_utils import (
    date_value,
    dcat_uri,
    is_type,
    object_value,
    skosno_old_uri,
    skosno_uri,
    skosxl_uri,
    value_set,
    value_translations,
    xkos_uri_v_2,
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
    for range_ref in graph.objects(definition_ref, skosno_old_uri("omfang")):
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
    uri = (
        uri
        if uri
        else object_value(graph, definition_ref, skosno_old_uri("forholdTilKilde"))
    )
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


def parse_definition(graph: Graph, definition_ref: URIRef) -> Definition:
    return Definition(
        text=value_translations(graph, definition_ref, RDFS.label),
        remark=value_translations(graph, definition_ref, SKOS.scopeNote),
        targetGroup=extract_target_group(graph, definition_ref),
        sourceRelationship=extract_source_relationship(graph, definition_ref),
        range=extract_range(graph, definition_ref),
        sources=extract_sources(graph, definition_ref),
        lastUpdated=date_value(graph, definition_ref, DCTERMS.modified),
    )


def extract_definition(graph: Graph, concept_uri: URIRef) -> Optional[Definition]:
    definitions = []
    for definition_ref in graph.objects(concept_uri, skosno_uri("definisjon")):
        definitions.append(parse_definition(graph, definition_ref))
    for definition_ref in graph.objects(
        concept_uri, skosno_old_uri("betydningsbeskrivelse")
    ):
        definitions.append(parse_definition(graph, definition_ref))
    return definitions[0] if len(definitions) > 0 else None


def parse_associative_relation(
    graph: Graph, associative_relation_ref: URIRef
) -> AssociativeRelation:
    return AssociativeRelation(
        description=value_translations(
            graph, associative_relation_ref, DCTERMS.description
        ),
        related=object_value(graph, associative_relation_ref, SKOS.related),
    )


def extract_associative_relations(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[AssociativeRelation]]:
    associative_relations = []
    for associative_relation_ref in graph.objects(
        concept_uri, skosno_uri("assosiativRelasjon")
    ):
        associative_relations.append(
            parse_associative_relation(graph, associative_relation_ref)
        )
    return associative_relations if len(associative_relations) > 0 else None


def parse_partitive_relation(
    graph: Graph, partitive_relation_ref: URIRef
) -> PartitiveRelation:
    return PartitiveRelation(
        description=value_translations(
            graph, partitive_relation_ref, DCTERMS.description
        ),
        hasPart=object_value(graph, partitive_relation_ref, DCTERMS.hasPart),
        isPartOf=object_value(graph, partitive_relation_ref, DCTERMS.isPartOf),
    )


def extract_partitive_relations(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[PartitiveRelation]]:
    partitive_relations = []
    for partitive_relation_ref in graph.objects(
        concept_uri, skosno_uri("partitivRelasjon")
    ):
        partitive_relations.append(
            parse_partitive_relation(graph, partitive_relation_ref)
        )
    return partitive_relations if len(partitive_relations) > 0 else None


def parse_generic_relation(
    graph: Graph, generic_relation_ref: URIRef
) -> GenericRelation:
    return GenericRelation(
        divisioncriterion=value_translations(
            graph, generic_relation_ref, skosno_uri("inndelingskriterium")
        ),
        generalizes=object_value(
            graph, generic_relation_ref, xkos_uri_v_2("generalizes")
        ),
        specializes=object_value(
            graph, generic_relation_ref, xkos_uri_v_2("specializes")
        ),
    )


def extract_generic_relations(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[GenericRelation]]:
    generic_relations = []
    for generic_relation_ref in graph.objects(
        concept_uri, skosno_uri("generiskRelasjon")
    ):
        generic_relations.append(parse_generic_relation(graph, generic_relation_ref))
    return generic_relations if len(generic_relations) > 0 else None


def parse_collection(graph: Graph, concept_record_uri: URIRef) -> Optional[Collection]:
    collection_record_uri = graph.value(concept_record_uri, DCTERMS.isPartOf)

    if collection_record_uri and is_type(
        dcat_uri("CatalogRecord"), graph, collection_record_uri
    ):
        collection_uri = graph.value(collection_record_uri, FOAF.primaryTopic)

        if collection_uri and is_type(SKOS.Collection, graph, collection_uri):
            return Collection(
                id=object_value(graph, collection_record_uri, DCTERMS.identifier),
                publisher=extract_publisher(graph, collection_uri),
                label=value_translations(graph, collection_uri, RDFS.label),
                uri=collection_uri.toPython(),
                description=value_translations(
                    graph, collection_uri, DCTERMS.description
                ),
            )
    return None


def create_application_language_dict(application: URIRef) -> Dict[str, str]:
    dict = {}
    if application.language:
        dict[application.language] = application.toPython()
    else:
        dict["nb"] = application.toPython()
    return dict


def parse_applications(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[Dict[str, str]]]:
    applications = []
    for application in graph.objects(concept_uri, skosno_uri("bruksområde")):
        applications.append(create_application_language_dict(application))
    for application in graph.objects(concept_uri, skosno_old_uri("bruksområde")):
        applications.append(create_application_language_dict(application))
    return applications if len(applications) > 0 else None


def parse_label_set(
    graph: Graph, concept_uri: URIRef, predicate: URIRef
) -> Optional[List[Dict[str, str]]]:
    values = []
    for label in graph.objects(concept_uri, predicate):
        literal_form = value_translations(graph, label, skosxl_uri("literalForm"))
        if literal_form:
            values.append(literal_form)
    return values if len(values) > 0 else None


def parse_concept(graph: Graph, fdk_record_uri: URIRef, concept_uri: URIRef) -> Concept:

    concept_temporal_list = extract_temporal(graph, concept_uri)
    concept_temporal = concept_temporal_list[0] if concept_temporal_list else Temporal()
    contact_points = extract_contact_points(graph, concept_uri)

    pref_label_list = parse_label_set(graph, concept_uri, skosxl_uri("prefLabel"))

    return Concept(
        id=object_value(graph, fdk_record_uri, DCTERMS.identifier),
        uri=fdk_record_uri.toPython() if fdk_record_uri else None,
        identifier=concept_uri.toPython() if concept_uri else None,
        harvest=extract_meta_data(graph, fdk_record_uri),
        collection=parse_collection(graph, fdk_record_uri),
        publisher=extract_publisher(graph, concept_uri),
        subject=value_translations(graph, concept_uri, DCTERMS.subject),
        application=parse_applications(graph, concept_uri),
        example=value_translations(graph, concept_uri, SKOS.example),
        prefLabel=pref_label_list[0]
        if pref_label_list and len(pref_label_list) > 0
        else None,
        hiddenLabel=parse_label_set(graph, concept_uri, skosxl_uri("hiddenLabel")),
        altLabel=parse_label_set(graph, concept_uri, skosxl_uri("altLabel")),
        contactPoint=contact_points[0] if contact_points else None,
        definition=extract_definition(graph, concept_uri),
        seeAlso=value_set(graph, concept_uri, RDFS.seeAlso),
        isReplacedBy=value_set(graph, concept_uri, DCTERMS.isReplacedBy),
        replaces=value_set(graph, concept_uri, DCTERMS.replaces),
        validFromIncluding=concept_temporal.startDate,
        validToIncluding=concept_temporal.endDate,
        associativeRelation=extract_associative_relations(graph, concept_uri),
        partitiveRelation=extract_partitive_relations(graph, concept_uri),
        genericRelation=extract_generic_relations(graph, concept_uri),
    )
