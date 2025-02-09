"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""

import sys
import ply.lex as lex
import ply.yacc as yacc

from src.output import Output
from src.tokens import *
from src.parser.program import *

lexer = lex.lex()
parser = yacc.yacc(outputdir="generated", start="program", errorlog=yacc.NullLogger())


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as content_file:
        parser.parse(content_file.read())
    Output.print()



