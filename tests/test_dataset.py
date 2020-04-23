"""Test cases."""
import pytest

from fdk_rdf_parser.classes import Dataset, HarvestMetaData, QualityAnnotation, SkosConcept, Publisher, Distribution
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
            publisher=Publisher(uri='http://data.brreg.no/enhetsregisteret/enhet/987654321'),
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

def test_dataset_has_quality_annotations():

    src = """
        @prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix dqv:   <http://www.w3.org/ns/dqvNS#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix prov:  <http://www.w3.org/ns/prov#> .

        <https://testdirektoratet.no/model/dataset/quality>
                a                   dcat:Dataset ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Currentness> ;
                    prov:hasBody     [] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Availability> ;
                    prov:hasBody     [ rdf:value  "availability"@en ] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Relevance> ;
                    prov:hasBody     [ rdf:value  "relevans"@nb ] ] ;
                dqv:hasQualityAnnotation  [ 
                    a                dqv:QualityAnnotation ;
                    dqv:inDimension  <http://iso.org/25012/2008/dataquality/Completeness> ;
                    prov:hasBody     [ rdf:value  "Completeness"@en ] ] ."""

    expected = Dataset(
        uri='https://testdirektoratet.no/model/dataset/quality',
        harvest=HarvestMetaData(),
        hasCurrentnessAnnotation=QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Currentness'
        ),
        hasAvailabilityAnnotation=QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Availability',
            hasBody={'en':'availability'}
        ),
        hasRelevanceAnnotation=QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Relevance',
            hasBody={'nb':'relevans'}
        ),
        hasCompletenessAnnotation=QualityAnnotation(
            inDimension='http://iso.org/25012/2008/dataquality/Completeness',
            hasBody={'en':'Completeness'}
        )
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/quality')


    assert parseDataset(graph, URIRef('record'), subject) == expected

def test_legal_basis_fields():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dcatno:legalBasisForRestriction
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://restriction.no" ;
                  skos:prefLabel  "skjermingshjemmel"@nb
                ] ;
                dcatno:legalBasisForProcessing
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://processing.no" ;
                  skos:prefLabel  "behandlingsgrunnlag"@nb
                ] ;
                dcatno:legalBasisForAccess
                [ a               skos:Concept , dct:RightsStatement ;
                  dct:source      "https://access.no" ;
                  skos:prefLabel  "utleveringshjemmel"@nb
                ] ."""

    expected = Dataset(
        uri='https://testdirektoratet.no/model/dataset/0',
        harvest=HarvestMetaData(),
        legalBasisForRestriction=[SkosConcept(
            uri = 'https://restriction.no',
            prefLabel = {'nb':'skjermingshjemmel'},
            extraType = 'http://purl.org/dc/terms/RightsStatement'
        )],
        legalBasisForProcessing=[SkosConcept(
            uri = 'https://processing.no',
            prefLabel = {'nb':'behandlingsgrunnlag'},
            extraType = 'http://purl.org/dc/terms/RightsStatement'
        )],
        legalBasisForAccess=[SkosConcept(
            uri = 'https://access.no',
            prefLabel = {'nb':'utleveringshjemmel'},
            extraType = 'http://purl.org/dc/terms/RightsStatement'
        )]
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/0')


    assert parseDataset(graph, URIRef('record'), subject) == expected

def test_informationmodel_and_conformsto():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                dct:conformsTo
                [ a               skos:Concept , dct:Standard ;
                  dct:source      "https://conformsto.no" ;
                  skos:prefLabel  "conforms to"@en
                ] ;
                dcatno:informationModel
                [ a               skos:Concept , dct:Standard ;
                  dct:source      "https://informationmodel.no" ;
                  skos:prefLabel  "information model"@en
                ] ."""

    expected = Dataset(
        uri='https://testdirektoratet.no/model/dataset/0',
        harvest=HarvestMetaData(),
        conformsTo=[SkosConcept(
            uri = 'https://conformsto.no',
            prefLabel = {'en':'conforms to'},
            extraType = 'http://purl.org/dc/terms/Standard'
        )],
        informationModel=[SkosConcept(
            uri = 'https://informationmodel.no',
            prefLabel = {'en':'information model'},
            extraType = 'http://purl.org/dc/terms/Standard'
        )]
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/0')


    assert parseDataset(graph, URIRef('record'), subject) == expected

def test_distribution_and_sample():

    src = """
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <http://difi.no/dcatno#> .
        @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix adms:  <http://www.w3.org/ns/adms#> .

        <https://testdirektoratet.no/model/dataset/0>
                a                         dcat:Dataset ;
                adms:sample               [ a                dcat:Distribution ;
                                            dct:description  "adsgjkv  cghj     dghdh"@nb ;
                                            dct:format       "application/ATF" ;
                                            dcat:accessURL   <https://application/ATF.com>
                                          ] ;
                dcat:distribution         [ a                dcat:Distribution ;
                                            dct:conformsTo   [ a               dct:Standard , skos:Concept ;
                                                               dct:source      "https://hopp.no" ;
                                                               skos:prefLabel  "standard1"@nb
                                                             ] ;
                                            dct:description  "asdadrtyrtydfghdgh  dgh dfgh dh"@nb ;
                                            dct:format       "application/ATF" ;
                                            dct:license      [ a           dct:LicenseDocument , skos:Concept ;
                                                               dct:source  "http://creativecommons.org/publicdomain/zero/1.0/"
                                                             ] ;
                                            dct:type         "Feed" ;
                                            dcat:accessURL   <https://distribusjonsentralen.no> ;
                                            foaf:page        [ a           foaf:Document , skos:Concept ;
                                                               dct:source  "https://dokumentsjon.com"
                                                             ]
                                          ] ."""

    expected = Dataset(
        uri='https://testdirektoratet.no/model/dataset/0',
        harvest=HarvestMetaData(),
        sample=[Distribution(
            description={'nb':'adsgjkv  cghj     dghdh'},
            format=['application/ATF'],
            accessURL=['https://application/ATF.com']
        )],
        distribution=[Distribution(
            conformsTo=[SkosConcept(
                uri = 'https://hopp.no',
                prefLabel = {'nb':'standard1'},
                extraType = 'http://purl.org/dc/terms/Standard')],
            description={'nb':'asdadrtyrtydfghdgh  dgh dfgh dh'},
            format=['application/ATF'],
            license=[SkosConcept(
                uri = 'http://creativecommons.org/publicdomain/zero/1.0/',
                extraType = 'http://purl.org/dc/terms/LicenseDocument')],
            type='Feed',
            accessURL=['https://distribusjonsentralen.no'],
            page=[SkosConcept(
                uri = 'https://dokumentsjon.com',
                extraType = 'http://xmlns.com/foaf/0.1/Document')]
        )]
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(u'https://testdirektoratet.no/model/dataset/0')


    assert parseDataset(graph, URIRef('record'), subject) == expected
