import logging
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
    DatasetSeries,
    InSeries,
    PartialDataset,
    SkosConcept,
)
from fdk_rdf_parser.rdf_utils import (
    adms_uri,
    cpsv_uri,
    dcat_ap_no_uri,
    dcat_uri,
    dqv_iso_uri,
    fdk_uri,
    object_value,
    prov_uri,
    resource_list,
    value_list,
    value_set,
    value_translations,
)
from .catalog import parse_catalog
from .conforms_to import extract_conforms_to
from .dcat_resource import parse_dcat_resource
from .distribution import extract_distributions
from .harvest_meta_data import extract_meta_data
from .qualified_attribution import extract_qualified_attributions
from .quality_annotation import extract_quality_annotation
from .reference_data_code import (
    extract_reference_data_code,
    extract_reference_data_code_list,
)
from .references import extract_references
from .skos_concept import extract_skos_concept
from .subject import extract_subjects
from .temporal import extract_temporal


def parse_dataset(
    datasets_graph: Graph, record_uri: URIRef, dataset_uri: URIRef
) -> PartialDataset:
    quality_annotations = extract_quality_annotation(datasets_graph, dataset_uri)
    cpsv_follows = extract_legal_basis_from_cpsv_follows(datasets_graph, dataset_uri)
    dataset_series_uri = object_value(datasets_graph, dataset_uri, dcat_uri("inSeries"))

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
        spatial=extract_reference_data_code_list(
            datasets_graph, dataset_uri, DCTERMS.spatial
        ),
        source=object_value(datasets_graph, dataset_uri, dcat_ap_no_uri("source")),
        objective=value_translations(
            datasets_graph, dataset_uri, dcat_ap_no_uri("objective")
        ),
        page=value_set(datasets_graph, dataset_uri, FOAF.page),
        temporal=extract_temporal(datasets_graph, dataset_uri),
        subject=extract_subjects(datasets_graph, dataset_uri),
        provenance=extract_reference_data_code(
            datasets_graph, dataset_uri, DCTERMS.provenance
        ),
        accrualPeriodicity=extract_reference_data_code(
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
        legalBasisForRestriction=cpsv_follows["restriction"]
        if len(cpsv_follows["restriction"]) > 0
        else extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("legalBasisForRestriction")
        ),
        legalBasisForProcessing=cpsv_follows["processing"]
        if len(cpsv_follows["processing"]) > 0
        else extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("legalBasisForProcessing")
        ),
        legalBasisForAccess=cpsv_follows["access"]
        if len(cpsv_follows["access"]) > 0
        else extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("legalBasisForAccess")
        ),
        conformsTo=extract_conforms_to(datasets_graph, dataset_uri),
        informationModel=extract_skos_concept(
            datasets_graph, dataset_uri, dcat_ap_no_uri("informationModel")
        ),
        references=extract_references(datasets_graph, dataset_uri),
        qualifiedAttributions=extract_qualified_attributions(
            datasets_graph, dataset_uri, prov_uri("qualifiedAttribution")
        ),
        catalog=parse_catalog(datasets_graph, record_uri),
        isOpenData=extract_boolean(datasets_graph, dataset_uri, fdk_uri("isOpenData")),
        isAuthoritative=extract_boolean(
            datasets_graph, dataset_uri, fdk_uri("isAuthoritative")
        ),
        isRelatedToTransportportal=extract_boolean(
            datasets_graph, dataset_uri, fdk_uri("isRelatedToTransportportal")
        ),
        inSeries=extract_series_info(datasets_graph, URIRef(dataset_series_uri))
        if dataset_series_uri
        else None,
        prev=object_value(datasets_graph, dataset_uri, dcat_uri("prev")),
    )

    dataset.add_values_from_dcat_resource(
        parse_dcat_resource(
            graph=datasets_graph,
            subject=dataset_uri,
        )
    )

    return dataset


def parse_dataset_series(datasets_graph: Graph, dataset_uri: URIRef) -> DatasetSeries:
    prev_dataset_uri = object_value(datasets_graph, dataset_uri, dcat_uri("last"))
    return DatasetSeries(
        last=prev_dataset_uri,
        datasetsInSeries=extract_datasets_in_series(
            datasets_graph, dataset_uri.toPython(), prev_dataset_uri
        )
        if prev_dataset_uri
        else None,
    )


def extract_datasets_in_series(
    datasets_graph: Graph, dataset_series_uri: str, last_dataset_uri: str
) -> List[str]:
    datasets_in_series: List[str] = [last_dataset_uri]
    cur_dataset_uri: Optional[str] = last_dataset_uri

    while prev_dataset_uri := object_value(
        datasets_graph, URIRef(str(cur_dataset_uri)), dcat_uri("prev")
    ):
        # Check for circular graphs
        if prev_dataset_uri in datasets_in_series:
            logging.warning(
                f"Circular linking in dataset series {dataset_series_uri}, on dataset {cur_dataset_uri}. Aborting list traversal."
            )
            break
        datasets_in_series.append(prev_dataset_uri)
        cur_dataset_uri = prev_dataset_uri

    # Verify that all datasets in series are included
    number_of_datasets_in_series = len(
        list(
            datasets_graph.subjects(
                dcat_uri("inSeries"), URIRef(dataset_series_uri), unique=True
            )
        )
    )
    if len(datasets_in_series) != number_of_datasets_in_series:
        logging.warning(
            f"List of datasets in series {dataset_series_uri} is incomplete, linked list might be broken."
        )

    return datasets_in_series


def extract_series_info(datasets_graph: Graph, dataset_series_uri: URIRef) -> InSeries:
    series_title = value_translations(datasets_graph, dataset_series_uri, DCTERMS.title)
    catalog_record_of_series_uri = next(
        datasets_graph.subjects(FOAF.primaryTopic, dataset_series_uri), None
    )
    series_id = object_value(
        datasets_graph, catalog_record_of_series_uri, DCTERMS.identifier
    )
    return InSeries(uri=dataset_series_uri.toPython(), title=series_title, id=series_id)


def extract_boolean(
    datasets_graph: Graph, dataset_uri: URIRef, predicate: URIRef
) -> bool:
    value = object_value(datasets_graph, dataset_uri, predicate)
    return value if value and isinstance(value, bool) else False


def extract_legal_basis_from_cpsv_follows(
    datasets_graph: Graph, dataset_uri: URIRef
) -> Dict[str, List[SkosConcept]]:
    legal_basis_for: Dict[str, List[SkosConcept]] = {
        "restriction": [],
        "processing": [],
        "access": [],
    }

    for legal_resource in resource_list(
        datasets_graph, dataset_uri, cpsv_uri("follows")
    ):
        rule_type = object_value(datasets_graph, legal_resource, DCTERMS.type)
        implements_ref = datasets_graph.value(legal_resource, cpsv_uri("implements"))
        if rule_type and implements_ref:
            legal_type_ref = datasets_graph.value(implements_ref, DCTERMS.type)
            skos_concept = SkosConcept(
                uri=object_value(datasets_graph, implements_ref, RDFS.seeAlso),
                extraType=rule_type,
                prefLabel=value_translations(
                    datasets_graph, legal_type_ref, SKOS.prefLabel
                )
                if legal_type_ref
                else None,
            )

            if "ruleForNonDisclosure" in rule_type:
                legal_basis_for["restriction"].append(skos_concept)
            elif "ruleForDataProcessing" in rule_type:
                legal_basis_for["processing"].append(skos_concept)
            elif "ruleForDisclosure" in rule_type:
                legal_basis_for["access"].append(skos_concept)

    return legal_basis_for
