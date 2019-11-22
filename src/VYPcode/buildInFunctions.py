from src.VYPcode.VYPaFunction import VYPaFunction
from src.VYPcode.instructions import CREATE, SETWORD, COPY, WRITES
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
        MAIN_INSTRUCTION_TAPE.add(CREATE("$DST", len(word)))
        MAIN_INSTRUCTION_TAPE.add(SETWORD("$DST", 1, word))
        MAIN_INSTRUCTION_TAPE.add(COPY("$ACC", 1))
        MAIN_INSTRUCTION_TAPE.add(WRITES("$ACC"))




# readInt
# readString
# length
# subStr
