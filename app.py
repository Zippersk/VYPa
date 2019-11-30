import sys
import ply.lex as lex
import ply.yacc as yacc

from src.output import Output
from src.tokens import *
from src.rules.rules import *


lexer = lex.lex()
parser = yacc.yacc(outputdir="generated", start="program")


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as content_file:  # todo check for error in arguments
        parser.parse(content_file.read())
    Output.print()



