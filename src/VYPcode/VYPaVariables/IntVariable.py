from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaOperations.operations import CREATE, COPY, SETWORD
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.scopes.scopes import get_current_scope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


class IntVariable(VYPaVariable):
    def __init__(self, name):
        super().__init__("int", name)
        self.declare()

    def declare(self) -> VYPaVariable:
        get_current_scope().add_variable(self)
        MAIN_INSTRUCTION_TAPE.add(CREATE("INT_SIZE"))  # this constant is defined in the beginning of instruction tape
        MAIN_INSTRUCTION_TAPE.add(COPY(VYPaRegister.DestinationReg, self.imm))  # we use prefix which is scope level
        MAIN_INSTRUCTION_TAPE.add(SETWORD(self.imm, 0, 0))  # set default value
        return self
