from typing import (
    Dict,
    List,
    Optional,
)

from rdflib import (
    Graph,
    Literal,
    RDF,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
    RDFS,
    SKOS,
)
from rdflib.term import Node

from fdk_rdf_parser.classes import Concept
from fdk_rdf_parser.classes.concept import (
    AssociativeRelation,
    Collection,
    Definition,
    GenericRelation,
    PartitiveRelation,
    Subject,
    TextAndURI,
)
from fdk_rdf_parser.rdf_utils import (
    date_value,
    dcat_uri,
    euvoc_uri,
    has_literal_value_on_predicate,
    has_value_on_predicate,
    is_type,
    object_value,
    resource_list,
    resource_uri_value,
    skosno_uri,
    skosxl_uri,
    uneskos_uri,
    value_set,
    value_translations,
    value_translations_list,
    xkos_uri_v_2,
)
from .contactpoint import extract_contact_points
from .harvest_meta_data import extract_meta_data
from .publisher import (
    extract_creator,
    extract_publisher,
)
from .temporal import extract_temporal_skos


def parse_text_and_uri(graph: Graph, subject: Node) -> TextAndURI:
    return TextAndURI(
        text=value_translations(graph, subject, RDFS.label),
        uri=resource_uri_value(graph.value(subject, RDFS.seeAlso)),
    )


def extract_range_deprecated(
    graph: Graph, definition_ref: URIRef
) -> Optional[TextAndURI]:
    range_list = []
    for range_ref in graph.objects(definition_ref, skosno_uri("omfang")):
        range_list.append(parse_text_and_uri(graph, range_ref))
    return range_list[0] if len(range_list) == 1 else None


def extract_range(graph: Graph, definition_ref: URIRef) -> Optional[List[TextAndURI]]:
    range_list = []
    for range_obj in graph.objects(definition_ref, skosno_uri("valueRange")):
        value = TextAndURI()
        if isinstance(range_obj, URIRef):
            value.uri = range_obj.toPython()
        elif isinstance(range_obj, Literal):
            if range_obj.language:
                value.text = {range_obj.language: range_obj.toPython()}
            else:
                value.text = {"nb": range_obj.toPython()}
        if value.uri is not None or value.text is not None:
            range_list.append(value)
    return range_list if len(range_list) > 0 else None


def extract_sources_deprecated(
    graph: Graph, definition_ref: URIRef
) -> Optional[List[TextAndURI]]:
    sources = []
    for source_ref in graph.objects(definition_ref, DCTERMS.source):
        sources.append(parse_text_and_uri(graph, source_ref))
    return sources if len(sources) > 0 else None


def extract_sources(graph: Graph, definition_ref: URIRef) -> Optional[List[TextAndURI]]:
    sources = []
    for source_ref in graph.objects(definition_ref, DCTERMS.source):
        sources.append(
            TextAndURI(
                text=value_translations(graph, source_ref, RDFS.label),
                uri=resource_uri_value(source_ref),
            )
        )
    return sources if len(sources) > 0 else None


def extract_subjects(graph: Graph, concept_ref: URIRef) -> Optional[List[Subject]]:
    subjects = []
    for subject_node in graph.objects(concept_ref, DCTERMS.subject):
        label: Dict[str, str] = dict()
        if isinstance(subject_node, Literal):
            if subject_node.language:
                label[subject_node.language] = subject_node.toPython()
            else:
                label["nb"] = subject_node.toPython()
        else:
            translations = value_translations(graph, subject_node, SKOS.prefLabel)
            label = translations if translations else dict()
        if len(label) > 0:
            subjects.append(Subject(label=label))
    return subjects if len(subjects) > 0 else None


def extract_status(graph: Graph, concept_ref: URIRef) -> Optional[Dict[str, str]]:
    status: Dict[str, str] = dict()
    for subject_node in graph.objects(concept_ref, euvoc_uri("status")):
        if isinstance(subject_node, Literal):
            if subject_node.language:
                status[subject_node.language] = subject_node.toPython()
            else:
                status["nb"] = subject_node.toPython()
        else:
            translations = value_translations(graph, subject_node, SKOS.prefLabel)
            status = translations if translations else dict()
    return status if len(status) > 0 else None


def extract_target_group_deprecated(
    graph: Graph, definition_ref: URIRef
) -> Optional[str]:
    uri = object_value(graph, definition_ref, DCTERMS.audience)
    if not uri:
        return None
    if "allmennheten" in uri:
        return "allmennheten"
    elif "fagspesialist" in uri:
        return "fagspesialist"
    else:
        return None


def extract_source_relationship_deprecated(
    graph: Graph, definition_ref: URIRef
) -> Optional[str]:
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


def parse_definition_deprecated(graph: Graph, definition_ref: URIRef) -> Definition:
    return Definition(
        text=value_translations(graph, definition_ref, RDFS.label),
        remark=value_translations(graph, definition_ref, SKOS.scopeNote),
        targetGroup=extract_target_group_deprecated(graph, definition_ref),
        sourceRelationship=extract_source_relationship_deprecated(
            graph, definition_ref
        ),
        range=extract_range_deprecated(graph, definition_ref),
        sources=extract_sources_deprecated(graph, definition_ref),
    )


def parse_euvoc_definition(graph: Graph, definition_ref: URIRef) -> Definition:
    return Definition(
        text=value_translations(graph, definition_ref, RDF.value),
        targetGroup=object_value(graph, definition_ref, DCTERMS.audience),
        sourceRelationship=object_value(
            graph, definition_ref, skosno_uri("relationshipWithSource")
        ),
        sources=extract_sources(graph, definition_ref),
    )


def parse_skos_definition(graph: Graph, concept_ref: URIRef) -> Definition:
    return Definition(text=value_translations(graph, concept_ref, SKOS.definition))


def extract_definitions(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[Definition]]:
    definitions: List[Definition] = list()
    if has_value_on_predicate(graph, concept_uri, euvoc_uri("xlDefinition")):
        for definition_ref in resource_list(
            graph, concept_uri, euvoc_uri("xlDefinition")
        ):
            definitions.append(parse_euvoc_definition(graph, definition_ref))
    elif has_value_on_predicate(graph, concept_uri, SKOS.definition):
        definitions.append(parse_skos_definition(graph, concept_uri))
    else:
        for definition_ref in resource_list(
            graph, concept_uri, skosno_uri("definisjon")
        ):
            definitions.append(parse_definition_deprecated(graph, definition_ref))

    if definitions:
        return definitions
    return None


def definition_has_not_target_group(definition: Definition) -> bool:
    if definition.targetGroup is None:
        return True
    else:
        return False


def get_first_definition_with_no_target_group(
    definitions: Optional[List[Definition]],
) -> Optional[Definition]:
    if definitions is not None:
        filtered_definitions = list(
            filter(definition_has_not_target_group, definitions)
        )
        if filtered_definitions:
            return filtered_definitions[0]
        else:
            return definitions[0]
    else:
        return None


def parse_associative_relation_deprecated(
    graph: Graph, associative_relation_ref: Node
) -> AssociativeRelation:
    return AssociativeRelation(
        description=value_translations(
            graph, associative_relation_ref, DCTERMS.description
        ),
        related=object_value(graph, associative_relation_ref, SKOS.related),
    )


def parse_associative_relation(
    graph: Graph, associative_relation_ref: Node
) -> AssociativeRelation:
    return AssociativeRelation(
        description=value_translations(
            graph, associative_relation_ref, skosno_uri("relationRole")
        ),
        related=object_value(
            graph, associative_relation_ref, skosno_uri("hasToConcept")
        ),
    )


def extract_associative_relations(
    graph: Graph, concept_uri: URIRef
) -> Optional[List[AssociativeRelation]]:
    associative_relations = []

    if has_value_on_predicate(graph, concept_uri, skosno_uri("isFromConceptIn")):
        for associative_relation_ref in graph.objects(
            concept_uri, skosno_uri("isFromConceptIn")
        ):
            associative_relations.append(
                parse_associative_relation(graph, associative_relation_ref)
            )
    else:
        for associative_relation_ref in graph.objects(
            concept_uri, skosno_uri("assosiativRelasjon")
        ):
            associative_relations.append(
                parse_associative_relation_deprecated(graph, associative_relation_ref)
            )
    return associative_relations if len(associative_relations) > 0 else None


def parse_partitive_relation(
    graph: Graph, partitive_relation_ref: Node
) -> PartitiveRelation:
    return PartitiveRelation(
        description=value_translations(
            graph, partitive_relation_ref, DCTERMS.description
        ),
        hasPart=object_value(
            graph, partitive_relation_ref, skosno_uri("hasPartitiveConcept")
        ),
        isPartOf=object_value(
            graph, partitive_relation_ref, skosno_uri("hasComprehensiveConcept")
        ),
    )


def parse_partitive_relation_deprecated(
    graph: Graph, partitive_relation_ref: Node
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
    if has_value_on_predicate(
        graph, concept_uri, skosno_uri("hasPartitiveConceptRelation")
    ):
        for partitive_relation_ref in graph.objects(
            concept_uri, skosno_uri("hasPartitiveConceptRelation")
        ):
            partitive_relations.append(
                parse_partitive_relation(graph, partitive_relation_ref)
            )
    else:
        for partitive_relation_ref in graph.objects(
            concept_uri, skosno_uri("partitivRelasjon")
        ):
            partitive_relations.append(
                parse_partitive_relation_deprecated(graph, partitive_relation_ref)
            )

    return partitive_relations if len(partitive_relations) > 0 else None


def parse_generic_relation(graph: Graph, generic_relation_ref: Node) -> GenericRelation:
    return GenericRelation(
        divisioncriterion=value_translations(
            graph, generic_relation_ref, DCTERMS.description
        ),
        generalizes=object_value(
            graph, generic_relation_ref, skosno_uri("hasSpecificConcept")
        ),
        specializes=object_value(
            graph, generic_relation_ref, skosno_uri("hasGenericConcept")
        ),
    )


def parse_generic_relation_deprecated(
    graph: Graph, generic_relation_ref: Node
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

    if has_value_on_predicate(
        graph, concept_uri, skosno_uri("hasGenericConceptRelation")
    ):
        for generic_relation_ref in graph.objects(
            concept_uri, skosno_uri("hasGenericConceptRelation")
        ):
            generic_relations.append(
                parse_generic_relation(graph, generic_relation_ref)
            )
    else:
        for generic_relation_ref in graph.objects(
            concept_uri, skosno_uri("generiskRelasjon")
        ):
            generic_relations.append(
                parse_generic_relation_deprecated(graph, generic_relation_ref)
            )
    return generic_relations if len(generic_relations) > 0 else None


def extract_collection_label(
    graph: Graph, collection_uri: Node
) -> Optional[Dict[str, str]]:
    if has_literal_value_on_predicate(graph, collection_uri, DCTERMS.title):
        return value_translations(graph, collection_uri, DCTERMS.title)
    else:
        return value_translations(graph, collection_uri, RDFS.label)


def parse_collection(graph: Graph, concept_record_uri: Node) -> Optional[Collection]:
    collection_record_uri = graph.value(concept_record_uri, DCTERMS.isPartOf)

    if collection_record_uri and is_type(
        dcat_uri("CatalogRecord"), graph, collection_record_uri
    ):
        collection_uri: Optional[Node] = graph.value(
            collection_record_uri, FOAF.primaryTopic
        )

        if collection_uri and is_type(SKOS.Collection, graph, collection_uri):
            return Collection(
                id=object_value(graph, collection_record_uri, DCTERMS.identifier),
                publisher=extract_publisher(graph, collection_uri),
                label=extract_collection_label(graph, collection_uri),
                uri=resource_uri_value(collection_uri),
                description=value_translations(
                    graph, collection_uri, DCTERMS.description
                ),
            )
    return None


def extract_pref_label(graph: Graph, concept_uri: URIRef) -> Optional[Dict[str, str]]:
    if has_literal_value_on_predicate(graph, concept_uri, SKOS.prefLabel):
        return value_translations(graph, concept_uri, SKOS.prefLabel)
    else:
        deprecated_labels = [
            value_translations(graph, label_ref, skosxl_uri("literalForm"))
            for label_ref in graph.objects(concept_uri, skosxl_uri("prefLabel"))
        ]
        return deprecated_labels[0] if len(deprecated_labels) > 0 else None


def extract_labels(
    graph: Graph, concept_uri: URIRef, predicate: URIRef, predicate_deprecated: URIRef
) -> Optional[List[Dict[str, str]]]:
    labels = list()
    if has_literal_value_on_predicate(graph, concept_uri, predicate):
        main_labels = value_translations_list(graph, concept_uri, predicate)
        labels.extend(main_labels) if main_labels is not None else None

    else:
        deprecated_labels = [
            value_translations(graph, label, skosxl_uri("literalForm"))
            for label in graph.objects(concept_uri, predicate_deprecated)
        ]

        for label in deprecated_labels:
            labels.append(label) if label is not None else None

    return labels if len(labels) > 0 else None


def _parse_concept(graph: Graph, fdk_record_uri: Node, concept_uri: URIRef) -> Concept:

    concept_temporal = extract_temporal_skos(graph, concept_uri)
    contact_points = extract_contact_points(graph, concept_uri)

    definition_list = extract_definitions(graph, concept_uri)

    return Concept(
        id=object_value(graph, fdk_record_uri, DCTERMS.identifier),
        uri=resource_uri_value(fdk_record_uri),
        identifier=concept_uri.toPython() if concept_uri else None,
        harvest=extract_meta_data(graph, fdk_record_uri),
        collection=parse_collection(graph, fdk_record_uri),
        publisher=extract_publisher(graph, concept_uri),
        creator=extract_creator(graph, concept_uri),
        subject=extract_subjects(graph, concept_uri),
        status=extract_status(graph, concept_uri),
        example=value_translations(graph, concept_uri, SKOS.example),
        prefLabel=extract_pref_label(graph, concept_uri),
        hiddenLabel=extract_labels(
            graph, concept_uri, SKOS.hiddenLabel, skosxl_uri("hiddenLabel")
        ),
        altLabel=extract_labels(
            graph, concept_uri, SKOS.altLabel, skosxl_uri("altLabel")
        ),
        contactPoint=contact_points[0] if contact_points else None,
        definition=get_first_definition_with_no_target_group(definition_list),
        definitions=definition_list,
        seeAlso=value_set(graph, concept_uri, RDFS.seeAlso),
        isReplacedBy=value_set(graph, concept_uri, DCTERMS.isReplacedBy),
        replaces=value_set(graph, concept_uri, DCTERMS.replaces),
        validFromIncluding=concept_temporal.startDate,
        validToIncluding=concept_temporal.endDate,
        associativeRelation=extract_associative_relations(graph, concept_uri),
        partitiveRelation=extract_partitive_relations(graph, concept_uri),
        genericRelation=extract_generic_relations(graph, concept_uri),
        created=date_value(graph, concept_uri, DCTERMS.created),
        exactMatch=value_set(graph, concept_uri, SKOS.exactMatch),
        closeMatch=value_set(graph, concept_uri, SKOS.closeMatch),
        memberOf=value_set(graph, concept_uri, uneskos_uri("memberOf")),
        remark=value_translations(graph, concept_uri, SKOS.scopeNote),
        range=extract_range(graph, concept_uri),
    )
