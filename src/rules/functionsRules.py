from src.VYPcode import Stack
from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaOperations.operations import RETURN, JUMP
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.VYPaVariables.VariableAddress import VariableAddress
from src.VYPcode.scopes.ProgramTree import PT
from src.VYPcode.utils import declare_variable


def p_function(t):
    '''function : function_head statements_block'''
    if not t[1].name == "main" and PT.is_in_global_scope():
        PT.get_current_scope().instruction_tape.add(RETURN(Stack.top()))
    else:
        PT.get_current_scope().instruction_tape.add(JUMP("END"))


def p_function_head(t):
    '''function_head : type NAME LPAREN functions_params RPAREN
                | type NAME LPAREN functions_params_empty RPAREN'''
    t[0] = VYPaFunction(t[1], t[2], t[4]).declare()


def p_functions_params_empty(t):
    '''functions_params_empty : VOID'''
    t[0] = []  # return empty if functions does not have any arguments


def p_functions_params(t):
    '''functions_params : type NAME
                        | type NAME COMMA functions_params'''
    if t[3]:
        t[0] = t[3].append(declare_variable(t[1], t[2]))
    else:
        t[0] = [declare_variable(t[1], t[2])]


def p_function_call(t):
    '''statement : NAME LPAREN function_params RPAREN'''
    Stack.allocate(1)  # Allocate memory for SP (it will be used for return)

    if t[1] == "print":
        param: VariableAddress
        for param in t[3]:
            Stack.push(param.set_as_param())
            # TODO: add some prefix to these functions so user can not redefine it
            if param.is_int():
                PT.get_global_scope().get_function("printInt").call([param])
            elif param.is_str():
                PT.get_global_scope().get_function("printString").call([param])
            else:
                # TODO print object???
                pass
    else:
        for param in t[3]:
            Stack.push(param.set_as_param())

        try:
            PT.get_global_function(t[1]).call(t[3])
        except Exception:
            # function was not declared yet
            VYPaFunction(None, t[1], t[3]).call(t[3])


def p_function_call_params(t):
    '''function_params : expression
                       | expression COMMA function_params'''
    if len(t) > 2:
        t[0] = t[3].append(t[1])
    else:
        t[0] = [t[1]]
