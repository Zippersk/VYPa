class RegisterBase:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"${self.name}"


class VYPaRegister:
    Accumulator = RegisterBase("ACCUMULATOR")
    StackPointer = RegisterBase("SP")
    DestinationReg = RegisterBase("ALLOCATION")   # Destination register for results of CREATE instruction
