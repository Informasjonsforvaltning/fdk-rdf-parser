from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, RDF, XSD

from fdk_rdf_parser.classes.model_property import ModelProperty
from fdk_rdf_parser.rdf_utils import (
    identifier_list,
    model_dcat_ap_no_uri,
    object_value,
    resource_list,
    value_list,
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
        propertyTypes=value_list(graph, prop_ref, RDF.type),
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
        hasType=identifier_list(graph, has_type_refs),
        formsSymmetryWith=object_value(graph, symmetry_ref, DCTERMS.identifier),
        hasDataType=object_value(graph, data_type_ref, DCTERMS.identifier),
        hasSimpleType=object_value(graph, simple_type_ref, DCTERMS.identifier),
        hasObjectType=object_value(graph, object_type_ref, DCTERMS.identifier),
        hasValueFrom=object_value(graph, value_from_ref, DCTERMS.identifier),
        isAbstractionOf=object_value(graph, abstraction_ref, DCTERMS.identifier),
        refersTo=object_value(graph, refers_to_ref, DCTERMS.identifier),
        hasSome=identifier_list(graph, has_some_refs),
        hasMember=object_value(graph, member_ref, DCTERMS.identifier),
        contains=object_value(graph, contains_ref, DCTERMS.identifier),
        hasSupplier=object_value(graph, supplier_ref, DCTERMS.identifier),
        hasGeneralConcept=object_value(graph, general_concept_ref, DCTERMS.identifier),
        notification=value_translations(
            graph, prop_ref, model_dcat_ap_no_uri("notification")
        ),
    )
