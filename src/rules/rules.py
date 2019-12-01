from src.VYPcode.VYPaOperations.operations import LABEL
from src.error import Error
from src.instructionsTape import MAIN_INSTRUCTION_TAPE
from src.rules.functionsRules import *
from src.rules.classRules import *
from src.rules.statementsRules import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_program(t):
    '''program : init program_body'''
    main: VYPaFunction = PT.get_global_scope().get_function("main")
    if not (main and main.type == "void"):
        Error(Error.SemanticError, "wrong type or not defined Main function")

    MAIN_INSTRUCTION_TAPE.add_constant_section()
    MAIN_INSTRUCTION_TAPE.merge(PT.get_global_scope().instruction_tape)
    MAIN_INSTRUCTION_TAPE.add(LABEL("END"))
    PT.pop_scope()


def p_init(t):
    '''init : '''
    PT.push_scope()
    MAIN_INSTRUCTION_TAPE.add_build_in_functions()


def p_program_body(t):
    '''program_body : statement
           | function
           | class'''
    pass


def p_type(t):
    '''type : STRING
             | INT
             | VOID'''
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)
