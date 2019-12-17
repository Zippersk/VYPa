"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import SET
from src.VYPcode.Registers.Registers import VYPaRegister


class AST_variable_call(AST_block):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.variable = None
        self.type = None
        self.stack_offset = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.variable = self.get_variable(self.name)
        self.type = self.variable.type
        self.instruction_tape.add(SET(AST_value(self.type, str(VYPaRegister.Accumulator)), str(self)))
        return self.instruction_tape

    def __str__(self):
        self.stack_offset = self.get_variable_offset(self.name)
        return self.stack.get(-self.stack_offset)


