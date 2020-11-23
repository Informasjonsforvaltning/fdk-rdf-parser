from unittest.mock import Mock

from rdflib import Graph, URIRef

from fdk_rdf_parser import parse_information_models
from fdk_rdf_parser.classes import (
    Catalog,
    ContactPoint,
    HarvestMetaData,
    InformationModel,
    Publisher,
    SkosCode,
    Temporal,
    ThemeLOS,
)
from fdk_rdf_parser.classes.model_element import (
    ModelCodeElement,
    ModelElement,
)
from fdk_rdf_parser.classes.model_property import ModelProperty
from fdk_rdf_parser.parse_functions import parse_information_model
from fdk_rdf_parser.parse_functions.info_model import (
    add_elements_to_model,
    add_properties_to_model,
)


def test_parse_info_model_no_elements(
    mock_organizations_and_reference_data: Mock,
) -> None:

    src = """@prefix adms:  <http://www.w3.org/ns/adms#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
@prefix xkos:  <https://rdf-vocabulary.ddialliance.org/xkos/> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

digdir:Tidsintervall  a  dct:PeriodOfTime , owl:NamedIndividual ;
        dcat:startDate  "2016-02-11T00:00:00+01:00"^^xsd:dateTime .

digdir:KontaktOss  a        owl:NamedIndividual , vcard:Kind ;
        vcard:fn            "Avdeling for digitalisering" ;
        vcard:hasEmail      <mailto:informasjonsforvaltning@digdir.no> ;
        vcard:hasTelephone  <tel:12345678> .

digdir:Utgiver  a       foaf:Agent , owl:NamedIndividual ;
        dct:identifier  "991825827" ;
        dct:type        "Organisasjonsledd"@nb ;
        foaf:name       "Digitaliseringsdirektoratet"@nb .

digdir:Diversemodell  a    modelldcatno:InformationModel , owl:NamedIndividual ;
        dct:description    "Modell med diverse i. Inneholder modellelementer som AltMuligModell skal peke til."@nb ;
        dct:hasFormat      digdir:AlternativModellformat ;
        dct:identifier     "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell" ;
        dct:isPartOf       digdir:AltMuligModell ;
        dct:isReplacedBy   digdir:AdresseModell ;
        dct:issued         "2016-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:language       <http://publications.europa.eu/resource/authority/language/NOB> ;
        dct:license        <http://creativecommons.org/licenses/by/4.0/deed.no> ;
        dct:modified       "2017-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:publisher      digdir:Utgiver ;
        dct:spatial        <http://sws.geonames.org/3144096/> ;
        dct:temporal       digdir:Tidsintervall ;
        dct:title          "Diversemodell"@nb ;
        dct:type           "Fellesmodell"@nb ;
        owl:versionInfo    "1.0" ;
        adms:status        <http://purl.org/adms/status/Completed> ;
        adms:versionNotes  "Lagt til objekttypen Timeline"@nb ;
        dcat:contactPoint  digdir:KontaktOss ;
        dcat:keyword       "Adresse"@nb ;
        dcat:theme         <https://psi.norge.no/los/tema/skole-og-utdanning> ;
        foaf:homepage      <https://www.difi.no/fagomrader-og-tjenester/digitalisering-og-samordning/nasjonal-arkitektur/informasjonsforvaltning/adresse-felles-informasjonsmodell> ;
        modelldcatno:informationModelIdentifier
                "https://www.digdir.no/diversemodell" .

<https://informationmodels.staging.fellesdatakatalog.digdir.no/informationmodels/77e07f69-5fb4-30c7-afca-bffe179dc3b3>
        a                  dcat:CatalogRecord ;
        dct:identifier     "77e07f69-5fb4-30c7-afca-bffe179dc3b3" ;
        dct:isPartOf       <https://informationmodels.staging.fellesdatakatalog.digdir.no/catalogs/03953a9d-5b6b-34ec-b41c-dcdcb21874d9> ;
        dct:issued         "2020-10-13T11:35:47.394Z"^^xsd:dateTime ;
        dct:modified       "2020-10-13T11:35:47.394Z"^^xsd:dateTime ;
        foaf:primaryTopic  digdir:Diversemodell .

<https://informationmodels.staging.fellesdatakatalog.digdir.no/catalogs/03953a9d-5b6b-34ec-b41c-dcdcb21874d9>
        a                  dcat:CatalogRecord ;
        dct:identifier     "03953a9d-5b6b-34ec-b41c-dcdcb21874d9" ;
        dct:issued         "2020-10-06T10:29:22.705Z"^^xsd:dateTime ;
        dct:modified       "2020-10-13T11:35:47.394Z"^^xsd:dateTime ;
        foaf:primaryTopic  digdir:Katalog ."""

    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell": InformationModel(
            identifier=[
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell"
            ],
            publisher=Publisher(
                uri="https://organizations.fellesdatakatalog.digdir.no/organizations/991825827",
                prefLabel={"nb": "Digitaliseringsdirektoratet"},
            ),
            title={"nb": "Diversemodell"},
            description={
                "nb": "Modell med diverse i. Inneholder modellelementer som AltMuligModell skal peke til."
            },
            descriptionFormatted={
                "nb": "Modell med diverse i. Inneholder modellelementer som AltMuligModell skal peke til."
            },
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
            keyword=[{"nb": "Adresse"}],
            contactPoint=[
                ContactPoint(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#KontaktOss",
                    fullname="Avdeling for digitalisering",
                    email="informasjonsforvaltning@digdir.no",
                    hasTelephone="12345678",
                )
            ],
            dctType="Fellesmodell",
            issued="2016-09-28T00:00:00+01:00",
            modified="2017-09-28T00:00:00+01:00",
            language=[
                SkosCode(
                    uri="http://publications.europa.eu/resource/authority/language/NOB",
                    code="NOB",
                    prefLabel={
                        "en": "Norwegian Bokmål",
                        "nb": "Norsk Bokmål",
                        "nn": "Norsk Bokmål",
                        "no": "Norsk Bokmål",
                    },
                )
            ],
            id="77e07f69-5fb4-30c7-afca-bffe179dc3b3",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-13T11:35:47Z", changed=["2020-10-13T11:35:47Z"]
            ),
            license=[
                SkosCode(
                    uri="http://creativecommons.org/licenses/by/4.0/deed.no",
                    code="CC BY 4.0 DEED",
                    prefLabel={"en": "Creative Commons Attribution 4.0 International"},
                )
            ],
            informationModelIdentifier="https://www.digdir.no/diversemodell",
            spatial=[
                SkosCode(
                    uri="http://sws.geonames.org/3144096/",
                    code="http://sws.geonames.org/3144096/",
                    prefLabel={"no": "Norge"},
                )
            ],
            isPartOf="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AltMuligModell",
            isReplacedBy="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AdresseModell",
            temporal=[
                Temporal(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Tidsintervall",
                    startDate="2016-02-11T00:00:00+01:00",
                )
            ],
            hasFormat=[
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AlternativModellformat"
            ],
            homepage="https://www.difi.no/fagomrader-og-tjenester/digitalisering-og-samordning/nasjonal-arkitektur/informasjonsforvaltning/adresse-felles-informasjonsmodell",
            status="http://purl.org/adms/status/Completed",
            versionInfo="1.0",
            losTheme=[
                ThemeLOS(
                    children=["https://psi.norge.no/los/tema/grunnskole"],
                    isTema=True,
                    losPaths=["skole-og-utdanning"],
                    name={
                        "nn": "Skule og utdanning",
                        "nb": "Skole og utdanning",
                        "en": "Schools and education",
                    },
                    uri="https://psi.norge.no/los/tema/skole-og-utdanning",
                    synonyms=[],
                )
            ],
            type="informationmodels",
        )
    }

    assert parse_information_models(src) == expected


def test_parse_info_model_with_elements(
    mock_organizations_and_reference_data: Mock,
) -> None:
    src = """@prefix adms:  <http://www.w3.org/ns/adms#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
@prefix xkos:  <https://rdf-vocabulary.ddialliance.org/xkos/> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

digdir:Utgiver  a       foaf:Agent , owl:NamedIndividual ;
        dct:identifier  "991825827" ;
        dct:type        "Organisasjonsledd"@nb ;
        foaf:name       "Digitaliseringsdirektoratet"@nb .

digdir:Diversemodell  a    modelldcatno:InformationModel , owl:NamedIndividual ;
        modelldcatno:containsModelElement
                ex-abstrakt:EBU_EditorialObject , digdir:Kjønn ;
        modelldcatno:informationModelIdentifier
                "https://www.digdir.no/diversemodell" .

ex-abstrakt:EBU_EditorialObject
        a                modelldcatno:ObjectType , <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject> , owl:NamedIndividual ;
        dct:description  "Klasse, som er et modellelement, men og viser at den er hentet fra en annen ontologi"@nb ;
        dct:identifier   "http://example.com/test_abstraksjon#EBU_EditorialObject" ;
        modelldcatno:hasProperty  digdir:kjønn , digdir:sivilstand ;
        modelldcatno:hasProperty  [ a             modelldcatno:Attribute , owl:NamedIndividual ;
            dct:identifier     "statsborgerskap"^^xsd:string ;
            dct:title          "statsborgerskap"@nb ] ;
        dct:title        "redaksjonell objekt"@nn , "Editorial Object"@en , "Editorial Object"@nb .

digdir:Kjønn  a         owl:NamedIndividual , modelldcatno:CodeList ;
        dct:identifier  "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn" ;
        dct:title       "Sex"@en , "Kjønn"@nn , "Kjønn"@nb .

digdir:kjønn  a                      owl:NamedIndividual , modelldcatno:Attribute ;
        dct:identifier               "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn" ;
        dct:title                    "kjønn"@nb ;
        xsd:maxOccurs                "1"^^xsd:nonNegativeInteger ;
        modelldcatno:hasValueFrom    digdir:Kjønn ;
        modelldcatno:sequenceNumber  "3"^^xsd:positiveInteger .

digdir:Kvinne  a         owl:NamedIndividual , modelldcatno:CodeElement ;
        dct:identifier  "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kvinne"^^xsd:string ;
        skos:inScheme   digdir:Kjønn ;
        skos:topConceptOf digdir:Kjønn ;
        xkos:next         digdir:Mann ;
        skos:prefLabel  "kvinne"@nb , "kvinne"@nn , "woman"@en .

digdir:Mann  a           owl:NamedIndividual , modelldcatno:CodeElement ;
        dct:identifier  "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Mann"^^xsd:string ;
        skos:inScheme   digdir:Kjønn ;
        xkos:next       digdir:Ubestemt ;
        skos:prefLabel  "mann"@nb , "mann"@nb , "man"@en .

digdir:sivilstand  a             modelldcatno:Attribute , owl:NamedIndividual ;
        dct:identifier     "sivilstand"^^xsd:string ;
        dct:title          "sivilstand"@nb .

<https://informationmodels.staging.fellesdatakatalog.digdir.no/informationmodels/77e07f69-5fb4-30c7-afca-bffe179dc3b3>
        a                  dcat:CatalogRecord ;
        dct:identifier     "77e07f69-5fb4-30c7-afca-bffe179dc3b3" ;
        dct:isPartOf       <https://informationmodels.staging.fellesdatakatalog.digdir.no/catalogs/03953a9d-5b6b-34ec-b41c-dcdcb21874d9> ;
        dct:issued         "2020-10-13T11:35:47.394Z"^^xsd:dateTime ;
        dct:modified       "2020-10-13T11:35:47.394Z"^^xsd:dateTime ;
        foaf:primaryTopic  digdir:Diversemodell .

<https://informationmodels.staging.fellesdatakatalog.digdir.no/catalogs/03953a9d-5b6b-34ec-b41c-dcdcb21874d9>
        a                  dcat:CatalogRecord ;
        dct:identifier     "03953a9d-5b6b-34ec-b41c-dcdcb21874d9" ;
        dct:issued         "2020-10-06T10:29:22.705Z"^^xsd:dateTime ;
        dct:modified       "2020-10-13T11:35:47.394Z"^^xsd:dateTime ;
        foaf:primaryTopic  digdir:Katalog .

digdir:Katalog  a           dcat:Catalog , owl:NamedIndividual ;
        dct:description     "Katalog med oversikt over Digitaliseringsdirektoratets modeller"@nb ;
        dct:identifier      "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Katalog" ;
        dct:license         <http://creativecommons.org/licenses/by/4.0/deed.no> ;
        dct:modified        "2017-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:publisher       digdir:Utgiver ;
        dct:spatial         <http://sws.geonames.org/3144096/> ;
        dct:title           "Digitaliseringsdirektoratets modellkatalog"@nb ;
        modelldcatno:model  digdir:Diversemodell .
"""

    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell": InformationModel(
            publisher=Publisher(
                uri="https://organizations.fellesdatakatalog.digdir.no/organizations/991825827",
                prefLabel={"nb": "Digitaliseringsdirektoratet"},
            ),
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
            id="77e07f69-5fb4-30c7-afca-bffe179dc3b3",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-13T11:35:47Z", changed=["2020-10-13T11:35:47Z"]
            ),
            catalog=Catalog(
                id="03953a9d-5b6b-34ec-b41c-dcdcb21874d9",
                publisher=Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/991825827",
                    prefLabel={"nb": "Digitaliseringsdirektoratet"},
                ),
                title={"nb": "Digitaliseringsdirektoratets modellkatalog"},
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Katalog",
                description={
                    "nb": "Katalog med oversikt over Digitaliseringsdirektoratets modeller"
                },
            ),
            informationModelIdentifier="https://www.digdir.no/diversemodell",
            containsModelElements=[
                "http://example.com/test_abstraksjon#EBU_EditorialObject",
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
            ],
            modelElements={
                "http://example.com/test_abstraksjon#EBU_EditorialObject": ModelElement(
                    uri="http://example.com/test_abstraksjon#EBU_EditorialObject",
                    identifier="http://example.com/test_abstraksjon#EBU_EditorialObject",
                    title={
                        "nb": "Editorial Object",
                        "en": "Editorial Object",
                        "nn": "redaksjonell objekt",
                    },
                    description={
                        "nb": "Klasse, som er et modellelement, men og viser at den er hentet fra en annen ontologi"
                    },
                    hasProperty=[
                        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                        "sivilstand",
                        "statsborgerskap",
                    ],
                    elementTypes=[
                        "http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject",
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#ObjectType",
                    ],
                ),
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn": ModelElement(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                    identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                    title={"nb": "Kjønn", "en": "Sex", "nn": "Kjønn"},
                    elementTypes=[
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#CodeList",
                    ],
                    codes=[
                        ModelCodeElement(
                            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kvinne",
                            prefLabel={"en": "woman", "nn": "kvinne", "nb": "kvinne"},
                            inScheme=[
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
                            ],
                            topConceptOf=[
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
                            ],
                            nextElement=[
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Mann"
                            ],
                        ),
                        ModelCodeElement(
                            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Mann",
                            prefLabel={"en": "man", "nb": "mann"},
                            inScheme=[
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
                            ],
                            nextElement=[
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Ubestemt"
                            ],
                        ),
                    ],
                ),
            },
            modelProperties={
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn": ModelProperty(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                    identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                    title={"nb": "kjønn"},
                    propertyTypes=[
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                    ],
                    maxOccurs=1,
                    sequenceNumber=3,
                    hasValueFrom="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                ),
                "sivilstand": ModelProperty(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#sivilstand",
                    identifier="sivilstand",
                    title={"nb": "sivilstand"},
                    propertyTypes=[
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                    ],
                ),
                "statsborgerskap": ModelProperty(
                    identifier="statsborgerskap",
                    title={"nb": "statsborgerskap"},
                    propertyTypes=[
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                    ],
                ),
            },
            type="informationmodels",
        )
    }

    assert parse_information_models(src) == expected


def test_handles_missing_elements() -> None:
    src = """@prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .

    digdir:Diversemodell  a    modelldcatno:InformationModel , owl:NamedIndividual ;
            modelldcatno:containsModelElement
                    [ a                modelldcatno:ObjectType , <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject> , owl:NamedIndividual ;
                      dct:identifier   "http://example.com/test_abstraksjon#EBU_EditorialObject" ;
                      modelldcatno:hasProperty  digdir:kjønn ] ;
            modelldcatno:containsModelElement
                    digdir:Kjønn ;
            modelldcatno:informationModelIdentifier
                    "https://www.digdir.no/diversemodell" .

    ex-abstrakt:EBU_EditorialObject
            a                modelldcatno:ObjectType , <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject> , owl:NamedIndividual ;
            dct:identifier   "http://example.com/test_abstraksjon#EBU_EditorialObject" ;
            modelldcatno:hasProperty  digdir:kjønn ."""

    expected = InformationModel(
        uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
        harvest=HarvestMetaData(),
        informationModelIdentifier="https://www.digdir.no/diversemodell",
        containsModelElements=[
            "http://example.com/test_abstraksjon#EBU_EditorialObject"
        ],
        modelElements={
            "http://example.com/test_abstraksjon#EBU_EditorialObject": ModelElement(
                identifier="http://example.com/test_abstraksjon#EBU_EditorialObject",
                elementTypes=[
                    "http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject",
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#ObjectType",
                ],
            ),
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        u"https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell"
    )

    assert parse_information_model(graph, URIRef("record"), subject) == expected


def test_elements_are_not_added_twice() -> None:
    src = """@prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .

    digdir:Diversemodell  a    modelldcatno:InformationModel , owl:NamedIndividual ;
            modelldcatno:containsModelElement
                    digdir:Kjønn ;
            modelldcatno:informationModelIdentifier
                    "https://www.digdir.no/diversemodell" .

    digdir:kjønn  a                      owl:NamedIndividual , modelldcatno:Attribute ;
            dct:identifier               "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn" ;
            dct:title                    "kjønn"@nb ;
            xsd:maxOccurs                "1"^^xsd:nonNegativeInteger ;
            modelldcatno:hasValueFrom    digdir:Kjønn ;
            modelldcatno:sequenceNumber  "3"^^xsd:positiveInteger .

    ex-abstrakt:EBU_EditorialObject
            a                modelldcatno:ObjectType , <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject> , owl:NamedIndividual ;
            dct:identifier   "http://example.com/test_abstraksjon#EBU_EditorialObject" ;
            modelldcatno:hasProperty  digdir:kjønn ."""

    expected = InformationModel(
        uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
        harvest=HarvestMetaData(),
        informationModelIdentifier="https://www.digdir.no/diversemodell",
        containsModelElements=[
            "http://example.com/test_abstraksjon#EBU_EditorialObject"
        ],
        modelElements={
            "http://example.com/test_abstraksjon#EBU_EditorialObject": ModelElement(
                uri="http://example.com/test_abstraksjon#EBU_EditorialObject",
                identifier="http://example.com/test_abstraksjon#EBU_EditorialObject",
                title={"en": "Is not added twice"},
            ),
        },
        modelProperties={
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn": ModelProperty(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                title={"en": "Is not added twice"},
            )
        },
    )

    input_model = InformationModel(
        uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
        harvest=HarvestMetaData(),
        informationModelIdentifier="https://www.digdir.no/diversemodell",
        containsModelElements=[
            "http://example.com/test_abstraksjon#EBU_EditorialObject"
        ],
        modelElements={
            "http://example.com/test_abstraksjon#EBU_EditorialObject": ModelElement(
                uri="http://example.com/test_abstraksjon#EBU_EditorialObject",
                identifier="http://example.com/test_abstraksjon#EBU_EditorialObject",
                title={"en": "Is not added twice"},
            ),
        },
        modelProperties={
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn": ModelProperty(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                title={"en": "Is not added twice"},
            )
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    elements = [URIRef("http://example.com/test_abstraksjon#EBU_EditorialObject")]
    props = [
        URIRef(
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn"
        )
    ]

    input_model = add_elements_to_model(input_model, graph, elements)
    input_model = add_properties_to_model(input_model, graph, props)

    assert input_model == expected


def test_parse_handles_escaped_double_quote(
    mock_organizations_and_reference_data: Mock,
) -> None:

    src = """
<rdf:RDF
    xmlns:dct="http://purl.org/dc/terms/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:modelldcatno="https://data.norge.no/vocabulary/modelldcatno#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:digdir="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#"
    xmlns:dcat="http://www.w3.org/ns/dcat#"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
  <dcat:CatalogRecord rdf:about="https://informationmodels.staging.fellesdatakatalog.digdir.no/informationmodels/77e07f69-5fb4-30c7-afca-bffe179dc3b3">
    <foaf:primaryTopic>
      <owl:NamedIndividual rdf:about="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell">
        <dct:description xml:lang="nb">handles escaped \"double quote\"</dct:description>
        <rdf:type rdf:resource="https://data.norge.no/vocabulary/modelldcatno#InformationModel"/>
      </owl:NamedIndividual>
    </foaf:primaryTopic>
    <dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime"
    >2020-10-13T11:35:47.394Z</dct:modified>
    <dct:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime"
    >2020-10-13T11:35:47.394Z</dct:issued>
    <dct:isPartOf rdf:resource="https://informationmodels.staging.fellesdatakatalog.digdir.no/catalogs/03953a9d-5b6b-34ec-b41c-dcdcb21874d9"/>
    <dct:identifier>77e07f69-5fb4-30c7-afca-bffe179dc3b3</dct:identifier>
  </dcat:CatalogRecord>
</rdf:RDF>"""

    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell": InformationModel(
            description={"nb": 'handles escaped "double quote"'},
            descriptionFormatted={"nb": 'handles escaped "double quote"'},
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
            id="77e07f69-5fb4-30c7-afca-bffe179dc3b3",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-13T11:35:47Z", changed=["2020-10-13T11:35:47Z"]
            ),
            type="informationmodels",
        )
    }

    assert parse_information_models(src, rdf_format="xml") == expected


def test_parse_handles_newline(mock_organizations_and_reference_data: Mock,) -> None:

    src = """
<rdf:RDF
    xmlns:dct="http://purl.org/dc/terms/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:modelldcatno="https://data.norge.no/vocabulary/modelldcatno#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:digdir="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#"
    xmlns:dcat="http://www.w3.org/ns/dcat#"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
  <dcat:CatalogRecord rdf:about="https://informationmodels.staging.fellesdatakatalog.digdir.no/informationmodels/77e07f69-5fb4-30c7-afca-bffe179dc3b3">
    <foaf:primaryTopic>
      <owl:NamedIndividual rdf:about="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell">
        <dct:description xml:lang="nb">handles \n newline</dct:description>
        <rdf:type rdf:resource="https://data.norge.no/vocabulary/modelldcatno#InformationModel"/>
      </owl:NamedIndividual>
    </foaf:primaryTopic>
    <dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime"
    >2020-10-13T11:35:47.394Z</dct:modified>
    <dct:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime"
    >2020-10-13T11:35:47.394Z</dct:issued>
    <dct:isPartOf rdf:resource="https://informationmodels.staging.fellesdatakatalog.digdir.no/catalogs/03953a9d-5b6b-34ec-b41c-dcdcb21874d9"/>
    <dct:identifier>77e07f69-5fb4-30c7-afca-bffe179dc3b3</dct:identifier>
  </dcat:CatalogRecord>
</rdf:RDF>"""

    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell": InformationModel(
            description={"nb": "handles \n newline"},
            descriptionFormatted={"nb": "handles \n newline"},
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
            id="77e07f69-5fb4-30c7-afca-bffe179dc3b3",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-13T11:35:47Z", changed=["2020-10-13T11:35:47Z"]
            ),
            type="informationmodels",
        )
    }

    assert parse_information_models(src, rdf_format="xml") == expected


def test_elements_from_properties_are_added_to_model() -> None:
    src = """@prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .

    digdir:Diversemodell  a    modelldcatno:InformationModel , owl:NamedIndividual ;
            modelldcatno:informationModelIdentifier
                    "https://www.digdir.no/diversemodell" .

    digdir:kjønn  a                      owl:NamedIndividual , modelldcatno:Attribute ;
            dct:identifier               "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn" ;
            dct:title                    "kjønn"@nb ;
            modelldcatno:hasValueFrom    digdir:Kjønn .

    digdir:Kjønn  a                      modelldcatno:CodeList , owl:NamedIndividual ;
      dct:identifier                "missing-element"^^xsd:string ;
      dct:title                      "Kjønn"@nb , "Kjønn"@nn , "Sex"@en ."""

    expected = InformationModel(
        uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
        harvest=HarvestMetaData(),
        informationModelIdentifier="https://www.digdir.no/diversemodell",
        modelElements={
            "missing-element": ModelElement(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                identifier="missing-element",
                title={"en": "Sex", "nn": "Kjønn", "nb": "Kjønn"},
                elementTypes=[
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#CodeList",
                ],
                codes=[],
            )
        },
        modelProperties={
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn": ModelProperty(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                title={"nb": "kjønn"},
                propertyTypes=[
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                ],
                hasValueFrom="missing-element",
            )
        },
    )

    input_model = InformationModel(
        uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
        harvest=HarvestMetaData(),
        informationModelIdentifier="https://www.digdir.no/diversemodell",
    )

    graph = Graph().parse(data=src, format="turtle")
    props = [
        URIRef(
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn"
        )
    ]

    input_model = add_properties_to_model(input_model, graph, props)

    assert input_model == expected
