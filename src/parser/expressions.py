from src.TypeChecker.LazyTypeChecker import LazyTypeChecker
from src.VYPcode.Instructions.Instructions import ADDI, SUBI, DIVI, MULI
from src.VYPcode.Scopes.ProgramTree import PT
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Variables.VYPaIntVariable import VYPaIntVariable
from src.VYPcode.Variables.VYPaStringVariable import VYPaStringVariable


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        PT.get_current_scope().instruction_tape.add(ADDI(t[1], t[3]))

    elif t[2] == '-':
        PT.get_current_scope().instruction_tape.add(SUBI(t[1], t[3]))

    elif t[2] == '*':
        PT.get_current_scope().instruction_tape.add(MULI(t[1], t[3]))

    elif t[2] == '/':
        PT.get_current_scope().instruction_tape.add(DIVI(t[1], t[3]))

    LazyTypeChecker.plus(t[1], t[3])
    t[0] = VYPaIntVariable("*ACC")


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    # %prec UMINUS overrides the default rule precedence--setting it to that of UMINUS in the precedence specifier.
    PT.get_current_scope().instruction_tape.add(SUBI(t[1], str(0)))
    LazyTypeChecker(t[1], VYPaInt())
    t[0] = VYPaIntVariable("*ACC")


def p_expression_parens(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_string(t):
    'expression : WORD'
    t[0] = VYPaStringVariable()
    t[0].set_value(t[1])


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = VYPaIntVariable()
    t[0].set_value(t[1])


def p_expression_variable(t):
    'expression : NAME'
    t[0] = PT.get_variable(t[1])


def p_expression_function_call(t):
    'expression : function_call'
    t[0] = t[1]
