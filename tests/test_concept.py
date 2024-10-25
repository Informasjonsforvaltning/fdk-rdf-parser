from dataclasses import asdict
from unittest.mock import Mock

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser import parse_concepts
from fdk_rdf_parser.classes import (
    Concept,
    DCATContactPoint,
    HarvestMetaData,
    Publisher,
)
from fdk_rdf_parser.classes.concept import (
    AssociativeRelation,
    Collection,
    Definition,
    GenericRelation,
    PartitiveRelation,
    Subject,
    TextAndURI,
)
from fdk_rdf_parser.fdk_rdf_parser import (
    parse_concept,
    parse_concept_as_dict,
)
from fdk_rdf_parser.parse_functions import _parse_concept


def test_parse_concepts(mock_reference_data_client: Mock) -> None:
    src = """
@prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
@prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
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
@prefix euvoc:  <http://publications.europa.eu/ontology/euvoc#> .
@prefix uneskos: <http://purl.org/umu/uneskos#> .
@prefix schema:  <http://schema.org/> .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028>
        a               skos:Collection ;
        dct:title      "Concept collection belonging to 910258028" ;
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
        dct:temporal        [ a           dct:PeriodOfTime ;
                                schema:startDate "2020-05-29"^^xsd:date;
                                schema:endDate "2021-05-29"^^xsd:date;
                                ] ;
        dct:created        "2023-02-17"^^xsd:date ;
        dct:identifier      "1843b048-f9af-4665-8e53-3c001d0166c0" ;
        dct:modified        "2019-12-16"^^xsd:date ;
        euvoc:status        <http://publications.europa.eu/resource/authority/concept-status/CURRENT> ;
        dct:publisher       <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        dct:creator         <https://data.brreg.no/enhetsregisteret/api/enheter/123456789> ;
        skos:exactMatch     <http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940> ;
        skos:closeMatch     <http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940> ;
        uneskos:memberOf    <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ;
        skosxl:altLabel     [ a                   skosxl:Label ;
                              skosxl:literalForm  "w"@nb
                            ] ;
        skosxl:hiddenLabel  [ ] ;
        skos:hiddenLabel    "hidden"@nb ;
        skosxl:prefLabel    [ a                   skosxl:Label ;
                              skosxl:literalForm  "to"@nb
                            ] ;
        skosno:isFromConceptIn    [ rdf:type                skosno:AssociativeConceptRelation ;
                                  skosno:relationRole       "RelationRole"@nb ;
                                  skosno:hasToConcept  <http://begrepskatalogen/begrep/organisasjon>
                                ] ;
        skosno:partitivRelasjon [ rdf:type                    skosno:PartitivRelasjon ;
                                  dct:description  "Inndelingskriterium"@nb ;
                                  dct:hasPart     <http://begrepskatalogen/begrep/blad>
                                ] ;
        skosno:partitivRelasjon [ rdf:type                    skosno:PartitivRelasjon ;
                                  dct:description  "Inndelingskriterium"@nb ;
                                  dct:isPartOf     <http://begrepskatalogen/begrep/tre>
                                ] ;
        skosno:generiskRelasjon [ rdf:type                    skosno:GeneriskRelasjon ;
                                  skosno:inndelingskriterium  "Inndelingskriterium"@nb ;
                                  xkos:generalizes    <http://begrepskatalogen/begrep/biffbestikk>
                                ] ;
        skosno:generiskRelasjon [ rdf:type                    skosno:GeneriskRelasjon ;
                                  skosno:inndelingskriterium  "Inndelingskriterium"@nb ;
                                  xkos:specializes    <http://begrepskatalogen/begrep/bestikk>
                                ] ;
        euvoc:xlDefinition       [ a           euvoc:XlNote ;
                                  rdf:value  "def-1"@nb ;
                                  dct:source <https://lovdata.no/dokument/NL/lov/1997-02-28-19/kap14#kap14> ;
                                  skosno:relationshipWithSource  <https://data.norge.no/vocabulary/relationship-with-source-type#self-composed>
                                ] ;
        euvoc:xlDefinition       [ a           euvoc:XlNote ;
                                  rdf:value  "def-2"@nb ;
                                  dct:audience <https://data.norge.no/vocabulary/audience-type#public> ;
                                  skosno:relationshipWithSource  <https://data.norge.no/vocabulary/relationship-with-source-type#self-composed>
                                ] ;
        skosno:valueRange       [ ]  .

<https://lovdata.no/dokument/NL/lov/1997-02-28-19/kap14#kap14>
        a           rdfs:Resource ;
        rdfs:label  "Kildenavn"@nb .

<https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190>
        a                  skos:Concept ;
        dct:identifier     "3609b02d-72c5-47e0-a6b8-df0a503cf190" ;
        dct:modified       "2020-09-08"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        dct:subject        [ ] ;
        skosno:hasPartitiveConceptRelation [
                                  rdf:type  skosno:PartitiveConceptRelation ;
                                  dct:description  "Inndelingskriterium"@nb ;
                                  skosno:hasPartitiveConcept     <http://begrepskatalogen/begrep/blad>
                                ] ;
        skosno:hasPartitiveConceptRelation [
                                  rdf:type  skosno:PartitiveConceptRelation ;
                                  dct:description  "Inndelingskriterium"@nb ;
                                  skosno:hasComprehensiveConcept     <http://begrepskatalogen/begrep/tre>
                                ] ;
        skosno:assosiativRelasjon    [ rdf:type                skosno:AssosiativRelasjon ;
                                       dct:description         "Beskrivelse"@nb ;
                                       skos:related  <http://begrepskatalogen/begrep/virksomhet> ] ;
        skosno:hasGenericConceptRelation [
                                  rdf:type  skosno:GenericConceptRelation ;
                                  dct:description  "Inndelingskriterium"@nb ;
                                  skosno:hasSpecificConcept    <http://begrepskatalogen/begrep/biffbestikk>
                                ] ;
        skosno:hasGenericConceptRelation [
                                  rdf:type  skosno:GenericConceptRelation ;
                                  dct:description  "Inndelingskriterium"@nb ;
                                  skosno:hasGenericConcept    <http://begrepskatalogen/begrep/bestikk>
                                ] ;
        euvoc:status       "status nb" , "status en"@en ;
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
                           ] ;
        skosno:definisjon  [ a           skosno:Definisjon ;
                              rdfs:label  "ugyldig-audience-og-forholdtilkilde"@nb ;
                              dct:audience skosno:ugyldig ;
                              skosno:forholdTilKilde  skosno:ugyldig
                            ] .


<http://publications.europa.eu/resource/authority/concept-status/CURRENT>
        skos:prefLabel  "current"@en , "gjeldende"@no , "gjeldande"@nn , "gjeldende"@nb .

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
        dct:subject        "jobb" , "work"@en , <https://catalog-admin-service.staging.fellesdatakatalog.digdir.no/123456789/concepts/subjects#3> ;
        dct:subject        [ a                   skos:Concept ;
                             skos:prefLabel      "bnode subject"@en
                           ] ;
        skos:prefLabel     "dokument"@nn , "dokument"@nb ;
        skosno:definisjon  [ a                       skosno:Definisjon ;
                             rdfs:label              "eit skriftstykke, eit skriftleg utgreiing og inneheld informasjon. Eit dokument er meint for kommunikasjon eller lagring av data. "@nn ;
                             dct:source              [ rdfs:label    "Noe sted et sted"@nb ;
                                                       rdfs:seeAlso  <http://example.com/>
                                                     ] ;
                             skosno:forholdTilKilde  skosno:basertPåKilde
                           ] .

<https://catalog-admin-service.staging.fellesdatakatalog.digdir.no/123456789/concepts/subjects#3>
        a               skos:Concept;
        dct:identifier  "https://catalog-admin-service.staging.fellesdatakatalog.digdir.no/123456789/concepts/subjects#3"^^xsd:anyURI;
        skos:broader    <https://catalog-admin-service.staging.fellesdatakatalog.digdir.no/123456789/concepts/subjects#1>;
        skos:inScheme   <https://catalog-admin-service.staging.fellesdatakatalog.digdir.no/123456789/concepts/subjects>;
        skos:prefLabel  "nb 3"@nb , "nn 3"@nn .

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
        dct:isReplacedBy   "http://begrepskatalogen/begrep/be5d8b8b-c3fb-11e9-8d53-005056825ca0" ;
        dct:replaces       "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940" ;
        dct:identifier     "c4ae179e-6a3a-42bc-85a2-1e32d75fc013" ;
        dct:modified       "2020-11-04"^^xsd:date ;
        dct:publisher      <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
        skosxl:prefLabel   [ a                   skosxl:Label ;
                             skosxl:literalForm  "lua og sokka"@nn
                           ] ;
        skosno:definisjon  [ a           skosno:Definisjon ;
                             rdfs:label  "klesplagg for hode og hender"@nb
                           ] ;
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
            created="2023-02-17",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
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
            creator=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/123456789"
            ),
            exactMatch={
                "http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940"
            },
            closeMatch={
                "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940"
            },
            memberOf={
                "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028"
            },
            prefLabel={"nb": "to"},
            status={
                "en": "current",
                "no": "gjeldende",
                "nn": "gjeldande",
                "nb": "gjeldende",
            },
            hiddenLabel=[{"nb": "hidden"}],
            altLabel=[{"nb": "w"}],
            definition=Definition(
                text={"nb": "def-1"},
                sourceRelationship="https://data.norge.no/vocabulary/relationship-with-source-type#self-composed",
                sources=[
                    TextAndURI(
                        uri="https://lovdata.no/dokument/NL/lov/1997-02-28-19/kap14#kap14",
                        text={"nb": "Kildenavn"},
                    )
                ],
            ),
            definitions=[
                Definition(
                    text={"nb": "def-1"},
                    sourceRelationship="https://data.norge.no/vocabulary/relationship-with-source-type#self-composed",
                    sources=[
                        TextAndURI(
                            uri="https://lovdata.no/dokument/NL/lov/1997-02-28-19/kap14#kap14",
                            text={"nb": "Kildenavn"},
                        )
                    ],
                ),
                Definition(
                    text={"nb": "def-2"},
                    targetGroup="https://data.norge.no/vocabulary/audience-type#public",
                    sourceRelationship="https://data.norge.no/vocabulary/relationship-with-source-type#self-composed",
                ),
            ],
            associativeRelation=[
                AssociativeRelation(
                    description={"nb": "RelationRole"},
                    related="http://begrepskatalogen/begrep/organisasjon",
                )
            ],
            partitiveRelation=[
                PartitiveRelation(
                    description={"nb": "Inndelingskriterium"},
                    hasPart="http://begrepskatalogen/begrep/blad",
                ),
                PartitiveRelation(
                    description={"nb": "Inndelingskriterium"},
                    isPartOf="http://begrepskatalogen/begrep/tre",
                ),
            ],
            genericRelation=[
                GenericRelation(
                    divisioncriterion={"nb": "Inndelingskriterium"},
                    generalizes="http://begrepskatalogen/begrep/biffbestikk",
                ),
                GenericRelation(
                    divisioncriterion={"nb": "Inndelingskriterium"},
                    specializes="http://begrepskatalogen/begrep/bestikk",
                ),
            ],
            type="concept",
            validFromIncluding="2020-05-29",
            validToIncluding="2021-05-29",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190": Concept(
            id="fc8baf8d-6146-3b69-93c5-52bd41592c4e",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/fc8baf8d-6146-3b69-93c5-52bd41592c4e",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
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
            status={"nb": "status nb", "en": "status en"},
            partitiveRelation=[
                PartitiveRelation(
                    description={"nb": "Inndelingskriterium"},
                    hasPart="http://begrepskatalogen/begrep/blad",
                ),
                PartitiveRelation(
                    description={"nb": "Inndelingskriterium"},
                    isPartOf="http://begrepskatalogen/begrep/tre",
                ),
            ],
            associativeRelation=[
                AssociativeRelation(
                    description={"nb": "Beskrivelse"},
                    related="http://begrepskatalogen/begrep/virksomhet",
                ),
            ],
            genericRelation=[
                GenericRelation(
                    divisioncriterion={"nb": "Inndelingskriterium"},
                    generalizes="http://begrepskatalogen/begrep/biffbestikk",
                ),
                GenericRelation(
                    divisioncriterion={"nb": "Inndelingskriterium"},
                    specializes="http://begrepskatalogen/begrep/bestikk",
                ),
            ],
            altLabel=[{"nb": "stabilisator"}],
            definition=Definition(text={"nb": "ugyldig-audience-og-forholdtilkilde"}),
            definitions=[
                Definition(
                    text={"nb": "en stabil stabilisator på midten"},
                    sourceRelationship="egendefinert",
                    targetGroup="fagspesialist",
                    sources=[TextAndURI(uri=None, text=None)],
                ),
                Definition(
                    text={"nb": "ugyldig-audience-og-forholdtilkilde"},
                ),
            ],
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef": Concept(
            id="71f860be-ad4c-3ae7-8344-c0b727d4d3b0",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/71f860be-ad4c-3ae7-8344-c0b727d4d3b0",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/9f25b5ad-8aa7-4233-853b-7434e20aeaef",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
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
            subject=[
                Subject(label={"nb": "jobb"}),
                Subject(label={"en": "work"}),
                Subject(label={"nb": "nb 3", "nn": "nn 3"}),
                Subject(label={"en": "bnode subject"}),
            ],
            prefLabel={"nn": "dokument", "nb": "dokument"},
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
            definitions=[
                Definition(
                    text={
                        "nn": "eit skriftstykke, eit skriftleg utgreiing og inneheld informasjon. Eit dokument er meint for kommunikasjon eller lagring av data. "
                    },
                    sourceRelationship="basertPåKilde",
                    sources=[
                        TextAndURI(
                            uri="http://example.com/", text={"nb": "Noe sted et sted"}
                        )
                    ],
                )
            ],
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3": Concept(
            id="35367473-a4c0-3f55-bbdb-fcdbffb6f67a",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/35367473-a4c0-3f55-bbdb-fcdbffb6f67a",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/523ff894-638b-44a2-a4fd-3e96a5a8a5a3",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
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
            definitions=[
                Definition(
                    text={"nb": "Et begrep som en bruke til å teste med"},
                    targetGroup="allmennheten",
                    sourceRelationship="sitatFraKilde",
                    range=TextAndURI(uri="http://example.com/", text={"nb": "test"}),
                )
            ],
            type="concept",
        ),
        "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013": Concept(
            id="bb4a8fa6-16ba-3dc9-92e6-42773dc985de",
            uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/bb4a8fa6-16ba-3dc9-92e6-42773dc985de",
            identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/c4ae179e-6a3a-42bc-85a2-1e32d75fc013",
            harvest=HarvestMetaData(
                firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
            ),
            publisher=Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/910258028",
            ),
            prefLabel={"nn": "lua og sokka"},
            contactPoint=DCATContactPoint(
                email="informasjonsforvaltning@brreg.no",
                hasTelephone="+4775007500",
            ),
            definition=Definition(
                text={"nb": "klesplagg for hode og hender"},
            ),
            definitions=[
                Definition(
                    text={"nb": "klesplagg for hode og hender"},
                )
            ],
            seeAlso={
                "http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940",
                "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940",
                "http://begrepskatalogen/begrep/be5d8b8b-c3fb-11e9-8d53-005056825ca0",
                "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/3609b02d-72c5-47e0-a6b8-df0a503cf190",
            },
            isReplacedBy={
                "http://begrepskatalogen/begrep/be5d8b8b-c3fb-11e9-8d53-005056825ca0"
            },
            replaces={
                "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940"
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
            firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
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

    result = _parse_concept(graph, record_uri, concept_uri)

    assert result == expected


def test_parse_concept(mock_reference_data_client: Mock) -> None:
    src = """
    @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
    @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
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
    @prefix euvoc:  <http://publications.europa.eu/ontology/euvoc#> .
    @prefix uneskos: <http://purl.org/umu/uneskos#> .

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

    <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0>
            a                   skos:Concept ;
            dct:created        "2023-02-17"^^xsd:date ;
            dct:identifier      "1843b048-f9af-4665-8e53-3c001d0166c0" ;
            dct:modified        "2019-12-16"^^xsd:date ;
            euvoc:status        <http://publications.europa.eu/resource/authority/concept-status/CURRENT> ;
            dct:publisher       <https://data.brreg.no/enhetsregisteret/api/enheter/910258028> ;
            skos:exactMatch     <http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940> ;
            skos:closeMatch     <http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940> ;
            uneskos:memberOf    <https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028> ;
            skos:altLabel       "altLabel", "altLabel2"@en, "altLabel3"@en ;
            skosxl:hiddenLabel  [ ] ;
            skosxl:prefLabel    [ a                   skosxl:Label ;
                                skosxl:literalForm  "to"@nb
                                ] ;
            skos:definition     "skos_definition"@nb ;
            skosno:valueRange
                                  "test-nn"@nn,
                                  "test",
                                  <https://range.com> ;
            euvoc:startDate       "2020-05-29"^^xsd:date;
            euvoc:endDate         "2021-05-29"^^xsd:date .


    <http://publications.europa.eu/resource/authority/concept-status/CURRENT>
            skos:prefLabel  "current"@en , "gjeldende"@no , "gjeldande"@nn , "gjeldende"@nb .


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

    expected = Concept(
        id="55a38009-e114-301f-aa7c-8b5f09529f0f",
        uri="https://concepts.staging.fellesdatakatalog.digdir.no/concepts/55a38009-e114-301f-aa7c-8b5f09529f0f",
        created="2023-02-17",
        identifier="https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028/1843b048-f9af-4665-8e53-3c001d0166c0",
        range=[
            TextAndURI(text={"nn": "test-nn"}),
            TextAndURI(text={"nb": "test"}),
            TextAndURI(uri="https://range.com"),
        ],
        harvest=HarvestMetaData(
            firstHarvested="2021-02-17T09:39:13Z", modified="2021-02-17T09:39:13Z"
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
        exactMatch={
            "http://begrepskatalogen/begrep/20b2e2ab-9fe1-11e5-a9f8-e4115b280940"
        },
        closeMatch={
            "http://begrepskatalogen/begrep/20b2e2aa-9fe1-11e5-a9f8-e4115b280940"
        },
        memberOf={
            "https://registrering-begrep-api.staging.fellesdatakatalog.digdir.no/910258028"
        },
        prefLabel={"nb": "to"},
        status={
            "en": "current",
            "no": "gjeldende",
            "nn": "gjeldande",
            "nb": "gjeldende",
        },
        altLabel=[{"nb": "altLabel"}, {"en": "altLabel2"}, {"en": "altLabel3"}],
        definition=Definition(
            text={"nb": "skos_definition"},
        ),
        definitions=[
            Definition(
                text={"nb": "skos_definition"},
            )
        ],
        type="concept",
        validFromIncluding="2020-05-29",
        validToIncluding="2021-05-29",
    )

    result = parse_concept(src)

    assert result == expected

    result_json_serializable = parse_concept_as_dict(src)
    assert result_json_serializable == asdict(expected)
