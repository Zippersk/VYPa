from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.binaryOperations.ADD import AST_ADD
from src.VYPcode.AST.blocks.binaryOperations.AND import AST_AND
from src.VYPcode.AST.blocks.binaryOperations.DIV import AST_DIVI
from src.VYPcode.AST.blocks.binaryOperations.EQ import AST_EQ
from src.VYPcode.AST.blocks.binaryOperations.GT import AST_GT
from src.VYPcode.AST.blocks.binaryOperations.LT import AST_LT
from src.VYPcode.AST.blocks.binaryOperations.MUL import AST_MULI
from src.VYPcode.AST.blocks.binaryOperations.NOT import AST_NOT
from src.VYPcode.AST.blocks.binaryOperations.OR import AST_OR
from src.VYPcode.AST.blocks.binaryOperations.SUB import AST_SUBI
from src.VYPcode.AST.blocks.binaryOperations.cast import AST_cast
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
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


def p_expression_and(t):
    '''expression : expression AND expression'''
    t[0] = AST_AND(t[1], t[3])


def p_expression_or(t):
    '''expression : expression OR expression'''
    t[0] = AST_OR(t[1], t[3])


def p_expression_equal(t):
    '''expression : expression EQUAL expression'''
    t[0] = AST_EQ(t[1], t[3])


def p_expression_notequal(t):
    '''expression : expression NOTEQUAL expression'''
    t[0] = AST_NOT(AST_EQ(t[1], t[3]))


def p_expression_greater(t):
    '''expression : expression GREATER expression'''
    t[0] = AST_GT(t[1], t[3])


def p_expression_greater_equal(t):
    '''expression : expression GREATEREQUAL expression'''
    greater = AST_GT(t[1], t[3])
    equal = AST_EQ(t[1], t[3])
    t[0] = AST_OR(greater, equal)


def p_expression_less(t):
    '''expression : expression LESS expression'''
    t[0] = AST_LT(t[1], t[3])


def p_expression_less_equal(t):
    '''expression : expression LESSEQUAL expression'''
    less = AST_LT(t[1], t[3])
    equal = AST_EQ(t[1], t[3])
    t[0] = AST_OR(less, equal)


def p_expression_not(t):
    '''expression : NEGATION expression'''
    t[0] = AST_NOT(t[1])


def p_expression_parens(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_string(t):
    'expression : WORD'
    t[0] = AST_value(VYPaString(), t[1])


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = AST_value(VYPaInt(), t[1])


def p_expression_variable(t):
    'expression : NAME'
    t[0] = AST_variable_call(t[1])


def p_expression_function_call(t):
    'expression : function_call'
    t[0] = t[1]

def p_expression_cast(t):
    '''expression : LPAREN type RPAREN expression'''
    t[0] = AST_cast(t[2], t[4])
