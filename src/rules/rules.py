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
    '''program : new_scope statement
           | new_scope function
           | new_scope class'''
    MAIN_INSTRUCTION_TAPE.merge(get_current_scope().instruction_tape)
    MAIN_INSTRUCTION_TAPE.add_constant_section()
    pop_scope()


def p_type(t):
    '''type : STRING
             | INT
             | VOID'''
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)
