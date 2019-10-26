import sys
import ply.lex as lex
import ply.yacc as yacc
from src.VYPcode.utils import print_code_header, print_code_aliases
from src.tokens import *
from src.rules import *


lexer = lex.lex()
parser = yacc.yacc(outputdir="generated")


def parse():
    print_code_header()
    print_code_aliases()
    with open(sys.argv[1], 'r') as content_file:  # todo check for error in arguments
        parser.parse(content_file.read(), debug=True)


parse()



