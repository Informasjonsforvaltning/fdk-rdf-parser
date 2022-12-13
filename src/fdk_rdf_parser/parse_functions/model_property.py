from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDF,
    XSD,
)

from fdk_rdf_parser.classes.model_property import ModelProperty
from fdk_rdf_parser.rdf_utils import (
    model_dcat_ap_no_uri,
    object_value,
    resource_list,
    uri_or_identifier,
    uri_or_identifier_list,
    value_set,
    value_translations,
)


def parse_model_property(graph: Graph, prop_ref: URIRef) -> ModelProperty:
    prop_uri = None
    if isinstance(prop_ref, URIRef):
        prop_uri = prop_ref.toPython()

    has_type_refs = resource_list(graph, prop_ref, model_dcat_ap_no_uri("hasType"))
    has_some_refs = resource_list(graph, prop_ref, model_dcat_ap_no_uri("hasSome"))

    symmetry_ref = graph.value(prop_ref, model_dcat_ap_no_uri("formsSymmetryWith"))
    data_type_ref = graph.value(prop_ref, model_dcat_ap_no_uri("hasDataType"))
    simple_type_ref = graph.value(prop_ref, model_dcat_ap_no_uri("hasSimpleType"))
    object_type_ref = graph.value(prop_ref, model_dcat_ap_no_uri("hasObjectType"))
    value_from_ref = graph.value(prop_ref, model_dcat_ap_no_uri("hasValueFrom"))
    abstraction_ref = graph.value(prop_ref, model_dcat_ap_no_uri("isAbstractionOf"))
    refers_to_ref = graph.value(prop_ref, model_dcat_ap_no_uri("refersTo"))
    member_ref = graph.value(prop_ref, model_dcat_ap_no_uri("hasMember"))
    contains_ref = graph.value(prop_ref, model_dcat_ap_no_uri("contains"))
    supplier_ref = graph.value(prop_ref, model_dcat_ap_no_uri("hasSupplier"))
    general_concept_ref = graph.value(
        prop_ref, model_dcat_ap_no_uri("hasGeneralConcept")
    )

    return ModelProperty(
        uri=prop_uri,
        identifier=object_value(graph, prop_ref, DCTERMS.identifier),
        propertyTypes=value_set(graph, prop_ref, RDF.type),
        title=value_translations(graph, prop_ref, DCTERMS.title),
        description=value_translations(graph, prop_ref, DCTERMS.description),
        subject=object_value(graph, prop_ref, DCTERMS.subject),
        minOccurs=object_value(graph, prop_ref, XSD.minOccurs),
        maxOccurs=object_value(graph, prop_ref, XSD.maxOccurs),
        relationPropertyLabel=value_translations(
            graph, prop_ref, model_dcat_ap_no_uri("relationPropertyLabel")
        ),
        sequenceNumber=object_value(
            graph, prop_ref, model_dcat_ap_no_uri("sequenceNumber")
        ),
        belongsToModule=object_value(
            graph, prop_ref, model_dcat_ap_no_uri("belongsToModule")
        ),
        hasType=uri_or_identifier_list(graph, has_type_refs),
        formsSymmetryWith=uri_or_identifier(graph, symmetry_ref),
        hasDataType=uri_or_identifier(graph, data_type_ref),
        hasSimpleType=uri_or_identifier(graph, simple_type_ref),
        hasObjectType=uri_or_identifier(graph, object_type_ref),
        hasValueFrom=uri_or_identifier(graph, value_from_ref),
        isAbstractionOf=uri_or_identifier(graph, abstraction_ref),
        refersTo=uri_or_identifier(graph, refers_to_ref),
        hasSome=uri_or_identifier_list(graph, has_some_refs),
        hasMember=uri_or_identifier(graph, member_ref),
        contains=uri_or_identifier(graph, contains_ref),
        hasSupplier=uri_or_identifier(graph, supplier_ref),
        hasGeneralConcept=uri_or_identifier(graph, general_concept_ref),
        notification=value_translations(
            graph, prop_ref, model_dcat_ap_no_uri("notification")
        ),
    )
