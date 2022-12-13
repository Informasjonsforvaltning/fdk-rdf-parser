from typing import List

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
    OWL,
)

from fdk_rdf_parser.classes import InformationModel
from fdk_rdf_parser.rdf_utils import (
    adms_uri,
    model_dcat_ap_no_uri,
    object_value,
    prof_uri,
    resource_list,
    uri_or_identifier,
    uri_or_identifier_list,
    value_set,
    value_translations,
)
from .catalog import parse_catalog
from .dcat_resource import parse_dcat_resource
from .dct_standard import extract_dct_standard_list
from .format import extract_formats
from .harvest_meta_data import extract_meta_data
from .model_element import parse_model_element
from .model_property import parse_model_property
from .skos_code import extract_skos_code_list
from .temporal import extract_temporal


def parse_information_model(
    graph: Graph, fdk_record_uri: URIRef, info_model_uri: URIRef
) -> InformationModel:

    subjects = value_set(graph, info_model_uri, DCTERMS.subject)
    model_element_refs = resource_list(
        graph, info_model_uri, model_dcat_ap_no_uri("containsModelElement")
    )

    info_model = InformationModel(
        id=object_value(graph, fdk_record_uri, DCTERMS.identifier),
        harvest=extract_meta_data(graph, fdk_record_uri),
        catalog=parse_catalog(graph, fdk_record_uri),
        conformsTo=extract_dct_standard_list(graph, info_model_uri, DCTERMS.conformsTo),
        license=extract_skos_code_list(graph, info_model_uri, DCTERMS.license),
        informationModelIdentifier=object_value(
            graph, info_model_uri, model_dcat_ap_no_uri("informationModelIdentifier")
        ),
        spatial=extract_skos_code_list(graph, info_model_uri, DCTERMS.spatial),
        temporal=extract_temporal(graph, info_model_uri),
        isPartOf=object_value(graph, info_model_uri, DCTERMS.isPartOf),
        hasPart=object_value(graph, info_model_uri, DCTERMS.hasPart),
        isReplacedBy=object_value(graph, info_model_uri, DCTERMS.isReplacedBy),
        isProfileOf=extract_dct_standard_list(
            graph, info_model_uri, prof_uri("isProfileOf")
        ),
        replaces=object_value(graph, info_model_uri, DCTERMS.replaces),
        hasFormat=extract_formats(graph, info_model_uri),
        homepage=object_value(graph, info_model_uri, FOAF.homepage),
        status=object_value(graph, info_model_uri, adms_uri("status")),
        versionInfo=object_value(graph, info_model_uri, OWL.versionInfo),
        versionNotes=value_translations(
            graph, info_model_uri, adms_uri("versionNotes")
        ),
        subjects=subjects,
        containsSubjects=subjects.copy() if subjects else None,
        containsModelElements=uri_or_identifier_list(graph, model_element_refs),
    )

    info_model.add_values_from_dcat_resource(
        parse_dcat_resource(
            graph,
            info_model_uri,
        )
    )

    return add_elements_to_model(info_model, graph, model_element_refs)


def add_elements_to_model(
    info_model: InformationModel, graph: Graph, element_refs: List[URIRef]
) -> InformationModel:
    for element_ref in element_refs:

        element_id_optional = uri_or_identifier(graph, element_ref)
        if element_id_optional:
            element_id = str(element_id_optional)
            if (
                info_model.modelElements is None
                or info_model.modelElements.get(element_id) is None
            ):
                info_model.add_model_element(parse_model_element(graph, element_ref))

                has_property_refs = resource_list(
                    graph, element_ref, model_dcat_ap_no_uri("hasProperty")
                )
                info_model = add_properties_to_model(
                    info_model, graph, has_property_refs
                )

    return info_model


def add_properties_to_model(
    info_model: InformationModel, graph: Graph, prop_refs: List[URIRef]
) -> InformationModel:
    for prop_ref in prop_refs:

        prop_id_optional = uri_or_identifier(graph, prop_ref)
        if prop_id_optional:
            prop_id = str(prop_id_optional)
            if (
                info_model.modelProperties is None
                or info_model.modelProperties.get(prop_id) is None
            ):
                info_model.add_model_property(parse_model_property(graph, prop_ref))

                property_ref_predicates = [model_dcat_ap_no_uri("formsSymmetryWith")]

                for predicate in property_ref_predicates:
                    property_refs = resource_list(graph, prop_ref, predicate)
                    info_model = add_properties_to_model(
                        info_model, graph, property_refs
                    )

                element_ref_predicates = [
                    model_dcat_ap_no_uri("hasType"),
                    model_dcat_ap_no_uri("isAbstractionOf"),
                    model_dcat_ap_no_uri("refersTo"),
                    model_dcat_ap_no_uri("hasDataType"),
                    model_dcat_ap_no_uri("hasSimpleType"),
                    model_dcat_ap_no_uri("hasObjectType"),
                    model_dcat_ap_no_uri("hasValueFrom"),
                    model_dcat_ap_no_uri("hasSome"),
                    model_dcat_ap_no_uri("hasMember"),
                    model_dcat_ap_no_uri("contains"),
                    model_dcat_ap_no_uri("hasSupplier"),
                    model_dcat_ap_no_uri("hasGeneralConcept"),
                ]

                for predicate in element_ref_predicates:
                    element_refs = resource_list(graph, prop_ref, predicate)
                    info_model = add_elements_to_model(info_model, graph, element_refs)

    return info_model
