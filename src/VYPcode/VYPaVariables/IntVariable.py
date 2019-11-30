from src.VYPcode.VYPaOperations.operations import ADDI, DIVI, MULI, SUBI, SET
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.scopes.scopes import get_current_scope
from src.error import Exit, Error


class IntVariable(VYPaVariable):
    def __init__(self, name="Anonymous"):
        super().__init__("int", name)

    def declare(self):
        zero = IntVariable()
        zero.set_value(0)
        get_current_scope().instruction_tape.add(SET(self, zero))
        super().declare()

    def plus(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            get_current_scope().instruction_tape.add(ADDI(self, another_variable))
        else:
            # TODO: enable int and string concatination
            pass

    def subtract(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            get_current_scope().instruction_tape.add(SUBI(self, another_variable))
        else:
            Exit(Error.TypeError, "Can not subtract int with string")

    def multiply(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            get_current_scope().instruction_tape.add(MULI(self, another_variable))
        else:
            Exit(Error.TypeError, "Can not multiply int with string")

    def divide(self, another_variable: VYPaVariable):
        if another_variable.is_int():
            get_current_scope().instruction_tape.add(DIVI(self, another_variable))
        else:
            Exit(Error.TypeError, "Can not divide int with string")


