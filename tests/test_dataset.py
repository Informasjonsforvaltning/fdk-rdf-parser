"""Test cases."""
import pytest

from fdk_rdf_parser.classes import Dataset, HarvestMetaData
from fdk_rdf_parser.parse_functions import parseDataset
from fdk_rdf_parser import parseDatasets
from rdflib import Graph, URIRef
import isodate

def test_parse_multiple_datasets():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/4667277a-9d27-32c1-aed5-612fa601f393>
                a                  dcat:record ;
                dct:identifier     "4667277a-9d27-32c1-aed5-612fa601f393" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/1> .

        <https://testdirektoratet.no/model/dataset/1>
                a                         dcat:Dataset .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca-62d7-34d5-aa4c-d39b5db033ae>
                a                  dcat:record ;
                dct:identifier     "a1c680ca-62d7-34d5-aa4c-d39b5db033ae" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/123>
                a                  dcat:record ;
                dct:identifier     "123" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ."""

    expected = {
        'https://testdirektoratet.no/model/dataset/0': Dataset(
            id='a1c680ca-62d7-34d5-aa4c-d39b5db033ae',
            harvest=HarvestMetaData(
                firstHarvested=isodate.parse_datetime("2020-03-12T11:52:16.122Z"),
                changed=[isodate.parse_datetime("2020-03-12T11:52:16.122Z"), isodate.parse_datetime("2020-03-12T11:52:16.123Z")]),
            uri='https://testdirektoratet.no/model/dataset/0',
        ), 
        'https://testdirektoratet.no/model/dataset/1': Dataset(
            id='4667277a-9d27-32c1-aed5-612fa601f393',
            harvest=HarvestMetaData(
                firstHarvested=isodate.parse_datetime("2020-03-12T11:52:16.122Z"),
                changed=[isodate.parse_datetime("2020-03-12T11:52:16.122Z"), isodate.parse_datetime("2020-03-12T11:52:16.123Z")]),
            uri='https://testdirektoratet.no/model/dataset/1'
        )
    }


    assert parseDatasets(src) == expected

def test_parse_dataset():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dct:accrualPeriodicity    <http://publications.europa.eu/resource/authority/frequency> ;
                dct:identifier            "adb4cf00-31c8-460c-9563-55f204cf8221" ;
                dct:publisher             <http://data.brreg.no/enhetsregisteret/enhet/987654321> ;
                dct:provenance            <http://data.brreg.no/datakatalog/provinens/tredjepart> ;
                dcat:endpointDescription  <https://testdirektoratet.no/openapi/dataset/0.yaml> ;
                dct:spatial               <https://data.geonorge.no/administrativeEnheter/fylke/id/173142> ;
                dct:subject               <https://testdirektoratet.no/model/concept/0> ,
                                          <https://testdirektoratet.no/model/concept/1> ;
                foaf:page                 <https://testdirektoratet.no> .

        <https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca-62d7-34d5-aa4c-d39b5db033ae>
                a                  dcat:record ;
                dct:identifier     "a1c680ca-62d7-34d5-aa4c-d39b5db033ae" ;
                dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
                dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> ."""

    expected = Dataset(
            id='a1c680ca-62d7-34d5-aa4c-d39b5db033ae',
            harvest=HarvestMetaData(
                firstHarvested=isodate.parse_datetime("2020-03-12T11:52:16.122Z"),
                changed=[isodate.parse_datetime("2020-03-12T11:52:16.122Z"), isodate.parse_datetime("2020-03-12T11:52:16.123Z")]),
            identifier=['adb4cf00-31c8-460c-9563-55f204cf8221'],
            uri='https://testdirektoratet.no/model/dataset/0',
            publisher='http://data.brreg.no/enhetsregisteret/enhet/987654321',
            page=['https://testdirektoratet.no'],
            subject=['https://testdirektoratet.no/model/concept/0','https://testdirektoratet.no/model/concept/1'],
            accrualPeriodicity='http://publications.europa.eu/resource/authority/frequency',
            provenance='http://data.brreg.no/datakatalog/provinens/tredjepart',
            spatial=['https://data.geonorge.no/administrativeEnheter/fylke/id/173142']
        )

    datasetsGraph = Graph().parse(data=src, format="turtle")
    datasetURI = URIRef(u'https://testdirektoratet.no/model/dataset/0')
    recordURI = URIRef(u'https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca-62d7-34d5-aa4c-d39b5db033ae')

    assert parseDataset(datasetsGraph, recordURI, datasetURI) == expected