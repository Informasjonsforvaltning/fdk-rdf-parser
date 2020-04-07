from rdflib import Graph, URIRef

def objectValue(graph: Graph, subject: URIRef, predicate: URIRef):
    value = graph.value(subject, predicate)
    return value.toPython() if value != None else None

def objectList(graph: Graph, subject: URIRef, predicate: URIRef):
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj.toPython())
    values.sort()
    return values
