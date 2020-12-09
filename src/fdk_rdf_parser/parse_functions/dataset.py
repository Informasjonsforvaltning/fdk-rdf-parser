from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import PartialDataset
from fdk_rdf_parser.rdf_utils import (
    adms_uri,
    catalog_ref,
    dcat_ap_no_uri,
    dcat_uri,
    dqv_iso_uri,
    object_value,
    prov_uri,
    value_list,
    value_set,
    value_translations,
)
from .catalog import parse_catalog
from .dcat_resource import parse_dcat_resource
from .distribution import extract_distributions
from .harvest_meta_data import extract_meta_data
from .qualified_attribution import extract_qualified_attributions
from .quality_annotation import extract_quality_annotation
from .references import extract_references
from .skos_code import extract_skos_code, extract_skos_code_list
from .skos_concept import extract_skos_concept
from .subject import extract_subjects
from .temporal import extract_temporal


def parse_dataset(
    datasets_graph: Graph, record_uri: URIRef, dataset_uri: URIRef
) -> PartialDataset:
    quality_annotations = extract_quality_annotation(datasets_graph, dataset_uri)

    dataset = PartialDataset(
        id=object_value(datasets_graph, record_uri, DCTERMS.identifier),
        admsIdentifier=value_set(datasets_graph, dataset_uri, adms_uri("identifier")),
        harvest=extract_meta_data(datasets_graph, record_uri),
        accessRightsComment=value_list(
            datasets_graph, dataset_uri, dcat_ap_no_uri("accessRightsComment")
        ),
        distribution=extract_distributions(
            datasets_graph, dataset_uri, dcat_uri("distribution")
        ),
        sample=extract_distributions(datasets_graph, dataset_uri, adms_uri("sample")),
        spatial=extract_skos_code_list(datasets_graph, dataset_uri, DCTERMS.spatial),
        source=object_value(datasets_graph, dataset_uri, dcat_ap_no_uri("source")),
        objective=value_translations(
            datasets_graph, dataset_uri, dcat_ap_no_uri("objective")
        ),
        page=value_set(datasets_graph, dataset_uri, FOAF.page),
        temporal=extract_temporal(datasets_graph, dataset_uri),
        subject=extract_subjects(datasets_graph, dataset_uri),
        provenance=extract_skos_code(datasets_graph, dataset_uri, DCTERMS.provenance),
        accrualPeriodicity=extract_skos_code(
            datasets_graph, dataset_uri, DCTERMS.accrualPeriodicity
        ),
        hasAccuracyAnnotation=quality_annotations.get(
            dqv_iso_uri("Accuracy").toPython()
        ),
        hasCompletenessAnnotation=quality_annotations.get(
            dqv_iso_uri("Completeness").toPython()
        ),
        hasCurrentnessAnnotation=quality_annotations.get(
            dqv_iso_uri("Currentness").toPython()
        ),
        hasAvailabilityAnnotation=quality_annotations.get(
            dqv_iso_uri("Availability").toPython()
        ),
        hasRelevanceAnnotation=quality_annotations.get(
            dqv_iso_uri("Relevance").toPython()
        ),
        legalBasisForRestriction=extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("legalBasisForRestriction")
        ),
        legalBasisForProcessing=extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("legalBasisForProcessing")
        ),
        legalBasisForAccess=extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("legalBasisForAccess")
        ),
        conformsTo=extract_skos_concept(
            datasets_graph, dataset_uri, DCTERMS.conformsTo
        ),
        informationModel=extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("informationModel")
        ),
        references=extract_references(datasets_graph, dataset_uri),
        qualifiedAttributions=extract_qualified_attributions(
            datasets_graph, dataset_uri, prov_uri("qualifiedAttribution")
        ),
        catalog=parse_catalog(datasets_graph, record_uri),
    )

    dataset.add_values_from_dcat_resource(
        parse_dcat_resource(
            graph=datasets_graph,
            subject=dataset_uri,
            catalog_subject=catalog_ref(datasets_graph, record_uri),
        )
    )

    return dataset
