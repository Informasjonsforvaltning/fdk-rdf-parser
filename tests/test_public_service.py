from unittest.mock import Mock

from fdk_rdf_parser import parse_public_services
from fdk_rdf_parser.classes import (
    Agent,
    Channel,
    Cost,
    CriterionRequirement,
    CVContactPoint,
    Evidence,
    HarvestMetaData,
    LegalResource,
    OpeningHoursSpecification,
    Output,
    Participation,
    PublicService,
    Publisher,
    Rule,
    Service,
    SkosCode,
    SkosConcept,
)


def test_complete_public_services(
    mock_reference_data_client: Mock,
) -> None:
    src = """
            @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
            @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
            @prefix rov:   <http://www.w3.org/ns/regorg#> .
            @prefix cpsv: <http://purl.org/vocab/cpsv#> .
            @prefix dct: <http://purl.org/dc/terms/> .
            @prefix cv: <http://data.europa.eu/m8g/> .
            @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
            @prefix dcat:  <http://www.w3.org/ns/dcat#> .
            @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
            @prefix schema:  <http://schema.org/> .
            @prefix eli: <http://data.europa.eu/eli/ontology#> .
            @prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
            @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
            @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> a cpsv:PublicService ;
                    cv:hasCompetentAuthority    <http://public-service-publisher.fellesdatakatalog.digdir.no/public-organisation/3> ;
                    cv:isGroupedBy              <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    dct:description             "Dette skjemaet  brukes for å registrere en ny virksomhet, eller søke om godkjenning av en ny næringsmiddelvirksomhet. Skjemaet skal også brukes dersom du vil utvide aktiviteten i en allerede eksisterende virksomhet og starte med en ny aktivitet som ikke er registrert."@nb ;
                    dct:identifier              "4" ;
                    dct:title                   "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                    cv:hasChannel             <http://public-service-publisher.fellesdatakatalog.digdir.no/channel/2> ;
                    cv:hasCompetentAuthority    <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
                    cv:hasContactPoint <http://public-service-publisher.fellesdatakatalog.digdir.no/contact/1> ;
                    cv:hasCost <http://public-service-publisher.fellesdatakatalog.digdir.no/cost/15>, <http://public-service-publisher.fellesdatakatalog.digdir.no/cost/16> ;
                    cv:hasCriterion <http://public-service-publisher.fellesdatakatalog.digdir.no/criterion-requirement/5>  ;
                    cv:hasLegalResource <http://public-service-publisher.fellesdatakatalog.digdir.no/legalresource/1> ;
                    cv:hasParticipation <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> ;
                    cv:isClassifiedBy <https://data.norge.no/concepts/17> , <https://data.norge.no/concepts/16> ;
                    cv:isDescribedAt <https://data.norge.no/node/1127> ;
                    cv:isGroupedBy <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    cv:processingTime "P1D"^^xsd:duration ;
                    cv:sector <https://data.norge.no/concepts/2> ;
                    dct:description "Ei offentleg teneste som tener som døme til bruk i utvikling"@nn ;
                    dct:identifier "1" ;
                    dct:language <http://publications.europa.eu/resource/authority/language/NOB>;
                    dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> ;
                    dct:requires <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> ;
                    dct:spatial <https://data.geonorge.no/administrativeEnheter/kommune/id/172833>;
                    dct:title "Ei offentleg teneste"@nb ;
                    cpsv:follows <http://public-service-publisher.fellesdatakatalog.digdir.no/rule/1> ;
                    cpsv:hasInput <http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1> ;
                    cpsv:produces <http://public-service-publisher.fellesdatakatalog.digdir.no/output/4> ;
                    dcat:keyword "Serveringsbevilling"@nb .

            <https://data.norge.no/concepts/1>
                    a               skos:Concept ;
                    skos:prefLabel  "Starte og drive en bedrift"@nb , "Starting business"@en .

            <https://data.norge.no/concepts/15>
                    a               skos:Concept ;
                    skos:prefLabel  "Daglig leder"@nb .

            <https://data.norge.no/concepts/16>
                    a               skos:Concept ;
                    skos:prefLabel  "Kafé"@nb .

            <https://data.norge.no/concepts/17>
                    a               skos:Concept ;
                    skos:prefLabel  "Spiserestaurant"@nb .

            <https://data.norge.no/concepts/2>
                    a               skos:Concept ;
                    skos:prefLabel  "Nacekode: 56.1"@nb .

            <https://data.norge.no/concepts/101>
                    a               skos:Concept ;
                    skos:prefLabel  "Datakonsument"@nb ; .

            <https://data.norge.no/concepts/153>
                    a skos:Concept ;
                    skos:prefLabel "Attest"@nb .

            <https://data.norge.no/concepts/205>
                    a skos:Concept ;
                    skos:prefLabel "Tillatelse"@nb, "Permit"@en .

            <https://data.norge.no/concepts/257>
                    a skos:Concept ;
                    skos:prefLabel  "Post"@nb , "Mail"@en .

            <https://data.norge.no/concepts/308> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/cost/15>
                    a  cv:Cost ;
                    cv:currency           <http://publications.europa.eu/resource/authority/currency/NOK> ;
                    cv:ifAccessedThrough  <http://public-service-publisher.fellesdatakatalog.digdir.no/channel/10> ;
                    cv:isDefinedBy        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
                    cv:value              4.27 ;
                    dct:description       "4,27 kr pr. vareliter for alkoholholdig drikk i gruppe 3" ;
                    dct:identifier        "15" .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/cost/16>
                    a  cv:Cost ;
                    cv:currency           <http://publications.europa.eu/resource/authority/currency/NOK> ;
                    cv:value              0 ;
                    dct:identifier        "16" .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/channel/2>
                    a cv:Channel ;
                    cv:ownedBy      <http://public-service-publisher.fellesdatakatalog.digdir.no/public-organisation/1> ;
                    dct:identifier  "2" ;
                    dct:type        <https://data.norge.no/concepts/257> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/channel/10>
                    a cv:Channel ;
                    cv:ownedBy      <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
                    dct:identifier  "10" ;
                    dct:type        <https://data.norge.no/concepts/257> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/criterion-requirement/5>
                    a               cv:CriterionRequirement ;
                    dct:identifier  "5" ;
                    dct:title       "Krav om vandel"@nb ;
                    dct:type        <https://data.norge.no/concepts/153> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1>
                    a               cv:Participation ;
                    cv:role         <https://data.norge.no/concepts/101> ;
                    dct:description "Statistisk sentralbyrås Virksomhets- og foretaksregister"@nb ;
                    dct:identifier  "1" ; .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6>
                    a                cv:Participation ;
                    cv:role          <https://data.norge.no/concepts/15> ;
                    dct:description  "Mattilsynet"@nb ;
                    dct:identifier   "6" .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1>
                    a                cv:Evidence ;
                    dct:description  "Vandelsattest"@nb ;
                    dct:identifier   "1" ;
                    dct:title        "Vandelsattest"@nb .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/output/4>
                    a                cv:Output ;
                    dct:description  "Serveringsbevilling"@nb ;
                    dct:identifier   "4" ;
                    dct:title        "Serveringsbevilling"@nb ;
                    dct:type         <https://data.norge.no/concepts/205> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/contact/1>
                    rdf:type cv:ContactPoint;
                    schema:hoursAvailable <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exApningstidResepsjon.ttl>;
                    cv:ContactPage <https://www.bronnoy.kommune.no/>;
                    cv:email "mailto:postmottak@bronnoy.kommune.no"^^xsd:anyURI;
                    vcard:hasLanguage <http://publications.europa.eu/resource/authority/language/NOB>,
                       <http://publications.europa.eu/resource/authority/language/NNO>,
                       <http://publications.europa.eu/resource/authority/language/ENG>;
                    cv:telephone "tel:+4775012000";
                    cv:openingHours "Resepsjonen er åpent for henvendelser mandag - fredag: kl  10:00 - 14:00."@no,
                       "Teksten blir vist på nynorsk."@nn,
                       "The reception is open for inquiries Monday - Friday: 10:00 - 14:00."@en;
                    cv:specialOpeningHoursSpecification <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHelligdagerStengt.ttl> .

            <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exApningstidResepsjon.ttl>
                    rdf:type cv:OpeningHoursSpecification;
                    schema:dayOfWeek <https://schema.org/Monday>,
                        <https://schema.org/Tuesday>,
                        <https://schema.org/Wednesday>,
                        <https://schema.org/Thursday>,
                        <https://schema.org/Friday>;
                    schema:closes "14:00:00"^^xsd:time;
                    schema:opens "10:00:00"^^xsd:time .

            <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exHelligdagerStengt.ttl>
                    rdf:type cv:OpeningHoursSpecification;
                    schema:dayOfWeek <https://schema.org/PublicHolidays> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/rule/1> a cpsv:Rule ;
                    dct:description     "Lov om behandlingsmåten i forvaltningssaker (https://lovdata.no/lov/1967-02-10)"@nb ;
                    dct:identifier      "1" ;
                    dct:language        <http://publications.europa.eu/resource/authority/language/NOB> ;
                    dct:title           "Lov om behandlingsmåten i forvaltningssaker"@nb ;
                    cpsv:implements     <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> , <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/legalresource/1> a eli:LegalResource ;
                    dct:description     "Lov om Enhetsregisteret"@nb ;
                    rdfs:seeAlso         <https://lovdata.no/eli/lov/1994/06/03/15/nor/html> ; .

            <https://data.brreg.no/enhetsregisteret/api/enheter/971526920> a dct:Agent ;
                    dct:identifier "971526920" ;
                    dct:title "Statistisk sentralbyrå"@nb ;
                    foaf:name "STATISTISK SENTRALBYRÅ" ;
                    cv:playsRole <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> ; .

            <https://data.brreg.no/enhetsregisteret/api/enheter/971526921> a dct:Agent ;
                    dct:identifier "971526921" ;
                    dct:title "Tull"@nb ;
                    foaf:name "TULLEBYRÅ" ;
                    cv:playsRole <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6> ; .


            <http://localhost:5000/services/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .

            <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789>
                    a                      rov:RegisteredOrganization ;
                    dct:identifier         "123456789" ;
                    rov:legalName          "Digitaliseringsdirektoratet" ;
                    foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
                    rov:orgType            orgtype:ORGL ;
                    br:orgPath             "/STAT/987654321/123456789" ."""

    event_src = """
            @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
            @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
            @prefix rov:   <http://www.w3.org/ns/regorg#> .
            @prefix cpsv: <http://purl.org/vocab/cpsv#> .
            @prefix dct: <http://purl.org/dc/terms/> .
            @prefix cv: <http://data.europa.eu/m8g/> .
            @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
            @prefix dcat:  <http://www.w3.org/ns/dcat#> .
            @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
            @prefix schema:  <http://schema.org/> .
            @prefix eli: <http://data.europa.eu/eli/ontology#> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> a cv:BusinessEvent ;
                dct:identifier "1" ;
                dct:title "Starte og drive restaurant"@nb ;
                dct:description "Elektronisk prosess for etablering og oppstart av en bedrift."@nb ;
                dct:type <https://data.norge.no/concepts/306> ;
                dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ,
                            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> ;
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/events/2> a cv:LifeEvent ;
                dct:identifier "2" ;
                dct:title "Oppgjør etter dødsfall"@nb ;
                dct:description "Elektronisk prosess for oppgjør etter dødsfall."@nb ;
                dct:type <https://data.norge.no/concepts/308> ;
                dct:relation <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> ;
                cv:hasCompetentAuthority    <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
            .

            <https://data.norge.no/concepts/300> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <https://data.norge.no/concepts/304> a skos:Concept ;
                    skos:broader    <https://data.norge.no/concepts/310> ;
                    skos:narrower   <https://data.norge.no/concepts/306> ;
                    skos:prefLabel  "Drive en bedrift"@nb
            .

            <https://data.norge.no/concepts/306> a skos:Concept ;
                    skos:broader    <https://data.norge.no/concepts/304> ;
                    skos:prefLabel  "Skatt og avgift"@nb
            .

            <https://data.norge.no/concepts/308> a skos:Concept ;
                    skos:prefLabel "Dødsfall og arv"@nb ;
            .

            <https://data.norge.no/concepts/310> a skos:Concept ;
                    skos:narrower   <https://data.norge.no/concepts/304> ;
                    skos:prefLabel  "Starte og drive en bedrift"@nb
            .

            <http://localhost:5000/events/fdk-2>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-2" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/events/2>
            .

            <http://localhost:5000/events/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1>
            .

            <http://localhost:5000/events/fdk-4>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-4" ;
                    dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
            .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                    cv:hasCompetentAuthority    <http://public-service-publisher.fellesdatakatalog.digdir.no/public-organisation/3> ;
                    cv:isGroupedBy              <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> ;
                    dct:description             "Dette skjemaet  brukes for å registrere en ny virksomhet, eller søke om godkjenning av en ny næringsmiddelvirksomhet. Skjemaet skal også brukes dersom du vil utvide aktiviteten i en allerede eksisterende virksomhet og starte med en ny aktivitet som ikke er registrert."@nb ;
                    dct:identifier              "4" ;
                    dct:title                   "Ny næringsmiddelvirksomhet inkl. matkontaktmaterialer"@nb
            .

            <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789>
                    a                      rov:RegisteredOrganization ;
                    dct:identifier         "123456789" ;
                    rov:legalName          "Digitaliseringsdirektoratet" ;
                    foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
                    rov:orgType            orgtype:ORGL ;
                    br:orgPath             "/STAT/987654321/123456789" ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            isGroupedBy=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            ],
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "en": "Norwegian Digitalisation Agency",
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                    },
                    organisasjonsform="ORGL",
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
                SkosCode(
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
            hasCriterion=[
                CriterionRequirement(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/criterion-requirement/5",
                    identifier="5",
                    name={"nb": "Krav om vandel"},
                    type=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/153",
                            prefLabel={"nb": "Attest"},
                        )
                    ],
                ),
            ],
            hasParticipation=[
                Participation(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                    identifier="1",
                    description={
                        "nb": "Statistisk sentralbyrås Virksomhets- og foretaksregister"
                    },
                    role=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/101",
                            prefLabel={"nb": "Datakonsument"},
                            extraType=None,
                        )
                    ],
                    agents=[
                        Agent(
                            uri="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                            identifier="971526920",
                            title={"nb": "Statistisk sentralbyrå"},
                            name="STATISTISK SENTRALBYRÅ",
                            playsRole=[
                                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1"
                            ],
                        )
                    ],
                )
            ],
            hasInput=[
                Evidence(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/evidence/1",
                    identifier="1",
                    name={"nb": "Vandelsattest"},
                    description={"nb": "Vandelsattest"},
                    type=None,
                    language=None,
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
                        SkosCode(
                            uri="http://publications.europa.eu/resource/authority/language/ENG",
                            code="ENG",
                            prefLabel={
                                "en": "English",
                                "nb": "Engelsk",
                                "nn": "Engelsk",
                                "no": "Engelsk",
                            },
                        ),
                        SkosCode(
                            uri="http://publications.europa.eu/resource/authority/language/NNO",
                            code="NNO",
                            prefLabel={
                                "en": "Norwegian Nynorsk",
                                "nb": "Norsk Nynorsk",
                                "nn": "Norsk Nynorsk",
                                "no": "Norsk Nynorsk",
                            },
                        ),
                        SkosCode(
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
                            dayOfWeek=["https://schema.org/PublicHolidays"],
                        )
                    ],
                    hoursAvailable=[
                        OpeningHoursSpecification(
                            uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exApningstidResepsjon.ttl",
                            dayOfWeek=[
                                "https://schema.org/Friday",
                                "https://schema.org/Monday",
                                "https://schema.org/Thursday",
                                "https://schema.org/Tuesday",
                                "https://schema.org/Wednesday",
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
                        SkosCode(
                            uri="http://publications.europa.eu/resource/authority/language/NOB",
                            code=None,
                            prefLabel=None,
                        )
                    ],
                    name={"nb": "Lov om behandlingsmåten i forvaltningssaker"},
                )
            ],
            hasLegalResource=[
                LegalResource(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/legalresource/1",
                    description={"nb": "Lov om Enhetsregisteret"},
                    url="https://lovdata.no/eli/lov/1994/06/03/15/nor/html",
                )
            ],
            hasChannel=[
                Channel(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/channel/2",
                    identifier="2",
                    type=SkosConcept(
                        uri="https://data.norge.no/concepts/257",
                        prefLabel={"nb": "Post", "en": "Mail"},
                    ),
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
                    ifAccessedThrough=Channel(
                        uri="http://public-service-publisher.fellesdatakatalog.digdir.no/channel/10",
                        identifier="10",
                        type=SkosConcept(
                            uri="https://data.norge.no/concepts/257",
                            prefLabel={"nb": "Post", "en": "Mail"},
                        ),
                    ),
                    isDefinedBy=[
                        Publisher(
                            uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                            id="123456789",
                            name="Digitaliseringsdirektoratet",
                            orgPath="/STAT/987654321/123456789",
                            prefLabel={
                                "en": "Norwegian Digitalisation Agency",
                                "nn": "Digitaliseringsdirektoratet",
                                "nb": "Digitaliseringsdirektoratet",
                            },
                            organisasjonsform="ORGL",
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
            type="publicservices",
        ),
    }

    assert parse_public_services(src, event_src) == expected


def test_parse_multiple_public_services(
    mock_reference_data_client: Mock,
) -> None:
    src = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                dct:identifier "1" ;
                dct:title "Ei offentleg teneste"@nb ;
                dct:description "Ei offentleg teneste som tener som døme til bruk i utvikling"@nn ;
                cv:processingTime "not valid duration type"^^xsd:duration ;
                cv:hasCompetentAuthority <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> ;
                cv:hasParticipation <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1>, <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6> ;
                cv:isGroupedBy <http://public-service-publisher.fellesdatakatalog.digdir.no/events/1> .

        <http://localhost:5000/services/fdk-1>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-1" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> a cpsv:PublicService ;
                dct:identifier "2" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ;
                cv:hasCompetentAuthority <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/991825827> .

        <http://localhost:5000/services/fdk-2>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-2" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> a cpsv:PublicService ;
                dct:identifier "3" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ; .

        <http://localhost:5000/services/fdk-3>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-3" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/4> a cpsv:PublicService ;
                dct:identifier "4" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ; .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> a cv:Participation ;
                dct:identifier "1" ;
                dct:description "Statistisk sentralbyrås Virksomhets- og foretaksregister"@nb ;
                cv:role <https://data.norge.no/concepts/101> ;
        .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6>
                a                cv:Participation ;
                cv:role          <https://data.norge.no/concepts/15> ;
                dct:description  "Mattilsynet"@nb ;
                dct:identifier   "6" .

        <https://data.brreg.no/enhetsregisteret/api/enheter/985399077> a dct:Agent ;
                dct:identifier "985399077" ;
                dct:title "Mattilsynet"@nb ;
                foaf:name "MATTILSYNET" ;
                cv:playsRole <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1>,
                            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6> ;
        .

        <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789>
                a                      rov:RegisteredOrganization ;
                dct:identifier         "123456789" ;
                rov:legalName          "Digitaliseringsdirektoratet" ;
                foaf:name              "Digitaliseringsdirektoratet"@nn , "Digitaliseringsdirektoratet"@nb , "Norwegian Digitalisation Agency"@en ;
                rov:orgType            orgtype:ORGL ;
                br:orgPath             "/STAT/987654321/123456789" .

        <http://localhost:5000/services/fdk-4>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-4" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            isGroupedBy=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/events/1",
            ],
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "en": "Norwegian Digitalisation Agency",
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                    },
                    organisasjonsform="ORGL",
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            hasParticipation=[
                Participation(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                    identifier="1",
                    description={
                        "nb": "Statistisk sentralbyrås Virksomhets- og foretaksregister"
                    },
                    role=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/101",
                            prefLabel=None,
                            extraType=None,
                        )
                    ],
                    agents=[
                        Agent(
                            uri="https://data.brreg.no/enhetsregisteret/api/enheter/985399077",
                            identifier="985399077",
                            title={"nb": "Mattilsynet"},
                            name="MATTILSYNET",
                            playsRole=[
                                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6",
                            ],
                        )
                    ],
                ),
                Participation(
                    uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6",
                    identifier="6",
                    description={"nb": "Mattilsynet"},
                    role=[
                        SkosConcept(
                            uri="https://data.norge.no/concepts/15",
                            prefLabel=None,
                            extraType=None,
                        )
                    ],
                    agents=[
                        Agent(
                            uri="https://data.brreg.no/enhetsregisteret/api/enheter/985399077",
                            identifier="985399077",
                            title={"nb": "Mattilsynet"},
                            name="MATTILSYNET",
                            playsRole=[
                                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/6",
                            ],
                        )
                    ],
                ),
            ],
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
                Publisher(
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

    assert parse_public_services(src) == expected


def test_parse_cpsvno_services(
    mock_reference_data_client: Mock,
) -> None:
    src = """
        @prefix adms:   <http://www.w3.org/ns/adms#> .
        @prefix cccev:  <http://data.europa.eu/m8g/cccev/> .
        @prefix cpsv:   <http://purl.org/vocab/cpsv#> .
        @prefix cpsvno: <https://data.norge.no/vocabulary/cpsvno#> .
        @prefix cv:     <http://data.europa.eu/m8g/> .
        @prefix dcat:   <http://www.w3.org/ns/dcat#> .
        @prefix dcatno: <https://data.norge.no/vocabulary/dcatno#> .
        @prefix dct:    <http://purl.org/dc/terms/> .
        @prefix eli:    <http://data.europa.eu/eli/ontology#> .
        @prefix foaf:   <http://xmlns.com/foaf/0.1/> .
        @prefix locn:   <http://www.w3.org/ns/locn#> .
        @prefix odrl:   <http://www.w3.org/ns/odrl/2/> .
        @prefix org:    <http://www.w3.org/ns/org#> .
        @prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix schema: <http://schema.org/> .
        @prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
        @prefix vcard:  <http://www.w3.org/2006/vcard/ns#> .
        @prefix xkos:   <http://rdf-vocabulary.ddialliance.org/xkos#> .
        @prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

        <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exAktorDummy.ttl>
                rdf:type        foaf:Agent ;
                dct:identifier  "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exAktorDummy.ttl"^^xsd:anyURI ;
                locn:address    [ rdf:type          locn:Address ;
                                  locn:fullAddress  "Dummygata 1, Dummyby, Dummyland"@nb
                                ] ;
                foaf:name       "Dummy aktør"@nb , "Dummy aktør"@nn , "Dummy agent"@en .

        <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteresultatDummy.ttl>
                rdf:type         cv:Output ;
                dct:description  "The text is displayed in English."@en , "Teksten blir vist på nynorsk."@nn , "Dette er et dummy tjenesteresultat som kan brukes i forbindelse med testing av CPSV-AP-NO når det er behov for en relasjon til et tjenesteresultat."@nb ;
                dct:identifier   "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteresultatDummy.ttl"^^xsd:anyURI ;
                dct:language     <http://publications.europa.eu/resource/authority/language/ENG> , <http://publications.europa.eu/resource/authority/language/NOB> , <http://publications.europa.eu/resource/authority/language/NNO> ;
                dct:title        "Dummy tjenesteresultat"@nb , "Dummy tjenesteresultat"@nn , "Dummy service result"@en .

        <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exKontaktpunktDummy.ttl>
                rdf:type cv:ContactPoint;
                cv:contactPage <https://example.org/exKontaktside>;
                cv:email "mailto:postmottak@example.org"^^xsd:anyURI;
                cv:telephone "tel:+4712345678";
                vcard:hasLanguage <http://publications.europa.eu/resource/authority/language/NOB>,
                    <http://publications.europa.eu/resource/authority/language/NNO>,
                    <http://publications.europa.eu/resource/authority/language/ENG> .

        <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl>
                rdf:type           cpsvno:Service ;
                cv:ownedBy         <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exAktorDummy.ttl> ;
                dct:description    "The text is displayed in English."@en , "Teksten blir vist på nynorsk."@nn , "Dette er en dummytjeneste som kan brukes i forbindelse med testing av CPSV-AP-NO når det er behov for en relasjon til en tjeneste som det ikke finnes eksempel på ennå."@nb ;
                dct:identifier     "https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl"^^xsd:anyURI ;
                dct:language       <http://publications.europa.eu/resource/authority/language/ENG> , <http://publications.europa.eu/resource/authority/language/NOB> ;
                dct:title          "Dummy service"@en , "Dummytjeneste"@nn , "Dummytjeneste"@nb ;
                cpsv:produces      <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteresultatDummy.ttl> ;
                cv:hasContactPoint  <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exKontaktpunktDummy.ttl> .

        <https://www.staging.fellesdatakatalog.digdir.no/public-services/1fc38c3c-1c86-3161-a9a7-e443fd94d413>
                rdf:type           dcat:CatalogRecord ;
                dct:identifier     "1fc38c3c-1c86-3161-a9a7-e443fd94d413" ;
                dct:issued         "2022-05-18T11:26:51.589Z"^^xsd:dateTime ;
                dct:modified       "2022-05-18T11:26:51.589Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exTjenesteDummy.ttl> ."""

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
                Publisher(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exAktorDummy.ttl",
                    id="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exAktorDummy.ttl",
                    name="Dummy aktør",
                    prefLabel={
                        "nb": "Dummy aktør",
                        "nn": "Dummy aktør",
                        "en": "Dummy agent",
                    },
                )
            ],
            contactPoint=[
                CVContactPoint(
                    uri="https://raw.githubusercontent.com/Informasjonsforvaltning/cpsv-ap-no/develop/examples/exKontaktpunktDummy.ttl",
                    email=["mailto:postmottak@example.org"],
                    telephone=["tel:+4712345678"],
                    contactPage=["https://example.org/exKontaktside"],
                    language=[
                        SkosCode(
                            uri="http://publications.europa.eu/resource/authority/language/ENG",
                            code="ENG",
                            prefLabel={
                                "en": "English",
                                "nb": "Engelsk",
                                "nn": "Engelsk",
                                "no": "Engelsk",
                            },
                        ),
                        SkosCode(
                            uri="http://publications.europa.eu/resource/authority/language/NNO",
                            code="NNO",
                            prefLabel={
                                "en": "Norwegian Nynorsk",
                                "nb": "Norsk Nynorsk",
                                "nn": "Norsk Nynorsk",
                                "no": "Norsk Nynorsk",
                            },
                        ),
                        SkosCode(
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
                SkosCode(
                    uri="http://publications.europa.eu/resource/authority/language/ENG",
                    code="ENG",
                    prefLabel={
                        "en": "English",
                        "nb": "Engelsk",
                        "nn": "Engelsk",
                        "no": "Engelsk",
                    },
                ),
                SkosCode(
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
                )
            ],
            type="publicservices",
        )
    }

    assert parse_public_services(src) == expected
