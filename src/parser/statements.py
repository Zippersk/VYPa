"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.assigment import AST_assigment
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.expression import AST_expression
from src.VYPcode.AST.blocks.ifelse import AST_ifelse
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.AST.blocks.while_loop import AST_while


def p_statements_block(t):
    "statements_block : LBRACKET statements RBRACKET"""
    t[0] = t[2]


def p_statements(t):
    '''statements : statement SEMICOLON statements
                  |'''
    if len(t) > 3:
        t[3].insert(0, t[1])
        t[0] = t[3]
    elif len(t) > 2:
        t[0] = [t[1]]
    else:
        t[0] = []


def p_statements_if_else(t):
    '''statements : if_statement statements'''
    if len(t) > 2:
        t[2].insert(0, t[1])
        t[0] = t[2]
    elif len(t) > 2:
        t[0] = [t[1]]
    else:
        t[0] = []


def p_statement_while_loop(t):
    '''statements : while_loop statements'''
    if len(t) > 2:
        t[2].insert(0, t[1])
        t[0] = t[2]
    elif len(t) > 2:
        t[0] = [t[1]]
    else:
        t[0] = []


def p_if_else(t):
    '''if_statement : IF LPAREN expression RPAREN statements_block ELSE statements_block'''
    t[0] = AST_ifelse(AST_expression(t[3]), t[5], t[7])


def p_while_loop(t):
    '''while_loop : WHILE LPAREN expression RPAREN statements_block'''
    t[0] = AST_while(AST_expression(t[3]), t[5])


def p_statement_assign(t):
    '''statement : NAME ASSIGMENT expression'''
    t[0] = AST_assigment(AST_variable_call(t[1]), AST_expression(t[3]))


def p_statement_declaration(t):
    '''statement : type variables_declaration '''
    t[0] = AST_declaration(t[1], t[2])


def p_variables_declaration(t):
    '''variables_declaration : NAME COMMA variables_declaration
                             | NAME'''
    if len(t) > 2:
        t[3].insert(0, t[1])
        t[0] = t[3]
    else:
        t[0] = [t[1]]


def p_statement_function_call(t):
    'statement : function_call'
    t[0] = AST_expression(t[1])
