

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_program(t):
    '''program : statement
           | function
           | class'''
    pass


from src.rules.functionsRules import *
from src.rules.classRules import *
from src.rules.statementsRules import *

def p_type(t):
    '''type : STRING
             | INT
             | VOID'''
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)
