import re

from src.error import Exit, Error

tokens = (
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGMENT',
    'LPAREN', 'RPAREN', 'CLASS', 'ELSE', 'IF', 'INT', 'NEW', 'RETURN', 'STRING', 'SUPER', 'THIS', 'VOID', 'WHILE',
    'LBRACKET', 'RBRACKET', 'NEGATION', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL', 'EQUAL', 'NOTEQUAL',
    'AND', 'OR', 'LINECOMMENT', 'BLOCKCOMMENT', 'WORD', 'COMMA', 'SEMICOLON'
)

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGMENT = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'(?!(new|false|true|if|else|return|class|void|int|string|super|this|while)\b)[a-zA-Z_][a-zA-Z0-9_]*'
t_CLASS = r'class'
t_ELSE = r'else'
t_IF = r'if'
t_INT = r'int'
t_NEW = r'new'
t_RETURN = r'return'
t_STRING = r'string'
t_SUPER = r'super'
t_THIS = r'this'
t_VOID = r'void'
t_WHILE = r'while'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_NEGATION = r'\!'
t_LESS = r'<'
t_LESSEQUAL = r'=<'
t_GREATER = r'>'
t_GREATEREQUAL = r'=>'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_COMMA = r','
t_SEMICOLON = r';'
t_NUMBER = r'[0-9]+'

# Ignored characters
t_ignore = " \t"


def t_WORD(t):
    r'\"([^\\\n]|(\\.))*?\"'  # should be all printable characters

    hexChars = [x for x in re.findall(r'\\x[A-F,a-f,0-9]{6}', t.value)]

    for hexChar in hexChars:
        unicode_char = chr(int(hexChar[2:], 16))
        t.value = t.value.replace(hexChar, unicode_char)

    return t


def t_LINECOMMENT(t):
    r'\/\/.*'
    pass


def t_BLOCKCOMMENT(t):
    r'\/\*(\*(?!\/)|[^*])*\*\/'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    Exit(Error.LexicalError, f"Illegal character '{t.value[0]}' on line {t.lexer.lineno}")
