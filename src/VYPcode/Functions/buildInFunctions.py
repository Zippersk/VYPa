from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.function_return import AST_return
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.Instructions import WRITEI, WRITES, READI, GETSIZE, READS
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
        if self.return_expression:
            ret_value = AST_return(self.function, self.return_expression)
            return self.instructions.merge(ret_value.get_instructions())
        else:
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
        self.function.add_variable(VYPaInt(), "number")
        self.return_expression = AST_value(self.function, VYPaInt(), self.stack.top())
        self.instructions.add(READI(VYPaRegister.DestinationReg))
        self.stack.set(VYPaRegister.DestinationReg)


class ReadStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "readString", [])
        self.function.add_variable(VYPaString(), "string")
        self.return_expression = AST_value(self.function, VYPaString(), self.stack.top())
        self.instructions.add(READS(VYPaRegister.DestinationReg))
        self.stack.set(VYPaRegister.DestinationReg)


class LengthVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "length", [AST_variable(None, VYPaInt(), "number")])
        self.function.add_variable(VYPaInt(), "number")
        self.return_expression = AST_value(self.function, VYPaInt(), self.stack.top())
        self.instructions.add(GETSIZE(VYPaRegister.DestinationReg, self.function.stack.top()))
        self.stack.set(VYPaRegister.DestinationReg)


class SubStrVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "subStr", [AST_variable(None, VYPaString(), "s"),
                                                  AST_variable(None, VYPaInt(), "i"),
                                                  AST_variable(None, VYPaInt(), "n")])
        # TODO: implement substr function

