from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaOperations.operations import SET, LABEL
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.VYPaFunctions.buildInFunctions import is_build_in_function
from src.VYPcode.scopes.scopes import get_current_scope


def p_function(t):
    '''function : function_head statements_block'''
    #t[0] = t[1].AddBody(t[2])


def p_function_head(t):
    '''function_head : type NAME LPAREN functions_params RPAREN
                | type NAME LPAREN functions_params_empty RPAREN'''
    get_current_scope().instruction_tape.add(LABEL(f"func_{t[2]}"))
    t[0] = VYPaFunction.declare(t[1], t[2], t[4])


def p_functions_params_empty(t):
    '''functions_params_empty : VOID'''
    t[0] = []  # return empty if functions does not have any arguments


def p_functions_params(t):
    '''functions_params : type NAME
                        | type NAME COMMA functions_params'''
    if t[3]:
        t[0] = t[3].append(VYPaVariable.declare_variable(t[1], t[2]))
    else:
        t[0] = [VYPaVariable.declare_variable(t[1], t[2])]


def p_function_call(t):
    '''statement : NAME LPAREN function_params RPAREN'''
    for num, param in enumerate(t[3], 1):
        get_current_scope().instruction_tape.add(SET(f"[{VYPaRegister.StackPointer}+{num}]", param))

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



