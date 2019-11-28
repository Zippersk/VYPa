from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaOperations.operations import CREATE, SETWORD, COPY, WRITES
from src.instructionsTape import MAIN_INSTRUCTION_TAPE


def is_build_in_function(name, params):
    if name == "print":
        return printVYPa(params)
    return None


class printVYPa(VYPaFunction):
    def __init__(self, params):
        super().__init__("void", "print", params)

    def call(self):
        word = self.params[0].get_value()
        MAIN_INSTRUCTION_TAPE.add(CREATE(VYPaRegister.DestinationReg, len(word)))
        MAIN_INSTRUCTION_TAPE.add(SETWORD(VYPaRegister.DestinationReg, 1, word))
        MAIN_INSTRUCTION_TAPE.add(COPY(VYPaRegister.Accumulator, 1))
        MAIN_INSTRUCTION_TAPE.add(WRITES(VYPaRegister.Accumulator))




# readInt
# readString
# length
# subStr
