from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import DIVI, AND, OR, NOT
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.error import Exit, Error


class AST_NOT(AST_block):
    def __init__(self, expression):
        super().__init__(None)
        self.expression = expression
        self.type = None

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.expression.get_instructions(self))
        self.type = VYPaInt()
        self.check_types()
        self.add_instruction(NOT(self.expression))
        return self.instruction_tape

    def __str__(self):
        return str(AST_value(self.type, str(VYPaRegister.Accumulator)))

    def check_types(self):
        if self.expression.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")