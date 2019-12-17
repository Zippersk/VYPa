"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import ADDI, LTI, LTS, WRITEI, WRITES
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_LT(AST_binOperation):
    def __init__(self, left, right):
        super().__init__(left, None, right)

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.left.get_instructions(self))
        self.instruction_tape.merge(self.right.get_instructions(self))

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
        self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
        self.add_expression_stack_offset()
        return self.instruction_tape
