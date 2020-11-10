from rdflib import URIRef


def dcat_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/dcat#{sub_string}")


def adms_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/adms#{sub_string}")


def dcat_ap_no_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://difi.no/dcatno#{sub_string}")


def owl_time_uri(sub_string: str) -> URIRef:
    return URIRef(f"https://www.w3.org/TR/owl-time/{sub_string}")


def schema_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://schema.org/{sub_string}")


def vcard_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://www.w3.org/2006/vcard/ns#{sub_string}")


def dct_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://purl.org/dc/terms/{sub_string}")


def dqv_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/dqvNS#{sub_string}")


def dqv_iso_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://iso.org/25012/2008/dataquality/{sub_string}")


def prov_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/prov#{sub_string}")


def dcat_api_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://dcat.no/dcatapi/{sub_string}")


def rov_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/regorg#{sub_string}")


def br_uri(sub_string: str) -> URIRef:
    return URIRef(
        f"https://github.com/Informasjonsforvaltning/organization-catalogue/blob/develop/src/main/resources/ontology/organization-catalogue.owl#{sub_string}"  # noqa: B950
    )


def model_dcat_ap_no_uri(sub_string: str) -> URIRef:
    return URIRef(f"https://data.norge.no/vocabulary/modelldcatno#{sub_string}")


def xkos_uri(sub_string: str) -> URIRef:
    return URIRef(f"https://rdf-vocabulary.ddialliance.org/xkos/{sub_string}")


def cv_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://data.europa.eu/m8g/{sub_string}")


def cpsv_uri(sub_string: str) -> URIRef:
    return URIRef(f"http://purl.org/vocab/cpsv#{sub_string}")
