class RegisterBase:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class VYPaRegister:
    Accumulator = RegisterBase("ACC")
    DestinationReg = RegisterBase("DST")   # Destination register for results of CREATE instruction
