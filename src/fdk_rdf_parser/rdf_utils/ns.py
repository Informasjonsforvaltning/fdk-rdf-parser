from rdflib import URIRef

def dcatURI(subString) -> URIRef:
    return URIRef(u'http://www.w3.org/ns/dcat#' + subString)

def admsURI(subString) -> URIRef:
    return URIRef(u'http://www.w3.org/ns/adms#' + subString)

def dcatApNoURI(subString) -> URIRef:
    return URIRef(u'http://difi.no/dcatno#' + subString)

def owlTimeURI(subString) -> URIRef:
    return URIRef(u'https://www.w3.org/TR/owl-time/' + subString)

def schemaURI(subString) -> URIRef:
    return URIRef(u'http://schema.org/' + subString)

def vcardURI(subString) -> URIRef:
    return URIRef(u'http://www.w3.org/2006/vcard/ns#' + subString)

def dctURI(subString) -> URIRef:
    return URIRef(u'http://purl.org/dc/terms/' + subString)
