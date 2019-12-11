from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.function import AST_function
from src.VYPcode.AST.blocks.function_return import AST_return
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Instructions.Instructions import WRITEI, WRITES, READI, GETSIZE, READS, LABEL, DUMPSTACK, DUMPREGS
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid


class VYPaBuildInFunctionClass(AST_function):
    def __init__(self, type, name, params):
        super().__init__(type, name, params)
        self.return_expression = None
        self.function = AST.get_root().add_function(self)
        self.label = f"buildIn_{name}"



class PrintIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printInt", [AST_variable(VYPaInt(), "number")])
        block = AST_block()
        block.add_instruction(WRITEI(self.function.stack.top()))
        self.add_block(block)


class PrintStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printString", [AST_variable(VYPaString(), "string")])
        block = AST_block()
        block.add_instruction(DUMPSTACK())
        block.add_instruction(DUMPREGS())
        block.add_instruction(WRITES(self.function.stack.top()))
        self.add_block(block)


class ReadIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaInt(), "readInt", [])
        self.add_block(AST_declaration(VYPaInt(), ["number"]))

        readi_block = AST_block()
        readi_block.add_instruction(READI(VYPaRegister.DestinationReg))
        readi_block.stack.set(VYPaRegister.DestinationReg)
        self.add_block(readi_block)

        self.add_block(AST_return(AST_value(VYPaInt(), self.stack.top())))


class ReadStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaString(), "readString", [])
        self.add_block(AST_declaration(VYPaString(), ["string"]))

        reads_block = AST_block()
        reads_block.add_instruction(READS(VYPaRegister.DestinationReg))
        reads_block.stack.set(VYPaRegister.DestinationReg)
        self.add_block(reads_block)

        self.add_block(AST_return(AST_value(VYPaString(), self.stack.top())))


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

