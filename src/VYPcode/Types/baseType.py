from src.VYPcode.Registers.Registers import RegisterBase


class VYPaBaseType:
    def __init__(self, name, default):
        self.default = default
        self.name = name

    def get_name(self):
        return self.name

    def get_default(self):
        return self.default

    def __eq__(self, other):
        # register is none types so every type is equal to register
        return isinstance(other, RegisterBase) or self.name == other.name
