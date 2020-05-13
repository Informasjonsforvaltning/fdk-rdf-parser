org_response = """
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
        br:domainName          "difi.no" ;
        br:municipality        <https://data.geonorge.no/administrativeEnheter/kommune/id/173018> ;
        br:nace                "84.110" ;
        br:norwegianRegistry   <https://data.brreg.no/enhetsregisteret/api/enheter/123456789> ;
        br:orgPath             "/STAT/987654321/123456789" ;
        br:sectorCode          "6100" .
"""
