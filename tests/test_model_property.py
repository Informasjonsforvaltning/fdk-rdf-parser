from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import InformationModel
from fdk_rdf_parser.classes.model_property import ModelProperty
from fdk_rdf_parser.parse_functions.model_property import parse_model_property


def test_handles_missing_type() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:noType
        dct:identifier                "noType"^^xsd:string ;
        dct:title           "No type"@en ."""

    expected = ModelProperty(
        uri="https://testdirektoratet.no/model#noType",
        identifier="noType",
        title={"en": "No type"},
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model#noType")

    assert parse_model_property(graph, subject) == expected


def test_parse_property_type_note() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:farge a            owl:NamedIndividual ,
                                modelldcatno:Attribute ,
                                modelldcatno:Note ;
         dct:identifier                "farge"^^xsd:string ;
         modelldcatno:hasSimpleType   testdir:groenn ;
         modelldcatno:notification  "Fargen gjelder rammen (en note tekst)"@nb, "Fargen gjeld ramma (ein notetekst)"@nn , "The color applies to the frame (a note text)"@en .

    testdir:groenn a           owl:NamedIndividual ,
                                      modelldcatno:SimpleType ;
            dct:identifier                "groenn"^^xsd:string ;
            dct:title              "Grønn"@nb , "Grøn"@nn , "Green"@en ."""

    expected = ModelProperty(
        uri="https://testdirektoratet.no/model#farge",
        identifier="farge",
        notification={
            "nn": "Fargen gjeld ramma (ein notetekst)",
            "nb": "Fargen gjelder rammen (en note tekst)",
            "en": "The color applies to the frame (a note text)",
        },
        propertyTypes={
            "http://www.w3.org/2002/07/owl#NamedIndividual",
            "https://data.norge.no/vocabulary/modelldcatno#Attribute",
            "https://data.norge.no/vocabulary/modelldcatno#Note",
        },
        hasSimpleType="https://testdirektoratet.no/model#groenn",
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model#farge")

    assert parse_model_property(graph, subject) == expected


def test_parse_property_type_abstraction() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:lapp a           owl:NamedIndividual ,
                              modelldcatno:Note ;
        dct:identifier                "http://example.com/test_note#lapp"^^xsd:string ;
        dct:title           "Bemerk!"@nb , "Notice"@en , "Merk"@nn ."""

    expected = ModelProperty(
        uri="https://testdirektoratet.no/model#lapp",
        identifier="http://example.com/test_note#lapp",
        title={"nn": "Merk", "nb": "Bemerk!", "en": "Notice"},
        propertyTypes={
            "http://www.w3.org/2002/07/owl#NamedIndividual",
            "https://data.norge.no/vocabulary/modelldcatno#Note",
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model#lapp")

    assert parse_model_property(graph, subject) == expected


def test_parse_has_data_type() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:gyldighetsperiode
        a                         owl:NamedIndividual , modelldcatno:Role ;
        modelldcatno:hasDataType  testdir:Periode ."""

    expected = ModelProperty(
        uri="https://testdirektoratet.no/model#gyldighetsperiode",
        hasDataType="https://testdirektoratet.no/model#Periode",
        propertyTypes={
            "http://www.w3.org/2002/07/owl#NamedIndividual",
            "https://data.norge.no/vocabulary/modelldcatno#Role",
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model#gyldighetsperiode")

    assert parse_model_property(graph, subject) == expected


def test_parse_has_value_from_bnode() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:sivilstand  a                 owl:NamedIndividual , modelldcatno:Attribute ;
        modelldcatno:hasValueFrom    [ a  owl:NamedIndividual , modelldcatno:CodeList ;
                                       dct:identifier    "Sivilstand" ] ."""

    expected = ModelProperty(
        uri="https://testdirektoratet.no/model#sivilstand",
        hasValueFrom="Sivilstand",
        propertyTypes={
            "http://www.w3.org/2002/07/owl#NamedIndividual",
            "https://data.norge.no/vocabulary/modelldcatno#Attribute",
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model#sivilstand")

    assert parse_model_property(graph, subject) == expected


def test_has_value_from_not_added_when_bnode_and_missing_identifier() -> None:
    src = """
    @prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix testdir: <https://testdirektoratet.no/model#> .

    testdir:sivilstand  a                 owl:NamedIndividual , modelldcatno:Attribute ;
        modelldcatno:hasValueFrom    [ a  owl:NamedIndividual , modelldcatno:CodeList ;
                                       dct:title    "Sivilstand"@nb ] ."""

    expected = ModelProperty(
        uri="https://testdirektoratet.no/model#sivilstand",
        propertyTypes={
            "http://www.w3.org/2002/07/owl#NamedIndividual",
            "https://data.norge.no/vocabulary/modelldcatno#Attribute",
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u"https://testdirektoratet.no/model#sivilstand")

    assert parse_model_property(graph, subject) == expected


def test_subject_added_to_infomodel_contains_subjects() -> None:
    prop = ModelProperty(
        uri="https://example.com/element", subject="https://example.com/subject"
    )
    expected = InformationModel(
        containsSubjects={"https://example.com/subject"},
        modelProperties={"https://example.com/element": prop},
    )

    infomodel = InformationModel()
    infomodel.add_model_property(prop)

    assert infomodel == expected
