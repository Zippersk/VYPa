from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import SET


class AST_assigment(AST_block):
    def __init__(self, name, expression):
        super().__init__()
        self.expression = expression

    def get_instructions(self):
        self.variable = self.get_variable(self.name)
        self.instruction_tape.merge(self.expression.get_instructions())
        self.instruction_tape.add(SET(self.variable, self.expression))
        return self.instruction_tape
