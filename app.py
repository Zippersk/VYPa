# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
import sys
from VYPcode.utils import print_code_header, print_code_aliases

from tokens import *

# Build the lexer
import ply.lex as lex

lexer = lex.lex()

from rules import *
import ply.yacc as yacc

parser = yacc.yacc(outputdir="generated")


def parse():
    print_code_header()
    print_code_aliases()
    with open(sys.argv[1], 'r') as content_file:  # todo check for error in arguments
        parser.parse(content_file.read())


parse()



