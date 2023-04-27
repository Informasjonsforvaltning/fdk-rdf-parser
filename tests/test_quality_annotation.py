from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import QualityAnnotation
from fdk_rdf_parser.parse_functions import extract_quality_annotation
from fdk_rdf_parser.rdf_utils import dqv_iso_uri


def test_quality_annotations() -> None:
    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dqv:   <http://www.w3.org/ns/dqv#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix oa:    <http://www.w3.org/ns/oa#> .

        <https://testdirektoratet.no/model/dataset/quality>
                a                   dcat:Dataset ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Currentness> ;
                    oa:hasBody     [] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Availability> ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "availability" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Accuracy> ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "Accuracy" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Relevance> ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "relevans" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/NNO> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension
                        <http://iso.org/25012/2008/dataquality/Completeness> ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ] ."""

    expected = {
        "http://iso.org/25012/2008/dataquality/Currentness": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Currentness"
        ),
        "http://iso.org/25012/2008/dataquality/Availability": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Availability",
            hasBody={"en": "availability"},
        ),
        "http://iso.org/25012/2008/dataquality/Accuracy": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Accuracy",
            hasBody={"en": "Accuracy"},
        ),
        "http://iso.org/25012/2008/dataquality/Relevance": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Relevance",
            hasBody={"nn": "relevans"},
        ),
        "http://iso.org/25012/2008/dataquality/Completeness": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Completeness"
        ),
    }

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/quality")

    assert extract_quality_annotation(graph, subject) == expected


def test_quality_annotations_with_prefix() -> None:
    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dqv:   <http://www.w3.org/ns/dqv#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix oa:    <http://www.w3.org/ns/oa#> .
        @prefix iso:   <http://iso.org/25012/2008/dataquality/> .

        <https://testdirektoratet.no/model/dataset/quality>
                a                   dcat:Dataset ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Currentness ;
                    oa:hasBody     [] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Availability ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "availability" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Accuracy ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "Accuracy" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Relevance ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "relevans" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/NOB> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Completeness ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ] ."""

    expected = {
        "http://iso.org/25012/2008/dataquality/Currentness": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Currentness"
        ),
        "http://iso.org/25012/2008/dataquality/Availability": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Availability",
            hasBody={"en": "availability"},
        ),
        "http://iso.org/25012/2008/dataquality/Accuracy": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Accuracy",
            hasBody={"en": "Accuracy"},
        ),
        "http://iso.org/25012/2008/dataquality/Relevance": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Relevance",
            hasBody={"nb": "relevans"},
        ),
        "http://iso.org/25012/2008/dataquality/Completeness": QualityAnnotation(
            inDimension="http://iso.org/25012/2008/dataquality/Completeness"
        ),
    }

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/quality")

    annotations = extract_quality_annotation(graph, subject)
    assert annotations == expected


def test_has_annotation() -> None:
    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dqv:   <http://www.w3.org/ns/dqv#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix oa:    <http://www.w3.org/ns/oa#> .
        @prefix iso:   <http://iso.org/25012/2008/dataquality/> .

        <https://testdirektoratet.no/model/dataset/quality>
                a                   dcat:Dataset ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Currentness ;
                    oa:hasBody     [] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Availability ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "availability" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Accuracy ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "Accuracy" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/ENG> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Relevance ;
                    oa:hasBody     [ a    oa:TextualBody ;
                        rdf:value  "relevans" ;
                        dct:language     <http://publications.europa.eu/resource/authority/language/NOB> ;
                        dct:format       <http://publications.europa.eu/resource/authority/file-type/TXT> ] ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension iso:Completeness ] ;
                dqv:hasQualityAnnotation  [
                    a                dqv:QualityAnnotation ] ."""

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef("https://testdirektoratet.no/model/dataset/quality")

    annotations = extract_quality_annotation(graph, subject)

    assert annotations.get(dqv_iso_uri("Availability").toPython()) == QualityAnnotation(
        hasBody={"en": "availability"},
        inDimension="http://iso.org/25012/2008/dataquality/Availability",
    )
