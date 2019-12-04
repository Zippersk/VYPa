from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Stack import Stack
from src.VYPcode.Functions.VYPaFunction import VYPaFunction
from src.VYPcode.Instructions.Instructions import LABEL, WRITEI, RETURN, DUMPSTACK, WRITES, READI, READS, GETSIZE, \
    COMMENT
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.VYPcode.Variables import VYPaStringVariable
from src.VYPcode.Variables.VYPaIntVariable import VYPaIntVariable
from src.VYPcode.Variables.VYPaStringVariable import VYPaStringVariable
from src.VYPcode.Scopes.ProgramTree import PT


class VYPaBuildInFunctionClass(VYPaFunction):
    def __init__(self, type, name, params):
        super().__init__(type, name, params)
        self.label = f"buildIn_{name}"
        super().declare()

    def register(self):

        self.get_instructions()
        self.deallocate_and_return()
        PT.pop_scope()
        PT.get_current_scope().instruction_tape.add(COMMENT(""))


class PrintIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printInt", [VYPaIntVariable("number")])

    def get_instructions(self):
        PT.get_current_scope().instruction_tape.add(WRITEI(Stack.top()))
        self.deallocate_and_return()


class PrintStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printString", [VYPaStringVariable("string")])

    def get_instructions(self):
        PT.get_current_scope().instruction_tape.add(WRITES(Stack.top()))
        self.deallocate_and_return()


class ReadIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "readInt", [])

    def get_instructions(self):
        n = VYPaIntVariable("n").declare()
        PT.get_current_scope().instruction_tape.add(READI(VYPaRegister.DestinationReg))
        Stack.set(VYPaRegister.DestinationReg)
        self.deallocate_and_return(n)


class ReadStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "readString", [])

    def get_instructions(self):
        s = VYPaStringVariable("s").declare()
        PT.get_current_scope().instruction_tape.add(READS(VYPaRegister.DestinationReg))
        Stack.set(VYPaRegister.DestinationReg)
        self.deallocate_and_return(s)


class LengthVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "length", [VYPaStringVariable("s")])

    def get_instructions(self):
        PT.get_current_scope().instruction_tape.add(GETSIZE(VYPaRegister.DestinationReg, Stack.top()))
        n = VYPaIntVariable("n").declare()
        Stack.set(VYPaRegister.DestinationReg)
        self.deallocate_and_return(n)


class SubStrVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "subStr", [VYPaStringVariable("s"), VYPaIntVariable("i"), VYPaIntVariable("n")])
        # TODO: implement substr function

