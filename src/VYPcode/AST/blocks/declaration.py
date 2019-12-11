from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Instructions.Instructions import SET, CREATE, SETWORD
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Exit, Error


class AST_declaration(AST_block):
    def __init__(self, type, variable_names):
        super().__init__()
        self.variable_names = variable_names
        self.type = type

    def declare_integer(self, name):
        self.stack.push(str(0))
        return AST_variable(VYPaInt(), name)

    def declare_string(self, name):
        self.instruction_tape.add(CREATE(VYPaRegister.DestinationReg, 1))
        self.instruction_tape.add(SETWORD(VYPaRegister.DestinationReg, 0, '""'))
        self.stack.push(VYPaRegister.DestinationReg)
        return AST_variable(VYPaString(), name)

    def get_instructions(self, parent):
        self.parent = parent
        for name in self.variable_names:
            if self.type == VYPaInt():
                parent.add_variable(self.declare_integer(name))
            elif self.type == VYPaString():
                parent.add_variable(self.declare_string(name))
            elif self.type == VYPaVoid():
                Exit(Error.SemanticError, "Can not create void variable")

        return self.instruction_tape

