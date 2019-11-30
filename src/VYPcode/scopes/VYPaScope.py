from collections import OrderedDict

from src.VYPcode.VYPaOperations.operations import ADDI
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.instructionsTape import InstructionTape


class VYPaScope:
    def __init__(self):
        self.variables = OrderedDict()
        self.functions = OrderedDict()
        self.stack_offset = 0
        self.instruction_tape = InstructionTape()

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

    def get_variable_index(self, name):
        # get index of variable
        return list(self.variables).index(name)

    def pop(self):
        for variable in self.variables.values():
            variable.compute_stack_offset()
        self.stack_offset = len(self.variables)
        self.instruction_tape.insert_in_beginning(ADDI(VYPaRegister.StackPointer, self.stack_offset, VYPaRegister.StackPointer))
