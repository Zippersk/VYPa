"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.base import AST_block

from src.VYPcode.Instructions.Instructions import SET
from src.VYPcode.Registers.Registers import VYPaRegister


class AST_value(AST_block):
    def __init__(self, type, value):
        super().__init__()
        self.value = value
        self.type = type
        self.stack_offset = 0

    def __str__(self):
        s = str(self.value)
        return s.replace("\n", r"\n").replace("\t", r"\t")

    def get_instructions(self, parent):
        self.instruction_tape.add(SET(AST_value(self.type, str(VYPaRegister.Accumulator)), str(self)))
        return self.instruction_tape
