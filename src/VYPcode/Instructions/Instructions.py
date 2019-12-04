from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.InstructionsBaseClasses import *

# TODO: Write type checks!
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class ADDI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("ADDI", destination, second, third)

    def __str__(self):
        if self.second.type != self.third.type:
            Exit(Error.SemanticError, "Type check error!")
        return super().__str__()


class SUBI(ThreeArgsInstruction):
    def __init__(self, second, third, destination=VYPaRegister.Accumulator):
        super().__init__("SUBI", destination, second, third)

    def __str__(self):
        if self.second.type != VYPaInt() or self.third.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")
        return super().__str__()


class MULI(ThreeArgsInstruction):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("MULI", first, second, third)

    def __str__(self):
        if self.second.type != VYPaInt() or self.third.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")
        return super().__str__()


class DIVI(ThreeArgsInstruction):
    def __init__(self, second, third):
        first = VYPaRegister.Accumulator  # result of all arithmetic operations are stored in ACC register
        super().__init__("DIVI", first, second, third)

    def __str__(self):
        if self.second.type != VYPaInt() or self.third.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")
        return super().__str__()


class CONSTANT(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("CONSTANT", first, second)


class ALIAS(TwoArgsInstruction):
    def __init__(self, first, second):
        super().__init__("ALIAS", first, second)


class WRITES(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("WRITES", first)

    def __str__(self):
        if self.first.type != VYPaString():
            Exit(Error.SemanticError, "Type check error!")
        return super().__str__()


class WRITEI(OneArgsInstruction):
    def __init__(self, first):
        super().__init__("WRITEI", first)

    def __str__(self):
        if self.first.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")
        return super().__str__()


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
    def __init__(self, first, second, calling_params):
        super().__init__("CALL", first, second)
        self.calling_params = calling_params

    def check_params(self, calling_params):
        if len(calling_params) != len(self.second.params):
            Exit(Error.SyntaxError, "Wrong number of parameters")
        for calling_param, declared_param in zip(calling_params, self.second.params):
            if calling_param.get_type() != declared_param.get_type():
                Exit(Error.TypesIncompatibility, "Parameters types mismatch")

    def __str__(self):
        if self.second.name == "*print":
            if self.calling_params[0].get_type() == VYPaInt():
                self.second_str = "buildIn_printInt"
            elif self.calling_params[0].get_type() == VYPaString():
                self.second_str = "buildIn_printString"
            else:
                # TODO print object???
                Exit(Error.InternalError, "Not implemented yet")
        else:
            self.check_params(self.calling_params)

        return super().__str__()


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


class EMPTYLINE(OperationBase):
    def __str__(self):
        return ''
