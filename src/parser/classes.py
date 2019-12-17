"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.assigment import AST_assigment
from src.VYPcode.AST.blocks.class_block import AST_class
from src.VYPcode.AST.blocks.class_instance import AST_class_instance
from src.VYPcode.AST.blocks.class_variable_call import AST_class_variable_call
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.expression import AST_expression
from src.VYPcode.AST.blocks.function import AST_function
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaInt import VYPaInt


def p_class(t):
    '''class : CLASS NAME COLON NAME class_body'''
    t[0] = AST_class(t[2], t[4])
    for statement in t[5]:
        if isinstance(statement, AST_function):
            statement.add_param(AST_variable(VYPaClass(t[2]), "this"))
            statement.set_label(f"class_{t[2]}_func_{statement.name}")
            statement.set_name(f"{t[2]}_{statement.name}")
            AST.root.add_function(statement)
        else:
            t[0].add_declaration(statement)


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


def p_expression_new_class_instance(t):
    '''expression : NEW NAME'''
    t[0] = AST_class_instance(t[2])


def p_expression_class_variable_call(t):
    '''expression : class_variable_call'''
    t[0] = t[1]


def p_class_variable_call(t):
    '''class_variable_call : NAME DOT NAME
                           | THIS DOT NAME
                           | SUPER DOT NAME'''
    t[0] = AST_class_variable_call(t[1], t[3])


def p_statement_class_variable_assign(t):
    '''statement : class_variable_call ASSIGMENT expression'''
    t[0] = AST_assigment(t[1], AST_expression(t[3]))


def p_class_function_call(t):
    '''expression : NAME DOT NAME LPAREN function_params RPAREN'''
    t[0] = AST_function_call(t[5], t[6])


def p_class_this_function_call(t):
    '''expression : THIS DOT NAME LPAREN function_params RPAREN'''
    t[0] = AST_function_call(t[3], t[5])


def p_class_super_function_call(t):
    '''expression : SUPER DOT NAME LPAREN function_params RPAREN'''
    t[0] = AST_function_call(t[3], t[5])
