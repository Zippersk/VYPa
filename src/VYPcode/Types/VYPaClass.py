from src.VYPcode.Types.baseType import VYPaBaseType


class VYPaClass(VYPaBaseType):
    def __init__(self, name):
        # TODO set default type for classes zero chunk id
        super().__init__(name, 0)
