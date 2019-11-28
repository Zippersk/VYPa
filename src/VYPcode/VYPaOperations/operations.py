from src.VYPcode.VYPaRegisters.Registers import VYPaRegister
from src.VYPcode.VYPaOperations.operationsBaseClasses import *


class ADDI(ThreeArgsOperation):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("ADDI", first, second, third)


class SUBI(ThreeArgsOperation):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("SUBI", first, second, third)


class MULI(ThreeArgsOperation):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("MULI", first, second, third)


class DIVI(ThreeArgsOperation):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("MULI", first, second, third)


class CONSTANT(TwoArgsOperation):
    def __init__(self, first, second):
        super().__init__("CONSTANT", first, second)


class ALIAS(TwoArgsOperation):
    def __init__(self, first, second):
        super().__init__("ALIAS", first, second)


class WRITES(OneArgsOperation):
    def __init__(self, first):
        super().__init__("WRITES", first)


class SETWORD(ThreeArgsOperation):
    def __init__(self, first, second, third):
        super().__init__("SETWORD", first, second, third)


class CREATE(TwoArgsOperation):
    def __init__(self, second):
        first = VYPaRegister.DestinationReg  # we are always using this register for allocations
        super().__init__("CREATE", first, second)


class COPY(TwoArgsOperation):
    def __init__(self, first, second):
        super().__init__("COPY", first, second)


class DESTROY(OneArgsOperation):
    def __init__(self, first):
        super().__init__("DESTROY", first)
