from fdk_rdf_parser.classes import ConceptSchema, SkosCode, ThemeEU, ThemeLOS
from fdk_rdf_parser.reference_data import DataServiceReferenceData, DatasetReferenceData


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

<https://organizations.fellestestkatalog.no/organizations/111111111>
        a                      rov:RegisteredOrganization ;
        org:subOrganizationOf  <https://organizations.fellestestkatalog.no/organizations/111111111> ;
        rov:legalName          "Pythondirektoratet" ;
        rov:orgType            "ORGL" ;
        rov:registration       [ a                  adms:Identifier ;
                                 dct:issued         "2007-10-15" ;
                                 skos:notation      "111111111" ;
                                 adms:schemaAgency  "Brønnøysundregistrene"
                               ] ;
        foaf:name              "Pythondirektoratet"@nn , "Pythondirektoratet"@nb , "Norwegian Python Agency"@en ;
        br:municipality        <https://data.geonorge.no/administrativeEnheter/kommune/id/173018> ;
        br:nace                "84.110" ;
        br:norwegianRegistry   <https://data.brreg.no/enhetsregisteret/api/enheter/111111111> ;
        br:orgPath             "/STAT/987654321/111111111" ;
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

data_service_reference_data = DataServiceReferenceData(
    media_types={
        "text/csv": SkosCode(uri=None, code="text/csv", prefLabel={"nb": "CSV"}),
        "text/html": SkosCode(uri=None, code="text/html", prefLabel={"nb": "HTML"}),
        "application/json": SkosCode(
            uri=None, code="application/json", prefLabel={"nb": "JSON"}
        ),
        "application/rdf+xml": SkosCode(
            uri=None, code="application/rdf+xml", prefLabel={"nb": "RDF/XML"}
        ),
        "text/plain": SkosCode(uri=None, code="text/plain", prefLabel={"nb": "TXT"}),
        "application/xml": SkosCode(
            uri=None, code="application/xml", prefLabel={"nb": "XML"}
        ),
        "application/ld+json": SkosCode(
            uri=None, code="application/ld+json", prefLabel={"nb": "JSON-LD"}
        ),
        "text/turtle": SkosCode(
            uri=None, code="text/turtle", prefLabel={"nb": "Turtle"}
        ),
    }
)

dataset_reference_data = DatasetReferenceData(
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
        "http://creativecommons.org/licenses/by/4.0": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/",
            code="CC BY 4.0",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "http://creativecommons.org/licenses/by/4.0/deed.no": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/deed.no",
            code="CC BY 4.0 DEED",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "http://creativecommons.org/publicdomain/zero/1.0": SkosCode(
            uri="http://creativecommons.org/publicdomain/zero/1.0/",
            code="CC0 1.0",
            prefLabel={"en": "Creative Commons Universal Public Domain Dedication"},
        ),
        "http://data.norge.no/nlod": SkosCode(
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
        "https://creativecommons.org/licenses/by/4.0": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/",
            code="CC BY 4.0",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "https://creativecommons.org/licenses/by/4.0/deed.no": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/deed.no",
            code="CC BY 4.0 DEED",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "https://creativecommons.org/publicdomain/zero/1.0": SkosCode(
            uri="http://creativecommons.org/publicdomain/zero/1.0/",
            code="CC0 1.0",
            prefLabel={"en": "Creative Commons Universal Public Domain Dedication"},
        ),
        "https://data.norge.no/nlod": SkosCode(
            uri="http://data.norge.no/nlod/",
            code="NLOD",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "https://data.norge.no/nlod/no/1.0": SkosCode(
            uri="http://data.norge.no/nlod/no/1.0",
            code="NLOD10",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "https://data.norge.no/nlod/no/2.0": SkosCode(
            uri="http://data.norge.no/nlod/no/2.0",
            code="NLOD20",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
    },
    location={
        "http://sws.geonames.org/3144096": SkosCode(
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
    eu_themes={
        "http://publications.europa.eu/resource/authority/data-theme/AGRI": ThemeEU(
            id="http://publications.europa.eu/resource/authority/data-theme/AGRI",
            code="AGRI",
            startUse="2015-10-01",
            title={"en": "Agriculture, fisheries, forestry and food"},
            conceptSchema=ConceptSchema(
                id="http://publications.europa.eu/resource/authority/data-theme",
                title={"en": "Dataset types Named Authority List"},
                versioninfo="20160921-0",
                versionnumber="20160921-0",
            ),
        ),
        "http://publications.europa.eu/resource/authority/data-theme/ECON": ThemeEU(
            id="http://publications.europa.eu/resource/authority/data-theme/ECON",
            code="ECON",
            startUse="2015-10-01",
            title={"nb": "Økonomi og finans", "en": "Economy and finance"},
            conceptSchema=ConceptSchema(
                id="http://publications.europa.eu/resource/authority/data-theme",
                title={"en": "Dataset types Named Authority List"},
                versioninfo="20160921-0",
                versionnumber="20160921-0",
            ),
        ),
        "http://publications.europa.eu/resource/authority/data-theme/HEAL": ThemeEU(
            id="http://publications.europa.eu/resource/authority/data-theme/HEAL",
            code="HEAL",
            startUse="2015-10-01",
            title={"nb": "Helse"},
            conceptSchema=ConceptSchema(
                id="http://publications.europa.eu/resource/authority/data-theme",
                title={"en": "Dataset types Named Authority List"},
                versioninfo="20160921-0",
                versionnumber="20160921-0",
            ),
        ),
        "http://publications.europa.eu/resource/authority/data-theme/TRAN": ThemeEU(
            id="http://publications.europa.eu/resource/authority/data-theme/TRAN",
            code="TRAN",
            startUse="2015-10-01",
            title={"en": "Transport"},
            conceptSchema=ConceptSchema(
                id="http://publications.europa.eu/resource/authority/data-theme",
                title={"en": "Dataset types Named Authority List"},
                versioninfo="20160921-0",
                versionnumber="20160921-0",
            ),
        ),
    },
    los_themes={
        "https://psi.norge.no/los/tema/kultur": ThemeLOS(
            children=[
                "https://psi.norge.no/los/ord/film-og-kino",
                "https://psi.norge.no/los/ord/kulturtilbud",
            ],
            parents=["https://psi.norge.no/los/tema/kultur-idrett-og-fritid"],
            isTema=True,
            losPaths=["kultur-idrett-og-fritid/kultur"],
            name={"nn": "Kultur", "nb": "Kultur", "en": "Culture"},
            definition=None,
            uri="https://psi.norge.no/los/tema/kultur",
            synonyms=[],
            relatedTerms=None,
        ),
        "https://psi.norge.no/los/ord/film-og-kino": ThemeLOS(
            children=None,
            parents=["https://psi.norge.no/los/tema/kultur"],
            isTema=False,
            losPaths=["kultur-idrett-og-fritid/kultur/film-og-kino"],
            name={"nn": "Film og kino", "nb": "Film og kino", "en": "Film and cinema"},
            definition=None,
            uri="https://psi.norge.no/los/ord/film-og-kino",
            synonyms=["Billettbestilling", "Kinobillett", "Filmklubb"],
            relatedTerms=["https://psi.norge.no/los/ord/kulturtilbud"],
        ),
        "https://psi.norge.no/los/ord/utlan-og-reservasjon": ThemeLOS(
            children=None,
            parents=["https://psi.norge.no/los/tema/bibliotek"],
            isTema=False,
            losPaths=["kultur-idrett-og-fritid/bibliotek/utlan-og-reservasjon"],
            name={
                "nn": "Utlån og reservasjon",
                "nb": "Utlån og reservasjon",
                "en": "Loans and reservations",
            },
            definition=None,
            uri="https://psi.norge.no/los/ord/utlan-og-reservasjon",
            synonyms=[],
            relatedTerms=None,
        ),
        "https://psi.norge.no/los/tema/kultur-idrett-og-fritid": ThemeLOS(
            children=[
                "https://psi.norge.no/los/tema/kultur",
                "https://psi.norge.no/los/tema/bibliotek",
            ],
            parents=None,
            isTema=True,
            losPaths=["kultur-idrett-og-fritid"],
            name={
                "nn": "Kultur, idrett og fritid",
                "nb": "Kultur, idrett og fritid",
                "en": "Culture, sport and recreation",
            },
            definition=None,
            uri="https://psi.norge.no/los/tema/kultur-idrett-og-fritid",
            synonyms=[],
            relatedTerms=None,
        ),
        "https://psi.norge.no/los/ord/kulturtilbud": ThemeLOS(
            children=None,
            parents=["https://psi.norge.no/los/tema/kultur"],
            isTema=False,
            losPaths=["kultur-idrett-og-fritid/kultur/kulturtilbud"],
            name={
                "nn": "Kulturtilbod",
                "nb": "Kulturtilbud",
                "en": "Cultural activities",
            },
            definition=None,
            uri="https://psi.norge.no/los/ord/kulturtilbud",
            synonyms=["Dans", "Teater", "Musikk"],
            relatedTerms=["https://psi.norge.no/los/ord/film-og-kino"],
        ),
        "https://psi.norge.no/los/ord/tilpasset-opplaring": ThemeLOS(
            children=None,
            parents=["https://psi.norge.no/los/tema/grunnskole"],
            isTema=False,
            losPaths=["skole-og-utdanning/grunnskole/tilpasset-opplaring"],
            name={
                "nn": "Tilpassa opplæring",
                "nb": "Tilpasset opplæring",
                "en": "Adapted education",
            },
            definition=None,
            uri="https://psi.norge.no/los/ord/tilpasset-opplaring",
            synonyms=["Friskule", "Friskole"],
            relatedTerms=None,
        ),
        "https://psi.norge.no/los/tema/grunnskole": ThemeLOS(
            children=["https://psi.norge.no/los/ord/tilpasset-opplaring"],
            parents=["https://psi.norge.no/los/tema/skole-og-utdanning"],
            isTema=True,
            losPaths=["skole-og-utdanning/grunnskole"],
            name={"nn": "Grunnskule", "nb": "Grunnskole", "en": "Compulsory education"},
            definition=None,
            uri="https://psi.norge.no/los/tema/grunnskole",
            synonyms=[],
            relatedTerms=None,
        ),
        "https://psi.norge.no/los/tema/skole-og-utdanning": ThemeLOS(
            children=["https://psi.norge.no/los/tema/grunnskole"],
            parents=None,
            isTema=True,
            losPaths=["skole-og-utdanning"],
            name={
                "nn": "Skule og utdanning",
                "nb": "Skole og utdanning",
                "en": "Schools and education",
            },
            definition=None,
            uri="https://psi.norge.no/los/tema/skole-og-utdanning",
            synonyms=[],
            relatedTerms=None,
        ),
    },
)
