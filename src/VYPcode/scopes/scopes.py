from src.VYPcode.VYPaOperations.operations import DESTROY
from src.VYPcode.scopes.VYPaScope import VYPaScope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE

__scopes: [VYPaScope] = [VYPaScope()]
__classes = {}
__functions = {}


def push_scope():
    __scopes.append(VYPaScope())


def pop_scope():
    for variable in get_current_scope().variables:
        MAIN_INSTRUCTION_TAPE.add(DESTROY(variable))
    __scopes.pop()


def get_current_scope() -> VYPaScope:
    return __scopes[len(__scopes) - 1]


def get_variable(name: str):
    for scope in __scopes.reverse():
        variable = scope.get_variable(name)
        if variable:
            return variable

    Exception("Variable not defined!")


def get_scope_level():
    return len(__scopes) - 1
