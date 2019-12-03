from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.InstructionsBaseClasses import *


class ADDI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("ADDI", destination, second, third)


class SUBI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("SUBI", destination, second, third)


class MULI(ThreeArgsInstruction):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("MULI", first, second, third)


class DIVI(ThreeArgsInstruction):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("MULI", first, second, third)


class CONSTANT(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("CONSTANT", first, second)


class ALIAS(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("ALIAS", first, second)


class WRITES(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("WRITES", first)


class WRITEI(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("WRITEI", first)


class SETWORD(ThreeArgsInstruction):
    def __init__(self, first, second, third):
        super().__init__("SETWORD", first, second, third)


class CREATE(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("CREATE", first, second)


class COPY(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("COPY", first, second)


class DESTROY(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("DESTROY", first)


class SET(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("SET", first, second)


class LABEL(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("LABEL", first)


class JUMP(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("JUMP", first)


class CALL(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("CALL", first, second)


class RETURN(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("RETURN", first)


class DUMPSTACK(NoArgsInstruction):
    def __init__(self):
        super().__init__("DUMPSTACK")


class DUMPREGS(NoArgsInstruction):
    def __init__(self):
        super().__init__("DUMPREGS")


class COMMENT(OperationBase):
    def __init__(self, comment):
        self.comment = comment

    def __str__(self):
        return f'#  {self.comment}'