"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.Instructions.Instructions import LABEL, COMMENT
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Error, Exit
from src.instructionsTape import MAIN_INSTRUCTION_TAPE
from src.parser.functions import *
from src.parser.classes import *
from src.parser.statements import *
from src.parser.expressions import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUAL', 'NOTEQUAL'),
    ('left', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NEGATION'),
)

# dictionary of names
names = {}


def p_program(t):
    '''program : init program_body'''
    main = AST.get_root().get_function("main")
    if not (main and main.type == VYPaVoid()):
        Exit(Error.SemanticError, "wrong type or not defined Main function")

    MAIN_INSTRUCTION_TAPE.add_constant_section()
    MAIN_INSTRUCTION_TAPE.merge(AST.get_root().get_instructions(None))
    MAIN_INSTRUCTION_TAPE.add(LABEL("END"))


def p_init(t):
    '''init : '''
    MAIN_INSTRUCTION_TAPE.add_build_in_functions()


def p_program_body_empty(t):
    '''program_body :'''
    pass


def p_program_class(t):
    '''program_body : class program_body'''
    AST.root.add_class(t[1])
    t[0] = t[1]


def p_global_function(t):
    '''program_body : function program_body'''
    AST.root.add_function(t[1])
    t[0] = t[1]


def p_type(t):
    '''type : STRING
             | INT
             | VOID
             | NAME'''
    if t[1] == "int":
        t[0] = VYPaInt()
    elif t[1] == "string":
        t[0] = VYPaString()
    elif t[1] == "void":
        t[0] = VYPaVoid()
    else:
        t[0] = VYPaClass(t[1])

def p_error(t):
    print("Syntax error at '%s'" % t.value)
