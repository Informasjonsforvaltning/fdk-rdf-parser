from typing import (
    Any,
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import (
    CVContactPoint,
    DCATContactPoint,
)
from fdk_rdf_parser.parse_functions.opening_hours_specification import (
    extract_opening_hours_specification,
)
from fdk_rdf_parser.parse_functions.skos_code import extract_skos_code_list
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    dcat_uri,
    object_value,
    resource_list,
    schema_uri,
    value_list,
    value_translations,
    vcard_uri,
)


def extract_contact_points(
    graph: Graph, subject: URIRef
) -> Optional[List[DCATContactPoint]]:
    values = []
    for resource in resource_list(graph, subject, dcat_uri("contactPoint")):
        resource_uri = None
        if isinstance(resource, URIRef):
            resource_uri = resource.toPython()

        values.append(
            DCATContactPoint(
                uri=resource_uri,
                fullname=object_value(graph, resource, vcard_uri("fn")),
                email=extract_has_email(graph, resource),
                organizationName=value_translations(
                    graph, resource, vcard_uri("hasOrganizationName")
                ),
                organizationUnit=value_translations(
                    graph, resource, vcard_uri("organization-unit")
                ),
                hasURL=object_value(graph, resource, vcard_uri("hasURL")),
                hasTelephone=extract_has_telephone(graph, resource),
            )
        )

    return values if len(values) > 0 else None


def extract_has_telephone(graph: Graph, subject: Any) -> Optional[Any]:
    tel_ref = graph.value(subject, vcard_uri("hasTelephone"))
    if tel_ref:
        tel_value = object_value(graph, tel_ref, vcard_uri("hasValue"))
        if tel_value is None:
            tel_value = tel_ref.toPython()

        if "tel:" in tel_value:
            return tel_value[4:]
        else:
            return tel_value
    else:
        return None


def extract_has_email(graph: Graph, subject: Any) -> Optional[Any]:
    mail_ref = graph.value(subject, vcard_uri("hasEmail"))
    if mail_ref:
        email = object_value(graph, mail_ref, vcard_uri("hasValue"))
        if email is None:
            email = mail_ref.toPython()

        if "mailto:" in email:
            return email[7:]
        else:
            return email
    else:
        return None


def extract_cv_has_contact_point(
    graph: Graph, subject: URIRef
) -> Optional[List[CVContactPoint]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasContactPoint")):
        values.append(
            CVContactPoint(
                uri=resource.toPython() if isinstance(resource, URIRef) else None,
                contactType=value_translations(
                    graph, resource, schema_uri("contactType")
                ),
                email=value_list(graph, resource, cv_uri("email")),
                telephone=value_list(graph, resource, cv_uri("telephone")),
                contactPage=value_list(graph, resource, cv_uri("contactPage")),
                language=extract_skos_code_list(
                    graph, resource, vcard_uri("hasLanguage")
                ),
                openingHours=value_translations(
                    graph, resource, cv_uri("openingHours")
                ),
                specialOpeningHours=extract_opening_hours_specification(
                    graph, resource, cv_uri("specialOpeningHoursSpecification")
                ),
                hoursAvailable=extract_opening_hours_specification(
                    graph, resource, schema_uri("hoursAvailable")
                ),
            )
        )

    return values if len(values) > 0 else None
