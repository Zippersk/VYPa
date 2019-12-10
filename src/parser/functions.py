from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.variable import AST_variable


def p_function(t):
    '''function : function_head statements_block'''
    t[1].jump_out()
    t[0] = t[1]

def p_function_head(t):
    '''function_head : type NAME LPAREN functions_params RPAREN
                | type NAME LPAREN functions_params_empty RPAREN'''

    t[0] = AST.current.add_function(t[1], t[2], t[4])
    t[0].jump_in()


def p_functions_params_empty(t):
    '''functions_params_empty : VOID'''
    t[0] = []  # return empty if functions does not have any arguments


def p_functions_params(t):
    '''functions_params : type NAME
                        | type NAME COMMA functions_params'''
    if t[3]:
        t[3].insert(0, AST_variable(None, t[1], t[2]))
        t[0] = t[3]
    else:
        t[0] = [AST_variable(None, t[1], t[2])]


def p_function_call(t):
    '''function_call : NAME LPAREN function_params RPAREN'''
    t[0] = AST_function_call(None, t[1], t[3])


def p_return(t):
    '''statement : RETURN expression
                 | RETURN'''
    t[0] = AST.current.add_return(t[2])


def p_function_call_params(t):
    '''function_params : 
                       | expression
                       | expression COMMA function_params'''
    if len(t) > 2:
        t[3].insert(0, t[1])
        t[0] = t[3]
    elif len(t) > 1:
        t[0] = [t[1]]
    else:
        t[0] = []