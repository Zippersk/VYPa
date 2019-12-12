from src.VYPcode.AST.blocks.base import AST_block


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
        self.stack_offset = self.get_variable_offset(self.name)
        return self.instruction_tape

    def __str__(self):
        return self.stack.get(-self.stack_offset)


