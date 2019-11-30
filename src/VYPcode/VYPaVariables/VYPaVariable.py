from src.VYPcode.VYPaVariables.VariableAddress import VariableAddress
from src.VYPcode.scopes.scopes import get_current_scope


class VYPaVariable:
    def __init__(self, type, name="Anonymous"):
        self.stack_offset = None
        self.type = type
        self.name = name
        self.value = None

    def declare(self):
        get_current_scope().add_variable(self)

    def compute_stack_offset(self):
        self.stack_offset = len(get_current_scope().variables) - get_current_scope().get_variable_index(self.name)
        return self.stack_offset

    def set_value(self, value):
        self.value = value

    def get_type(self):
        return self.type

    def is_int(self):
        return self.type == "int"

    def is_str(self):
        return self.type == "string"

    def __str__(self):
        if self.name != "Anonymous":
            return str(VariableAddress(self.name))
        else:
            return str(self.value)

