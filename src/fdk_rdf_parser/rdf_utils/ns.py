from rdflib import URIRef


def dcatURI(subString: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/dcat#{subString}")


def admsURI(subString: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/adms#{subString}")


def dcatApNoURI(subString: str) -> URIRef:
    return URIRef(f"http://difi.no/dcatno#{subString}")


def owlTimeURI(subString: str) -> URIRef:
    return URIRef(f"https://www.w3.org/TR/owl-time/{subString}")


def schemaURI(subString: str) -> URIRef:
    return URIRef(f"http://schema.org/{subString}")


def vcardURI(subString: str) -> URIRef:
    return URIRef(f"http://www.w3.org/2006/vcard/ns#{subString}")


def dctURI(subString: str) -> URIRef:
    return URIRef(f"http://purl.org/dc/terms/{subString}")


def dqvURI(subString: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/dqvNS#{subString}")


def dqvIsoURI(subString: str) -> URIRef:
    return URIRef(f"http://iso.org/25012/2008/dataquality/{subString}")


def provURI(subString: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/prov#{subString}")


def dcatApiURI(subString: str) -> URIRef:
    return URIRef(f"http://dcat.no/dcatapi/{subString}")


def rovURI(subString: str) -> URIRef:
    return URIRef(f"http://www.w3.org/ns/regorg#{subString}")


def brURI(subString: str) -> URIRef:
    return URIRef(
        f"https://github.com/Informasjonsforvaltning/organization-catalogue/blob/develop/src/main/resources/ontology/organization-catalogue.owl#{subString}"  # noqa: B950
    )
