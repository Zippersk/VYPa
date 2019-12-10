from src.VYPcode.AST.blocks.base import AST_block


class AST_value(AST_block):
    def __init__(self, previous, type, value):
        super().__init__(previous)
        self.value = value
        self.type = type

    def __str__(self):
        return str(self.value)
