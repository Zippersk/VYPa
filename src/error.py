"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
import os
from enum import Enum

import sys


class Error(Enum):
    LexicalError = 11
    SyntaxError = 12
    TypesIncompatibility = 13
    SemanticError = 14
    CodeGenerationError = 15
    InternalError = 19


def Exit(code, reason):
    # print(reason) # remove error message before Assignment
    os._exit(code.value)
