from src.VYPcode.AST.blocks.class_block import AST_class
from src.VYPcode.AST.blocks.declaration import AST_declaration


def p_class(t):
    '''class : CLASS NAME COLON NAME class_body'''
    t[0].append(AST_class(t[2], t[4], t[5]))


def p_class_statements(t):
    '''class_body : LBRACKET class_statements RBRACKET'''
    t[0] = t[2]


def p_class_statements_empty(t):
    '''class_statements :'''
    t[0] = []


def p_class_statements_function(t):
    '''class_statements : function class_statements'''
    t[0].append(t[1])


def p_class_statements_variable_definition(t):
    '''class_statements : type variables_declaration SEMICOLON class_statements'''
    t[0].append(AST_declaration(t[1], t[2]))


def p_class_variable_call(t):
    '''expression : THIS DOT NAME'''
    t[1].name = "*this_" + t[1].name
    t[0].append(t[1])


def p_class_predecessor_variable_call(t):
    '''expression : SUPER DOT NAME'''
    t[1].name = "*super_" + t[1].name
    t[0].append(t[1])


def p_class_function_call(t):
    '''expression : THIS DOT function_call'''
    t[1].name = "*this_" + t[1].name
    t[0].append(t[1])


def p_class_predecessor_function_call(t):
    '''expression : SUPER DOT function_call'''
    t[1].name = "*super_" + t[1].name
    t[0].append(t[1])
