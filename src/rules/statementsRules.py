from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaOperations.operations import SET
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable
from src.VYPcode.scopes.scopes import pop_scope, push_scope, get_current_scope, get_variable
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
    get_current_scope().instruction_tape.add(SET(get_variable(t[1]), t[3]))


def p_statement_declaration(t):
    '''statement : type NAME ASSIGMENT'''
    declare_variable(t[1], t[2])
    get_current_scope().instruction_tape.add(SET(get_variable(t[2]), t[4]))


def p_statement_declaration_assign(t):
    '''statement : type NAME ASSIGMENT expression'''
    declare_variable(t[1], t[2])
    get_current_scope().instruction_tape.add(SET(get_variable(t[2]), t[4]))


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        t[1].plus(t[3])

    elif t[2] == '-':
        t[1].subtract(t[3])

    elif t[2] == '*':
        t[1].multiply(t[3])

    elif t[2] == '/':
        t[1].divide(t[3])

    t[0] = VYPaRegister.Accumulator


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    # %prec UMINUS overrides the default rule precedence--setting it to that of UMINUS in the precedence specifier.
    zero = IntVariable()
    zero.set_value(0)
    t[2].subtractzero()
    t[0] = VYPaRegister.Accumulator


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
    t[0] = get_variable(t[1])


