from rdflib.exceptions import ParserError as RdflibParserError


class ParserError(RdflibParserError):
    def __init__(self: "ParserError", msg: str = "Parser error") -> None:
        RdflibParserError.__init__(self, msg)
        self.msg: str = msg


class MultipleResourcesError(ValueError):
    pass


class MissingResourceError(ValueError):
    pass
