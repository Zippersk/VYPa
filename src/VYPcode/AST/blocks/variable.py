from src.VYPcode.AST.blocks.base import AST_block


class AST_variable(AST_block):
    def __init__(self, type, name):
        super().__init__()
        self.name = name
        self.type = type
