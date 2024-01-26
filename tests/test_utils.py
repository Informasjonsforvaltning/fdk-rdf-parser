from fdk_rdf_parser.rdf_utils import string_to_float


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
