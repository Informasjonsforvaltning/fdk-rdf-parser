from rdflib import URIRef

def dcatURI(subString) -> URIRef:
    return URIRef('http://www.w3.org/ns/dcat#' + subString)

def admsURI(subString) -> URIRef:
    return URIRef('http://www.w3.org/ns/adms#' + subString)

def dcatApNoURI(subString) -> URIRef:
    return URIRef('http://difi.no/dcatno#' + subString)

def owlTimeURI(subString) -> URIRef:
    return URIRef('https://www.w3.org/TR/owl-time/' + subString)

def schemaURI(subString) -> URIRef:
    return URIRef('http://schema.org/' + subString)

def vcardURI(subString) -> URIRef:
    return URIRef('http://www.w3.org/2006/vcard/ns#' + subString)

def dctURI(subString) -> URIRef:
    return URIRef('http://purl.org/dc/terms/' + subString)

def dqvURI(subString) -> URIRef:
    return URIRef('http://www.w3.org/ns/dqvNS#' + subString)

def dqvIsoURI(subString) -> URIRef:
    return URIRef('http://iso.org/25012/2008/dataquality/' + subString)

def provURI(subString) -> URIRef:
    return URIRef('http://www.w3.org/ns/prov#' + subString)

def dcatApiURI(subString) -> URIRef:
    return URIRef('http://dcat.no/dcatapi/' + subString)
