from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaOperations.operations import ADDI, DIVI, MULI, SUBI, SET
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable

from src.VYPcode.scopes.ProgramTree import PT
from src.error import Exit, Error


class IntVariable(VYPaVariable):
    def __init__(self, name="*Anonymous"):
        super().__init__("int", name)

    def declare(self):
        Stack.push(0)
        super().declare()

    def plus(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            PT.get_current_scope().instruction_tape.add(ADDI(self, another_variable))
        else:
            # TODO: enable int and string concatination
            pass
        return IntVariable("*ACC")

    def subtract(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            PT.get_current_scope().instruction_tape.add(SUBI(self, another_variable))
        else:
            Exit(Error.TypeError, "Can not subtract int with string")
        return IntVariable("*ACC")

    def multiply(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            PT.get_current_scope().instruction_tape.add(MULI(self, another_variable))
        else:
            Exit(Error.TypeError, "Can not multiply int with string")
        return IntVariable("*ACC")

    def divide(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            PT.get_current_scope().instruction_tape.add(DIVI(self, another_variable))
        else:
            Exit(Error.TypeError, "Can not divide int with string")
        return IntVariable("*ACC")


