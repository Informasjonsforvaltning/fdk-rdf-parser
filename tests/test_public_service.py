from unittest.mock import Mock

from fdk_rdf_parser import parse_public_services
from fdk_rdf_parser.classes import (
    Address,
    Agent,
    Channel,
    ConceptSchema,
    Cost,
    CVContactPoint,
    EuDataTheme,
    Evidence,
    HarvestMetaData,
    LegalResource,
    LosNode,
    OpeningHoursSpecification,
    Organization,
    Output,
    Participation,
    PublicService,
    ReferenceDataCode,
    Requirement,
    Rule,
    Service,
    SkosConcept,
)
from fdk_rdf_parser.classes.evidence import EvidenceRdfType


def test_complete_public_services(
    mock_reference_data_client: Mock,
) -> None:
    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            admsStatus=ReferenceDataCode(
                uri="http://purl.org/adms/status/Completed",
                code="Completed",
                prefLabel={"nn": "Ferdigstilt", "nb": "Ferdigstilt", "en": "Completed"},
            ),
            dctType=[
                ReferenceDataCode(
                    uri="http://publications.europa.eu/resource/authority/main-activity/airport",
                    code="airport",
                    prefLabel={"en": "Airport-related activities"},
                )
            ],
            subject=[
                SkosConcept(uri="http://testbegrep0.no"),
                SkosConcept(uri="http://testbegrep1.no"),
            ],
            homepage=["http://testhomepage0.no", "http://testhomepage1.no"],
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            isGroupedBy=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            ],
            hasCompetentAuthority=[
                Organization(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                    identifier="123456789",
                    name={"nb": "Digitaliseringsdirektoratet"},
                    orgPath="/STAT/987654321/123456789",
                    title={
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                        "en": "Norwegian Digitalisation Agency",
                    },
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            keyword=[{"nb": "Serveringsbevilling"}],
            sector=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/2",
                    prefLabel={"nb": "Nacekode: 56.1"},
                    extraType=None,
                )
            ],
            isClassifiedBy=[
                SkosConcept(
                    uri="https://data.norge.no/concepts/16",
                    prefLabel={"nb": "Kafé"},
                    extraType=None,
                ),
                SkosConcept(
                    uri="https://data.norge.no/concepts/17",
                    prefLabel={"nb": "Spiserestaurant"},
                    extraType=None,
                ),
            ],
            isDescribedAt=[
                SkosConcept(
                    uri="https://data.norge.no/node/1127",
                )
            ],
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
                ),
            ],
            holdsRequirement=[
                Requirement(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/requirement/5",
                    identifier="5",
                    dctTitle={"no": "Et attestkrav"},
                    description={"no": "Et viktig krav som må tilfredsstilles."},
                    fulfils=[
                        "http://public-service-publisher.fellesdatakatalog.digdir.no/rule/1"
                    ],
                    dctType=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/153",
                            prefLabel={"nb": "Attest"},
                        )
                    ],
                ),
            ],
            hasParticipation=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
            ],
            hasInput=[
                Evidence(
                    rdfType=EvidenceRdfType.EVIDENCE_TYPE,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1",
                    identifier="1",
                    name={"nb": "Vandelsattest"},
                    description={"nb": "Vandelsattest"},
                    language=[
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/ENG",
                            code="ENG",
                            prefLabel={
                                "nn": "Engelsk",
                                "no": "Engelsk",
                                "nb": "Engelsk",
                                "en": "English",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NNO",
                            code="NNO",
                            prefLabel={
                                "nn": "Norsk Nynorsk",
                                "no": "Norsk Nynorsk",
                                "nb": "Norsk Nynorsk",
                                "en": "Norwegian Nynorsk",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code="NOB",
                            prefLabel={
                                "nn": "Norsk Bokmål",
                                "no": "Norsk Bokmål",
                                "nb": "Norsk Bokmål",
                                "en": "Norwegian Bokmål",
                            },
                        ),
                    ],
                    dctType=[
                        ReferenceDataCode(
                            uri="https://data.norge.no/vocabulary/evidence-type#attestation",
                            code="attestation",
                            prefLabel={"nb": "attest", "en": "attestation"},
                        ),
                    ],
                    page=["https://example.org/exDokumentasjonsSide"],
                ),
                Evidence(
                    rdfType=EvidenceRdfType.DATASET_TYPE,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/2",
                    identifier="2",
                    name={"nb": "Nødvendig dokumentasjon"},
                    description={"nb": "Annen dokumentasjon"},
                    dctType=None,
                    language=[
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code="NOB",
                            prefLabel={
                                "nn": "Norsk Bokmål",
                                "no": "Norsk Bokmål",
                                "nb": "Norsk Bokmål",
                                "en": "Norwegian Bokmål",
                            },
                        ),
                    ],
                    page=["https://example.org/exDokumentasjonsSide2"],
                ),
                Evidence(
                    rdfType=EvidenceRdfType.UNKNOWN,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/3",
                    identifier="3",
                    name={"nb": "Ugyldig dokumentasjonstype"},
                ),
                Evidence(
                    rdfType=EvidenceRdfType.UNKNOWN,
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exDokumentasjon.ttl",
                ),
            ],
            produces=[
                Output(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/output/4",
                    identifier="4",
                    name={"nb": "Serveringsbevilling"},
                    description={"nb": "Serveringsbevilling"},
                    type=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/205",
                            prefLabel={"nb": "Tillatelse", "en": "Permit"},
                        )
                    ],
                ),
            ],
            requires=[
                Service(
                    id="4",
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
                    identifier="4",
                    title={
                        "nb": "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"
                    },
                )
            ],
            contactPoint=[
                CVContactPoint(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/contact/1",
                    email=["mailto:postmottak@bronnoy.kommune.no"],
                    telephone=["tel:+4775012000"],
                    language=[
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/ENG",
                            code="ENG",
                            prefLabel={
                                "en": "English",
                                "nb": "Engelsk",
                                "nn": "Engelsk",
                                "no": "Engelsk",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NNO",
                            code="NNO",
                            prefLabel={
                                "en": "Norwegian Nynorsk",
                                "nb": "Norsk Nynorsk",
                                "nn": "Norsk Nynorsk",
                                "no": "Norsk Nynorsk",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code="NOB",
                            prefLabel={
                                "en": "Norwegian Bokmål",
                                "nb": "Norsk Bokmål",
                                "nn": "Norsk Bokmål",
                                "no": "Norsk Bokmål",
                            },
                        ),
                    ],
                    openingHours={
                        "no": "Resepsjonen er åpent for henvendelser mandag - fredag: kl  10:00 - 14:00.",
                        "nn": "Teksten blir vist på nynorsk.",
                        "en": "The reception is open for inquiries Monday - Friday: 10:00 - 14:00.",
                    },
                    specialOpeningHours=[
                        OpeningHoursSpecification(
                            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHelligdagerStengt.ttl",
                            dayOfWeek=[
                                ReferenceDataCode(
                                    uri="https://schema.org/PublicHolidays",
                                    code="PublicHolidays",
                                    prefLabel={
                                        "nn": "Offentlege fridagar",
                                        "nb": "Offentlige fridager",
                                        "en": "Public holidays",
                                    },
                                )
                            ],
                        )
                    ],
                    hoursAvailable=[
                        OpeningHoursSpecification(
                            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exApningstidResepsjon.ttl",
                            dayOfWeek=[
                                ReferenceDataCode(
                                    uri="https://schema.org/Friday",
                                    code="Friday",
                                    prefLabel={
                                        "nn": "Fredag",
                                        "nb": "Fredag",
                                        "en": "Friday",
                                    },
                                ),
                                ReferenceDataCode(
                                    uri="https://schema.org/Monday",
                                    code="Monday",
                                    prefLabel={
                                        "nn": "Måndag",
                                        "nb": "Mandag",
                                        "en": "Monday",
                                    },
                                ),
                                ReferenceDataCode(
                                    uri="https://schema.org/Thursday",
                                    code="Thursday",
                                    prefLabel={
                                        "nn": "Torsdag",
                                        "nb": "Torsdag",
                                        "en": "Thursday",
                                    },
                                ),
                                ReferenceDataCode(
                                    uri="https://schema.org/Tuesday",
                                    code="Tuesday",
                                    prefLabel={
                                        "nn": "Tysdag",
                                        "nb": "Tirsdag",
                                        "en": "Tuesday",
                                    },
                                ),
                                ReferenceDataCode(
                                    uri="https://schema.org/Wednesday",
                                    code="Wednesday",
                                    prefLabel={
                                        "nn": "Onsdag",
                                        "nb": "Onsdag",
                                        "en": "Wednesday",
                                    },
                                ),
                            ],
                        )
                    ],
                )
            ],
            follows=[
                Rule(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/rule/1",
                    identifier="1",
                    description={
                        "nb": "Lov om behandlingsmåten i forvaltningssaker (https://lovdata.no/lov/1967-02-10)"
                    },
                    language=[
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code=None,
                            prefLabel=None,
                        )
                    ],
                    name={"nb": "Lov om behandlingsmåten i forvaltningssaker"},
                    implements=[
                        "http://public-service-publisher.fellesdatakatalog.digdir.no/legalresource/1"
                    ],
                )
            ],
            hasLegalResource=[
                LegalResource(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/legalresource/1",
                    dctTitle={"nb": "Lov om Enhetsregisteret"},
                    description={"nb": "Lov om Enhetsregisteret"},
                    seeAlso=["https://lovdata.no/eli/lov/1994/06/03/15/nor/html"],
                    relation=[
                        "http://public-service-publisher.fellesdatakatalog.digdir.no/legalresource/2"
                    ],
                )
            ],
            hasChannel=[
                Channel(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/channel/2",
                    identifier="2",
                    channelType=ReferenceDataCode(
                        uri="https://data.norge.no/vocabulary/service-channel-type#assistant",
                        prefLabel={"nb": "assistent", "en": "assistant"},
                        code="assistant",
                    ),
                    description={"nb": "Lov om Enhetsregisteret"},
                    processingTime="P1D",
                    email=["mailto:postmottak@bronnoy.kommune.no"],
                    url=["http://testurl.com"],
                    address=[
                        Address(
                            streetAddress="Sivert Nielsens gt. 24",
                            locality="Brønnøysund",
                            postalCode="8905",
                            countryName={"nb": "Norge", "en": "Norway"},
                        )
                    ],
                    hasInput=[
                        "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exDokumentasjon.ttl"
                    ],
                    telephone=["tel:+4712345678"],
                )
            ],
            processingTime="P1D",
            hasCost=[
                Cost(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/cost/15",
                    identifier="15",
                    description={
                        "nb": "4,27 kr pr. vareliter for alkoholholdig drikk i gruppe 3"
                    },
                    currency="http://publications.europa.eu/resource/authority/currency/NOK",
                    ifAccessedThrough="http://public-service-publisher.fellesdatakatalog.digdir.no/channel/2",
                    isDefinedBy=[
                        Organization(
                            uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                            identifier="123456789",
                            name={"nb": "Digitaliseringsdirektoratet"},
                            orgPath="/STAT/987654321/123456789",
                            title={
                                "en": "Norwegian Digitalisation Agency",
                                "nn": "Digitaliseringsdirektoratet",
                                "nb": "Digitaliseringsdirektoratet",
                            },
                        )
                    ],
                    value="4.27",
                ),
                Cost(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/cost/16",
                    identifier="16",
                    description=None,
                    currency="http://publications.europa.eu/resource/authority/currency/NOK",
                    ifAccessedThrough=None,
                    value="0",
                ),
            ],
            relation=[
                Service(
                    id="4",
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
                    identifier="4",
                    title={
                        "nb": "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"
                    },
                )
            ],
            spatial=[
                "https://data.geonorge.no/administrativeEnheter/kommune/id/172833"
            ],
            associatedBroaderTypesByEvents=[
                "https://data.norge.no/concepts/306",
                "https://data.norge.no/concepts/304",
                "https://data.norge.no/concepts/310",
            ],
            participatingAgents=[
                Agent(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                    identifier="971526920",
                    name={"nb": "Statistisk sentralbyrå"},
                    playsRole=[
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                            identifier="1",
                            description={
                                "nb": "Statistisk sentralbyrås Virksomhets- og foretaksregister"
                            },
                            agent="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                            role=[
                                ReferenceDataCode(
                                    uri="https://data.norge.no/vocabulary/role-type#data-consumer",
                                    code="data-consumer",
                                    prefLabel={
                                        "nb": "datakonsument",
                                        "en": "data consumer",
                                    },
                                ),
                            ],
                        )
                    ],
                )
            ],
        ),
    }

    with open("tests/test_data/public_service0.ttl", "r") as src, open(
        "tests/test_data/event0.ttl", "r"
    ) as event_src:
        assert parse_public_services(src.read(), event_src.read()) == expected


def test_parse_multiple_public_services(
    mock_reference_data_client: Mock,
) -> None:
    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            admsStatus=ReferenceDataCode(uri="http://is-not-in-ref-data.test"),
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            isGroupedBy=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            ],
            hasCompetentAuthority=[
                Organization(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                    identifier="123456789",
                    name={"nb": "Digitaliseringsdirektoratet"},
                    orgPath="/STAT/987654321/123456789",
                    title={
                        "en": "Norwegian Digitalisation Agency",
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                    },
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/2": PublicService(
            id="fdk-2",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
            identifier="2",
            title={"nn": "Ei anna offentleg teneste"},
            description={
                "nb": "Ei anna offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=[
                Organization(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/991825827",
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/3": PublicService(
            id="fdk-3",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/3",
            identifier="3",
            title={"nn": "Ei anna offentleg teneste"},
            description={
                "nb": "Ei anna offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=None,
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
    }

    with open("tests/test_data/public_service1.ttl", "r") as src:
        assert parse_public_services(src.read()) == expected


def test_parse_cpsvno_services(
    mock_reference_data_client: Mock,
) -> None:
    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl": Service(
            id="1fc38c3c-1c86-3161-a9a7-e443fd94d413",
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl",
            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl",
            title={"en": "Dummy service", "nn": "Dummytjeneste", "nb": "Dummytjeneste"},
            description={
                "en": "The text is displayed in English.",
                "nn": "Teksten blir vist på nynorsk.",
                "nb": "Dette er en dummytjeneste som kan brukes i forbindelse med testing av CPSV-AP-NO når det er behov for en relasjon til en tjeneste som det ikke finnes eksempel på ennå.",
            },
            harvest=HarvestMetaData(
                firstHarvested="2022-05-18T11:26:51Z", changed=["2022-05-18T11:26:51Z"]
            ),
            ownedBy=[
                Organization(
                    uri="https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced",
                    identifier="https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced",
                    name={"nb": "Organisasjon i Brønnøysund"},
                    orgType=ReferenceDataCode(
                        uri="http://purl.org/adms/publishertype/NonGovernmentalOrganisation",
                        prefLabel={
                            "nn": "Ikkje-statleg organisasjon",
                            "nb": "Ikke-statlig organisasjon",
                            "en": "Non-Governmental Organisation",
                        },
                        code="NonGovernmentalOrganisation",
                    ),
                    spatial=[
                        "http://publications.europa.eu/resource/authority/country/NOR",
                        "https://data.geonorge.no/administrativeEnheter/kommune/id/172833",
                    ],
                    homepage=["https://www.bronnoy.organisasjon.no"],
                ),
            ],
            contactPoint=[
                CVContactPoint(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exKontaktpunktDummy.ttl",
                    contactType={"nb": "Kontakt test"},
                    email=["mailto:postmottak@example.org"],
                    telephone=["tel:+4712345678"],
                    contactPage=["https://example.org/exKontaktside"],
                    language=[
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/ENG",
                            code="ENG",
                            prefLabel={
                                "en": "English",
                                "nb": "Engelsk",
                                "nn": "Engelsk",
                                "no": "Engelsk",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NNO",
                            code="NNO",
                            prefLabel={
                                "en": "Norwegian Nynorsk",
                                "nb": "Norsk Nynorsk",
                                "nn": "Norsk Nynorsk",
                                "no": "Norsk Nynorsk",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code="NOB",
                            prefLabel={
                                "en": "Norwegian Bokmål",
                                "nb": "Norsk Bokmål",
                                "nn": "Norsk Bokmål",
                                "no": "Norsk Bokmål",
                            },
                        ),
                    ],
                )
            ],
            language=[
                ReferenceDataCode(
                    uri="http://publications.europa.eu/resource/authority/language/ENG",
                    code="ENG",
                    prefLabel={
                        "en": "English",
                        "nb": "Engelsk",
                        "nn": "Engelsk",
                        "no": "Engelsk",
                    },
                ),
                ReferenceDataCode(
                    uri="http://publications.europa.eu/resource/authority/language/NOB",
                    code="NOB",
                    prefLabel={
                        "en": "Norwegian Bokmål",
                        "nb": "Norsk Bokmål",
                        "nn": "Norsk Bokmål",
                        "no": "Norsk Bokmål",
                    },
                ),
            ],
            produces=[
                Output(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteresultatDummy.ttl",
                    identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteresultatDummy.ttl",
                    name={
                        "nb": "Dummy tjenesteresultat",
                        "nn": "Dummy tjenesteresultat",
                        "en": "Dummy service result",
                    },
                    description={
                        "en": "The text is displayed in English.",
                        "nn": "Teksten blir vist på nynorsk.",
                        "nb": "Dette er et dummy tjenesteresultat som kan brukes i forbindelse med testing av CPSV-AP-NO når det er behov for en relasjon til et tjenesteresultat.",
                    },
                    language=[
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/ENG",
                            code="ENG",
                            prefLabel={
                                "nn": "Engelsk",
                                "no": "Engelsk",
                                "nb": "Engelsk",
                                "en": "English",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NNO",
                            code="NNO",
                            prefLabel={
                                "nn": "Norsk Nynorsk",
                                "no": "Norsk Nynorsk",
                                "nb": "Norsk Nynorsk",
                                "en": "Norwegian Nynorsk",
                            },
                        ),
                        ReferenceDataCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code="NOB",
                            prefLabel={
                                "nn": "Norsk Bokmål",
                                "no": "Norsk Bokmål",
                                "nb": "Norsk Bokmål",
                                "en": "Norwegian Bokmål",
                            },
                        ),
                    ],
                )
            ],
            type="publicservices",
            thematicAreaUris=[
                "http://publications.europa.eu/resource/authority/data-theme/GOVE",
                "https://psi.norge.no/los/tema/naring",
                "https://psi.norge.no/not/in/los/or/eu",
            ],
            losThemes=[
                LosNode(
                    children=[
                        "https://psi.norge.no/los/tema/tilskuddsordninger-for-naring",
                        "https://psi.norge.no/los/tema/naringsliv",
                        "https://psi.norge.no/los/tema/naringsutvikling",
                        "https://psi.norge.no/los/tema/landbruk",
                        "https://psi.norge.no/los/tema/handel-og-service",
                    ],
                    parents=None,
                    isTema=True,
                    losPaths=["naring"],
                    name={"nn": "Næring", "nb": "Næring", "en": "Business"},
                    definition=None,
                    uri="https://psi.norge.no/los/tema/naring",
                    synonyms=[],
                    relatedTerms=None,
                ),
            ],
            euDataThemes=[
                EuDataTheme(
                    id="http://publications.europa.eu/resource/authority/data-theme/GOVE",
                    code="GOVE",
                    startUse="2015-10-01",
                    title={
                        "nn": "Forvaltning og offentleg sektor",
                        "no": "Forvaltning og offentlig sektor",
                        "nb": "Forvaltning og offentlig sektor",
                        "en": "Government and public sector",
                    },
                    conceptSchema=ConceptSchema(
                        id="http://publications.europa.eu/resource/authority/data-theme",
                        title={"en": "Data theme"},
                        versioninfo="20200923-0",
                        versionnumber="20200923-0",
                    ),
                ),
            ],
        )
    }

    with open("tests/test_data/service0.ttl", "r") as src:
        assert parse_public_services(src.read()) == expected


def test_service_evidence_collection_from_channel(
    mock_reference_data_client: Mock,
) -> None:
    expected = {
        "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl": Service(
            id="1fc38c3c-1c86-3161-a9a7-e443fd94d413",
            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl",
            identifier="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl",
            harvest=HarvestMetaData(
                firstHarvested="2022-05-18T11:26:51Z", changed=["2022-05-18T11:26:51Z"]
            ),
            type="publicservices",
            hasInput=[
                Evidence(
                    rdfType=EvidenceRdfType.EVIDENCE_TYPE,
                    uri="999999999",
                    identifier="999999999",
                ),
                Evidence(
                    rdfType=EvidenceRdfType.EVIDENCE_TYPE,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1",
                    identifier="1",
                    name={"nb": "Vandelsattest"},
                    description={"nb": "Vandelsattest"},
                ),
                Evidence(
                    rdfType=EvidenceRdfType.EVIDENCE_TYPE,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/3",
                    identifier="3",
                    description={"nb": "Duplisert dokumentasjon"},
                ),
                Evidence(
                    rdfType=EvidenceRdfType.DATASET_TYPE,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/2",
                    identifier="2",
                    description={"nb": "Annen dokumentasjon"},
                    name={"nb": "Nødvendig dokumentasjon"},
                ),
                Evidence(
                    rdfType=EvidenceRdfType.UNKNOWN,
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/4",
                ),
            ],
            hasChannel=[
                Channel(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/channel/1",
                    identifier="1",
                    hasInput=[
                        "http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/2",
                        "http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/3",
                        "http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/4",
                    ],
                )
            ],
        )
    }

    with open("tests/test_data/service1.ttl", "r") as src:
        assert parse_public_services(src.read()) == expected
