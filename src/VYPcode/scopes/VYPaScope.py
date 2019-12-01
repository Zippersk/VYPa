from collections import OrderedDict


class VYPaScope:
    def __init__(self, previous_scope):
        self.previous_scope = previous_scope
        self.nested_scopes = []
        self.variables = OrderedDict()
        self.functions = OrderedDict()
        self.stack_offset = 0

        from src.instructionsTape import InstructionTape  # TODO: Fix circular dependencies
        self.instruction_tape = InstructionTape()

    def get_variable(self, name: str):
        """
        :rtype: VYPaVariable
        """
        return self.variables.get(name)

    def get_function(self, name: str):
        """
        :rtype: VYPaFunction
        """
        return self.functions.get(name)

    def add_function(self, function):
        """

        :type function: VYPaFunction
        """
        if not self.functions.get(function.name):
            self.functions[function.name] = function
            return function
        else:
            Exception(f"Function {function} already exists")

    def add_variable(self, variable):
        """

        :type variable: VYPaVariable
        """
        if not self.variables.get(variable.name):
            self.variables[variable.name] = variable
            return variable
        else:
            Exception(f"Variable {variable} already exists")

    def add_nested_scope(self, scope):
        self.nested_scopes.append(scope)
        return scope

    def get_variable_index(self, name):
        # get index of variable in the list
        return list(self.variables).index(name)

    def pop(self):
        for function in self.functions.values():
            function.throw_if_not_declared()

        from src.VYPcode.Stack import Stack  # TODO: fix circular dependencies
        Stack.deallocate(len(self.variables))

    def __str__(self):
        result = ""
        for variable in self.variables:
            result += f"{variable.type} {variable.name}\n"

        for function in self.functions:
            result += f"{function.type} {function.name} ( "
            for i, variable in enumerate(function.params, 1):
                result += f"{variable.type} {variable.name}"
                if i != len(function.params):
                    result += ", "
            result += ")\n"

        for nested_scope in self.nested_scopes:
            result += '\t\t'.join(str(nested_scope).splitlines(True))
