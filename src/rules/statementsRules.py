from src.VYPcode.VYPaVariable import VYPaVariable
from src.VYPcode.instructions import ADDI, SETWORD, CREATE
from src.VYPcode.scopes import pop_scope, push_scope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


def p_new_scope(p):
    "new_scope :"
    # Create a new scope for local variables
    push_scope()


def p_statements_block(t):
    "statements_block : LBRACKET new_scope statements RBRACKET"""
    t[0] = t[3]  # returns instructions tape for statements block
    pop_scope()


def p_statements(t):
    '''statements : statement SEMICOLON statements
                  | '''
    pass
    # if len(t) > 3:
    #     t[0] = t[3].merge(t[1])
    # if len(t) > 2:
    #     t[0] = t[1]
    # else:
    #     t[0] = None  # Blank instructions tape



def p_statement_assign(t):
    '''statement : NAME ASSIGMENT expression'''


def p_statement_declaration_assign(t):
    '''statement : type NAME ASSIGMENT expression'''


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        print(ADDI(t[0], t[1], t[3]))

        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]


def p_expression_string(t):
    'expression : WORD'
    MAIN_INSTRUCTION_TAPE.add(CREATE("$DST", len(t[1])))
    MAIN_INSTRUCTION_TAPE.add(SETWORD("$DST", 0, t[1]))
    t[0] = VYPaVariable("string", None)


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = VYPaVariable.declare_anonym_variable("int")
    t[0].PushValue()



def p_expression_variable(t):
    'expression : NAME'
    try:
        pass  # TODO make variable lookup
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


