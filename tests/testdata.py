from fdk_rdf_parser.classes import SkosCode
from fdk_rdf_parser.reference_data import ReferenceData

org_response_0 = """
@prefix br:    <https://github.com/Informasjonsforvaltning/organization-catalogue/blob/develop/src/main/resources/ontology/organization-catalogue.owl#> .
@prefix adms:  <http://www.w3.org/ns/adms#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix org:   <http://www.w3.org/ns/org#> .
@prefix rov:   <http://www.w3.org/ns/regorg#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://organizations.fellestestkatalog.no/organizations/123456789>
        a                      rov:RegisteredOrganization ;
        org:subOrganizationOf  <https://organizations.fellestestkatalog.no/organizations/987654321> ;
        rov:legalName          "Digitaliseringsdirektoratet" ;
        rov:orgType            "ORGL" ;
        rov:registration       [ a                  adms:Identifier ;
                                 dct:issued         "2007-10-15" ;
                                 skos:notation      "123456789" ;
                                 adms:schemaAgency  "Brønnøysundregistrene"
                               ] ;
        foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
        br:municipality        <https://data.geonorge.no/administrativeEnheter/kommune/id/173018> ;
        br:nace                "84.110" ;
        br:norwegianRegistry   <https://data.brreg.no/enhetsregisteret/api/enheter/123456789> ;
        br:orgPath             "/STAT/987654321/123456789" ;
        br:sectorCode          "6100" .
"""

org_response_1 = """
@prefix br:    <https://github.com/Informasjonsforvaltning/organization-catalogue/blob/develop/src/main/resources/ontology/organization-catalogue.owl#> .
@prefix adms:  <http://www.w3.org/ns/adms#> .
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix org:   <http://www.w3.org/ns/org#> .
@prefix rov:   <http://www.w3.org/ns/regorg#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://organizations.fellestestkatalog.no/organizations/987654321>
        a                      rov:RegisteredOrganization ;
        rov:legalName          "Testdirektoratet" ;
        rov:orgType            "ORGL" ;
        rov:registration       [ a                  adms:Identifier ;
                                 dct:issued         "2007-10-15" ;
                                 skos:notation      "987654321" ;
                                 adms:schemaAgency  "Brønnøysundregistrene"
                               ] ;
        br:municipality        <https://data.geonorge.no/administrativeEnheter/kommune/id/173018> ;
        br:nace                "84.110" ;
        br:norwegianRegistry   <https://data.brreg.no/enhetsregisteret/api/enheter/987654321> ;
        br:orgPath             "/STAT/987654321" ;
        br:sectorCode          "6100" .
"""

reference_data = ReferenceData(
    provenancestatement={
        "http://data.brreg.no/datakatalog/provinens": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens",
            code=None,
            prefLabel={"no": "Opphav", "en": "Provinens"},
        ),
        "http://data.brreg.no/datakatalog/provinens/bruker": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker",
            code="BRUKER",
            prefLabel={
                "nb": "Brukerinnsamlede data",
                "nn": "Brukerinnsamlede data",
                "en": "User collection",
            },
        ),
        "http://data.brreg.no/datakatalog/provinens/nasjonal": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/nasjonal",
            code="NASJONAL",
            prefLabel={
                "en": "Authoritativ source",
                "nb": "Autoritativ kilde",
                "nn": "Autoritativ kilde",
            },
        ),
        "http://data.brreg.no/datakatalog/provinens/tredjepart": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/tredjepart",
            code="TREDJEPART",
            prefLabel={"en": "Third party", "nb": "Tredjepart", "nn": "Tredjepart"},
        ),
        "http://data.brreg.no/datakatalog/provinens/vedtak": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/vedtak",
            code="VEDTAK",
            prefLabel={"nb": "Vedtak", "nn": "Vedtak", "en": "Governmental decisions"},
        ),
    },
    rightsstatement={
        "http://publications.europa.eu/resource/authority/access-right": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right",
            code=None,
            prefLabel={"en": "Access right Named Authority List"},
        ),
        "http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC",
            code="NON_PUBLIC",
            prefLabel={"en": "Non-public"},
        ),
        "http://publications.europa.eu/resource/authority/access-right/PUBLIC": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/PUBLIC",
            code="PUBLIC",
            prefLabel={"en": "Public"},
        ),
        "http://publications.europa.eu/resource/authority/access-right/RESTRICTED": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED",
            code="RESTRICTED",
            prefLabel={"en": "Restricted"},
        ),
    },
    frequency={
        "http://publications.europa.eu/resource/authority/frequency": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency",
            code=None,
            prefLabel={"en": "Frequency"},
        ),
        "http://publications.europa.eu/resource/authority/frequency/ANNUAL": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL",
            code="ANNUAL",
            prefLabel={"en": "annual"},
        ),
        "http://publications.europa.eu/resource/authority/frequency/DAILY": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/DAILY",
            code="DAILY",
            prefLabel={"en": "daily"},
        ),
        "http://publications.europa.eu/resource/authority/frequency/MONTHLY": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/MONTHLY",
            code="MONTHLY",
            prefLabel={"en": "monthly"},
        ),
        "http://publications.europa.eu/resource/authority/frequency/NEVER": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/NEVER",
            code="NEVER",
            prefLabel={"en": "never"},
        ),
        "http://publications.europa.eu/resource/authority/frequency/WEEKLY": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/WEEKLY",
            code="WEEKLY",
            prefLabel={"en": "weekly"},
        ),
    },
    linguisticsystem={
        "http://publications.europa.eu/resource/authority/language": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language",
            code=None,
            prefLabel={"en": "Languages Named Authority List"},
        ),
        "http://publications.europa.eu/resource/authority/language/ENG": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/ENG",
            code="ENG",
            prefLabel={
                "en": "English",
                "nb": "Engelsk",
                "nn": "Engelsk",
                "no": "Engelsk",
            },
        ),
        "http://publications.europa.eu/resource/authority/language/NOB": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NOB",
            code="NOB",
            prefLabel={
                "en": "Norwegian Bokmål",
                "nb": "Norsk Bokmål",
                "nn": "Norsk Bokmål",
                "no": "Norsk Bokmål",
            },
        ),
        "http://publications.europa.eu/resource/authority/language/NOR": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NOR",
            code="NOR",
            prefLabel={"nb": "Norsk", "nn": "Norsk", "no": "Norsk", "en": "Norwegian"},
        ),
        "http://publications.europa.eu/resource/authority/language/SMI": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/SMI",
            code="SMI",
            prefLabel={"en": "Sami languages"},
        ),
    },
    referencetypes={
        "http://purl.org/dc/terms/hasVersion": SkosCode(
            uri="http://purl.org/dc/terms/hasVersion",
            code="hasVersion",
            prefLabel={"en": "Has version"},
        ),
        "http://purl.org/dc/terms/isPartOf": SkosCode(
            uri="http://purl.org/dc/terms/isPartOf",
            code="isPartOf",
            prefLabel={"en": "Is Part Of"},
        ),
        "http://purl.org/dc/terms/isReferencedBy": SkosCode(
            uri="http://purl.org/dc/terms/isReferencedBy",
            code="isReferencedBy",
            prefLabel={
                "en": "Is Referenced By",
                "nn": "Er referert av",
                "nb": "Er referert av",
            },
        ),
        "http://purl.org/dc/terms/isReplacedBy": SkosCode(
            uri="http://purl.org/dc/terms/isReplacedBy",
            code="isReplacedBy",
            prefLabel={"en": "Is replaced by"},
        ),
        "http://purl.org/dc/terms/isRequiredBy": SkosCode(
            uri="http://purl.org/dc/terms/isRequiredBy",
            code="requires",
            prefLabel={"en": "Is required by"},
        ),
        "http://purl.org/dc/terms/isVersionOf": SkosCode(
            uri="http://purl.org/dc/terms/isVersionOf",
            code="isVersionOf",
            prefLabel={"en": "Is version of"},
        ),
        "http://purl.org/dc/terms/reference-types": SkosCode(
            uri="http://purl.org/dc/terms/reference-types",
            code=None,
            prefLabel={"nb": "Referanse typer"},
        ),
        "http://purl.org/dc/terms/references": SkosCode(
            uri="http://purl.org/dc/terms/references",
            code="references",
            prefLabel={"en": "References"},
        ),
        "http://purl.org/dc/terms/relation": SkosCode(
            uri="http://purl.org/dc/terms/relation",
            code="relation",
            prefLabel={"en": "Has relation to"},
        ),
        "http://purl.org/dc/terms/replaces": SkosCode(
            uri="http://purl.org/dc/terms/replaces",
            code="replaces",
            prefLabel={"en": "Replaces"},
        ),
        "http://purl.org/dc/terms/requires": SkosCode(
            uri="http://purl.org/dc/terms/requires",
            code="requires",
            prefLabel={"en": "Requires"},
        ),
        "http://purl.org/dc/terms/source": SkosCode(
            uri="http://purl.org/dc/terms/source",
            code="source",
            prefLabel={"en": "Source"},
        ),
    },
    openlicenses={
        "http://creativecommons.org/licenses/by/4.0/": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/",
            code="CC BY 4.0",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "http://creativecommons.org/licenses/by/4.0/deed.no": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/deed.no",
            code="CC BY 4.0 DEED",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "http://creativecommons.org/publicdomain/zero/1.0/": SkosCode(
            uri="http://creativecommons.org/publicdomain/zero/1.0/",
            code="CC0 1.0",
            prefLabel={"en": "Creative Commons Universal Public Domain Dedication"},
        ),
        "http://data.norge.no/nlod/": SkosCode(
            uri="http://data.norge.no/nlod/",
            code="NLOD",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "http://data.norge.no/nlod/no/1.0": SkosCode(
            uri="http://data.norge.no/nlod/no/1.0",
            code="NLOD10",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "http://data.norge.no/nlod/no/2.0": SkosCode(
            uri="http://data.norge.no/nlod/no/2.0",
            code="NLOD20",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
    },
    location={
        "http://sws.geonames.org/3144096/": SkosCode(
            uri="http://sws.geonames.org/3144096/",
            code="http://sws.geonames.org/3144096/",
            prefLabel={"no": "Norge"},
        ),
        "https://data.geonorge.no/administrativeEnheter/fylke/id/173159": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173159",
            code="https://data.geonorge.no/administrativeEnheter/fylke/id/173159",
            prefLabel={"no": "Oslo"},
        ),
        "https://data.geonorge.no/administrativeEnheter/kommune/id/173068": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/173068",
            code="https://data.geonorge.no/administrativeEnheter/kommune/id/173068",
            prefLabel={"no": "Trondheim"},
        ),
        "https://data.geonorge.no/administrativeEnheter/fylke/id/173152": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173152",
            code="https://data.geonorge.no/administrativeEnheter/fylke/id/173152",
            prefLabel={"no": "Rogaland"},
        ),
        "https://data.geonorge.no/administrativeEnheter/fylke/id/173142": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173142",
            code="https://data.geonorge.no/administrativeEnheter/fylke/id/173142",
            prefLabel={"no": "Finnmárku"},
        ),
        "https://data.geonorge.no/administrativeEnheter/nasjon/id/173163": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
            code="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
            prefLabel={"no": "Norge"},
        ),
        "https://data.geonorge.no/administrativeEnheter/kommune/id/173018": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/173018",
            code="https://data.geonorge.no/administrativeEnheter/kommune/id/173018",
            prefLabel={"no": "Oslo"},
        ),
    },
)
