from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.Instructions import LABEL, WRITEI, RETURN, DUMPSTACK, WRITES, READI, READS, GETSIZE, \
    COMMENT
from src.VYPcode.Stack import Stack
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.instructionsTape import InstructionTape


class VYPaBuildInFunctionClass():
    def __init__(self, type, name, params):
        self.instructions = InstructionTape()
        self.stack = Stack(self.instructions)
        self.return_expression = None
        self.function = AST.get_root().add_function(type, name, params)
        for param in params:
            param.set_parent(self.function)

        self.function.add_body(self)

    def get_instructions(self):
        return self.instructions


class PrintIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printInt", [AST_variable(None, VYPaInt(), "number")])
        self.instructions.add(WRITEI(self.function.stack.top()))


class PrintStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printString", [AST_variable(None, VYPaString(), "string")])
        self.instructions.add(WRITES(self.function.stack.top()))


class ReadIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "readInt", [])
        self.return_expression = self.function.add_variable(VYPaInt(), "number")
        self.instructions.add(READI(VYPaRegister.DestinationReg))
        self.stack.set(VYPaRegister.DestinationReg)


class ReadStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "readString", [])
        self.return_expression = self.function.add_variable(VYPaString(), "s")
        self.instructions.add(READI(VYPaRegister.DestinationReg))
        self.stack.set(VYPaRegister.DestinationReg)


class LengthVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "length", [AST_variable(None, VYPaInt(), "number")])

        self.instructions.add(GETSIZE(VYPaRegister.DestinationReg, self.function.stack.top()))
        self.return_expression = self.function.add_variable(VYPaInt(), "number")
        self.stack.set(VYPaRegister.DestinationReg)


class SubStrVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "subStr", [AST_variable(None, VYPaString(), "s"),
                                                  AST_variable(None, VYPaInt(), "i"),
                                                  AST_variable(None, VYPaInt(), "n")])
        # TODO: implement substr function

