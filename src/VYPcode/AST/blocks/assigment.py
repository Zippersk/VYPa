from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import SET


class AST_assigment(AST_block):
    def __init__(self, previous, variable, expression):
        super().__init__(previous)
        self.expression = expression
        self.variable = variable

    def get_instructions(self):
        self.instruction_tape.add(SET(self.variable, self.expression))
        return self.instruction_tape
