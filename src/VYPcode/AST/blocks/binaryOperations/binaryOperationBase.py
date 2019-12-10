from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt


class AST_binOperation(AST_block):
    def __init__(self, left, instruction, right):
        super().__init__(None)
        self.left = left
        self.right = right
        self.instruction = instruction

        self.left.set_parent(self)
        self.right.set_parent(self)

        self.type = None

    def get_instructions(self):
        self.check_types()
        self.type = VYPaInt()
        self.add_instruction(self.instruction(self.left, self.right))

    def __str__(self):
        return AST_value(self, self.type, str(VYPaRegister.Accumulator))

    def check_types(self):
        pass
