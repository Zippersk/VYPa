from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.Instructions.Instructions import ADDI
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_ADD(AST_binOperation):
    def __init__(self, left, right):
        super().__init__(left, None, right)

    def check_types(self):
        if self.left.type != self.right.type:
            Exit(Error.SemanticError, "Type check error!")

    def get_instructions(self):
        if self.left.type == VYPaInt() and self.left.type == VYPaString():
            self.instruction = ADDI
            self.check_types()
            self.type = VYPaInt()
            self.add_instruction(self.instruction(self.left, self.right))
        else:
            # TODO: implement concatenation of strings
            pass

        return self.instruction_tape
