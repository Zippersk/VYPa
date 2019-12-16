from src.VYPcode.AST.blocks.class_block import AST_class
from src.VYPcode.AST.blocks.class_instance import AST_class_instance
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.function import AST_function
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.variable_call import AST_variable_call

from src.common import CallType


def p_class(t):
    '''class : CLASS NAME COLON NAME class_body'''       
    t[0] = AST_class(t[2], t[4])
    for statement in t[5]:
        if isinstance(statement, AST_function):
            t[0].add_function(statement)
        else:
            t[0].add_block(statement)


def p_class_statements(t):
    '''class_body : LBRACKET class_statements RBRACKET'''
    t[0] = t[2]


def p_class_statements_empty(t):
    '''class_statements :'''
    t[0] = []


def p_class_statements_function(t):
    '''class_statements : function class_statements'''
    if len(t) > 2 and t[2] is not None:
        t[2].append(t[1])
        t[0] = t[2]
    else:
        t[0] = [t[1]]


def p_class_statements_variable_definition(t):
    '''class_statements : type variables_declaration SEMICOLON class_statements'''
    if len(t) > 4 and t[4] is not None:
        t[4].append(AST_declaration(t[1], t[2]))
        t[0] = t[4]
    else:
        t[0] = [AST_declaration(t[1], t[2])]


def p_class_variable_call(t):
    '''expression : NAME DOT NAME'''
    t[0] = AST_variable_call(t[3], CallType.INSTANCE, t[1])


def p_class_function_call(t):
    '''expression : NAME DOT NAME LPAREN function_params RPAREN'''

    t[0] = AST_function_call(t[5], t[6], CallType.INSTANCE, t[1])


def p_expression_new_class_instance(t):
    '''expression : NEW NAME'''
    t[0] = AST_class_instance(t[2])


def p_class_this_variable_call(t):
    '''expression : THIS DOT NAME'''
    t[0] = AST_variable_call(t[1], CallType.THIS)


def p_class_this_function_call(t):
    '''expression : THIS DOT NAME LPAREN function_params RPAREN'''

    t[0] = AST_function_call(t[3], t[5], CallType.THIS)


def p_class_super_variable_call(t):
    '''expression : SUPER DOT NAME'''
    t[0] = AST_variable_call(t[1], CallType.SUPER)


def p_class_super_function_call(t):
    '''expression : SUPER DOT NAME LPAREN function_params RPAREN'''
    t[0] = AST_function_call(t[3], t[5], CallType.SUPER)

