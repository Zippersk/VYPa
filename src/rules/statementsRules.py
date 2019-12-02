from src.LazyCodeEvaluation.LazyTypeChecker import LazyTypeChecker
from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaOperations.operations import SET, ADDI, SUBI, MULI, DIVI
from src.VYPcode.VYPaTypes.VYPaInt import VYPaInt
from src.VYPcode.VYPaTypes.VYPaString import VYPaString
from src.VYPcode.VYPaTypes.VYPaVoid import VYPaVoid
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable
from src.VYPcode.scopes.ProgramTree import PT
from src.VYPcode.utils import declare_variable


def p_new_scope(p):
    "new_scope :"
    # Create a new scope for local variables
    PT.push_scope()


def p_statements_block(t):
    "statements_block : LBRACKET new_scope statements RBRACKET"""
    PT.pop_scope()


def p_statements(t):
    '''statements : statement SEMICOLON statements
                  | '''
    pass


def p_statement_assign(t):
    '''statement : NAME ASSIGMENT expression'''
    variable = PT.get_variable(t[1])
    PT.get_current_scope().instruction_tape.add(SET(variable, t[3]))
    LazyTypeChecker(variable, t[3].get_type())


def p_statement_declaration(t):
    '''statement : type NAME'''
    declare_variable(t[1], t[2])


def p_statement_declaration_assign(t):
    '''statement : type NAME ASSIGMENT expression'''
    variable = declare_variable(t[1], t[2])
    PT.get_current_scope().instruction_tape.add(SET(variable, t[4]))
    LazyTypeChecker(variable, t[4].get_type())


def p_statement_function_call(t):
    'statement : function_call'
    PT.get_current_scope().add_relative_SP(-1)
    # function was called as a statement so we can throw away it's result



def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        PT.get_current_scope().instruction_tape.add(ADDI(t[1], t[3]))
        LazyTypeChecker.plus(t[1], t[3])

    elif t[2] == '-':
        PT.get_current_scope().instruction_tape.add(SUBI(t[1], t[3]))
        LazyTypeChecker.subtract(t[1], t[3])

    elif t[2] == '*':
        PT.get_current_scope().instruction_tape.add(MULI(t[1], t[3]))
        LazyTypeChecker.multiply(t[1], t[3])

    elif t[2] == '/':
        PT.get_current_scope().instruction_tape.add(DIVI(t[1], t[3]))
        LazyTypeChecker.divide(t[1], t[3])

    t[0] = IntVariable("*ACC")


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    # %prec UMINUS overrides the default rule precedence--setting it to that of UMINUS in the precedence specifier.
    PT.get_current_scope().instruction_tape.add(SUBI(t[1], str(0)))
    LazyTypeChecker(t[1], VYPaInt())
    t[0] = IntVariable("*ACC")


def p_expression_string(t):
    'expression : WORD'
    t[0] = StringVariable()
    t[0].set_value(t[1])


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = IntVariable()
    t[0].set_value(t[1])


def p_expression_variable(t):
    'expression : NAME'
    t[0] = PT.get_variable(t[1])


def p_expression_function_call(t):
    'expression : function_call'
    t[0] = t[1]
    PT.get_current_scope().add_relative_SP(-1)
