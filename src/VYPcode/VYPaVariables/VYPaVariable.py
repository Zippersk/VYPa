from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.scopes.ProgramTree import PT


class VYPaVariable:
    def __init__(self, type, name="*Anonymous"):
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

    def __str__(self):
        if self.name == "*Anonymous":
            return str(self.value)
        elif self.name == "*ACC":
            return str(VYPaRegister.Accumulator)
        else:
            all_variables = len(self.scope.variables)
            position = self.scope.get_variable_index(self.name)

            return Stack.get(-(all_variables - position + self.scope.relative_SP - 1))
