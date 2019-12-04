from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Variables.VariableBase import VYPaVariableBase


class VYPaIntVariable(VYPaVariableBase):
    def __init__(self, name="*Anonymous"):
        super().__init__(VYPaInt(), name)

    def declare(self):
        from src.VYPcode.Stack import Stack
        Stack.push(str(0))
        super().declare()
        return self


