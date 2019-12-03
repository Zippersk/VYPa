class RegisterBase:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"${self.name}"


class VYPaRegister:
    Accumulator = RegisterBase("ACC")
    StackPointer = RegisterBase("SP")
    DestinationReg = RegisterBase("DST")   # Destination register for results of CREATE instruction
