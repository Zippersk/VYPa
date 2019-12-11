from src.VYPcode.AST.blocks.base import AST_block


class AST_variable(AST_block):
    def __init__(self, type, name):
        super().__init__()
        self.name = name
        self.type = type

    def get_stack_offset(self):
        return self.get_parent().get_variable_index(self.name)

    def __str__(self):
        return self.stack.get(-self.get_stack_offset())
