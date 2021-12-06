from fdk_rdf_parser.classes import (
    ConceptSchema,
    EuDataTheme,
    LosNode,
    MediaTypeOrExtent,
    MediaTypeOrExtentType,
    SkosCode,
)
from fdk_rdf_parser.reference_data import (
    DataServiceReferenceData,
    DatasetReferenceData,
    PublicServiceReferenceData,
)


data_service_reference_data = DataServiceReferenceData(
    media_types={
        "www.iana.org/assignments/media-types/text/csv": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/text/csv",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="csv",
            code="text/csv",
        ),
        "www.iana.org/assignments/media-types/text/html": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/text/html",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="html",
            code="text/html",
        ),
        "www.iana.org/assignments/media-types/application/json": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/json",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="json",
            code="application/json",
        ),
        "www.iana.org/assignments/media-types/application/rdf+xml": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/rdf+xml",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="rdf+xml",
            code="application/rdf+xml",
        ),
        "www.iana.org/assignments/media-types/application/xml": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/xml",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="xml",
            code="application/xml",
        ),
        "www.iana.org/assignments/media-types/application/ld+json": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/ld+json",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="ld+json",
            code="application/ld+json",
        ),
        "www.iana.org/assignments/media-types/text/turtle": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/text/turtle",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="turtle",
            code="text/turtle",
        ),
        "www.iana.org/assignments/media-types/application/vnd.geo+json": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/vnd.geo+json",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="vnd.geo+json",
            code="application/vnd.geo+json",
        ),
        "publications.europa.eu/resource/authority/file-type/7Z": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/7Z",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="7Z",
            code="7Z",
        ),
        "publications.europa.eu/resource/authority/file-type/AAC": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/AAC",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="AAC",
            code="AAC",
        ),
        "publications.europa.eu/resource/authority/file-type/AKN4EU_ZIP": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/AKN4EU_ZIP",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="AKN4EU_ZIP",
            code="AKN4EU_ZIP",
        ),
        "publications.europa.eu/resource/authority/file-type/XML": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/XML",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="XML",
            code="XML",
        ),
    }
)

public_service_reference_data = PublicServiceReferenceData(
    linguisticsystem={
        "publications.europa.eu/resource/authority/language": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language",
            code=None,
            prefLabel={"en": "Languages Named Authority List"},
        ),
        "publications.europa.eu/resource/authority/language/ENG": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/ENG",
            code="ENG",
            prefLabel={
                "en": "English",
                "nb": "Engelsk",
                "nn": "Engelsk",
                "no": "Engelsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOB": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NOB",
            code="NOB",
            prefLabel={
                "en": "Norwegian Bokmål",
                "nb": "Norsk Bokmål",
                "nn": "Norsk Bokmål",
                "no": "Norsk Bokmål",
            },
        ),
        "publications.europa.eu/resource/authority/language/NNO": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NNO",
            code="NNO",
            prefLabel={
                "en": "Norwegian Nynorsk",
                "nb": "Norsk Nynorsk",
                "nn": "Norsk Nynorsk",
                "no": "Norsk Nynorsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOR": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NOR",
            code="NOR",
            prefLabel={"nb": "Norsk", "nn": "Norsk", "no": "Norsk", "en": "Norwegian"},
        ),
        "publications.europa.eu/resource/authority/language/SMI": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/SMI",
            code="SMI",
            prefLabel={"en": "Sami languages"},
        ),
    },
)

dataset_reference_data = DatasetReferenceData(
    provenancestatement={
        "data.brreg.no/datakatalog/provinens": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens",
            code=None,
            prefLabel={"no": "Opphav", "en": "Provinens"},
        ),
        "data.brreg.no/datakatalog/provinens/bruker": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker",
            code="BRUKER",
            prefLabel={
                "nb": "Brukerinnsamlede data",
                "nn": "Brukerinnsamlede data",
                "en": "User collection",
            },
        ),
        "data.brreg.no/datakatalog/provinens/nasjonal": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/nasjonal",
            code="NASJONAL",
            prefLabel={
                "en": "Authoritativ source",
                "nb": "Autoritativ kilde",
                "nn": "Autoritativ kilde",
            },
        ),
        "data.brreg.no/datakatalog/provinens/tredjepart": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/tredjepart",
            code="TREDJEPART",
            prefLabel={"en": "Third party", "nb": "Tredjepart", "nn": "Tredjepart"},
        ),
        "data.brreg.no/datakatalog/provinens/vedtak": SkosCode(
            uri="http://data.brreg.no/datakatalog/provinens/vedtak",
            code="VEDTAK",
            prefLabel={"nb": "Vedtak", "nn": "Vedtak", "en": "Governmental decisions"},
        ),
    },
    rightsstatement={
        "publications.europa.eu/resource/authority/access-right": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right",
            code=None,
            prefLabel={"en": "Access right Named Authority List"},
        ),
        "publications.europa.eu/resource/authority/access-right/NON_PUBLIC": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC",
            code="NON_PUBLIC",
            prefLabel={"en": "Non-public"},
        ),
        "publications.europa.eu/resource/authority/access-right/PUBLIC": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/PUBLIC",
            code="PUBLIC",
            prefLabel={"en": "Public"},
        ),
        "publications.europa.eu/resource/authority/access-right/RESTRICTED": SkosCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED",
            code="RESTRICTED",
            prefLabel={"en": "Restricted"},
        ),
    },
    frequency={
        "publications.europa.eu/resource/authority/frequency": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency",
            code=None,
            prefLabel={"en": "Frequency"},
        ),
        "publications.europa.eu/resource/authority/frequency/ANNUAL": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL",
            code="ANNUAL",
            prefLabel={"en": "annual"},
        ),
        "publications.europa.eu/resource/authority/frequency/DAILY": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/DAILY",
            code="DAILY",
            prefLabel={"en": "daily"},
        ),
        "publications.europa.eu/resource/authority/frequency/MONTHLY": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/MONTHLY",
            code="MONTHLY",
            prefLabel={"en": "monthly"},
        ),
        "publications.europa.eu/resource/authority/frequency/NEVER": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/NEVER",
            code="NEVER",
            prefLabel={"en": "never"},
        ),
        "publications.europa.eu/resource/authority/frequency/WEEKLY": SkosCode(
            uri="http://publications.europa.eu/resource/authority/frequency/WEEKLY",
            code="WEEKLY",
            prefLabel={"en": "weekly"},
        ),
    },
    linguisticsystem={
        "publications.europa.eu/resource/authority/language": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language",
            code=None,
            prefLabel={"en": "Languages Named Authority List"},
        ),
        "publications.europa.eu/resource/authority/language/ENG": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/ENG",
            code="ENG",
            prefLabel={
                "en": "English",
                "nb": "Engelsk",
                "nn": "Engelsk",
                "no": "Engelsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOB": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NOB",
            code="NOB",
            prefLabel={
                "en": "Norwegian Bokmål",
                "nb": "Norsk Bokmål",
                "nn": "Norsk Bokmål",
                "no": "Norsk Bokmål",
            },
        ),
        "publications.europa.eu/resource/authority/language/NNO": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NNO",
            code="NNO",
            prefLabel={
                "en": "Norwegian Nynorsk",
                "nb": "Norsk Nynorsk",
                "nn": "Norsk Nynorsk",
                "no": "Norsk Nynorsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOR": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/NOR",
            code="NOR",
            prefLabel={"nb": "Norsk", "nn": "Norsk", "no": "Norsk", "en": "Norwegian"},
        ),
        "publications.europa.eu/resource/authority/language/SMI": SkosCode(
            uri="http://publications.europa.eu/resource/authority/language/SMI",
            code="SMI",
            prefLabel={"en": "Sami languages"},
        ),
    },
    referencetypes={
        "purl.org/dc/terms/hasVersion": SkosCode(
            uri="http://purl.org/dc/terms/hasVersion",
            code="hasVersion",
            prefLabel={"en": "Has version"},
        ),
        "purl.org/dc/terms/isPartOf": SkosCode(
            uri="http://purl.org/dc/terms/isPartOf",
            code="isPartOf",
            prefLabel={"en": "Is Part Of"},
        ),
        "purl.org/dc/terms/isReferencedBy": SkosCode(
            uri="http://purl.org/dc/terms/isReferencedBy",
            code="isReferencedBy",
            prefLabel={
                "en": "Is Referenced By",
                "nn": "Er referert av",
                "nb": "Er referert av",
            },
        ),
        "purl.org/dc/terms/isReplacedBy": SkosCode(
            uri="http://purl.org/dc/terms/isReplacedBy",
            code="isReplacedBy",
            prefLabel={"en": "Is replaced by"},
        ),
        "purl.org/dc/terms/isRequiredBy": SkosCode(
            uri="http://purl.org/dc/terms/isRequiredBy",
            code="requires",
            prefLabel={"en": "Is required by"},
        ),
        "purl.org/dc/terms/isVersionOf": SkosCode(
            uri="http://purl.org/dc/terms/isVersionOf",
            code="isVersionOf",
            prefLabel={"en": "Is version of"},
        ),
        "purl.org/dc/terms/reference-types": SkosCode(
            uri="http://purl.org/dc/terms/reference-types",
            code=None,
            prefLabel={"nb": "Referanse typer"},
        ),
        "purl.org/dc/terms/references": SkosCode(
            uri="http://purl.org/dc/terms/references",
            code="references",
            prefLabel={"en": "References"},
        ),
        "purl.org/dc/terms/relation": SkosCode(
            uri="http://purl.org/dc/terms/relation",
            code="relation",
            prefLabel={"en": "Has relation to"},
        ),
        "purl.org/dc/terms/replaces": SkosCode(
            uri="http://purl.org/dc/terms/replaces",
            code="replaces",
            prefLabel={"en": "Replaces"},
        ),
        "purl.org/dc/terms/requires": SkosCode(
            uri="http://purl.org/dc/terms/requires",
            code="requires",
            prefLabel={"en": "Requires"},
        ),
        "purl.org/dc/terms/source": SkosCode(
            uri="http://purl.org/dc/terms/source",
            code="source",
            prefLabel={"en": "Source"},
        ),
    },
    openlicenses={
        "creativecommons.org/licenses/by/4.0": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/",
            code="CC BY 4.0",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "creativecommons.org/licenses/by/4.0/deed.no": SkosCode(
            uri="http://creativecommons.org/licenses/by/4.0/deed.no",
            code="CC BY 4.0 DEED",
            prefLabel={"en": "Creative Commons Attribution 4.0 International"},
        ),
        "creativecommons.org/publicdomain/zero/1.0": SkosCode(
            uri="https://creativecommons.org/publicdomain/zero/1.0/",
            code="CC0 1.0",
            prefLabel={"en": "Creative Commons Universal Public Domain Dedication"},
        ),
        "data.norge.no/nlod": SkosCode(
            uri="http://data.norge.no/nlod/",
            code="NLOD",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "data.norge.no/nlod/no/1.0": SkosCode(
            uri="https://data.norge.no/nlod/no/1.0",
            code="NLOD10",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "data.norge.no/nlod/no/2.0": SkosCode(
            uri="http://data.norge.no/nlod/no/2.0",
            code="NLOD20",
            prefLabel={"en": "Norwegian Licence for Open Government Data"},
        ),
        "ftp://data.norge.no/no/protocol": SkosCode(
            uri="ftp://data.norge.no/no/protocol",
            code="NOPROTOCOL",
            prefLabel={"en": "No protocol example"},
        ),
    },
    location={
        "sws.geonames.org/3144096": SkosCode(
            uri="http://sws.geonames.org/3144096/",
            code="http://sws.geonames.org/3144096/",
            prefLabel={"no": "Norge"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/173159": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173159",
            code="https://data.geonorge.no/administrativeEnheter/fylke/id/173159",
            prefLabel={"no": "Oslo"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/173068": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/173068",
            code="https://data.geonorge.no/administrativeEnheter/kommune/id/173068",
            prefLabel={"no": "Trondheim"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/173152": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173152",
            code="https://data.geonorge.no/administrativeEnheter/fylke/id/173152",
            prefLabel={"no": "Rogaland"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/173142": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/173142",
            code="https://data.geonorge.no/administrativeEnheter/fylke/id/173142",
            prefLabel={"no": "Finnmárku"},
        ),
        "data.geonorge.no/administrativeEnheter/nasjon/id/173163": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
            code="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
            prefLabel={"no": "Norge"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/173018": SkosCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/173018",
            code="https://data.geonorge.no/administrativeEnheter/kommune/id/173018",
            prefLabel={"no": "Oslo"},
        ),
    },
    eu_data_themes={
        "publications.europa.eu/resource/authority/data-theme/AGRI": EuDataTheme(
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
        "publications.europa.eu/resource/authority/data-theme/ECON": EuDataTheme(
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
        "publications.europa.eu/resource/authority/data-theme/HEAL": EuDataTheme(
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
        "publications.europa.eu/resource/authority/data-theme/TRAN": EuDataTheme(
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
        "psi.norge.no/los/tema/kultur": LosNode(
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
        "psi.norge.no/los/ord/film-og-kino": LosNode(
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
        "psi.norge.no/los/ord/utlan-og-reservasjon": LosNode(
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
        "psi.norge.no/los/tema/kultur-idrett-og-fritid": LosNode(
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
        "psi.norge.no/los/ord/kulturtilbud": LosNode(
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
        "psi.norge.no/los/ord/tilpasset-opplaring": LosNode(
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
        "psi.norge.no/los/tema/grunnskole": LosNode(
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
        "psi.norge.no/los/tema/skole-og-utdanning": LosNode(
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
    media_types={
        "www.iana.org/assignments/media-types/text/csv": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/text/csv",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="csv",
            code="text/csv",
        ),
        "www.iana.org/assignments/media-types/text/html": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/text/html",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="html",
            code="text/html",
        ),
        "www.iana.org/assignments/media-types/application/json": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/json",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="json",
            code="application/json",
        ),
        "www.iana.org/assignments/media-types/application/rdf+xml": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/rdf+xml",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="rdf+xml",
            code="application/rdf+xml",
        ),
        "www.iana.org/assignments/media-types/application/xml": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/xml",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="xml",
            code="application/xml",
        ),
        "www.iana.org/assignments/media-types/application/ld+json": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/ld+json",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="ld+json",
            code="application/ld+json",
        ),
        "www.iana.org/assignments/media-types/text/turtle": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/text/turtle",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="turtle",
            code="text/turtle",
        ),
        "www.iana.org/assignments/media-types/application/vnd.geo+json": MediaTypeOrExtent(
            uri="https://www.iana.org/assignments/media-types/application/vnd.geo+json",
            type=MediaTypeOrExtentType.MEDIA_TYPE,
            name="vnd.geo+json",
            code="application/vnd.geo+json",
        ),
        "publications.europa.eu/resource/authority/file-type/7Z": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/7Z",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="7Z",
            code="7Z",
        ),
        "publications.europa.eu/resource/authority/file-type/AAC": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/AAC",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="AAC",
            code="AAC",
        ),
        "publications.europa.eu/resource/authority/file-type/AKN4EU_ZIP": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/AKN4EU_ZIP",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="AKN4EU_ZIP",
            code="AKN4EU_ZIP",
        ),
        "publications.europa.eu/resource/authority/file-type/XML": MediaTypeOrExtent(
            uri="http://publications.europa.eu/resource/authority/file-type/XML",
            type=MediaTypeOrExtentType.FILE_TYPE,
            name="XML",
            code="XML",
        ),
    },
)
