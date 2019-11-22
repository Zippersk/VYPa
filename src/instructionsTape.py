from typing import List
from src.VYPcode.instructions import ALIAS, OperationBase
from src.output import Output


class InstructionTape:
    __instructions: List[OperationBase] = []

    def __init__(self):
        pass

    def __str__(self):
        print(self.__instructions)

    def add(self, instruction):
        self.__instructions.append(instruction)

    def merge(self, another_instructions_tape):
        self.__instructions += another_instructions_tape.__instructions


MAIN_INSTRUCTION_TAPE = InstructionTape()


def add_constant_section():
    # define registers aliases
    MAIN_INSTRUCTION_TAPE.add(ALIAS("FP", "$0"))
    MAIN_INSTRUCTION_TAPE.add(ALIAS("ACC", "$1"))
    MAIN_INSTRUCTION_TAPE.add(ALIAS("DST", "$2"))  # Destination register for results of CREATE instruction

