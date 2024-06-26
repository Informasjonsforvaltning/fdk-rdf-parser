from dataclasses import asdict
from unittest.mock import Mock

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser import (
    parse_information_model,
    parse_information_model_as_dict,
    parse_information_models,
)
from fdk_rdf_parser.classes import (
    Catalog,
    DCATContactPoint,
    DctStandard,
    Format,
    HarvestMetaData,
    InformationModel,
    LosNode,
    Publisher,
    ReferenceDataCode,
    Temporal,
)
from fdk_rdf_parser.classes.model_element import (
    ModelCodeElement,
    ModelElement,
)
from fdk_rdf_parser.classes.model_property import ModelProperty
from fdk_rdf_parser.parse_functions import _parse_information_model
from fdk_rdf_parser.parse_functions.info_model import (
    add_elements_to_model,
    add_properties_to_model,
)


def test_parse_info_model_no_elements(
    mock_reference_data_client: Mock,
) -> None:
    src = """@prefix adms:  <http://www.w3.org/ns/adms#> .
@prefix at:    <http://publications.europa.eu/ontology/authority/> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
@prefix xkos:  <https://rdf-vocabulary.ddialliance.org/xkos/> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix dc:   <http://purl.org/dc/elements/1.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix prof:  <https://www.w3.org/ns/dx/prof/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

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
        dct:conformsTo          <https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model> ;
        dct:description    "Modell med diverse i. Inneholder modellelementer som AltMuligModell skal peke til."@nb ;
        dct:hasFormat      <https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png> , <https://format.for/mat> ;
        dct:identifier     "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell" ;
        dct:isPartOf       digdir:AltMuligModell ;
        dct:isReplacedBy   digdir:AdresseModell ;
        dct:issued         "2016-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:language       <http://publications.europa.eu/resource/authority/language/NOB> ;
        dct:license        <http://publications.europa.eu/resource/authority/licence/CC_BY_4_0> , [ ] ;
        dct:modified       "2017-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:publisher      digdir:Utgiver ;
        dct:spatial        <https://data.geonorge.no/administrativeEnheter/nasjon/id/173163> ;
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
        prof:isProfileOf   <https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model> ;
        modelldcatno:informationModelIdentifier
                "https://www.digdir.no/diversemodell" .

<http://publications.europa.eu/resource/authority/language/NOB>
        a           skos:Concept;
        at:authority-code      "NOB";
        skos:prefLabel     "Norsk Bokmål"@nb , "Norsk Bokmål"@nn , "Norsk Bokmål"@no , "Norwegian Bokmål"@en .

<http://publications.europa.eu/resource/authority/licence/CC_BY_4_0>
        a           skos:Concept;
        dc:identifier      "CC BY 4.0";
        skos:prefLabel     "Creative Commons Navngivelse 4.0 Internasjonal"@no , "Creative Commons Attribution 4.0 International"@en .

<https://data.geonorge.no/administrativeEnheter/nasjon/id/173163>
        a               dct:Location;
        dct:identifier  "173163";
        dct:title       "Norge" .

<https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png>
        a           foaf:Document ;
        dct:format  <http://publications.europa.eu/resource/authority/file-type/PNG> ;
        dct:language <http://pubs.europa.eu/resource/authority/language/NOR> ;
        rdfs:seeAlso <https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png> ;
        dct:title   "Image of the logical data model (LDM)"@en .

<https://format.for/mat>
        a           foaf:Document ;
        dct:format  <http://publications.europa.eu/resource/authority/file-type/JPG> ;
        dct:title   "Image of test"@en .

<https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model>
        a                dct:Standard ;
        rdfs:seeAlso     <https://statswiki.unece.org/display/gsim/GSIM+resources+repository> ;
        dct:title        "Generic Statistical Information Model"@en ;
        owl:versionInfo  "??" .

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

<https://psi.norge.no/los/tema/skole-og-utdanning>
        a                  skos:Concept ;
        skos:prefLabel     "Skule og utdanning"@nn , "Skole og utdanning"@nb , "Schools and education"@en ;
        <https://fellesdatakatalog.digdir.no/ontology/internal/themePath>
                "skole-og-utdanning" ."""

    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell": InformationModel(
            identifier={
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell"
            },
            publisher=Publisher(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Utgiver",
                id="991825827",
                name="Digitaliseringsdirektoratet",
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
                DCATContactPoint(
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
                ReferenceDataCode(
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
                firstHarvested="2020-10-13T11:35:47Z", modified="2020-10-13T11:35:47Z"
            ),
            conformsTo=[
                DctStandard(
                    uri="https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model",
                    title={"en": "Generic Statistical Information Model"},
                    seeAlso=[
                        "https://statswiki.unece.org/display/gsim/GSIM+resources+repository"
                    ],
                    versionInfo="??",
                )
            ],
            license=[
                ReferenceDataCode(
                    uri="http://publications.europa.eu/resource/authority/licence/CC_BY_4_0",
                    code="CC BY 4.0",
                    prefLabel={
                        "no": "Creative Commons Navngivelse 4.0 Internasjonal",
                        "en": "Creative Commons Attribution 4.0 International",
                    },
                )
            ],
            informationModelIdentifier="https://www.digdir.no/diversemodell",
            spatial=[
                ReferenceDataCode(
                    uri="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
                    code="173163",
                    prefLabel={"nb": "Norge"},
                )
            ],
            isPartOf="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AltMuligModell",
            isProfileOf=[
                DctStandard(
                    uri="https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model",
                    title={"en": "Generic Statistical Information Model"},
                    seeAlso=[
                        "https://statswiki.unece.org/display/gsim/GSIM+resources+repository"
                    ],
                    versionInfo="??",
                )
            ],
            isReplacedBy="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AdresseModell",
            temporal=[
                Temporal(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Tidsintervall",
                    startDate="2016-02-11T00:00:00+01:00",
                )
            ],
            hasFormat=[
                Format(
                    uri="https://format.for/mat",
                    title={"en": "Image of test"},
                    format="http://publications.europa.eu/resource/authority/file-type/JPG",
                ),
                Format(
                    uri="https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png",
                    title={"en": "Image of the logical data model (LDM)"},
                    format="http://publications.europa.eu/resource/authority/file-type/PNG",
                    seeAlso="https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png",
                    language=ReferenceDataCode(
                        uri="http://pubs.europa.eu/resource/authority/language/NOR",
                    ),
                ),
            ],
            homepage="https://www.difi.no/fagomrader-og-tjenester/digitalisering-og-samordning/nasjonal-arkitektur/informasjonsforvaltning/adresse-felles-informasjonsmodell",
            status="http://purl.org/adms/status/Completed",
            versionInfo="1.0",
            versionNotes={"nb": "Lagt til objekttypen Timeline"},
            themeUris=["https://psi.norge.no/los/tema/skole-og-utdanning"],
            losTheme=[
                LosNode(
                    isTema=True,
                    losPaths=["skole-og-utdanning"],
                    code="skole-og-utdanning",
                    name={
                        "nn": "Skule og utdanning",
                        "nb": "Skole og utdanning",
                        "en": "Schools and education",
                    },
                    uri="https://psi.norge.no/los/tema/skole-og-utdanning",
                )
            ],
            type="informationmodels",
        )
    }

    assert parse_information_models(src) == expected


def test_parse_info_model_with_elements(
    mock_reference_data_client: Mock,
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
        dct:publisher       digdir:Utgiver ;
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
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Utgiver",
                id="991825827",
                name="Digitaliseringsdirektoratet",
                prefLabel={"nb": "Digitaliseringsdirektoratet"},
            ),
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
            id="77e07f69-5fb4-30c7-afca-bffe179dc3b3",
            harvest=HarvestMetaData(
                firstHarvested="2020-10-13T11:35:47Z", modified="2020-10-13T11:35:47Z"
            ),
            catalog=Catalog(
                id="03953a9d-5b6b-34ec-b41c-dcdcb21874d9",
                publisher=Publisher(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Utgiver",
                    id="991825827",
                    name="Digitaliseringsdirektoratet",
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
                        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#sivilstand",
                        "statsborgerskap",
                    ],
                    elementTypes={
                        "http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject",
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#ObjectType",
                    },
                ),
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn": ModelElement(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                    identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                    title={"nb": "Kjønn", "en": "Sex", "nn": "Kjønn"},
                    elementTypes={
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#CodeList",
                    },
                    codes=[
                        ModelCodeElement(
                            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kvinne",
                            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kvinne",
                            prefLabel={"en": "woman", "nn": "kvinne", "nb": "kvinne"},
                            inScheme={
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
                            },
                            topConceptOf={
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
                            },
                            nextElement={
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Mann"
                            },
                        ),
                        ModelCodeElement(
                            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Mann",
                            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Mann",
                            prefLabel={"en": "man", "nb": "mann"},
                            inScheme={
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
                            },
                            nextElement={
                                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Ubestemt"
                            },
                        ),
                    ],
                ),
            },
            modelProperties={
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn": ModelProperty(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                    identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                    title={"nb": "kjønn"},
                    propertyTypes={
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                    },
                    maxOccurs=1,
                    sequenceNumber=3,
                    hasValueFrom="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                ),
                "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#sivilstand": ModelProperty(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#sivilstand",
                    identifier="sivilstand",
                    title={"nb": "sivilstand"},
                    propertyTypes={
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                    },
                ),
                "statsborgerskap": ModelProperty(
                    identifier="statsborgerskap",
                    title={"nb": "statsborgerskap"},
                    propertyTypes={
                        "http://www.w3.org/2002/07/owl#NamedIndividual",
                        "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                    },
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
                      modelldcatno:hasProperty  [ a owl:NamedIndividual , modelldcatno:Attribute ;
                                                  dct:title                    "kjønn"@nb ] ] ;
            modelldcatno:containsModelElement
                    [ a                modelldcatno:ObjectType , <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject> , owl:NamedIndividual ;
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
            "http://example.com/test_abstraksjon#EBU_EditorialObject",
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
        ],
        modelElements={
            "http://example.com/test_abstraksjon#EBU_EditorialObject": ModelElement(
                identifier="http://example.com/test_abstraksjon#EBU_EditorialObject",
                elementTypes={
                    "http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#EditorialObject",
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#ObjectType",
                },
            ),
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn": ModelElement(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn"
            ),
        },
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell"
    )

    assert _parse_information_model(graph, URIRef("record"), subject) == expected


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
    mock_reference_data_client: Mock,
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
                firstHarvested="2020-10-13T11:35:47Z", modified="2020-10-13T11:35:47Z"
            ),
            type="informationmodels",
        )
    }

    assert parse_information_models(src, rdf_format="xml") == expected


def test_parse_handles_newline(
    mock_reference_data_client: Mock,
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
                firstHarvested="2020-10-13T11:35:47Z", modified="2020-10-13T11:35:47Z"
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
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn": ModelElement(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
                identifier="missing-element",
                title={"en": "Sex", "nn": "Kjønn", "nb": "Kjønn"},
                elementTypes={
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#CodeList",
                },
                codes=[],
            )
        },
        modelProperties={
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn": ModelProperty(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#kjønn",
                title={"nb": "kjønn"},
                propertyTypes={
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                },
                hasValueFrom="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Kjønn",
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


def test_subjects_from_elements_and_properties_added_to_contains_subjects() -> None:
    src = """@prefix owl:   <http://www.w3.org/2002/07/owl#> .
    @prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
    @prefix dct:   <http://purl.org/dc/terms/> .
    @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
    @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
    @prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .

    digdir:Diversemodell  a    modelldcatno:InformationModel , owl:NamedIndividual ;
        dct:subject             ex-abstrakt:begrep0 , ex-abstrakt:begrep1 ;
        modelldcatno:containsModelElement
                ex-abstrakt:Elm .

    ex-abstrakt:prop  a             owl:NamedIndividual , modelldcatno:Attribute ;
        dct:subject                   ex-abstrakt:begrep3 .

    ex-abstrakt:Elm  a              modelldcatno:ObjectType , owl:NamedIndividual ;
        modelldcatno:hasProperty      ex-abstrakt:prop ;
        dct:subject                   ex-abstrakt:begrep2 ."""

    expected = InformationModel(
        uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell",
        harvest=HarvestMetaData(),
        subjects={
            "http://example.com/test_abstraksjon#begrep0",
            "http://example.com/test_abstraksjon#begrep1",
        },
        containsSubjects={
            "http://example.com/test_abstraksjon#begrep0",
            "http://example.com/test_abstraksjon#begrep1",
            "http://example.com/test_abstraksjon#begrep2",
            "http://example.com/test_abstraksjon#begrep3",
        },
        containsModelElements=["http://example.com/test_abstraksjon#Elm"],
        modelElements={
            "http://example.com/test_abstraksjon#Elm": ModelElement(
                uri="http://example.com/test_abstraksjon#Elm",
                subject="http://example.com/test_abstraksjon#begrep2",
                hasProperty=["http://example.com/test_abstraksjon#prop"],
                elementTypes={
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#ObjectType",
                },
            )
        },
        modelProperties={
            "http://example.com/test_abstraksjon#prop": ModelProperty(
                uri="http://example.com/test_abstraksjon#prop",
                subject="http://example.com/test_abstraksjon#begrep3",
                propertyTypes={
                    "http://www.w3.org/2002/07/owl#NamedIndividual",
                    "https://data.norge.no/vocabulary/modelldcatno#Attribute",
                },
            )
        },
        type="informationmodels",
    )

    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell"
    )

    result = _parse_information_model(graph, URIRef("record"), subject)

    assert result == expected


def test_code_element_subjects_are_added_to_containssubjects() -> None:
    src = """@prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .
        @prefix adms:  <http://www.w3.org/ns/adms#> .
        @prefix dct:   <http://purl.org/dc/terms/> .
        @prefix owl:   <http://www.w3.org/2002/07/owl#> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix locn: <http://www.w3.org/ns/locn#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        @prefix xkos: <https://rdf-vocabulary.ddialliance.org/xkos/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
        @prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .

        digdir:PersonOgEnhet  a         modelldcatno:InformationModel ;
                modelldcatno:containsModelElement digdir:Person;
                dct:identifier          "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#PersonOgEnhet"^^xsd:string .

        digdir:Person  a                     modelldcatno:ObjectType ;
                modelldcatno:hasProperty       digdir:sivilstand .


        digdir:Sivilstand  a                 modelldcatno:CodeList ;
                dct:subject        <http://begrepskatalogen/begrep/88804c58-ff43-11e6-9d97-005056825ca0> ;
                dct:title              "Sivilstand"@nb .

        digdir:sivilstand  a             modelldcatno:Attribute ;
                dct:subject <http://begrepskatalogen/begrep/88804c58-ff43-11e6-9d97-005056825ca0> ;
                dct:title          "sivilstand"@nb ;
                modelldcatno:hasValueFrom         digdir:Sivilstand ;
                modelldcatno:sequenceNumber "11"^^xsd:positiveInteger ;
                xsd:maxOccurs            "1"^^xsd:nonNegativeInteger .

        digdir:Ugift  a             modelldcatno:CodeElement ;
                dct:identifier    "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Ugift"^^xsd:string ;
                skos:inScheme     digdir:Sivilstand ;
                dct:subject       <http://begrepskatalogen/begrep/92f82e89-fb04-11e9-92b0-005056828ed3> ;
                xkos:next         digdir:Gift ;
                skos:topConceptOf digdir:Sivilstand ;
                skos:prefLabel    "sivilstand ugift"@nb ;
                skos:notation     "ugift"^^xsd:string .

    """
    graph = Graph().parse(data=src, format="turtle")
    subject = URIRef(
        "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#PersonOgEnhet"
    )
    result = _parse_information_model(graph, URIRef("record"), subject)
    assert result.containsSubjects is not None and len(result.containsSubjects) == 2


def test_parse_single_info_model(
    mock_reference_data_client: Mock,
) -> None:
    src = """@prefix adms:  <http://www.w3.org/ns/adms#> .
@prefix at:    <http://publications.europa.eu/ontology/authority/> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix ex-abstrakt: <http://example.com/test_abstraksjon#> .
@prefix xkos:  <https://rdf-vocabulary.ddialliance.org/xkos/> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix dc:   <http://purl.org/dc/elements/1.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix digdir: <https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix prof:  <https://www.w3.org/ns/dx/prof/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

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
        dct:conformsTo          <https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model> ;
        dct:description    "Modell med diverse i. Inneholder modellelementer som AltMuligModell skal peke til."@nb ;
        dct:hasFormat      <https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png> , <https://format.for/mat> ;
        dct:identifier     "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell" ;
        dct:isPartOf       digdir:AltMuligModell ;
        dct:isReplacedBy   digdir:AdresseModell ;
        dct:issued         "2016-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:language       <http://publications.europa.eu/resource/authority/language/NOB> ;
        dct:license        <http://publications.europa.eu/resource/authority/licence/CC_BY_4_0> , [ ] ;
        dct:modified       "2017-09-28T00:00:00+01:00"^^xsd:dateTime ;
        dct:publisher      digdir:Utgiver ;
        dct:spatial        <https://data.geonorge.no/administrativeEnheter/nasjon/id/173163> ;
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
        prof:isProfileOf   <https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model> ;
        modelldcatno:informationModelIdentifier
                "https://www.digdir.no/diversemodell" .

<http://publications.europa.eu/resource/authority/language/NOB>
        a           skos:Concept;
        at:authority-code      "NOB";
        skos:prefLabel     "Norsk Bokmål"@nb , "Norsk Bokmål"@nn , "Norsk Bokmål"@no , "Norwegian Bokmål"@en .

<http://publications.europa.eu/resource/authority/licence/CC_BY_4_0>
        a           skos:Concept;
        dc:identifier      "CC BY 4.0";
        skos:prefLabel     "Creative Commons Navngivelse 4.0 Internasjonal"@no , "Creative Commons Attribution 4.0 International"@en .

<https://data.geonorge.no/administrativeEnheter/nasjon/id/173163>
        a               dct:Location;
        dct:identifier  "173163";
        dct:title       "Norge" .

<https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png>
        a           foaf:Document ;
        dct:format  <http://publications.europa.eu/resource/authority/file-type/PNG> ;
        dct:language <http://pubs.europa.eu/resource/authority/language/NOR> ;
        rdfs:seeAlso <https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png> ;
        dct:title   "Image of the logical data model (LDM)"@en .

<https://format.for/mat>
        a           foaf:Document ;
        dct:format  <http://publications.europa.eu/resource/authority/file-type/JPG> ;
        dct:title   "Image of test"@en .

<https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model>
        a                dct:Standard ;
        rdfs:seeAlso     <https://statswiki.unece.org/display/gsim/GSIM+resources+repository> ;
        dct:title        "Generic Statistical Information Model"@en ;
        owl:versionInfo  "??" .

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

<https://psi.norge.no/los/tema/skole-og-utdanning>
        a                  skos:Concept ;
        skos:prefLabel     "Skule og utdanning"@nn , "Skole og utdanning"@nb , "Schools and education"@en ;
        <https://fellesdatakatalog.digdir.no/ontology/internal/themePath>
                "skole-og-utdanning" ."""

    expected = InformationModel(
        identifier={
            "https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Diversemodell"
        },
        publisher=Publisher(
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Utgiver",
            id="991825827",
            name="Digitaliseringsdirektoratet",
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
            DCATContactPoint(
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
            ReferenceDataCode(
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
            firstHarvested="2020-10-13T11:35:47Z", modified="2020-10-13T11:35:47Z"
        ),
        conformsTo=[
            DctStandard(
                uri="https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model",
                title={"en": "Generic Statistical Information Model"},
                seeAlso=[
                    "https://statswiki.unece.org/display/gsim/GSIM+resources+repository"
                ],
                versionInfo="??",
            )
        ],
        license=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/licence/CC_BY_4_0",
                code="CC BY 4.0",
                prefLabel={
                    "no": "Creative Commons Navngivelse 4.0 Internasjonal",
                    "en": "Creative Commons Attribution 4.0 International",
                },
            )
        ],
        informationModelIdentifier="https://www.digdir.no/diversemodell",
        spatial=[
            ReferenceDataCode(
                uri="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
                code="173163",
                prefLabel={"nb": "Norge"},
            )
        ],
        isPartOf="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AltMuligModell",
        isProfileOf=[
            DctStandard(
                uri="https://statswiki.unece.org/display/gsim/Generic+Statistical+Information+Model",
                title={"en": "Generic Statistical Information Model"},
                seeAlso=[
                    "https://statswiki.unece.org/display/gsim/GSIM+resources+repository"
                ],
                versionInfo="??",
            )
        ],
        isReplacedBy="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#AdresseModell",
        temporal=[
            Temporal(
                uri="https://raw.githubusercontent.com/Informasjonsforvaltning/model-publisher/master/src/model/model-catalog.ttl#Tidsintervall",
                startDate="2016-02-11T00:00:00+01:00",
            )
        ],
        hasFormat=[
            Format(
                uri="https://format.for/mat",
                title={"en": "Image of test"},
                format="http://publications.europa.eu/resource/authority/file-type/JPG",
            ),
            Format(
                uri="https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png",
                title={"en": "Image of the logical data model (LDM)"},
                format="http://publications.europa.eu/resource/authority/file-type/PNG",
                seeAlso="https://github.com/statisticsnorway/gsim-raml-schema/blob/master/ssb_gsim_ldm.png",
                language=ReferenceDataCode(
                    uri="http://pubs.europa.eu/resource/authority/language/NOR",
                ),
            ),
        ],
        homepage="https://www.difi.no/fagomrader-og-tjenester/digitalisering-og-samordning/nasjonal-arkitektur/informasjonsforvaltning/adresse-felles-informasjonsmodell",
        status="http://purl.org/adms/status/Completed",
        versionInfo="1.0",
        versionNotes={"nb": "Lagt til objekttypen Timeline"},
        themeUris=["https://psi.norge.no/los/tema/skole-og-utdanning"],
        losTheme=[
            LosNode(
                isTema=True,
                losPaths=["skole-og-utdanning"],
                code="skole-og-utdanning",
                name={
                    "nn": "Skule og utdanning",
                    "nb": "Skole og utdanning",
                    "en": "Schools and education",
                },
                uri="https://psi.norge.no/los/tema/skole-og-utdanning",
            )
        ],
        type="informationmodels",
    )

    assert parse_information_model(src) == expected
    assert parse_information_model_as_dict(src) == asdict(expected)
