from src.VYPcode.scopes.ProgramTree import PT


class VYPaVariable:
    def __init__(self, type, name="Anonymous"):
        self.type = type
        self.name = name
        self.value = None
        self.scope = PT.get_current_scope()

    def declare(self):
        PT.get_current_scope().add_variable(self)

    def set_value(self, value):
        self.value = value

    def get_type(self):
        return self.type

    def is_int(self):
        return self.type == "int"

    def is_str(self):
        return self.type == "string"


