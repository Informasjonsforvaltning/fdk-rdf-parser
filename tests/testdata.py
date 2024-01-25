from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.reference_data import (
    DatasetReferenceData,
    PublicServiceReferenceData,
)

public_service_reference_data = PublicServiceReferenceData(
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
    types={
        "publications.europa.eu/resource/authority/main-activity/defence": ReferenceDataCode(
            uri="http://publications.europa.eu/resource/authority/main-activity/defence",
            code="defence",
            prefLabel={"en": "Defence"},
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
)
