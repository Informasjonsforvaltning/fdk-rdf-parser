import pytest
from unittest.mock import Mock

from fdk_rdf_parser.classes.exceptions import (
    MissingResourceError,
    MultipleResourcesError,
    ParserError,
)
from fdk_rdf_parser.fdk_rdf_parser import parse_concept, parse_concept_as_dict


def test_parse_concept_missing_resource_raises_exception(
    mock_reference_data_client: Mock,
) -> None:
    src = """
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
    @prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix dcat:  <http://www.w3.org/ns/dcat#> .
    @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

    <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028>
            a               skos:Collection ;
            rdfs:label      "Concept collection belonging to 910258028" ;
            dct:identifier  "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028" ;
            dct:publisher   <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
            skos:member     <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0> .

    <https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f>
            a                  dcat:CatalogRecord ;
            dct:identifier     "55a38009-e114-301f-aa7c-8b5f09529f0f" ;
            dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
            dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
            dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
            foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0> .

    <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662>
            a                  dcat:CatalogRecord ;
            dct:identifier     "5e08611a-4e94-3d8f-9d9f-d3a292ec1662" ;
            dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
            dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
            foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ."""

    with pytest.raises(MissingResourceError):
        parse_concept(src)
    with pytest.raises(MissingResourceError):
        parse_concept_as_dict(src)


def test_parse_concept_multiple_resources_raises_exception(
    mock_reference_data_client: Mock,
) -> None:
    src = """
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
        @prefix dct:   <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix uneskos: <http://purl.org/umu/uneskos#> .

        <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028>
                a               skos:Collection ;
                dct:identifier  "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028" ;
                dct:publisher   <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
                skos:member     <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190> ,
                                <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0> ;
                .

        <https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f>
                a                  dcat:CatalogRecord ;
                dct:identifier     "55a38009-e114-301f-aa7c-8b5f09529f0f" ;
                dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
                foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0> ;
                .

        <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0>
                a                   skos:Concept ;
                dct:identifier      "1843b048-f9af-4665-8e53-3c001d0166c0" ;
                uneskos:memberOf    <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ;
                .

        <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190>
                a                  skos:Concept ;
                dct:identifier     "3609b02d-72c5-47e0-a6b8-df0a503cf190" ;
                .

        <https://concepts.staging.fellesdatakatalog.digdir.no/concepts/fc8baf8d-6146-3b69-93c5-52bd41592c4e>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fc8baf8d-6146-3b69-93c5-52bd41592c4e" ;
                dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
                foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190> ;
                .

        <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662>
                a                  dcat:CatalogRecord ;
                dct:identifier     "5e08611a-4e94-3d8f-9d9f-d3a292ec1662" ;
                dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
                dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ;
                .
    """

    with pytest.raises(MultipleResourcesError):
        parse_concept(src)
    with pytest.raises(MultipleResourcesError):
        parse_concept_as_dict(src)


def test_parse_invalid_rdf_raises_parse_error(
    mock_reference_data_client: Mock,
) -> None:
    bad_turtle = """
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

        <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662>
                a                  dcat:CatalogRecord ;
    """

    with pytest.raises(ParserError):
        parse_concept(bad_turtle)
