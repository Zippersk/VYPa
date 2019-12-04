from src.VYPcode import Stack
from src.VYPcode.Stack import Stack
from src.VYPcode.Functions.FunctionResult import FunctionResult
from src.VYPcode.Functions.VYPaFunction import VYPaFunction
from src.VYPcode.Instructions.Instructions import RETURN, JUMP, COMMENT, DUMPSTACK, DUMPREGS, ADDI
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.VYPcode.Variables.VariableBase import VYPaVariableBase
from src.VYPcode.Scopes.ProgramTree import PT
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

    func = PT.get_global_scope().get_function(t[2])
    if func:
        # function was called in the past,  before it was defined
        func.type = t[1]
        func.params = t[4]
        t[0] = func
    else:
        # new function
        t[0] = VYPaFunction(t[1], t[2], t[4])

    t[0].declare()
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
        if len(t[3]) == 0:
            Exit(Error.SemanticError, "Print called with zero params")

        for param in t[3]:
            t[0] = VYPaFunction(VYPaVoid(), "*print", [VYPaInt()]).call([param])

    else:
        func = PT.get_global_scope().get_function(t[1])
        if not func:
            # function was not declared yet
            func = VYPaFunction(None, t[1], t[3])
            PT.get_global_scope().add_function(func)

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