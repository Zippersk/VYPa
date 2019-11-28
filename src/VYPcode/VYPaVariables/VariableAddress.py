from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.scopes.VYPaScope import VYPaScope
from src.VYPcode.scopes.scopes import get_scopes


class VariableAddress:
    def __init__(self, name):
        self.variable, self.scopes_between = self.get_variable_and_scopes(name)

    def get_variable_and_scopes(self, name: str):
        """

        @param name: name of the variable
        @return: get variable, and scopes that are between current scope and scope where is variable declared
        """
        scopes: [VYPaScope] = []
        for scope in reversed(get_scopes()):
            variable = scope.get_variable(name)
            scopes.append(scopes)
            if variable:
                # remove local scope because we dont need to sub offset of local scope
                return variable, scopes[:-1],

        Exception("Variable not defined!")

    def __str__(self):
        offset = self.variable.stack_offset - 1
        for scope in self.scopes_between:
            offset += scope.offset

        return f"[{VYPaRegister.StackPointer}-{offset}]"
