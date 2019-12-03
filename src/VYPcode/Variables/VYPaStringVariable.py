from src.VYPcode.Stack import Stack
from src.VYPcode.Instructions.Instructions import CREATE, SET, SETWORD
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Variables.VariableBase import VYPaVariableBase

from src.VYPcode.Scopes.ProgramTree import PT


class StringVariable(VYPaVariableBase):
    def __init__(self, name="*Anonymous"):
        super().__init__(VYPaString(), name)

    def declare(self):
        PT.get_current_scope().instruction_tape.add(CREATE(VYPaRegister.DestinationReg, 1))
        PT.get_current_scope().instruction_tape.add(SETWORD(VYPaRegister.DestinationReg, 0, '""'))
        Stack.push(VYPaRegister.DestinationReg)
        super().declare()
        return self