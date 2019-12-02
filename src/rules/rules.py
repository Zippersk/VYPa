from src.LazyCodeEvaluation.LazyCodeEvaluater import LazyCode
from src.VYPcode.VYPaOperations.operations import LABEL, COMMENT
from src.error import Error
from src.instructionsTape import MAIN_INSTRUCTION_TAPE
from src.rules.functionsRules import *
from src.rules.classRules import *
from src.rules.statementsRules import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_program(t):
    '''program : init program_body'''
    main: VYPaFunction = PT.get_global_scope().get_function("main")
    if not (main and main.get_type() == VYPaVoid()):
        Error(Error.SemanticError, "wrong type or not defined Main function")

    MAIN_INSTRUCTION_TAPE.add_constant_section()
    MAIN_INSTRUCTION_TAPE.merge(PT.get_global_scope().instruction_tape)
    MAIN_INSTRUCTION_TAPE.add(LABEL("END"))
    LazyCode.run()  # run all lazy evaluate code


def p_init(t):
    '''init : '''
    PT.push_scope()
    PT.get_current_scope().instruction_tape.add(COMMENT(""))
    PT.get_current_scope().instruction_tape.add(COMMENT("BUILD IN FUNCTIONS SECTION START"))
    MAIN_INSTRUCTION_TAPE.add_build_in_functions()
    PT.get_current_scope().instruction_tape.add(COMMENT("BUILD IN FUNCTIONS SECTION END"))
    PT.get_current_scope().instruction_tape.add(COMMENT(""))


def p_program_body(t):
    '''program_body : statement program_body
           | function program_body
           | class program_body
           |'''
    pass


def p_type(t):
    '''type : STRING
             | INT
             | VOID'''
    if t[1] == "int":
        t[0] = VYPaInt()
    elif t[1] == "string":
        t[0] = VYPaString()
    elif t[1] == "void":
        t[0] = VYPaVoid()


def p_error(t):
    print("Syntax error at '%s'" % t.value)
