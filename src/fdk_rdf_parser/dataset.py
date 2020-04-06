from rdflib import Graph

def parseDatasets(rdfData: str):
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    return len(datasetsGraph)