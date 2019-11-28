from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaOperations.operations import COPY, SETWORD
from src.VYPcode.scopes.scopes import get_scope_level
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


class VYPaVariable:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.imm = f"${get_scope_level()}_{name}"  # Immediate Addressing (imm)

    def call(self):
        MAIN_INSTRUCTION_TAPE.add(COPY(VYPaRegister.Accumulator, self.imm))  # add variable to accumulator
        return self

    def assign(self, source):
        MAIN_INSTRUCTION_TAPE.add(SETWORD(self.imm, 0, source))  # set value from source (default is accumulator) to variable
        return self

    def __str__(self):
        return self.imm
