from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.VYPaFunctions.buildInFunctions import is_build_in_function


def p_function(t):
    '''function : function_head statements_block'''
    #t[0] = t[1].AddBody(t[2])


def p_function_head(t):
    '''function_head : type NAME LPAREN functions_params RPAREN
                | type NAME LPAREN functions_params_empty RPAREN'''
    t[0] = VYPaFunction.declare(t[1], t[2], t[4])


def p_functions_params_empty(t):
    '''functions_params_empty : VOID'''
    t[0] = []  # return empty if functions does not have any arguments


def p_functions_params(t):
    '''functions_params : type NAME
                        | type NAME COMMA functions_params'''
    if t[3]:
        t[0] = t[3].append(VYPaVariable.declare([1], t[2]))
    else:
        t[0] = [VYPaVariable.declare([1], t[2])]


def p_function_call(t):
    '''statement : NAME LPAREN function_params RPAREN'''
    build_in_function = is_build_in_function(t[1], t[3])
    if build_in_function:
        build_in_function.call()
    else:
        # TODO: handle logic for user defined functions
        pass


def p_function_call_params(t):
    '''function_params : expression
                       | expression COMMA function_params'''
    if len(t) > 2:
        t[0] = t[3].append(t[1])
    else:
        t[0] = [t[1]]



