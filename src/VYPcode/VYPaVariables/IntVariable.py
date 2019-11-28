from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaOperations.operations import CREATE, COPY, SETWORD, ADDI
from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable
from src.VYPcode.scopes.scopes import get_current_scope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


class IntVariable(VYPaVariable):
    def __init__(self, name):
        super().__init__("int", name)
        self.declare()

    def declare(self) -> VYPaVariable:
        get_current_scope().add_variable(self)

        return self
