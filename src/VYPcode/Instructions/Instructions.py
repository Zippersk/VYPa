"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.InstructionsBaseClasses import *

# TODO: Write type checks!
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class ADDI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("ADDI", destination, second, third)


class LTI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("LTI", destination, second, third)


class LTS(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("LTS", destination, second, third)


class GTI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("GTI", destination, second, third)


class GTS(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("GTS", destination, second, third)


class EQI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("EQI", destination, second, third)


class EQS(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("EQS", destination, second, third)


class AND(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("AND", destination, second, third)


class OR(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("OR", destination, second, third)


class NOT(TwoArgsInstruction):
    def __init__(self, second, destination=VYPaRegister.Accumulator):
        super().__init__("NOT", destination, second)


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
        super().__init__("DIVI", first, second, third)


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


class READI(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("READI", first)


class READS(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("READS", first)


class GETSIZE(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("GETSIZE", first, second)


class GETWORD(ThreeArgsInstruction):
    def __init__(self, first, second, third):
        super().__init__("GETWORD", first, second, third)


class SETWORD(ThreeArgsInstruction):
    def __init__(self, first, second, third):
        super().__init__("SETWORD", first, second, third)


class RESIZE(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("RESIZE", first, second)


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


class DUMPHEAP(NoArgsInstruction):
    def __init__(self):
        super().__init__("DUMPHEAP")



class COMMENT(OperationBase):
    def __init__(self, comment):
        self.comment = comment

    def __str__(self):
        return f'#  {self.comment}'


class EMPTYLINE(OperationBase):
    def __str__(self):
        return ''


class JUMPZ(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("JUMPZ", first, second)


class JUMP(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("JUMP", first)


class INT2STRING(TwoArgsInstruction):
    def __init__(self, second, destination=VYPaRegister.Accumulator):
        super().__init__("INT2STRING", destination, second)