from src.VYPcode.scopes.scopes import get_current_scope


class VYPaFunction:
    def __init__(self, type, name, params):
        self.body = None
        self.type = type
        self.params = params
        self.name = name

    @staticmethod
    def declare(type, name, params):
        return get_current_scope().add_function(VYPaFunction(type, name, params))
