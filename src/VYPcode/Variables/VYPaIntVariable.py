from src.VYPcode.Stack import Stack
from src.VYPcode.Instructions.Instructions import ADDI, DIVI, MULI, SUBI, SET
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Variables.VariableBase import VYPaVariableBase

from src.VYPcode.Scopes.ProgramTree import PT
from src.error import Exit, Error


class VYPaIntVariable(VYPaVariableBase):
    def __init__(self, name="*Anonymous"):
        super().__init__(VYPaInt(), name)

    def declare(self):
        Stack.push(str(0))
        super().declare()
        return self


