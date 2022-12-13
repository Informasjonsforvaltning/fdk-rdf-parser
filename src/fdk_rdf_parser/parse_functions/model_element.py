from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDF,
    SKOS,
    XSD,
)

from fdk_rdf_parser.classes.model_element import (
    ModelCodeElement,
    ModelElement,
)
from fdk_rdf_parser.rdf_utils import (
    model_dcat_ap_no_uri,
    object_value,
    resource_list,
    uri_or_identifier_list,
    value_set,
    value_translations,
    xkos_uri,
)

CODE_LIST = model_dcat_ap_no_uri("CodeList").toPython()
SIMPLE_TYPE = model_dcat_ap_no_uri("SimpleType").toPython()


def parse_model_element(graph: Graph, element_ref: URIRef) -> ModelElement:

    element_uri = None
    if isinstance(element_ref, URIRef):
        element_uri = element_ref.toPython()

    has_property_refs = resource_list(
        graph, element_ref, model_dcat_ap_no_uri("hasProperty")
    )

    element = ModelElement(
        uri=element_uri,
        identifier=object_value(graph, element_ref, DCTERMS.identifier),
        elementTypes=value_set(graph, element_ref, RDF.type),
        title=value_translations(graph, element_ref, DCTERMS.title),
        description=value_translations(graph, element_ref, DCTERMS.description),
        subject=object_value(graph, element_ref, DCTERMS.subject),
        belongsToModule=object_value(
            graph, element_ref, model_dcat_ap_no_uri("belongsToModule")
        ),
        hasProperty=uri_or_identifier_list(graph, has_property_refs),
    )

    if element.elementTypes is None:
        return element

    if CODE_LIST in element.elementTypes:
        return parse_model_code_list(graph, element_ref, element)
    elif SIMPLE_TYPE in element.elementTypes:
        return parse_model_simple_type(graph, element_ref, element)
    else:
        return element


def parse_model_code_list(
    graph: Graph, element_ref: URIRef, element: ModelElement
) -> ModelElement:
    codes = []
    for code_ref in graph.subjects(SKOS.inScheme, element_ref):
        codes.append(
            ModelCodeElement(
                uri=code_ref.toPython() if isinstance(code_ref, URIRef) else None,
                identifier=object_value(graph, code_ref, DCTERMS.identifier),
                prefLabel=value_translations(graph, code_ref, SKOS.prefLabel),
                inScheme=value_set(graph, code_ref, SKOS.inScheme),
                subject=object_value(graph, code_ref, DCTERMS.subject),
                notation=object_value(graph, code_ref, SKOS.notation),
                topConceptOf=value_set(graph, code_ref, SKOS.topConceptOf),
                definition=value_set(graph, code_ref, SKOS.definition),
                example=value_set(graph, code_ref, SKOS.example),
                exclusionNote=value_translations(
                    graph, code_ref, xkos_uri("exclusionNote")
                ),
                previousElement=value_set(graph, code_ref, xkos_uri("previous")),
                hiddenLabel=value_translations(graph, code_ref, SKOS.hiddenLabel),
                inclusionNote=value_translations(
                    graph, code_ref, xkos_uri("inclusionNote")
                ),
                note=value_translations(graph, code_ref, SKOS.note),
                nextElement=value_set(graph, code_ref, xkos_uri("next")),
                scopeNote=value_translations(graph, code_ref, SKOS.scopeNote),
                altLabel=value_translations(graph, code_ref, SKOS.altLabel),
            )
        )
    codes.sort()

    element.codeListReference = object_value(
        graph, element_ref, model_dcat_ap_no_uri("codeListReference")
    )
    element.codes = codes

    return element


def parse_model_simple_type(
    graph: Graph, element_ref: URIRef, element: ModelElement
) -> ModelElement:

    element.typeDefinitionReference = object_value(
        graph, element_ref, model_dcat_ap_no_uri("typeDefinitionReference")
    )
    element.fractionDigits = object_value(graph, element_ref, XSD.fractionDigits)
    element.length = object_value(graph, element_ref, XSD.length)
    element.maxInclusive = object_value(graph, element_ref, XSD.maxInclusive)
    element.maxLength = object_value(graph, element_ref, XSD.maxLength)
    element.minInclusive = object_value(graph, element_ref, XSD.minInclusive)
    element.minLength = object_value(graph, element_ref, XSD.minLength)
    element.pattern = object_value(graph, element_ref, XSD.pattern)
    element.totalDigits = object_value(graph, element_ref, XSD.totalDigits)

    return element
