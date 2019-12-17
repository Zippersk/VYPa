"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
﻿from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Instructions.Instructions import SET
from src.VYPcode.Registers.Registers import VYPaRegister


class AST_expression(AST_block):
    def __init__(self, expression_root):
        super().__init__()
        self.expression_root = expression_root
        self.type = None
        self.stack_offset = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.expression_root.get_instructions(self))
        self.type = self.expression_root.type
        if self.stack_offset > 0:
            self.stack.deallocate(self.stack_offset)
        return self.instruction_tape

    def add_expression_stack_offset(self):
        self.stack_offset += 1

    def get_variable_offset(self, name):
        return self.stack_offset + self.parent.get_variable_offset(name)

    def __str__(self):
        return str(AST_value(self.type, str(VYPaRegister.Accumulator)))
