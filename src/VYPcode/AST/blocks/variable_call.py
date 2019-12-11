from src.VYPcode.AST.blocks.base import AST_block


class AST_variable_call(AST_block):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = None

    def get_instructions(self):
        self.variable = self.get_variable(self.name)
        self.type = self.variable.type
        return self.instruction_tape

    def __str__(self):
        return str(self.variable)


