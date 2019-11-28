class VYPaScope:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.tempVariablesCount = 0

    def get_variable(self, name: str):
        """

        :rtype: VYPaVariable
        """
        if self.variables.get(name):
            return self.variables.get(name)

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

    def get_temp_variable_name(self):
        self.tempVariablesCount += 1
        return f"$temp_{self.tempVariablesCount}"