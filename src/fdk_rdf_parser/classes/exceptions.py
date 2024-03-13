from rdflib.exceptions import ParserError as RdflibParserError


class ParserError(RdflibParserError):
    pass


class MultipleResourcesError(ValueError):
    pass


class MissingResourceError(ValueError):
    pass
