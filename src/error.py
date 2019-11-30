from enum import Enum


class Error(Enum):
    LexicalError = 11
    SyntaxError = 12
    TypesIncompatibility = 13
    SemanticError = 14
    CodeGenerationError = 15
    InternalError = 19


def Exit(code, reason):
    print(reason)
    Exit(code)