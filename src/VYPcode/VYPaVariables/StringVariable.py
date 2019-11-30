from src.VYPcode.VYPaVariables.VYPaVariable import VYPaVariable


class StringVariable(VYPaVariable):
    def __init__(self, name="Anonymous"):
        super().__init__("string", name)

