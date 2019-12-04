from src.VYPcode.Instructions.Instructions import SET
from src.VYPcode.Scopes.ProgramTree import PT
from src.VYPcode.utils import declare_variable


def p_statements_block(t):
    "statements_block : LBRACKET statements RBRACKET"""
    PT.pop_scope()


def p_statements(t):
    '''statements : statement SEMICOLON statements
                  | '''
    pass


def p_statement_assign(t):
    '''statement : NAME ASSIGMENT expression'''
    variable = PT.get_variable(t[1])
    PT.get_current_scope().instruction_tape.add(SET(variable, t[3]))


def p_statement_declaration(t):
    '''statement : type variables_declaration '''
    for variable_name in t[2]:
        declare_variable(t[1], variable_name)


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
    # function was called as a statement so we can throw away it's result
    pass
