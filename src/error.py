"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
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
    exit(code)