from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import CREATE, SETWORD
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid


class AST_variable(AST_block):
    def __init__(self, previous, type, name):
        super().__init__(previous)
        self.name = name
        self.type = type

    def declare_integer(self):
        self.stack.push(str(0))
        return self

    def declare_string(self):
        self.instruction_tape.add(CREATE(VYPaRegister.DestinationReg, 1))
        self.instruction_tape.add(SETWORD(VYPaRegister.DestinationReg, 0, '""'))
        self.stack.push(VYPaRegister.DestinationReg)
        return self

    def get_instructions(self):
        if self.type == VYPaInt():
            self.declare_integer()
        elif self.type == VYPaString():
            self.declare_string()
        elif self.type == VYPaVoid():
            Exception("variable can not have type void")

        return self.instruction_tape

    def get_stack_offset(self):
        return self.get_parent().get_variable_index(self.name)

    def __str__(self):
        return self.stack.get(-self.get_stack_offset())
