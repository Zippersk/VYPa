from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Instructions.Instructions import SET


class AST_assigment(AST_block):
    def __init__(self, name, expression):
        super().__init__()
        self.name = name
        self.expression = expression

    def get_instructions(self, parent):
        self.parent = parent
        self.variable = AST_variable_call(self.name)
        self.variable.get_instructions(self)
        self.instruction_tape.merge(self.expression.get_instructions(self))
        self.instruction_tape.add(SET(self.variable, self.expression))
        return self.instruction_tape
