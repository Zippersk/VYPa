from src.VYPcode.AST.blocks.base import AST_block


class AST_variable_call(AST_block):
    def __init__(self, previous, variable):
        super().__init__(previous)
        self.variable = variable
        self.previous = previous
        self.type = None

    def get_instructions(self):
        self.type = self.variable.type
        return self.instruction_tape

    def __str__(self):
        return str(self.variable)


