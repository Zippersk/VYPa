from src.VYPcode.scopes.VYPaScope import VYPaScope
from src.error import Error, Exit


class ProgramTree:
    current_scope: VYPaScope or None

    def __init__(self):
        self.current_scope = None

    def push_scope(self):
        new_scope = VYPaScope(self.current_scope)
        if self.current_scope is not None:
            self.current_scope.add_nested_scope(new_scope)

        self.current_scope = new_scope

    def pop_scope(self):
        self.current_scope.pop()
        if self.current_scope.previous_scope:
            self.current_scope.previous_scope.instruction_tape.merge(self.current_scope.instruction_tape)

        self.current_scope = self.current_scope.previous_scope

    def get_current_scope(self) -> VYPaScope:
        return self.current_scope

    def traverse_previous_scopes(self, apply_function):
        scope = self.current_scope
        while scope is not None:
            result = apply_function(scope)
            if result:
                return result
            scope = scope.previous_scope

        return None

    def get_variable(self, name: str):
        """
        :rtype: src.VYPcode.VYPaVariables.VYPaVariable.VYPaVariable
        """
        def variable_filter(scope: VYPaScope):
            return scope.get_variable(name)

        variable = self.traverse_previous_scopes(variable_filter)
        if variable:
            return variable
        else:
            Exit(Error.SyntaxError, "Could not find variable")

    def get_function(self, name: str):
        """
        :rtype: src.VYPcode.VYPaFunctions.VYPaFunction.VYPaFunction
        """
        def function_filter(scope: VYPaScope):
            return scope.get_function(name)

        function = self.traverse_previous_scopes(function_filter)
        if function:
            return function
        else:
            Exit(Error.SyntaxError, "Could not find function")

    def get_global_scope(self) -> VYPaScope:
        def global_scope_filter(scope:VYPaScope):
            if scope.previous_scope is None:
                return scope
        return self.traverse_previous_scopes(global_scope_filter)

    def is_in_global_scope(self):
        return self.current_scope.previous_scope is None

    def __str__(self):
        return str(self.get_global_scope())

    def clear(self):
        self.current_scope = None


PT = ProgramTree()
