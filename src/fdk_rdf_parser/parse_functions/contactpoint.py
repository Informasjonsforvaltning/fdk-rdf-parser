from typing import Any, List, Optional

from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import ContactPoint
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    object_value,
    resource_list,
    value_translations,
    vcard_uri,
)


def extract_contact_points(
    graph: Graph, subject: URIRef
) -> Optional[List[ContactPoint]]:
    values = []
    for resource in resource_list(graph, subject, dcat_uri("contactPoint")):
        resource_uri = None
        if isinstance(resource, URIRef):
            resource_uri = resource.toPython()

        values.append(
            ContactPoint(
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
