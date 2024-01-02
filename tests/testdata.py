from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.reference_data import (
    DatasetReferenceData,
    PublicServiceReferenceData,
)

public_service_reference_data = PublicServiceReferenceData(
    linguisticsystem={
        "publications.europa.eu/resource/authority/language": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language",
            code=None,
            prefLabel={"en": "Languages Named Authority List"},
        ),
        "publications.europa.eu/resource/authority/language/ENG": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/ENG",
            code="ENG",
            prefLabel={
                "en": "English",
                "nb": "Engelsk",
                "nn": "Engelsk",
                "no": "Engelsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOB": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/NOB",
            code="NOB",
            prefLabel={
                "en": "Norwegian Bokmål",
                "nb": "Norsk Bokmål",
                "nn": "Norsk Bokmål",
                "no": "Norsk Bokmål",
            },
        ),
        "publications.europa.eu/resource/authority/language/NNO": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/NNO",
            code="NNO",
            prefLabel={
                "en": "Norwegian Nynorsk",
                "nb": "Norsk Nynorsk",
                "nn": "Norsk Nynorsk",
                "no": "Norsk Nynorsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOR": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/NOR",
            code="NOR",
            prefLabel={"nb": "Norsk", "nn": "Norsk", "no": "Norsk", "en": "Norwegian"},
        ),
        "publications.europa.eu/resource/authority/language/SMI": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/SMI",
            code="SMI",
            prefLabel={"en": "Sami languages"},
        ),
    },
    organization_types={
        "purl.org/adms/publishertype/IndustryConsortium": ReferenceDataCode(
            uri="http://purl.org/adms/publishertype/IndustryConsortium",
            code="IndustryConsortium",
            prefLabel={
                "nn": "Industrikonsortium",
                "nb": "Industrikonsortium",
                "en": "Industry consortium",
            },
        ),
        "purl.org/adms/publishertype/NationalAuthority": ReferenceDataCode(
            uri="http://purl.org/adms/publishertype/NationalAuthority",
            code="NationalAuthority",
            prefLabel={
                "nn": "Nasjonal myndigheit",
                "nb": "Nasjonal myndighet",
                "en": "National authority",
            },
        ),
    },
    role_types={
        "data.norge.no/vocabulary/role-type#data-consumer": ReferenceDataCode(
            uri="https://data.norge.no/vocabulary/role-type#data-consumer",
            code="data-consumer",
            prefLabel={
                "nb": "datakonsument",
                "en": "data consumer",
            },
        ),
        "data.norge.no/vocabulary/role-type#data-provider": ReferenceDataCode(
            uri="https://data.norge.no/vocabulary/role-type#data-provider",
            code="data-provider",
            prefLabel={"nb": "dataleverandør", "en": "data provider"},
        ),
    },
)

dataset_reference_data = DatasetReferenceData(
    provenancestatement={
        "data.brreg.no/datakatalog/provinens/bruker": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/bruker",
            code="BRUKER",
            prefLabel={
                "nn": "Brukerinnsamlede data",
                "nb": "Brukerinnsamlede data",
                "en": "User collection",
            },
        ),
        "data.brreg.no/datakatalog/provinens/nasjonal": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/nasjonal",
            code="NASJONAL",
            prefLabel={
                "nn": "Autoritativ kilde",
                "nb": "Autoritativ kilde",
                "en": "Authoritativ source",
            },
        ),
        "data.brreg.no/datakatalog/provinens/tredjepart": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/tredjepart",
            code="TREDJEPART",
            prefLabel={"nn": "Tredjepart", "nb": "Tredjepart", "en": "Third party"},
        ),
        "data.brreg.no/datakatalog/provinens/vedtak": ReferenceDataCode(
            uri="http://data.brreg.no/datakatalog/provinens/vedtak",
            code="VEDTAK",
            prefLabel={"nn": "Vedtak", "nb": "Vedtak", "en": "Governmental decisions"},
        ),
    },
    rightsstatement={
        "publications.europa.eu/resource/authority/access-right/CONFIDENTIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/CONFIDENTIAL",
            code="CONFIDENTIAL",
            prefLabel={"en": "confidential"},
        ),
        "publications.europa.eu/resource/authority/access-right/NON_PUBLIC": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC",
            code="NON_PUBLIC",
            prefLabel={"en": "non-public"},
        ),
        "publications.europa.eu/resource/authority/access-right/NORMAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/NORMAL",
            code="NORMAL",
            prefLabel={"en": "normal"},
        ),
        "publications.europa.eu/resource/authority/access-right/OP_DATPRO": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/OP_DATPRO",
            code="OP_DATPRO",
            prefLabel={"en": "Provisional data"},
        ),
        "publications.europa.eu/resource/authority/access-right/PUBLIC": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/PUBLIC",
            code="PUBLIC",
            prefLabel={"en": "public"},
        ),
        "publications.europa.eu/resource/authority/access-right/RESTRICTED": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/RESTRICTED",
            code="RESTRICTED",
            prefLabel={"en": "restricted"},
        ),
        "publications.europa.eu/resource/authority/access-right/SENSITIVE": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/access-right/SENSITIVE",
            code="SENSITIVE",
            prefLabel={"en": "sensitive"},
        ),
    },
    frequency={
        "publications.europa.eu/resource/authority/frequency/ANNUAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL",
            code="ANNUAL",
            prefLabel={"nn": "årleg", "no": "årlig", "nb": "årlig", "en": "annual"},
        ),
        "publications.europa.eu/resource/authority/frequency/ANNUAL_2": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL_2",
            code="ANNUAL_2",
            prefLabel={
                "nn": "halvårleg",
                "no": "halvårlig",
                "nb": "halvårlig",
                "en": "semiannual",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/ANNUAL_3": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/ANNUAL_3",
            code="ANNUAL_3",
            prefLabel={
                "nn": "tre gongar per år",
                "no": "tre ganger per år",
                "nb": "tre ganger per år",
                "en": "three times a year",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/BIDECENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/BIDECENNIAL",
            code="BIDECENNIAL",
            prefLabel={
                "nn": "kvart tjuande år",
                "no": "hvert tjuende år",
                "nb": "hvert tjuende år",
                "en": "bidecennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/BIENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/BIENNIAL",
            code="BIENNIAL",
            prefLabel={
                "nn": "annakvart år",
                "no": "annethvert år",
                "nb": "annethvert år",
                "en": "biennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/BIHOURLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/BIHOURLY",
            code="BIHOURLY",
            prefLabel={
                "nn": "annakvar time",
                "no": "annenhver time",
                "nb": "annenhver time",
                "en": "bihourly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/BIMONTHLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/BIMONTHLY",
            code="BIMONTHLY",
            prefLabel={
                "nn": "annakvar månad",
                "no": "annenhver måned",
                "nb": "annenhver måned",
                "en": "bimonthly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/BIWEEKLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/BIWEEKLY",
            code="BIWEEKLY",
            prefLabel={
                "nn": "kvar fjortande dag",
                "no": "hver fjortende dag",
                "nb": "hver fjortende dag",
                "en": "biweekly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/CONT": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/CONT",
            code="CONT",
            prefLabel={
                "nn": "kontinuerleg",
                "no": "kontinuerlig",
                "nb": "kontinuerlig",
                "en": "continuous",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/DAILY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/DAILY",
            code="DAILY",
            prefLabel={"nn": "dagleg", "no": "daglig", "nb": "daglig", "en": "daily"},
        ),
        "publications.europa.eu/resource/authority/frequency/DAILY_2": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/DAILY_2",
            code="DAILY_2",
            prefLabel={
                "nn": "to gongar per dag",
                "no": "to ganger per dag",
                "nb": "to ganger per dag",
                "en": "twice a day",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/DECENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/DECENNIAL",
            code="DECENNIAL",
            prefLabel={
                "nn": "kvart tiande år",
                "no": "hvert tiende år",
                "nb": "hvert tiende år",
                "en": "decennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/HOURLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/HOURLY",
            code="HOURLY",
            prefLabel={
                "nn": "kvar time",
                "no": "hver time",
                "nb": "hver time",
                "en": "hourly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/IRREG": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/IRREG",
            code="IRREG",
            prefLabel={
                "nn": "uregelmessig",
                "no": "uregelmessig",
                "nb": "uregelmessig",
                "en": "irregular",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/MONTHLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/MONTHLY",
            code="MONTHLY",
            prefLabel={
                "nn": "månadleg",
                "no": "månedlig",
                "nb": "månedlig",
                "en": "monthly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/MONTHLY_2": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/MONTHLY_2",
            code="MONTHLY_2",
            prefLabel={
                "nn": "to gongar i månaden",
                "no": "to ganger i måneden",
                "nb": "to ganger i måneden",
                "en": "semimonthly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/MONTHLY_3": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/MONTHLY_3",
            code="MONTHLY_3",
            prefLabel={
                "nn": "tre gongar i månaden",
                "no": "tre ganger i måneden",
                "nb": "tre ganger i måneden",
                "en": "three times a month",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/NEVER": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/NEVER",
            code="NEVER",
            prefLabel={"nn": "aldri", "no": "aldri", "nb": "aldri", "en": "never"},
        ),
        "publications.europa.eu/resource/authority/frequency/OP_DATPRO": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/OP_DATPRO",
            code="OP_DATPRO",
            prefLabel={"en": "Provisional data"},
        ),
        "publications.europa.eu/resource/authority/frequency/OTHER": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/OTHER",
            code="OTHER",
            prefLabel={"nn": "anna", "no": "annet", "nb": "annet", "en": "other"},
        ),
        "publications.europa.eu/resource/authority/frequency/QUADRENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/QUADRENNIAL",
            code="QUADRENNIAL",
            prefLabel={
                "nn": "kvart fjerde år",
                "no": "hvert fjerde år",
                "nb": "hvert fjerde år",
                "en": "quadrennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/QUARTERLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/QUARTERLY",
            code="QUARTERLY",
            prefLabel={
                "nn": "kvartalsvis",
                "no": "kvartalsvis",
                "nb": "kvartalsvis",
                "en": "quarterly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/QUINQUENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/QUINQUENNIAL",
            code="QUINQUENNIAL",
            prefLabel={
                "nn": "kvart femte år",
                "no": "hvert femte år",
                "nb": "hvert femte år",
                "en": "quinquennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/TRIDECENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/TRIDECENNIAL",
            code="TRIDECENNIAL",
            prefLabel={
                "nn": "kvart trettiande år",
                "no": "hvert trettiende år",
                "nb": "hvert trettiende år",
                "en": "tridecennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/TRIENNIAL": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/TRIENNIAL",
            code="TRIENNIAL",
            prefLabel={
                "nn": "kvart tredje år",
                "no": "hvert tredje år",
                "nb": "hvert tredje år",
                "en": "triennial",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/TRIHOURLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/TRIHOURLY",
            code="TRIHOURLY",
            prefLabel={
                "nn": "kvar tredje time",
                "no": "hver tredje time",
                "nb": "hver tredje time",
                "en": "trihourly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/UNKNOWN": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/UNKNOWN",
            code="UNKNOWN",
            prefLabel={"nn": "ukjent", "no": "ukjent", "nb": "ukjent", "en": "unknown"},
        ),
        "publications.europa.eu/resource/authority/frequency/UPDATE_CONT": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/UPDATE_CONT",
            code="UPDATE_CONT",
            prefLabel={
                "nn": "kontinuerleg oppdatert",
                "no": "kontinuerlig oppdatert",
                "nb": "kontinuerlig oppdatert",
                "en": "continuously updated",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/WEEKLY": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/WEEKLY",
            code="WEEKLY",
            prefLabel={
                "nn": "kvar veke",
                "no": "ukentlig",
                "nb": "ukentlig",
                "en": "weekly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/WEEKLY_2": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/WEEKLY_2",
            code="WEEKLY_2",
            prefLabel={
                "nn": "to gongar i veka",
                "no": "to ganger i uken",
                "nb": "to ganger i uken",
                "en": "semiweekly",
            },
        ),
        "publications.europa.eu/resource/authority/frequency/WEEKLY_3": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/frequency/WEEKLY_3",
            code="WEEKLY_3",
            prefLabel={
                "nn": "tre gongar i veka",
                "no": "tre ganger i uken",
                "nb": "tre ganger i uken",
                "en": "three times a week",
            },
        ),
    },
    linguisticsystem={
        "publications.europa.eu/resource/authority/language/ENG": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/ENG",
            code="ENG",
            prefLabel={
                "nn": "Engelsk",
                "no": "Engelsk",
                "nb": "Engelsk",
                "en": "English",
            },
        ),
        "publications.europa.eu/resource/authority/language/NNO": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/NNO",
            code="NNO",
            prefLabel={
                "nn": "Norsk Nynorsk",
                "no": "Norsk Nynorsk",
                "nb": "Norsk Nynorsk",
                "en": "Norwegian Nynorsk",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOB": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/NOB",
            code="NOB",
            prefLabel={
                "nn": "Norsk Bokmål",
                "no": "Norsk Bokmål",
                "nb": "Norsk Bokmål",
                "en": "Norwegian Bokmål",
            },
        ),
        "publications.europa.eu/resource/authority/language/NOR": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/NOR",
            code="NOR",
            prefLabel={"nn": "Norsk", "no": "Norsk", "nb": "Norsk", "en": "Norwegian"},
        ),
        "publications.europa.eu/resource/authority/language/SMI": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/language/SMI",
            code="SMI",
            prefLabel={"en": "Sami languages"},
        ),
    },
    referencetypes={
        "purl.org/dc/terms/hasVersion": ReferenceDataCode(
            uri="http://purl.org/dc/terms/hasVersion",
            code="hasVersion",
            prefLabel={"nn": "Har versjon", "nb": "Har versjon", "en": "Has version"},
        ),
        "purl.org/dc/terms/isPartOf": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isPartOf",
            code="isPartOf",
            prefLabel={"nn": "Er del av", "nb": "Er en del av", "en": "Is Part Of"},
        ),
        "purl.org/dc/terms/isReferencedBy": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isReferencedBy",
            code="isReferencedBy",
            prefLabel={
                "nn": "Er referert av",
                "nb": "Er referert av",
                "en": "Is Referenced By",
            },
        ),
        "purl.org/dc/terms/isReplacedBy": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isReplacedBy",
            code="isReplacedBy",
            prefLabel={
                "nn": "Er erstatta av",
                "nb": "Er erstattet av",
                "en": "Is replaced by",
            },
        ),
        "purl.org/dc/terms/isRequiredBy": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isRequiredBy",
            code="isRequiredBy",
            prefLabel={
                "nn": "Er påkravd av",
                "nb": "Er påkrevd av",
                "en": "Is required by",
            },
        ),
        "purl.org/dc/terms/isVersionOf": ReferenceDataCode(
            uri="http://purl.org/dc/terms/isVersionOf",
            code="isVersionOf",
            prefLabel={
                "nn": "Er versjon av",
                "nb": "Er versjon av",
                "en": "Is version of",
            },
        ),
        "purl.org/dc/terms/references": ReferenceDataCode(
            uri="http://purl.org/dc/terms/references",
            code="references",
            prefLabel={"nn": "Refererar", "nb": "Refererer", "en": "References"},
        ),
        "purl.org/dc/terms/relation": ReferenceDataCode(
            uri="http://purl.org/dc/terms/relation",
            code="relation",
            prefLabel={
                "nn": "Er relatert til",
                "nb": "Er relatert til",
                "en": "Has relation to",
            },
        ),
        "purl.org/dc/terms/replaces": ReferenceDataCode(
            uri="http://purl.org/dc/terms/replaces",
            code="replaces",
            prefLabel={"nn": "Erstatter", "nb": "Erstatter", "en": "Replaces"},
        ),
        "purl.org/dc/terms/requires": ReferenceDataCode(
            uri="http://purl.org/dc/terms/requires",
            code="requires",
            prefLabel={"nn": "Krevjar", "nb": "Krever", "en": "Requires"},
        ),
        "purl.org/dc/terms/source": ReferenceDataCode(
            uri="http://purl.org/dc/terms/source",
            code="source",
            prefLabel={
                "nn": "Er avleda frå (kjelde)",
                "nb": "Er avledet fra (kilde)",
                "en": "Source",
            },
        ),
    },
    openlicenses={
        "creativecommons.org/licenses/by/4.0": ReferenceDataCode(
            uri="http://creativecommons.org/licenses/by/4.0/",
            code="CC BY 4.0",
            prefLabel={
                "no": "Creative Commons Navngivelse 4.0 Internasjonal",
                "en": "Creative Commons Attribution 4.0 International",
            },
        ),
        "creativecommons.org/licenses/by/4.0/deed.no": ReferenceDataCode(
            uri="http://creativecommons.org/licenses/by/4.0/deed.no",
            code="CC BY 4.0 DEED",
            prefLabel={
                "no": "Creative Commons Navngivelse 4.0 Internasjonal",
                "en": "Creative Commons Attribution 4.0 International",
            },
        ),
        "creativecommons.org/publicdomain/zero/1.0": ReferenceDataCode(
            uri="http://creativecommons.org/publicdomain/zero/1.0/",
            code="CC0 1.0",
            prefLabel={
                "no": "Creative Commons Universal Fristatus-erklæring",
                "en": "Creative Commons Universal Public Domain Dedication",
            },
        ),
        "data.norge.no/nlod": ReferenceDataCode(
            uri="http://data.norge.no/nlod/",
            code="NLOD",
            prefLabel={
                "no": "Norsk lisens for offentlige data",
                "en": "Norwegian Licence for Open Government Data",
            },
        ),
        "data.norge.no/nlod/no": ReferenceDataCode(
            uri="http://data.norge.no/nlod/no/",
            code="NLOD",
            prefLabel={
                "no": "Norsk lisens for offentlige data",
                "en": "Norwegian Licence for Open Government Data",
            },
        ),
        "data.norge.no/nlod/no/1.0": ReferenceDataCode(
            uri="http://data.norge.no/nlod/no/1.0",
            code="NLOD10",
            prefLabel={
                "no": "Norsk lisens for offentlige data",
                "en": "Norwegian Licence for Open Government Data",
            },
        ),
        "data.norge.no/nlod/no/2.0": ReferenceDataCode(
            uri="http://data.norge.no/nlod/no/2.0",
            code="NLOD20",
            prefLabel={
                "no": "Norsk lisens for offentlige data",
                "en": "Norwegian Licence for Open Government Data",
            },
        ),
    },
    location={
        "data.geonorge.no/administrativeEnheter/nasjon/id/173163": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/nasjon/id/173163",
            code="173163",
            prefLabel={"no": "Norge"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/03": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/03",
            code="03",
            prefLabel={"no": "Oslo"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/11": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/11",
            code="11",
            prefLabel={"no": "Rogaland"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/15": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/15",
            code="15",
            prefLabel={"no": "Møre og Romsdal"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/18": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/18",
            code="18",
            prefLabel={"no": "Nordland"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/30": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/30",
            code="30",
            prefLabel={"no": "Viken"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/34": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/34",
            code="34",
            prefLabel={"no": "Innlandet"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/38": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/38",
            code="38",
            prefLabel={"no": "Vestfold og Telemark"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/42": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/42",
            code="42",
            prefLabel={"no": "Agder"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/46": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/46",
            code="46",
            prefLabel={"no": "Vestland"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/50": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/50",
            code="50",
            prefLabel={"no": "Trøndelag"},
        ),
        "data.geonorge.no/administrativeEnheter/fylke/id/54": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/fylke/id/54",
            code="54",
            prefLabel={"no": "Troms og Finnmark"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/0301": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/0301",
            code="0301",
            prefLabel={"no": "Oslo"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1101": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1101",
            code="1101",
            prefLabel={"no": "Eigersund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1103": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1103",
            code="1103",
            prefLabel={"no": "Stavanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1106": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1106",
            code="1106",
            prefLabel={"no": "Haugesund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1108": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1108",
            code="1108",
            prefLabel={"no": "Sandnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1111": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1111",
            code="1111",
            prefLabel={"no": "Sokndal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1112": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1112",
            code="1112",
            prefLabel={"no": "Lund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1114": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1114",
            code="1114",
            prefLabel={"no": "Bjerkreim"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1119": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1119",
            code="1119",
            prefLabel={"no": "Hå"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1120": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1120",
            code="1120",
            prefLabel={"no": "Klepp"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1121": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1121",
            code="1121",
            prefLabel={"no": "Time"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1122": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1122",
            code="1122",
            prefLabel={"no": "Gjesdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1124": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1124",
            code="1124",
            prefLabel={"no": "Sola"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1127": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1127",
            code="1127",
            prefLabel={"no": "Randaberg"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1130": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1130",
            code="1130",
            prefLabel={"no": "Strand"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1133": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1133",
            code="1133",
            prefLabel={"no": "Hjelmeland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1134": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1134",
            code="1134",
            prefLabel={"no": "Suldal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1135": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1135",
            code="1135",
            prefLabel={"no": "Sauda"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1144": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1144",
            code="1144",
            prefLabel={"no": "Kvitsøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1145": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1145",
            code="1145",
            prefLabel={"no": "Bokn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1146": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1146",
            code="1146",
            prefLabel={"no": "Tysvær"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1149": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1149",
            code="1149",
            prefLabel={"no": "Karmøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1151": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1151",
            code="1151",
            prefLabel={"no": "Utsira"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1160": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1160",
            code="1160",
            prefLabel={"no": "Vindafjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1505": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1505",
            code="1505",
            prefLabel={"no": "Kristiansund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1506": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1506",
            code="1506",
            prefLabel={"no": "Molde"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1507": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1507",
            code="1507",
            prefLabel={"no": "Ålesund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1511": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1511",
            code="1511",
            prefLabel={"no": "Vanylven"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1514": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1514",
            code="1514",
            prefLabel={"no": "Sande"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1515": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1515",
            code="1515",
            prefLabel={"no": "Herøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1516": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1516",
            code="1516",
            prefLabel={"no": "Ulstein"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1517": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1517",
            code="1517",
            prefLabel={"no": "Hareid"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1520": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1520",
            code="1520",
            prefLabel={"no": "Ørsta"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1525": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1525",
            code="1525",
            prefLabel={"no": "Stranda"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1528": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1528",
            code="1528",
            prefLabel={"no": "Sykkylven"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1531": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1531",
            code="1531",
            prefLabel={"no": "Sula"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1532": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1532",
            code="1532",
            prefLabel={"no": "Giske"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1535": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1535",
            code="1535",
            prefLabel={"no": "Vestnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1539": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1539",
            code="1539",
            prefLabel={"no": "Rauma"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1547": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1547",
            code="1547",
            prefLabel={"no": "Aukra"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1554": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1554",
            code="1554",
            prefLabel={"no": "Averøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1557": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1557",
            code="1557",
            prefLabel={"no": "Gjemnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1560": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1560",
            code="1560",
            prefLabel={"no": "Tingvoll"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1563": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1563",
            code="1563",
            prefLabel={"no": "Sunndal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1566": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1566",
            code="1566",
            prefLabel={"no": "Surnadal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1573": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1573",
            code="1573",
            prefLabel={"no": "Smøla"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1576": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1576",
            code="1576",
            prefLabel={"no": "Aure"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1577": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1577",
            code="1577",
            prefLabel={"no": "Volda"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1578": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1578",
            code="1578",
            prefLabel={"no": "Fjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1579": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1579",
            code="1579",
            prefLabel={"no": "Hustadvika"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1804": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1804",
            code="1804",
            prefLabel={"no": "Bodø"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1806": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1806",
            code="1806",
            prefLabel={"no": "Narvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1811": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1811",
            code="1811",
            prefLabel={"no": "Bindal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1812": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1812",
            code="1812",
            prefLabel={"no": "Sømna"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1813": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1813",
            code="1813",
            prefLabel={"no": "Brønnøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1815": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1815",
            code="1815",
            prefLabel={"no": "Vega"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1816": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1816",
            code="1816",
            prefLabel={"no": "Vevelstad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1818": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1818",
            code="1818",
            prefLabel={"no": "Herøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1820": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1820",
            code="1820",
            prefLabel={"no": "Alstahaug"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1822": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1822",
            code="1822",
            prefLabel={"no": "Leirfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1824": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1824",
            code="1824",
            prefLabel={"no": "Vefsn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1825": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1825",
            code="1825",
            prefLabel={"no": "Grane"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1826": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1826",
            code="1826",
            prefLabel={"no": "Hattfjelldal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1827": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1827",
            code="1827",
            prefLabel={"no": "Dønna"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1828": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1828",
            code="1828",
            prefLabel={"no": "Nesna"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1832": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1832",
            code="1832",
            prefLabel={"no": "Hemnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1833": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1833",
            code="1833",
            prefLabel={"no": "Rana"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1834": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1834",
            code="1834",
            prefLabel={"no": "Lurøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1835": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1835",
            code="1835",
            prefLabel={"no": "Træna"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1836": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1836",
            code="1836",
            prefLabel={"no": "Rødøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1837": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1837",
            code="1837",
            prefLabel={"no": "Meløy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1838": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1838",
            code="1838",
            prefLabel={"no": "Gildeskål"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1839": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1839",
            code="1839",
            prefLabel={"no": "Beiarn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1840": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1840",
            code="1840",
            prefLabel={"no": "Saltdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1841": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1841",
            code="1841",
            prefLabel={"no": "Fauske"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1845": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1845",
            code="1845",
            prefLabel={"no": "Sørfold"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1848": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1848",
            code="1848",
            prefLabel={"no": "Steigen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1851": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1851",
            code="1851",
            prefLabel={"no": "Lødingen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1853": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1853",
            code="1853",
            prefLabel={"no": "Evenes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1856": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1856",
            code="1856",
            prefLabel={"no": "Røst"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1857": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1857",
            code="1857",
            prefLabel={"no": "Værøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1859": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1859",
            code="1859",
            prefLabel={"no": "Flakstad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1860": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1860",
            code="1860",
            prefLabel={"no": "Vestvågøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1865": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1865",
            code="1865",
            prefLabel={"no": "Vågan"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1866": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1866",
            code="1866",
            prefLabel={"no": "Hadsel"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1867": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1867",
            code="1867",
            prefLabel={"no": "Bø"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1868": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1868",
            code="1868",
            prefLabel={"no": "Øksnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1870": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1870",
            code="1870",
            prefLabel={"no": "Sortland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1871": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1871",
            code="1871",
            prefLabel={"no": "Andøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1874": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1874",
            code="1874",
            prefLabel={"no": "Moskenes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/1875": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/1875",
            code="1875",
            prefLabel={"no": "Hamarøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3001": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3001",
            code="3001",
            prefLabel={"no": "Halden"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3002": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3002",
            code="3002",
            prefLabel={"no": "Moss"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3003": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3003",
            code="3003",
            prefLabel={"no": "Sarpsborg"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3004": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3004",
            code="3004",
            prefLabel={"no": "Fredrikstad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3005": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3005",
            code="3005",
            prefLabel={"no": "Drammen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3006": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3006",
            code="3006",
            prefLabel={"no": "Kongsberg"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3007": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3007",
            code="3007",
            prefLabel={"no": "Ringerike"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3011": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3011",
            code="3011",
            prefLabel={"no": "Hvaler"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3012": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3012",
            code="3012",
            prefLabel={"no": "Aremark"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3013": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3013",
            code="3013",
            prefLabel={"no": "Marker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3014": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3014",
            code="3014",
            prefLabel={"no": "Indre Østfold"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3015": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3015",
            code="3015",
            prefLabel={"no": "Skiptvet"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3016": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3016",
            code="3016",
            prefLabel={"no": "Rakkestad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3017": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3017",
            code="3017",
            prefLabel={"no": "Råde"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3018": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3018",
            code="3018",
            prefLabel={"no": "Våler"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3019": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3019",
            code="3019",
            prefLabel={"no": "Vestby"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3020": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3020",
            code="3020",
            prefLabel={"no": "Nordre Follo"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3021": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3021",
            code="3021",
            prefLabel={"no": "Ås"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3022": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3022",
            code="3022",
            prefLabel={"no": "Frogn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3023": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3023",
            code="3023",
            prefLabel={"no": "Nesodden"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3024": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3024",
            code="3024",
            prefLabel={"no": "Bærum"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3025": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3025",
            code="3025",
            prefLabel={"no": "Asker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3026": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3026",
            code="3026",
            prefLabel={"no": "Aurskog-Høland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3027": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3027",
            code="3027",
            prefLabel={"no": "Rælingen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3028": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3028",
            code="3028",
            prefLabel={"no": "Enebakk"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3029": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3029",
            code="3029",
            prefLabel={"no": "Lørenskog"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3030": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3030",
            code="3030",
            prefLabel={"no": "Lillestrøm"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3031": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3031",
            code="3031",
            prefLabel={"no": "Nittedal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3032": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3032",
            code="3032",
            prefLabel={"no": "Gjerdrum"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3033": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3033",
            code="3033",
            prefLabel={"no": "Ullensaker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3034": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3034",
            code="3034",
            prefLabel={"no": "Nes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3035": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3035",
            code="3035",
            prefLabel={"no": "Eidsvoll"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3036": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3036",
            code="3036",
            prefLabel={"no": "Nannestad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3037": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3037",
            code="3037",
            prefLabel={"no": "Hurdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3038": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3038",
            code="3038",
            prefLabel={"no": "Hole"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3039": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3039",
            code="3039",
            prefLabel={"no": "Flå"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3040": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3040",
            code="3040",
            prefLabel={"no": "Nesbyen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3041": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3041",
            code="3041",
            prefLabel={"no": "Gol"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3042": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3042",
            code="3042",
            prefLabel={"no": "Hemsedal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3043": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3043",
            code="3043",
            prefLabel={"no": "Ål"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3044": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3044",
            code="3044",
            prefLabel={"no": "Hol"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3045": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3045",
            code="3045",
            prefLabel={"no": "Sigdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3046": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3046",
            code="3046",
            prefLabel={"no": "Krødsherad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3047": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3047",
            code="3047",
            prefLabel={"no": "Modum"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3048": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3048",
            code="3048",
            prefLabel={"no": "Øvre Eiker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3049": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3049",
            code="3049",
            prefLabel={"no": "Lier"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3050": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3050",
            code="3050",
            prefLabel={"no": "Flesberg"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3051": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3051",
            code="3051",
            prefLabel={"no": "Rollag"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3052": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3052",
            code="3052",
            prefLabel={"no": "Nore og Uvdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3053": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3053",
            code="3053",
            prefLabel={"no": "Jevnaker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3054": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3054",
            code="3054",
            prefLabel={"no": "Lunner"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3401": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3401",
            code="3401",
            prefLabel={"no": "Kongsvinger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3403": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3403",
            code="3403",
            prefLabel={"no": "Hamar"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3405": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3405",
            code="3405",
            prefLabel={"no": "Lillehammer"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3407": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3407",
            code="3407",
            prefLabel={"no": "Gjøvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3411": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3411",
            code="3411",
            prefLabel={"no": "Ringsaker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3412": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3412",
            code="3412",
            prefLabel={"no": "Løten"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3413": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3413",
            code="3413",
            prefLabel={"no": "Stange"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3414": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3414",
            code="3414",
            prefLabel={"no": "Nord-Odal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3415": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3415",
            code="3415",
            prefLabel={"no": "Sør-Odal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3416": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3416",
            code="3416",
            prefLabel={"no": "Eidskog"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3417": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3417",
            code="3417",
            prefLabel={"no": "Grue"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3418": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3418",
            code="3418",
            prefLabel={"no": "Åsnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3419": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3419",
            code="3419",
            prefLabel={"no": "Våler"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3420": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3420",
            code="3420",
            prefLabel={"no": "Elverum"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3421": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3421",
            code="3421",
            prefLabel={"no": "Trysil"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3422": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3422",
            code="3422",
            prefLabel={"no": "Åmot"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3423": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3423",
            code="3423",
            prefLabel={"no": "Stor-Elvdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3424": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3424",
            code="3424",
            prefLabel={"no": "Rendalen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3425": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3425",
            code="3425",
            prefLabel={"no": "Engerdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3426": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3426",
            code="3426",
            prefLabel={"no": "Tolga"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3427": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3427",
            code="3427",
            prefLabel={"no": "Tynset"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3428": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3428",
            code="3428",
            prefLabel={"no": "Alvdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3429": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3429",
            code="3429",
            prefLabel={"no": "Folldal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3430": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3430",
            code="3430",
            prefLabel={"no": "Os"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3431": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3431",
            code="3431",
            prefLabel={"no": "Dovre"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3432": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3432",
            code="3432",
            prefLabel={"no": "Lesja"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3433": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3433",
            code="3433",
            prefLabel={"no": "Skjåk"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3434": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3434",
            code="3434",
            prefLabel={"no": "Lom"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3435": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3435",
            code="3435",
            prefLabel={"no": "Vågå"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3436": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3436",
            code="3436",
            prefLabel={"no": "Nord-Fron"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3437": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3437",
            code="3437",
            prefLabel={"no": "Sel"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3438": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3438",
            code="3438",
            prefLabel={"no": "Sør-Fron"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3439": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3439",
            code="3439",
            prefLabel={"no": "Ringebu"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3440": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3440",
            code="3440",
            prefLabel={"no": "Øyer"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3441": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3441",
            code="3441",
            prefLabel={"no": "Gausdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3442": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3442",
            code="3442",
            prefLabel={"no": "Østre Toten"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3443": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3443",
            code="3443",
            prefLabel={"no": "Vestre Toten"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3446": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3446",
            code="3446",
            prefLabel={"no": "Gran"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3447": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3447",
            code="3447",
            prefLabel={"no": "Søndre Land"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3448": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3448",
            code="3448",
            prefLabel={"no": "Nordre Land"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3449": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3449",
            code="3449",
            prefLabel={"no": "Sør-Aurdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3450": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3450",
            code="3450",
            prefLabel={"no": "Etnedal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3451": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3451",
            code="3451",
            prefLabel={"no": "Nord-Aurdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3452": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3452",
            code="3452",
            prefLabel={"no": "Vestre Slidre"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3453": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3453",
            code="3453",
            prefLabel={"no": "Øystre Slidre"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3454": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3454",
            code="3454",
            prefLabel={"no": "Vang"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3801": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3801",
            code="3801",
            prefLabel={"no": "Horten"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3802": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3802",
            code="3802",
            prefLabel={"no": "Holmestrand"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3803": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3803",
            code="3803",
            prefLabel={"no": "Tønsberg"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3804": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3804",
            code="3804",
            prefLabel={"no": "Sandefjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3805": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3805",
            code="3805",
            prefLabel={"no": "Larvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3806": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3806",
            code="3806",
            prefLabel={"no": "Porsgrunn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3807": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3807",
            code="3807",
            prefLabel={"no": "Skien"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3808": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3808",
            code="3808",
            prefLabel={"no": "Notodden"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3811": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3811",
            code="3811",
            prefLabel={"no": "Færder"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3812": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3812",
            code="3812",
            prefLabel={"no": "Siljan"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3813": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3813",
            code="3813",
            prefLabel={"no": "Bamble"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3814": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3814",
            code="3814",
            prefLabel={"no": "Kragerø"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3815": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3815",
            code="3815",
            prefLabel={"no": "Drangedal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3816": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3816",
            code="3816",
            prefLabel={"no": "Nome"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3817": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3817",
            code="3817",
            prefLabel={"no": "Midt-Telemark"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3818": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3818",
            code="3818",
            prefLabel={"no": "Tinn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3819": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3819",
            code="3819",
            prefLabel={"no": "Hjartdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3820": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3820",
            code="3820",
            prefLabel={"no": "Seljord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3821": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3821",
            code="3821",
            prefLabel={"no": "Kviteseid"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3822": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3822",
            code="3822",
            prefLabel={"no": "Nissedal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3823": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3823",
            code="3823",
            prefLabel={"no": "Fyresdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3824": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3824",
            code="3824",
            prefLabel={"no": "Tokke"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/3825": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/3825",
            code="3825",
            prefLabel={"no": "Vinje"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4201": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4201",
            code="4201",
            prefLabel={"no": "Risør"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4202": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4202",
            code="4202",
            prefLabel={"no": "Grimstad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4203": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4203",
            code="4203",
            prefLabel={"no": "Arendal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4204": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4204",
            code="4204",
            prefLabel={"no": "Kristiansand"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4205": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4205",
            code="4205",
            prefLabel={"no": "Lindesnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4206": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4206",
            code="4206",
            prefLabel={"no": "Farsund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4207": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4207",
            code="4207",
            prefLabel={"no": "Flekkefjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4211": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4211",
            code="4211",
            prefLabel={"no": "Gjerstad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4212": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4212",
            code="4212",
            prefLabel={"no": "Vegårshei"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4213": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4213",
            code="4213",
            prefLabel={"no": "Tvedestrand"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4214": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4214",
            code="4214",
            prefLabel={"no": "Froland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4215": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4215",
            code="4215",
            prefLabel={"no": "Lillesand"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4216": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4216",
            code="4216",
            prefLabel={"no": "Birkenes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4217": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4217",
            code="4217",
            prefLabel={"no": "Åmli"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4218": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4218",
            code="4218",
            prefLabel={"no": "Iveland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4219": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4219",
            code="4219",
            prefLabel={"no": "Evje og Hornnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4220": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4220",
            code="4220",
            prefLabel={"no": "Bygland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4221": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4221",
            code="4221",
            prefLabel={"no": "Valle"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4222": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4222",
            code="4222",
            prefLabel={"no": "Bykle"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4223": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4223",
            code="4223",
            prefLabel={"no": "Vennesla"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4224": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4224",
            code="4224",
            prefLabel={"no": "Åseral"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4225": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4225",
            code="4225",
            prefLabel={"no": "Lyngdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4226": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4226",
            code="4226",
            prefLabel={"no": "Hægebostad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4227": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4227",
            code="4227",
            prefLabel={"no": "Kvinesdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4228": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4228",
            code="4228",
            prefLabel={"no": "Sirdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4601": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4601",
            code="4601",
            prefLabel={"no": "Bergen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4602": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4602",
            code="4602",
            prefLabel={"no": "Kinn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4611": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4611",
            code="4611",
            prefLabel={"no": "Etne"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4612": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4612",
            code="4612",
            prefLabel={"no": "Sveio"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4613": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4613",
            code="4613",
            prefLabel={"no": "Bømlo"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4614": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4614",
            code="4614",
            prefLabel={"no": "Stord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4615": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4615",
            code="4615",
            prefLabel={"no": "Fitjar"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4616": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4616",
            code="4616",
            prefLabel={"no": "Tysnes"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4617": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4617",
            code="4617",
            prefLabel={"no": "Kvinnherad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4618": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4618",
            code="4618",
            prefLabel={"no": "Ullensvang"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4619": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4619",
            code="4619",
            prefLabel={"no": "Eidfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4620": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4620",
            code="4620",
            prefLabel={"no": "Ulvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4621": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4621",
            code="4621",
            prefLabel={"no": "Voss"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4622": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4622",
            code="4622",
            prefLabel={"no": "Kvam"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4623": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4623",
            code="4623",
            prefLabel={"no": "Samnanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4624": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4624",
            code="4624",
            prefLabel={"no": "Bjørnafjorden"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4625": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4625",
            code="4625",
            prefLabel={"no": "Austevoll"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4626": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4626",
            code="4626",
            prefLabel={"no": "Øygarden"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4627": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4627",
            code="4627",
            prefLabel={"no": "Askøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4628": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4628",
            code="4628",
            prefLabel={"no": "Vaksdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4629": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4629",
            code="4629",
            prefLabel={"no": "Modalen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4630": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4630",
            code="4630",
            prefLabel={"no": "Osterøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4631": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4631",
            code="4631",
            prefLabel={"no": "Alver"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4632": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4632",
            code="4632",
            prefLabel={"no": "Austrheim"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4633": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4633",
            code="4633",
            prefLabel={"no": "Fedje"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4634": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4634",
            code="4634",
            prefLabel={"no": "Masfjorden"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4635": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4635",
            code="4635",
            prefLabel={"no": "Gulen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4636": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4636",
            code="4636",
            prefLabel={"no": "Solund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4637": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4637",
            code="4637",
            prefLabel={"no": "Hyllestad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4638": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4638",
            code="4638",
            prefLabel={"no": "Høyanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4639": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4639",
            code="4639",
            prefLabel={"no": "Vik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4640": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4640",
            code="4640",
            prefLabel={"no": "Sogndal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4641": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4641",
            code="4641",
            prefLabel={"no": "Aurland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4642": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4642",
            code="4642",
            prefLabel={"no": "Lærdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4643": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4643",
            code="4643",
            prefLabel={"no": "Årdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4644": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4644",
            code="4644",
            prefLabel={"no": "Luster"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4645": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4645",
            code="4645",
            prefLabel={"no": "Askvoll"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4646": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4646",
            code="4646",
            prefLabel={"no": "Fjaler"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4647": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4647",
            code="4647",
            prefLabel={"no": "Sunnfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4648": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4648",
            code="4648",
            prefLabel={"no": "Bremanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4649": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4649",
            code="4649",
            prefLabel={"no": "Stad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4650": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4650",
            code="4650",
            prefLabel={"no": "Gloppen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/4651": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/4651",
            code="4651",
            prefLabel={"no": "Stryn"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5001": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5001",
            code="5001",
            prefLabel={"no": "Trondheim"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5006": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5006",
            code="5006",
            prefLabel={"no": "Steinkjer"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5007": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5007",
            code="5007",
            prefLabel={"no": "Namsos"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5014": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5014",
            code="5014",
            prefLabel={"no": "Frøya"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5020": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5020",
            code="5020",
            prefLabel={"no": "Osen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5021": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5021",
            code="5021",
            prefLabel={"no": "Oppdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5022": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5022",
            code="5022",
            prefLabel={"no": "Rennebu"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5025": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5025",
            code="5025",
            prefLabel={"no": "Røros"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5026": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5026",
            code="5026",
            prefLabel={"no": "Holtålen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5027": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5027",
            code="5027",
            prefLabel={"no": "Midtre Gauldal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5028": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5028",
            code="5028",
            prefLabel={"no": "Melhus"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5029": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5029",
            code="5029",
            prefLabel={"no": "Skaun"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5031": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5031",
            code="5031",
            prefLabel={"no": "Malvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5032": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5032",
            code="5032",
            prefLabel={"no": "Selbu"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5033": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5033",
            code="5033",
            prefLabel={"no": "Tydal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5034": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5034",
            code="5034",
            prefLabel={"no": "Meråker"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5035": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5035",
            code="5035",
            prefLabel={"no": "Stjørdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5036": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5036",
            code="5036",
            prefLabel={"no": "Frosta"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5037": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5037",
            code="5037",
            prefLabel={"no": "Levanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5038": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5038",
            code="5038",
            prefLabel={"no": "Verdal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5041": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5041",
            code="5041",
            prefLabel={"no": "Snåsa"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5042": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5042",
            code="5042",
            prefLabel={"no": "Lierne"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5043": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5043",
            code="5043",
            prefLabel={"no": "Røyrvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5044": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5044",
            code="5044",
            prefLabel={"no": "Namsskogan"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5045": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5045",
            code="5045",
            prefLabel={"no": "Grong"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5046": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5046",
            code="5046",
            prefLabel={"no": "Høylandet"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5047": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5047",
            code="5047",
            prefLabel={"no": "Overhalla"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5049": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5049",
            code="5049",
            prefLabel={"no": "Flatanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5052": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5052",
            code="5052",
            prefLabel={"no": "Leka"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5053": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5053",
            code="5053",
            prefLabel={"no": "Inderøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5054": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5054",
            code="5054",
            prefLabel={"no": "Indre Fosen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5055": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5055",
            code="5055",
            prefLabel={"no": "Heim"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5056": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5056",
            code="5056",
            prefLabel={"no": "Hitra"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5057": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5057",
            code="5057",
            prefLabel={"no": "Ørland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5058": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5058",
            code="5058",
            prefLabel={"no": "Åfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5059": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5059",
            code="5059",
            prefLabel={"no": "Orkland"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5060": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5060",
            code="5060",
            prefLabel={"no": "Nærøysund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5061": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5061",
            code="5061",
            prefLabel={"no": "Rindal"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5401": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5401",
            code="5401",
            prefLabel={"no": "Tromsø"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5402": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5402",
            code="5402",
            prefLabel={"no": "Harstad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5403": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5403",
            code="5403",
            prefLabel={"no": "Alta"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5404": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5404",
            code="5404",
            prefLabel={"no": "Vardø"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5405": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5405",
            code="5405",
            prefLabel={"no": "Vadsø"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5406": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5406",
            code="5406",
            prefLabel={"no": "Hammerfest"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5411": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5411",
            code="5411",
            prefLabel={"no": "Kvæfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5412": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5412",
            code="5412",
            prefLabel={"no": "Tjeldsund"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5413": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5413",
            code="5413",
            prefLabel={"no": "Ibestad"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5414": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5414",
            code="5414",
            prefLabel={"no": "Gratangen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5415": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5415",
            code="5415",
            prefLabel={"no": "Lavangen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5416": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5416",
            code="5416",
            prefLabel={"no": "Bardu"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5417": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5417",
            code="5417",
            prefLabel={"no": "Salangen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5418": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5418",
            code="5418",
            prefLabel={"no": "Målselv"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5419": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5419",
            code="5419",
            prefLabel={"no": "Sørreisa"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5420": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5420",
            code="5420",
            prefLabel={"no": "Dyrøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5421": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5421",
            code="5421",
            prefLabel={"no": "Senja"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5422": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5422",
            code="5422",
            prefLabel={"no": "Balsfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5423": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5423",
            code="5423",
            prefLabel={"no": "Karlsøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5424": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5424",
            code="5424",
            prefLabel={"no": "Lyngen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5425": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5425",
            code="5425",
            prefLabel={"no": "Storfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5426": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5426",
            code="5426",
            prefLabel={"no": "Kåfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5427": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5427",
            code="5427",
            prefLabel={"no": "Skjervøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5428": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5428",
            code="5428",
            prefLabel={"no": "Nordreisa"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5429": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5429",
            code="5429",
            prefLabel={"no": "Kvænangen"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5430": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5430",
            code="5430",
            prefLabel={"no": "Kautokeino"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5432": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5432",
            code="5432",
            prefLabel={"no": "Loppa"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5433": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5433",
            code="5433",
            prefLabel={"no": "Hasvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5434": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5434",
            code="5434",
            prefLabel={"no": "Måsøy"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5435": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5435",
            code="5435",
            prefLabel={"no": "Nordkapp"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5436": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5436",
            code="5436",
            prefLabel={"no": "Porsanger"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5437": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5437",
            code="5437",
            prefLabel={"no": "Karasjok"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5438": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5438",
            code="5438",
            prefLabel={"no": "Lebesby"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5439": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5439",
            code="5439",
            prefLabel={"no": "Gamvik"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5440": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5440",
            code="5440",
            prefLabel={"no": "Berlevåg"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5441": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5441",
            code="5441",
            prefLabel={"no": "Tana"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5442": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5442",
            code="5442",
            prefLabel={"no": "Nesseby"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5443": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5443",
            code="5443",
            prefLabel={"no": "Båtsfjord"},
        ),
        "data.geonorge.no/administrativeEnheter/kommune/id/5444": ReferenceDataCode(
            uri="https://data.geonorge.no/administrativeEnheter/kommune/id/5444",
            code="5444",
            prefLabel={"no": "Sør-Varanger"},
        ),
    },
)
