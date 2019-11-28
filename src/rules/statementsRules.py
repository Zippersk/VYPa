from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable
from src.VYPcode.VYPaOperations.operations import ADDI, SUBI, MULI, DIVI, SET
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.VYPaVariables.VariableAddress import VariableAddress
from src.VYPcode.scopes.scopes import pop_scope, push_scope, get_current_scope
from src.VYPcode.utils import declare_variable


def p_new_scope(p):
    "new_scope :"
    # Create a new scope for local variables
    push_scope()


def p_statements_block(t):
    "statements_block : LBRACKET new_scope statements RBRACKET"""
    pop_scope()


def p_statements(t):
    '''statements : statement SEMICOLON statements
                  | '''
    pass


def p_statement_assign(t):
    '''statement : NAME ASSIGMENT expression'''
    #  set value from accumulator register to variable
    get_current_scope().instruction_tape.add(SET(VariableAddress(t[1]), t[3]))


def p_statement_declaration_assign(t):
    '''statement : type NAME ASSIGMENT expression'''
    declare_variable(t[1], t[2])
    get_current_scope().instruction_tape.add(SET(VariableAddress(t[2]), t[4]))


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        get_current_scope().instruction_tape.add(ADDI(t[1], t[3]))
    elif t[2] == '-':
        get_current_scope().instruction_tape.add(SUBI(t[1], t[3]))
    elif t[2] == '*':
        get_current_scope().instruction_tape.add(MULI(t[1], t[3]))
    elif t[2] == '/':
        get_current_scope().instruction_tape.add(DIVI(t[1], t[3]))
    t[0] = VYPaRegister.Accumulator


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    # %prec UMINUS overrides the default rule precedence--setting it to that of UMINUS in the precedence specifier.
    get_current_scope().instruction_tape.add(SUBI(0, t[2]))
    t[0] = VYPaRegister.Accumulator


def p_expression_string(t):
    'expression : WORD'
    t[0] = t[1]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_expression_variable(t):
    'expression : NAME'
    t[0] = VariableAddress(t[1])


