from src.VYPcode.scopes.VYPaScope import VYPaScope

__scopes: [VYPaScope] = []
__classes = {}
__functions = {}


def push_scope():
    __scopes.append(VYPaScope())


def pop_scope():
    get_current_scope().pop()
    get_previous_scope().instruction_tape.merge(get_current_scope().instruction_tape)
    __scopes.pop()


def get_current_scope() -> VYPaScope:
    return __scopes[len(__scopes) - 1]


def get_previous_scope() -> VYPaScope:
    if len(__scopes) > 1:
        return __scopes[len(__scopes) - 2]
    else:
        return __scopes[0]


def get_scopes() -> [VYPaScope]:
    return __scopes


def get_variable(name: str):
    """
    :rtype: src.VYPcode.VYPaVariables.VYPaVariable.VYPaVariable
    """
    scope: VYPaScope
    for scope in reversed(get_scopes()):
        variable = scope.get_variable(name)
        if variable:
            return variable

    Exception("Could not find variable")

