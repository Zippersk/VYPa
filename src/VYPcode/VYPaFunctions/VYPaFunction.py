from src.VYPcode.VYPaOperations.operations import ADDI, LABEL
from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.scopes.scopes import get_current_scope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


class VYPaFunction:
    def __init__(self, type, name, params):
        self.body = None
        self.type = type
        self.params = params
        self.name = name

    def setup_SP(self):
        get_current_scope().instruction_tape.add(ADDI(VYPaRegister.StackPointer, len(self.params), VYPaRegister.StackPointer))

    @staticmethod
    def declare(type, name, params):
        return get_current_scope().add_function(VYPaFunction(type, name, params))
