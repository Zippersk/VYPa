from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaOperations.operations import CREATE, SETWORD, COPY, WRITES, SET, WRITEI
from src.VYPcode.VYPaVariables.VariableAddress import VariableAddress
from src.VYPcode.scopes.scopes import get_current_scope
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


def is_build_in_function(name, params):
    if name == "print":
        return printVYPa(params)
    return None


class printVYPa(VYPaFunction):
    def __init__(self, params):
        super().__init__("void", "print", params)

    def call(self):
        super().setup_SP()
        get_current_scope().instruction_tape.add(WRITEI(f"[{VYPaRegister.StackPointer}]"))




# readInt
# readString
# length
# subStr
