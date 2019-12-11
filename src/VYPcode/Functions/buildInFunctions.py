from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.function import AST_function
from src.VYPcode.AST.blocks.function_return import AST_return
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.Instructions import WRITEI, WRITES, READI, GETSIZE, READS, LABEL
from src.VYPcode.Stack import Stack
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.instructionsTape import InstructionTape


class VYPaBuildInFunctionClass(AST_function):
    def __init__(self, type, name, params):
        super().__init__(type, name, params)
        self.return_expression = None
        self.function = AST.get_root().add_function(self)
        self.label = f"buildIn_{name}"

    def get_instructions(self, parent):
        self.parent = parent
        if self.return_expression:
            ret_value = AST_return(self.return_expression)
            ret_value.set_parent(self.function)
            return self.instruction_tape.merge(ret_value.get_instructions(self))
        else:
            return self.instruction_tape


class PrintIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printInt", [AST_variable(VYPaInt(), "number")])
        self.instruction_tape.add(WRITEI(self.function.stack.top()))


class PrintStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printString", [AST_variable(VYPaString(), "string")])
        self.instruction_tape.add(WRITES(self.function.stack.top()))


class ReadIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "readInt", [])
        self.function.add_variable(AST_variable(VYPaInt(), "number"))
        self.return_expression = AST_value(VYPaInt(), self.stack.top())
        self.instruction_tape.add(READI(VYPaRegister.DestinationReg))
        self.stack.set(VYPaRegister.DestinationReg)


class ReadStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "readString", [])
        self.function.add_variable(AST_variable(VYPaString(), "string"))
        self.return_expression = AST_value(VYPaString(), self.stack.top())
        self.instruction_tape.add(READS(VYPaRegister.DestinationReg))
        self.stack.set(VYPaRegister.DestinationReg)


class LengthVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "length", [AST_variable(VYPaInt(), "number")])
        self.function.add_variable(AST_variable(VYPaInt(), "number"))
        self.return_expression = AST_value(VYPaInt(), self.stack.top())
        self.instruction_tape.add(GETSIZE(VYPaRegister.DestinationReg, self.function.stack.top()))
        self.stack.set(VYPaRegister.DestinationReg)


class SubStrVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "subStr", [AST_variable(VYPaString(), "s"),
                                                  AST_variable(VYPaInt(), "i"),
                                                  AST_variable(VYPaInt(), "n")])
        # TODO: implement substr function

