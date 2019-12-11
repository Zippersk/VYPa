from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.Instructions.Instructions import ADDI, LTI, LTS
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_LT(AST_binOperation):
    def __init__(self, left, right):
        super().__init__(left, None, right)

    def get_instructions(self):
        self.instruction_tape.merge(self.left.get_instructions())
        self.instruction_tape.merge(self.right.get_instructions())

        if self.left.type == VYPaInt() and self.right.type == VYPaInt():
            self.instruction = LTI
            self.type = VYPaInt()
            self.add_instruction(self.instruction(self.left, self.right))
        elif self.left.type == VYPaString() and self.right.type == VYPaString():
            self.instruction = LTS
            self.type = VYPaString()
            self.add_instruction(self.instruction(self.left, self.right))
        else:
            Exit(Error.SemanticError, "Types mismatch")
            pass

        return self.instruction_tape
