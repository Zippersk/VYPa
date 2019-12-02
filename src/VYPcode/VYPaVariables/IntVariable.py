from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaOperations.operations import ADDI, DIVI, MULI, SUBI, SET
from src.VYPcode.VYPaTypes.VYPaInt import VYPaInt
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable

from src.VYPcode.scopes.ProgramTree import PT
from src.error import Exit, Error


class IntVariable(VYPaVariable):
    def __init__(self, name="*Anonymous"):
        super().__init__(VYPaInt(), name)

    def declare(self):
        Stack.push(str(0))
        super().declare()
        return self


