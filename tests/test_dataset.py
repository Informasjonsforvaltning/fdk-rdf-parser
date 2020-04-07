"""Test cases."""
import pytest

from fdk_rdf_parser import parseDatasets, Dataset, HarvestMetaData
import isodate

def test_rdf():

    src0 = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://testdirektoratet.no/model/dataset/0>
        a                         dcat:Dataset ;
        dct:accessRights          <http://publications.europa.eu/resource/authority/access-right/PUBLIC> ;
        dct:description           "Beskrivelse av datasett 0"@nb , "Description of dataset 0"@en ;
        dct:identifier            "adb4cf00-31c8-460c-9563-55f204cf8221" ;
        dct:title                 "Datasett 0"@nb , "Dataset 0"@en ;
        dcat:contactPoint         [ a                          vcard:Organization ;
                                    vcard:hasOrganizationName  "Testdirektoratet"@nb ;
                                    vcard:hasURL               <https://testdirektoratet.no>
                                  ] ;
        dcat:endpointDescription  <https://testdirektoratet.no/openapi/dataset/0.yaml> ;
        dct:issued                "2019-03-22T13:11:16.546902"^^xsd:dateTime ;
        dct:language              <http://publications.europa.eu/resource/authority/language/NOR> ;
        dct:temporal              [ a                          dct:PeriodOfTime ;
                                    dcat:startDate           "2019-04-02T00:00:00"^^xsd:dateTime ] ;
        dcat:distribution         <https://testdirektoratet.no/model/distribution/0> ;
        dcat:keyword              "test", "fest" ;
        dcat:theme                <http://publications.europa.eu/resource/authority/data-theme/GOVE>,
                                  <http://publications.europa.eu/resource/authority/data-theme/TECH> ;
        foaf:page                 <https://testdirektoratet.no> .

<https://datasets.fellesdatakatalog.digdir.no/datasets/4667277a-9d27-32c1-aed5-612fa601f393>
        a                  dcat:record ;
        dct:identifier     "4667277a-9d27-32c1-aed5-612fa601f393" ;
        dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
        dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
        dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/1> .

<https://testdirektoratet.no/model/dataset/1>
        a                         dcat:Dataset ;
        dct:description           "Beskrivelse av datasett 1"@nb , "Description of dataset 1"@en ;
        dct:title                 "Datasett 1"@nb , "Dataset 1"@en ;
        dcat:contactPoint         [ a                          vcard:Organization ;
                                    vcard:hasOrganizationName  "Testdirektoratet"@nb ;
                                    vcard:hasURL               <https://testdirektoratet.no>
                                  ] ;
        dct:temporal              [ a                          dct:PeriodOfTime ;
                                    dcat:startDate           "2019-04-02T00:00:00"^^xsd:dateTime ] ;
        dcat:distribution         <https://testdirektoratet.no/model/distribution/1>, <https://testdirektoratet.no/model/distribution/2> ;
        dcat:endpointDescription  <https://testdirektoratet.no/openapi/dataset/1.yaml> .

<https://datasets.fellesdatakatalog.digdir.no/datasets/a1c680ca-62d7-34d5-aa4c-d39b5db033ae>
        a                  dcat:record ;
        dct:identifier     "a1c680ca-62d7-34d5-aa4c-d39b5db033ae" ;
        dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
        dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
        dct:modified       "2020-03-12T11:52:16.123Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://testdirektoratet.no/model/dataset/0> ."""

    expected = {
        'https://testdirektoratet.no/model/dataset/0': Dataset(
            id='a1c680ca-62d7-34d5-aa4c-d39b5db033ae',
            harvest=HarvestMetaData(
                firstHarvested=isodate.parse_datetime("2020-03-12T11:52:16.122Z"),
                changed=[isodate.parse_datetime("2020-03-12T11:52:16.122Z"), isodate.parse_datetime("2020-03-12T11:52:16.123Z")]),
            title={'nb':'Datasett 0','en':"Dataset 0"},
            description={'nb':'Beskrivelse av datasett 0','en':"Description of dataset 0"}
        ), 
        'https://testdirektoratet.no/model/dataset/1': Dataset(
            id='4667277a-9d27-32c1-aed5-612fa601f393',
            harvest=HarvestMetaData(
                firstHarvested=isodate.parse_datetime("2020-03-12T11:52:16.122Z"),
                changed=[isodate.parse_datetime("2020-03-12T11:52:16.122Z"), isodate.parse_datetime("2020-03-12T11:52:16.123Z")]),
            title={'nb':'Datasett 1','en':"Dataset 1"},
            description={'nb':'Beskrivelse av datasett 1','en':"Description of dataset 1"}
        )
    }


    assert parseDatasets(src0) == expected
