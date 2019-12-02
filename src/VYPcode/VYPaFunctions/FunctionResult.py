from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
function_call_number = 0  # just for unique variables name


class FunctionResult(VYPaVariable):

    def __init__(self, func):
        global function_call_number
        self.is_function_result = True
        self.func = func
        function_call_number += 1
        super().__init__(func.get_type(), f"*result_of_{func.name}_{function_call_number}")
        super().declare()

    def get_type(self):
        if self.func.get_type():
            return self.func.get_type()
        else:
            Exception("Try to read type of function result which is not set!!!!")
