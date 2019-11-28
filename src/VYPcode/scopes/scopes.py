from src.VYPcode.scopes.VYPaScope import VYPaScope
from src.instructionsTape import InstructionTape

__scopes: [VYPaScope] = [VYPaScope()]
__classes = {}
__functions = {}


def push_scope():
    __scopes.append(VYPaScope())


def pop_scope():
    get_current_scope().pop()
    __scopes.pop()


def get_current_scope() -> VYPaScope:
    return __scopes[len(__scopes) - 1]


def get_scopes() -> [VYPaScope]:
    return __scopes
