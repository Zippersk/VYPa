class AbstractSyntaxTree:
    def __init__(self):
        self.clear()

    def clear(self):
        from src.VYPcode.AST.blocks.program import AST_program
        self.root = AST_program()
        self.current = self.root

    def get_root(self):
        return self.root

    def get_current(self):
        return self.current


AST = AbstractSyntaxTree()
