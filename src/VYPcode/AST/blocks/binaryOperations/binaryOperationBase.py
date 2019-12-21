"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.NOT import AST_NOT
from src.VYPcode.AST.blocks.binaryOperations.cast import AST_cast
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import WRITES, WRITEI
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt


class AST_binOperation(AST_block):
    def __init__(self, left, instruction, right):
        super().__init__()
        self.left = left
        self.right = right
        self.instruction = instruction
        self.type = None
        self.stack_offset = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.stack_offset += parent.stack_offset
        self.instruction_tape.merge(self.left.get_instructions(self))
        self.instruction_tape.merge(self.right.get_instructions(self))
        self.type = VYPaInt()
        self.check_types()
        self.add_instruction(self.instruction(self.left, self.right))
        self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
        self.add_expression_stack_offset()
        return self.instruction_tape

    def add_expression_stack_offset(self):
        self.stack_offset += 1
        self.parent.add_expression_stack_offset()

    def __str__(self):
        return self.stack.get(self.stack_offset - self.parent.stack_offset)

    def check_types(self):
        pass
