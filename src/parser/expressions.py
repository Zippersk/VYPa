from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.binaryOperations.ADD import AST_ADD
from src.VYPcode.AST.blocks.binaryOperations.DIV import AST_DIVI
from src.VYPcode.AST.blocks.binaryOperations.MUL import AST_MULI
from src.VYPcode.AST.blocks.binaryOperations.SUB import AST_SUBI
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import ADDI, SUBI, DIVI, MULI
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString


def p_expression_plus(t):
    '''expression : expression PLUS expression'''
    t[0] = AST_ADD(t[1], t[3])


def p_expression_minus(t):
    '''expression : expression MINUS expression'''
    t[0] = AST_SUBI(t[1], t[3])

def p_expression_times(t):
    '''expression : expression TIMES expression'''
    t[0] = AST_MULI(t[1], t[3])


def p_expression_divide(t):
    '''expression : expression DIVIDE expression'''
    t[0] = AST_DIVI(t[1], t[3])


def p_expression_parens(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_string(t):
    'expression : WORD'
    t[0] = AST_value(None, VYPaString(), t[1])


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = AST_value(None, VYPaInt(), t[1])


def p_expression_variable(t):
    'expression : NAME'
    t[0] = AST.current.get_variable(t[1])


def p_expression_function_call(t):
    'expression : function_call'
    t[0] = t[1]
