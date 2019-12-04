class RegisterBase:
    def __init__(self, name):
        self.name = name
        self.type = self

    def __str__(self):
        return f"${self.name}"


class VYPaRegister:
    Accumulator = RegisterBase("ACCUMULATOR")
    StackPointer = RegisterBase("SP")
    DestinationReg = RegisterBase("ALLOCATION")   # Destination register for results of CREATE instruction


class VYPaStack(RegisterBase):
    def __init__(self, offset):
        super().__init__("STACK")
        self.offset = offset

    def __str__(self):
        if self.offset > 0:
            return f"[{VYPaRegister.StackPointer}+{self.offset}]"
        elif self.offset < 0:
            return f"[{VYPaRegister.StackPointer}-{abs(self.offset)}]"
        else:
            return f"[{VYPaRegister.StackPointer}]"
