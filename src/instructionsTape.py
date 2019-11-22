from typing import List
from src.VYPcode.instructions import ALIAS, OperationBase
from src.output import Output


class InstructionTape:

    def __init__(self):
        self.__instructions: List[OperationBase] = []

    def __str__(self):
        print(self.__instructions)

    def add(self, instruction):
        self.__instructions.append(instruction)

    def merge(self, another_instructions_tape):
        self.__instructions += another_instructions_tape.__instructions
        return self

    def get_instructions(self):
        return self.__instructions

    def add_constant_section(self):
        constants_instructions_tape = InstructionTape()
        constants_instructions_tape.add(ALIAS("FP", "$0"))
        constants_instructions_tape.add(ALIAS("ACC", "$1"))
        constants_instructions_tape.add(ALIAS("DST", "$2"))  # Destination register for results of CREATE instruction
        self.__instructions = constants_instructions_tape.merge(MAIN_INSTRUCTION_TAPE).get_instructions()


MAIN_INSTRUCTION_TAPE = InstructionTape()



