from src.VYPcode import Stack
from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaFunctions.FunctionResult import FunctionResult
from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaOperations.operations import RETURN, JUMP, COMMENT, DUMPSTACK, DUMPREGS, ADDI
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaTypes.VYPaInt import VYPaInt
from src.VYPcode.VYPaTypes.VYPaString import VYPaString
from src.VYPcode.VYPaTypes.VYPaVoid import VYPaVoid
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.scopes.ProgramTree import PT
from src.VYPcode.utils import declare_variable
from src.error import Exit, Error


def p_function(t):
    '''function : function_head statements_block'''
    if not t[1].name == "main" and PT.is_in_global_scope():
        PT.current_function.deallocate_and_return()
    else:
        PT.get_current_scope().instruction_tape.add(JUMP("END"))
    PT.get_current_scope().instruction_tape.add(COMMENT(f"End of function {t[1].name}"))
    PT.get_current_scope().instruction_tape.add(COMMENT(""))


def p_function_head(t):
    '''function_head : type NAME LPAREN functions_params RPAREN
                | type NAME LPAREN functions_params_empty RPAREN'''
    PT.get_current_scope().instruction_tape.add(COMMENT(""))
    PT.get_current_scope().instruction_tape.add(COMMENT(f"Start of function {t[2]}"))
    t[0] = VYPaFunction(t[1], t[2], t[4]).declare()
    PT.set_current_processing_function(t[0])


def p_functions_params_empty(t):
    '''functions_params_empty : VOID'''
    t[0] = []  # return empty if functions does not have any arguments


def p_functions_params(t):
    '''functions_params : type NAME
                        | type NAME COMMA functions_params'''
    if t[3]:
        t[3].insert(0, declare_variable(t[1], t[2]))
        t[0] = t[3]
    else:
        t[0] = [declare_variable(t[1], t[2])]


def p_function_call(t):
    '''function_call : NAME LPAREN function_params RPAREN'''

    Stack.allocate(2)  # Allocate memory for SP (it will be used for return) and function return value

    # print is a special function which can be called with multiple parameters
    # so internally we call PrintInt or PrintString for each parameter...
    if t[1] == "print":
        for param in t[3]:
            if param.get_type() == VYPaInt():
                PT.get_global_scope().get_function("printInt").call([param])
            elif param.get_type() == VYPaString():
                PT.get_global_scope().get_function("printString").call([param])
            else:
                Exit(Error.InternalError, "Not implemented yet") # TODO print object???
                pass

        t[0] = FunctionResult(PT.get_global_scope().get_function("printInt"))
        return
    else:
        try:
            func = PT.get_global_scope().get_function(t[1])
        except Exception:
            # function was not declared yet
            # TODO: add function to global scope and mark it as NON-defined
            func = VYPaFunction(None, t[1], t[3])

    t[0] = func.call(t[3])


def p_return(t):
    '''statement : RETURN expression
                 | RETURN'''

    if not t[2]:
        if PT.get_current_function().get_type() != VYPaVoid:
            Exit(Error.SyntaxError, "Function has empty return and is not void")

    PT.get_current_function().deallocate_and_return(t[2])


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