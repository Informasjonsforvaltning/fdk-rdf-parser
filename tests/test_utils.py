from datetime import datetime

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.rdf_utils import date_value, string_to_float


def test_string_to_float() -> None:
    assert string_to_float("3.14") == float(3.14)
    assert string_to_float("3,14") == float(3.14)
    assert string_to_float("314") == float(314)
    assert string_to_float("asdfg") is None
    assert string_to_float("3,000.14") == float(3000.14)
    assert string_to_float("3,000,14") is None
    assert string_to_float("3.000,14") == float(3000.14)
    assert string_to_float("3,000.000,14") is None
    assert string_to_float("3,000.000,14") is None


def test_date_value_timezone_normalization() -> None:
    """Test that date_value normalizes +00:00 timezone to Z format."""
    from datetime import timezone

    graph = Graph()
    subject = URIRef("http://example.com/test")
    predicate = DCTERMS.created

    # Add a datetime literal with UTC timezone that will result in +00:00 format
    # This simulates what RDFLib 7.2.1 now produces
    dt = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    literal = Literal(dt, datatype=URIRef("http://www.w3.org/2001/XMLSchema#dateTime"))
    graph.add((subject, predicate, literal))

    result = date_value(graph, subject, predicate)
    # The result should be normalized to use 'Z' instead of '+00:00'
    assert result == "2023-01-01T12:00:00Z"
