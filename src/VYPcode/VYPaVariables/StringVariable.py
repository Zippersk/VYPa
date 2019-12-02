from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaOperations.operations import CREATE, SET, SETWORD
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaTypes.VYPaString import VYPaString
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable

from src.VYPcode.scopes.ProgramTree import PT


class StringVariable(VYPaVariable):
    def __init__(self, name="*Anonymous"):
        super().__init__(VYPaString, name)

    def declare(self):
        PT.get_current_scope().instruction_tape.add(CREATE(VYPaRegister.DestinationReg, 1))
        PT.get_current_scope().instruction_tape.add(SETWORD(VYPaRegister.DestinationReg, 0, '""'))
        Stack.push(VYPaRegister.DestinationReg)
        super().declare()
        return self