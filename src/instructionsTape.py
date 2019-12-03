from typing import List

from src.VYPcode.Stack import Stack
from src.VYPcode.Functions.buildInFunctions import PrintIntVYPa, PrintStringVYPa
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.Instructions import ALIAS, OperationBase, CONSTANT, SET, JUMP


class InstructionTape:

    def __init__(self):
        self.__instructions: List[str] = []

    def __str__(self):
        print(self.__instructions)

    def add(self, instruction):
        self.__instructions.append(str(instruction))

    def insert_in_beginning(self, instruction):
        self.__instructions.insert(0, instruction)

    def merge(self, another_instructions_tape):
        self.__instructions += another_instructions_tape.__instructions
        return self

    def get_instructions(self):
        return self.__instructions

    def add_constant_section(self):
        constants_instructions_tape = InstructionTape()
        constants_instructions_tape.add(ALIAS(VYPaRegister.Accumulator.name, "$1"))
        constants_instructions_tape.add(ALIAS(VYPaRegister.DestinationReg.name, "$2"))
        constants_instructions_tape.add(JUMP("func_main"))
        self.__instructions = constants_instructions_tape.merge(MAIN_INSTRUCTION_TAPE).get_instructions()

    def add_build_in_functions(self):
        PrintIntVYPa().register()
        PrintStringVYPa().register()

    def clear(self):
        self.__instructions.clear()


MAIN_INSTRUCTION_TAPE = InstructionTape()
