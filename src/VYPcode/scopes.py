__variables = []
__classes = {}
__functions = {}
__global_scope = {}


def push_scope():
    __variables.append({})


def pop_scope():
    __variables.pop()


def get_current_scope() -> dict:
    return __variables[len(__variables)]


def add_scope_variable(variable):
    """

    :type variable: VYPaVariable
    """
    if not get_current_scope().get(variable.name):
        get_current_scope()[variable.name] = variable
        return variable
    else:
        Exception(f"Variable {variable} already exists")


def add_global_variable(variable):
    """

    :type variable: VYPaVariable
    """
    if not __global_scope.get(variable.name):
        __global_scope[variable.name] = variable
        return variable
    else:
        Exception(f"Variable {variable} already exists")


def get_variable(name: str):
    """

    :rtype: VYPaVariable
    """
    if get_current_scope().get(name):
        return get_current_scope().get(name)
    elif __global_scope.get(name):
        return __global_scope.get(name)
    else:
        Exception(f"Could not find variable with name {name}")


def add_function(function):
    """

    :type function: VYPaFunction
    """
    if not __functions.get(function.name):
        __functions[function.name] = function
        return function
    else:
        Exception(f"Function {function} already exists")