from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable
from src.VYPcode.VYPaOperations.operations import ADDI, SUBI, MULI, DIVI
from src.VYPcode.scopes.scopes import pop_scope, push_scope, get_variable, get_current_scope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


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
    variable = get_variable(t[1])
    variable.assign(t[3])  # assign value from accumulator


def p_statement_declaration_assign(t):
    '''statement : type NAME ASSIGMENT expression'''
    if t[1] == "int":
        t[0] = IntVariable(t[2])
    elif t[1] == "string":
        t[0] = StringVariable(t[2])
    elif t[1] == "void":
        Exception("variable can not have type void")

    t[0].assign(t[4])


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        MAIN_INSTRUCTION_TAPE.add(ADDI(t[1], t[3]))
    elif t[2] == '-':
        MAIN_INSTRUCTION_TAPE.add(SUBI(t[1], t[3]))
    elif t[2] == '*':
        MAIN_INSTRUCTION_TAPE.add(MULI(t[1], t[3]))
    elif t[2] == '/':
        MAIN_INSTRUCTION_TAPE.add(DIVI(t[1], t[3]))

    t[0] = VYPaRegister.Accumulator


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    # %prec UMINUS overrides the default rule precedence--setting it to that of UMINUS in the precedence specifier.
    MAIN_INSTRUCTION_TAPE.add(SUBI(VYPaRegister.Accumulator, 0, t[2]))
    t[0] = VYPaRegister.Accumulator


def p_expression_string(t):
    'expression : WORD'
    t[0] = StringVariable(get_current_scope().get_temp_variable_name())
    t[0].assign(t[1])


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = IntVariable(get_current_scope().get_temp_variable_name())
    t[0].assign(t[1])


def p_expression_variable(t):
    'expression : NAME'
    try:
        t[0] = get_variable(t[1]).imm
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


