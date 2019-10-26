from src.VYPcode.operations import *

# Parsing rules
from src.VYPcode.scopes import pop_scope, new_scope, push_scope

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


def p_function(t):
    '''function : function_type NAME LPAREN functions_params RPAREN function_body
                | function_type NAME LPAREN VOID RPAREN function_body'''
    pass

def p_class(t):
    '''class : CLASS NAME '''
    pass


def p_variable_type(t):
    '''variable_type : STRING
                     | INT'''


def p_function_type(t):
    '''function_type : STRING
                     | INT
                     | VOID'''


def p_functions_params(t):
    '''functions_params : variable_type NAME
                        | variable_type NAME COMMA functions_params'''


def p_function_body(t):
    '''function_body : new_scope statements_block'''


def p_statements_block(t):
    "statements_block : LBRACKET statements RBRACKET"""
    pop_scope()

def p_statements(t):
    '''statements : statement statements
                  | '''

def p_new_scope(t):
    "new_scope :"
    s = new_scope()
    push_scope(s)


def p_statement_assign(t):
    '''statement : NAME ASSIGMENT expression
                 | variable_type NAME ASSIGMENT expression'''
    names[t[1]] = t[3]


def p_statement_expr(t):
    'statement : expression'


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        print(ADDI(t[0], t[1], t[3]))

        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


def p_error(t):
    print("Syntax error at '%s'" % t.value)