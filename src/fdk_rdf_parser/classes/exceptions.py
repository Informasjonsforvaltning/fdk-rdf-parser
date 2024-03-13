from rdflib.exceptions import ParserError as RdflibParserError


class ParserError(RdflibParserError):
    def __init__(self, msg: str = "Parser error"):
        RdflibParserError.__init__(self, msg)
        self.msg: str = msg

    def __str__(self) -> str:
        return self.msg


class MultipleResourcesError(ValueError):
    pass


class MissingResourceError(ValueError):
    pass
