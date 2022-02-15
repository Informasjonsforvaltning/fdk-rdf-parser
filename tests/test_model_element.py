from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import InformationModel
from fdk_rdf_parser.classes.model_element import ModelElement
from fdk_rdf_parser.parse_functions.model_element import parse_model_element


def test_handles_missing_type() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:NoType
        dct:identifier                "NoType"^^xsd:string ;
        dct:title                      "No type"@en ."""

    expected = ModelElement(
        uri="https://testdirektoratet.no/model#NoType",
        identifier="NoType",
        title={"en": "No type"},
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model#NoType")

    assert parse_model_element(graph, subject) == expected


def test_parse_text_simple_type() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:SomeTextType
        a                            modelldcatno:SimpleType , owl:NamedIndividual ;
        modelldcatno:subject     "http://data.brreg.no/begrep/28155"^^xsd:anyURI ;
        dct:identifier                "SomeTextType"^^xsd:string ;
        dct:title                      "Some text"@en ;
        modelldcatno:typeDefinitionReference      "http://www.w3.org/2001/XMLSchema#string"^^xsd:anyURI ;
        xsd:length                   "9"^^xsd:nonNegativeInteger ;
        xsd:maxLength                   "9"^^xsd:nonNegativeInteger ;
        xsd:minLength                   "9"^^xsd:nonNegativeInteger ;
        xsd:pattern                  "[0-9]+"^^xsd:string ."""

    expected = ModelElement(
        uri="https://testdirektoratet.no/model#SomeTextType",
        identifier="SomeTextType",
        title={"en": "Some text"},
        elementTypes={
            "http://www.w3.org/2002/07/owl#NamedIndividual",
            "https://data.norge.no/vocabulary/modelldcatno#SimpleType",
        },
        typeDefinitionReference="http://www.w3.org/2001/XMLSchema#string",
        length=9,
        maxLength=9,
        minLength=9,
        pattern="[0-9]+",
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model#SomeTextType")

    assert parse_model_element(graph, subject) == expected


def test_subject_added_to_infomodel_contains_subjects() -> None:
    element = ModelElement(
        uri="https://example.com/element", subject="https://example.com/subject"
    )
    expected = InformationModel(
        containsSubjects={"https://example.com/subject"},
        modelElements={"https://example.com/element": element},
    )

    infomodel = InformationModel()
    infomodel.add_model_element(element)

    assert infomodel == expected
