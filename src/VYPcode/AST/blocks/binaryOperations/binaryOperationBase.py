from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt


class AST_binOperation(AST_block):
    def __init__(self, left, instruction, right):
        super().__init__()
        self.left = left
        self.right = right
        self.instruction = instruction
        self.type = None

    def get_instructions(self):
        self.instruction_tape.merge(self.left.get_instructions())
        self.instruction_tape.merge(self.right.get_instructions())
        self.type = VYPaInt()
        self.check_types()
        self.add_instruction(self.instruction(self.left, self.right))
        return self.instruction_tape

    def __str__(self):
        return str(AST_value(self.type, str(VYPaRegister.Accumulator)))

    def check_types(self):
        pass
