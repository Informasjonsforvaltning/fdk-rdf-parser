"""Test cases."""
import pytest

from fdk_rdf_parser import parseDatasets, Dataset, HarvestMetaData, ContactPoint, Distribution, Temporal
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
        dct:accrualPeriodicity    <http://publications.europa.eu/resource/authority/frequency> ;
        dct:description           "Beskrivelse av datasett 0"@nb , "Description of dataset 0"@en ;
        dct:identifier            "adb4cf00-31c8-460c-9563-55f204cf8221" ;
        dct:publisher             <http://data.brreg.no/enhetsregisteret/enhet/987654321> ;
        dct:title                 "Datasett 0"@nb , "Dataset 0"@en ;
        dcat:endpointDescription  <https://testdirektoratet.no/openapi/dataset/0.yaml> ;
        dct:issued                "2019-03-22T13:11:16.546902"^^xsd:dateTime ;
        dct:language              <http://publications.europa.eu/resource/authority/language/NOR> ;
        dct:temporal              [ a                          dct:PeriodOfTime ;
                                    dcat:startDate           "2019-04-02T00:00:00"^^xsd:dateTime ] ;
        dcat:keyword              "test"@nb ;
        dcat:theme                <http://publications.europa.eu/resource/authority/data-theme/GOVE>,
                                  <http://publications.europa.eu/resource/authority/data-theme/TECH> ;
        dct:subject               <https://testdirektoratet.no/model/concept/0> ,
                                  <https://testdirektoratet.no/model/concept/1> ;
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
        dct:publisher             <http://data.brreg.no/enhetsregisteret/enhet/123456789> ;
        dct:title                 "Datasett 1"@nb , "Dataset 1"@en ;
        dcat:contactPoint         <https://testdirektoratet.no/kontakt/testmann> ;
        dct:spatial               <https://data.geonorge.no/administrativeEnheter/fylke/id/173142> ;
        dct:temporal              [ a                          dct:PeriodOfTime ;
                                    dcat:startDate           "2019-04-02T00:00:00"^^xsd:dateTime ] ;
        dcat:distribution         <https://testdirektoratet.no/model/distribution/1> , <http://testdirektoratet.no/data/test/2> ;
        dct:provenance            <http://data.brreg.no/datakatalog/provinens/tredjepart> ;
        dcat:landingPage          <https://testdirektoratet.no> ;
        dcat:endpointDescription  <https://testdirektoratet.no/openapi/dataset/1.yaml> .

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
            identifier=['adb4cf00-31c8-460c-9563-55f204cf8221'],
            title={'nb':'Datasett 0','en':"Dataset 0"},
            description={'nb':'Beskrivelse av datasett 0','en':"Description of dataset 0"},
            uri='https://testdirektoratet.no/model/dataset/0',
            accessRights='http://publications.europa.eu/resource/authority/access-right/PUBLIC',
            publisher='http://data.brreg.no/enhetsregisteret/enhet/987654321',
            theme=['http://publications.europa.eu/resource/authority/data-theme/GOVE', 'http://publications.europa.eu/resource/authority/data-theme/TECH'],
            keyword=[{'nb': 'test'}],
            page=['https://testdirektoratet.no'],
            issued=isodate.parse_datetime("2019-03-22T13:11:16.546902"),
            temporal=[Temporal(startDate=isodate.parse_datetime("2019-04-02T00:00:00"))],
            subject=['https://testdirektoratet.no/model/concept/0','https://testdirektoratet.no/model/concept/1'],
            language=['http://publications.europa.eu/resource/authority/language/NOR'],
            accrualPeriodicity='http://publications.europa.eu/resource/authority/frequency'
        ), 
        'https://testdirektoratet.no/model/dataset/1': Dataset(
            id='4667277a-9d27-32c1-aed5-612fa601f393',
            harvest=HarvestMetaData(
                firstHarvested=isodate.parse_datetime("2020-03-12T11:52:16.122Z"),
                changed=[isodate.parse_datetime("2020-03-12T11:52:16.122Z"), isodate.parse_datetime("2020-03-12T11:52:16.123Z")]),
            title={'nb':'Datasett 1','en':"Dataset 1"},
            description={'nb':'Beskrivelse av datasett 1','en':"Description of dataset 1"},
            uri='https://testdirektoratet.no/model/dataset/1',
            publisher='http://data.brreg.no/enhetsregisteret/enhet/123456789',
            contactPoint=[ContactPoint(uri='https://testdirektoratet.no/kontakt/testmann')],
            distribution=[
                Distribution(uri='http://testdirektoratet.no/data/test/2'),
                Distribution(uri='https://testdirektoratet.no/model/distribution/1')
            ],
            temporal=[Temporal(startDate=isodate.parse_datetime("2019-04-02T00:00:00"))],
            landingPage=['https://testdirektoratet.no'],
            spatial=['https://data.geonorge.no/administrativeEnheter/fylke/id/173142'],
            provenance='http://data.brreg.no/datakatalog/provinens/tredjepart'
        )
    }


    assert parseDatasets(src0) == expected
