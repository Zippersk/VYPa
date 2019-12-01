from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.scopes.ProgramTree import PT
from src.error import Exit, Error


class VariableAddress(VYPaVariable):
    def __init__(self, variable):
        super().__init__(variable.type, variable.name)
        self.variable = variable
        self.variable_scope = variable.scope
        self.called_scope = PT.get_current_scope()
        self.is_param = False

    def set_as_param(self):
        self.is_param = True

    def __str__(self):
        if self.name == "Anonymous":
            return str(self.value)
        else:
            scope = self.called_scope
            offset_in_declared_scopes = len(self.scope.variables) - self.scope.get_variable_index(self.name)
            if not self.is_param:
                offset_in_declared_scopes -= 1

            offset_between_scopes = 0
            while True:
                if self.variable_scope == scope:
                    break
                elif scope.previous_scope:
                    scope = scope.previous_scope
                else:
                    Exit(Error.SyntaxError, "Could not reach variable from scope")

            return Stack.get(-(offset_in_declared_scopes + offset_between_scopes))