from unittest.mock import Mock

from rdflib import Graph, URIRef

from fdk_rdf_parser import parse_concepts
from fdk_rdf_parser.classes import Concept, ContactPoint, HarvestMetaData, Publisher
from fdk_rdf_parser.classes.concept import (
    AssociativeRelation,
    Collection,
    Definition,
    TextAndURI,
)
from fdk_rdf_parser.parse_functions import parse_concept


def test_parse_concepts(mock_reference_data_client: Mock) -> None:
    src = """
@prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/master/src/main/resources/ontology/organization-catalog.owl#> .
@prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/master/src/main/resources/ontology/org-type.ttl#> .
@prefix rov:   <http://www.w3.org/ns/regorg#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix skosno: <https://data.norge.no/vocabulary/skosno#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix xkos:  <http://rdf-vocabulary.ddialliance.org/xkos#> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028>
        a               skos:Collection ;
        rdfs:label      "Concept collection belonging to 910258028" ;
        dct:identifier  "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028" ;
        dct:publisher   <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skos:member     <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013> , <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190> , <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0> , <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef> , <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3> .

<https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f>
        a                  dcat:CatalogRecord ;
        dct:identifier     "55a38009-e114-301f-aa7c-8b5f09529f0f" ;
        dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0>
        a                   skos:Concept ;
        dct:identifier      "1843b048-f9af-4665-8e53-3c001d0166c0" ;
        dct:modified        "2019-12-16"^^xsd:date ;
        dct:publisher       <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skosxl:altLabel     [ a                   skosxl:Label ;
                              skosxl:literalForm  "w"@nb
                            ] ;
        skosxl:hiddenLabel  [ ] ;
        skosxl:prefLabel    [ a                   skosxl:Label ;
                              skosxl:literalForm  "to"@nb
                            ] ;
        skosno:assosiativRelasjon [ rdf:type                skosno:AssosiativRelasjon ;
                                  dct:description         "Beskrivelse"@nb ;
                                  skos:related  <http://begrepskatalogen/begrep/organisasjon>
                                ] ;
        skosno:assosiativRelasjon [ rdf:type                skosno:AssosiativRelasjon ;
                                  dct:description         "Beskrivelse"@nb ;
                                  skos:related  <http://begrepskatalogen/begrep/virksomhet>
                                ] ;
        skosno:definisjon   [ a           skosno:Definisjon ;
                              rdfs:label  "dfgfg"@nb ;
                              dct:audience skosno:blabla ;
                              skosno:forholdTilKilde  skosno:blabla
                            ] .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190>
        a                  skos:Concept ;
        dct:identifier     "3609b02d-72c5-47e0-a6b8-df0a503cf190" ;
        dct:modified       "2020-09-08"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skosxl:altLabel    [ a                   skosxl:Label ;
                             skosxl:literalForm  "stabilisator"@nb
                           ] ;
        skosxl:prefLabel   [ a                   skosxl:Label ;
                             skosxl:literalForm  "midtbaneanker"@nb
                           ] ;
        skosno:definisjon  [ a                       skosno:Definisjon ;
                             rdfs:label              "en stabil stabilisator på midten"@nb ;
                             dct:source              []  ;
                             dct:audience skosno:fagspesialist ;
                             skosno:forholdTilKilde  skosno:egendefinert
                           ] .

<https://concepts.staging.fellesdatakatalog.digdir.no/concepts/fc8baf8d-6146-3b69-93c5-52bd41592c4e>
        a                  dcat:CatalogRecord ;
        dct:identifier     "fc8baf8d-6146-3b69-93c5-52bd41592c4e" ;
        dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef>
        a                  skos:Concept ;
        dct:identifier     "9f25b5ad-8aa7-4233-853b-7434e20aeaef" ;
        dct:modified       "2020-02-14"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skosno:bruksområde "arbeid" ;
        skosxl:prefLabel   [ a                   skosxl:Label ;
                             skosxl:literalForm  "dokument"@nn
                           ] ;
        skosno:definisjon  [ a                       skosno:Definisjon ;
                             rdfs:label              "eit skriftstykke, eit skriftleg utgreiing og inneheld informasjon. Eit dokument er meint for kommunikasjon eller lagring av data. "@nn ;
                             dct:source              [ rdfs:label    "Noe sted et sted"@nb ;
                                                       rdfs:seeAlso  <http://example.com/>
                                                     ] ;
                             skosno:forholdTilKilde  skosno:basertPåKilde
                           ] .

<https://concepts.staging.fellesdatakatalog.digdir.no/concepts/35367473-a4c0-3f55-bbdb-fcdbffb6f67a>
        a                  dcat:CatalogRecord ;
        dct:identifier     "35367473-a4c0-3f55-bbdb-fcdbffb6f67a" ;
        dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3>
        a                  skos:Concept ;
        dct:identifier     "523ff894-638b-44a2-a4fd-3e96a5a8a5a3" ;
        dct:modified       "2020-02-14"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/987654321> ;
        skosxl:prefLabel   [ a                   skosxl:Label ;
                             skosxl:literalForm  "Testbegrep"@nb
                           ] ;
        skosno:definisjon  [ a           skosno:Definisjon ;
                             rdfs:label  "Et begrep som en bruke til å teste med"@nb ;
                             dct:audience skosno:allmennheten ;
                             skosno:forholdTilKilde  skosno:sitatFraKilde;
                             skosno:omfang [ rdfs:label    "test"@nb ;
                                             rdfs:seeAlso  <http://example.com/> ]
                           ] .

<https://concepts.staging.fellesdatakatalog.digdir.no/concepts/bb4a8fa6-16ba-3dc9-92e6-42773dc985de>
        a                  dcat:CatalogRecord ;
        dct:identifier     "bb4a8fa6-16ba-3dc9-92e6-42773dc985de" ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013> .

<https://concepts.staging.fellesdatakatalog.digdir.no/concepts/71f860be-ad4c-3ae7-8344-c0b727d4d3b0>
        a                  dcat:CatalogRecord ;
        dct:identifier     "71f860be-ad4c-3ae7-8344-c0b727d4d3b0" ;
        dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013>
        a                  skos:Concept ;
        rdfs:seeAlso       "http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940" , "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940" , "http://begrepskatalogen/begrep/be5d8b8b-c3fb-11e9-8d53-005056825ca0" , "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190" ;
        dct:identifier     "c4ae179e-6a3a-42bc-85a2-1e32d75fc013" ;
        dct:modified       "2020-11-04"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skosxl:prefLabel   [ a                   skosxl:Label ;
                             skosxl:literalForm  "lua og sokka"@nn
                           ] ;
        skosno:definisjon  [ a           skosno:Definisjon ;
                             rdfs:label  "klesplagg for hode og hender"@nb
                           ] ;
        skosno:bruksområde "hjem"@nb ;
        dcat:contactPoint             [ a                   vcard:Organization ;
                                        vcard:hasEmail      <mailto:informasjonsforvaltning@brreg.no> ;
                                        vcard:hasTelephone  <tel:+4775007500>
                                      ] .

<https://data.brreg.no/enhetsregisteret/api/enheter/987654321>
        a                      rov:RegisteredOrganization ;
        dct:identifier         "987654321" ;
        rov:legalName          "Testdirektoratet" ;
        foaf:name              "Testdirektoratet"@nb ;
        rov:orgType            orgtype:STAT ;
        br:orgPath             "/STAT/987654321" .

<https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662>
        a                  dcat:CatalogRecord ;
        dct:identifier     "5e08611a-4e94-3d8f-9d9f-d3a292ec1662" ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ."""

    expected = {
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0": Concept(
            id="55a38009-e114-301f-aa7c-8b5f09529f0f",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
            ),
            collection=Collection(
                id="5e08611a-4e94-3d8f-9d9f-d3a292ec1662",
                uri="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028",
                label={"nb": "Concept collection belonging to 910258028"},
                publisher=Publisher(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
                ),
            ),
            publisher=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
            ),
            prefLabel={"nb": "to"},
            altLabel=[{"nb": "w"}],
            definition=Definition(text={"nb": "dfgfg"}),
            associativeRelation=[
                AssociativeRelation(
                    description={"nb": "Beskrivelse"},
                    related="http://begrepskatalogen/begrep/organisasjon",
                ),
                AssociativeRelation(
                    description={"nb": "Beskrivelse"},
                    related="http://begrepskatalogen/begrep/virksomhet",
                ),
            ],
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190": Concept(
            id="fc8baf8d-6146-3b69-93c5-52bd41592c4e",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/fc8baf8d-6146-3b69-93c5-52bd41592c4e",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
            ),
            collection=Collection(
                id="5e08611a-4e94-3d8f-9d9f-d3a292ec1662",
                uri="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028",
                label={"nb": "Concept collection belonging to 910258028"},
                publisher=Publisher(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
                ),
            ),
            publisher=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
            ),
            prefLabel={"nb": "midtbaneanker"},
            altLabel=[{"nb": "stabilisator"}],
            definition=Definition(
                text={"nb": "en stabil stabilisator på midten"},
                sourceRelationship="egendefinert",
                targetGroup="fagspesialist",
                sources=[TextAndURI(uri=None, text=None)],
            ),
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef": Concept(
            id="71f860be-ad4c-3ae7-8344-c0b727d4d3b0",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/71f860be-ad4c-3ae7-8344-c0b727d4d3b0",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
            ),
            collection=Collection(
                id="5e08611a-4e94-3d8f-9d9f-d3a292ec1662",
                uri="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028",
                label={"nb": "Concept collection belonging to 910258028"},
                publisher=Publisher(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
                ),
            ),
            publisher=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
            ),
            application=[{"nb": "arbeid"}],
            prefLabel={"nn": "dokument"},
            definition=Definition(
                text={
                    "nn": "eit skriftstykke, eit skriftleg utgreiing og inneheld informasjon. Eit dokument er meint for kommunikasjon eller lagring av data. "
                },
                sourceRelationship="basertPåKilde",
                sources=[
                    TextAndURI(
                        uri="http://example.com/", text={"nb": "Noe sted et sted"}
                    )
                ],
            ),
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3": Concept(
            id="35367473-a4c0-3f55-bbdb-fcdbffb6f67a",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/35367473-a4c0-3f55-bbdb-fcdbffb6f67a",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
            ),
            collection=Collection(
                id="5e08611a-4e94-3d8f-9d9f-d3a292ec1662",
                uri="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028",
                label={"nb": "Concept collection belonging to 910258028"},
                publisher=Publisher(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
                ),
            ),
            publisher=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/987654321",
                id="987654321",
                name="Testdirektoratet",
                orgPath="/STAT/987654321",
                prefLabel={
                    "nb": "Testdirektoratet",
                },
                organisasjonsform="STAT",
            ),
            prefLabel={"nb": "Testbegrep"},
            definition=Definition(
                text={"nb": "Et begrep som en bruke til å teste med"},
                targetGroup="allmennheten",
                sourceRelationship="sitatFraKilde",
                range=TextAndURI(uri="http://example.com/", text={"nb": "test"}),
            ),
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013": Concept(
            id="bb4a8fa6-16ba-3dc9-92e6-42773dc985de",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/bb4a8fa6-16ba-3dc9-92e6-42773dc985de",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
            ),
            publisher=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
            ),
            application=[{"nb": "hjem"}],
            prefLabel={"nn": "lua og sokka"},
            contactPoint=ContactPoint(
                email="informasjonsforvaltning@brreg.no",
                hasTelephone="+4775007500",
            ),
            definition=Definition(
                text={"nb": "klesplagg for hode og hender"},
            ),
            seeAlso={
                "http://begrepskatalogen/begrep/be5d8b8b-c3fb-11e9-8d53-005056825ca0",
                "http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940",
                "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190",
                "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940",
            },
            type="concept",
        ),
    }

    result = parse_concepts(src)

    assert result == expected


def test_parse_concept_handles_wrong_collection_type(
    mock_reference_data_client: Mock,
) -> None:
    src = """@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028>
        a               dcat:Catalog ;
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

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0>
        a                   skos:Concept ;
        dct:identifier      "1843b048-f9af-4665-8e53-3c001d0166c0" .

<https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662>
        a                  dcat:CatalogRecord ;
        dct:identifier     "5e08611a-4e94-3d8f-9d9f-d3a292ec1662" ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ."""

    expected = Concept(
        id="55a38009-e114-301f-aa7c-8b5f09529f0f",
        uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f",
        identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0",
        harvest=HarvestMetaData(
            firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
        ),
        type="concept",
    )

    graph = Graph().parse(data=src, format="turtle")
    concept_uri = URIRef(
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0"
    )
    record_uri = URIRef(
        "https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f"
    )

    result = parse_concept(graph, record_uri, concept_uri)

    assert result == expected


def test_parse_concept_with_old_skosno(
    mock_reference_data_client: Mock,
) -> None:
    src = """@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix skosno: <http://difi.no/skosno#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://concepts.staging.fellesdatakatalog.digdir.no/concepts/35367473-a4c0-3f55-bbdb-fcdbffb6f67a>
        a                  dcat:CatalogRecord ;
        dct:identifier     "35367473-a4c0-3f55-bbdb-fcdbffb6f67a" ;
        dct:isPartOf       <https://concepts.staging.fellesdatakatalog.digdir.no/collections/5e08611a-4e94-3d8f-9d9f-d3a292ec1662> ;
        dct:issued         "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        dct:modified       "2021-02-17T09:39:13.293Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3>
        a                  skos:Concept ;
        dct:identifier     "523ff894-638b-44a2-a4fd-3e96a5a8a5a3" ;
        dct:modified       "2020-02-14"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skosxl:prefLabel   [ a                   skosxl:Label ;
                             skosxl:literalForm  "Testbegrep"@nb
                           ] ;
        skosno:bruksområde "arbeid" ;
        skosno:betydningsbeskrivelse  [ a           skosno:Definisjon ;
                             rdfs:label  "Et begrep som en bruke til å teste med"@nb ;
                             dct:audience skosno:allmennheten ;
                             skosno:forholdTilKilde  skosno:sitatFraKilde;
                             skosno:omfang [ rdfs:label    "test"@nb ;
                                             rdfs:seeAlso  <http://example.com/> ]
                           ] ."""

    expected = Concept(
        id="35367473-a4c0-3f55-bbdb-fcdbffb6f67a",
        uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/35367473-a4c0-3f55-bbdb-fcdbffb6f67a",
        identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3",
        harvest=HarvestMetaData(
            firstHarvested="2021-02-17T09:39:13Z", changed=["2021-02-17T09:39:13Z"]
        ),
        publisher=Publisher(
            uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
        ),
        prefLabel={"nb": "Testbegrep"},
        application=[{"nb": "arbeid"}],
        definition=Definition(
            text={"nb": "Et begrep som en bruke til å teste med"},
            targetGroup="allmennheten",
            sourceRelationship="sitatFraKilde",
            range=TextAndURI(uri="http://example.com/", text={"nb": "test"}),
        ),
        type="concept",
    )

    graph = Graph().parse(data=src, format="turtle")
    concept_uri = URIRef(
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3"
    )
    record_uri = URIRef(
        "https://concepts.staging.fellesdatakatalog.digdir.no/concepts/35367473-a4c0-3f55-bbdb-fcdbffb6f67a"
    )

    result = parse_concept(graph, record_uri, concept_uri)

    assert result == expected
