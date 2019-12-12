from src.VYPcode.AST.blocks.base import AST_block


class AST_value(AST_block):
    def __init__(self, type, value):
        super().__init__()
        self.value = value
        self.type = type

    def __str__(self):
        s = str(self.value)
        return s.replace("\n", r"\n").replace("\t", r"\t")
