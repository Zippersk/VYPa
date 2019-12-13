from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.NOT import AST_NOT
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
        self.was_executed = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.left.get_instructions(self))
        self.instruction_tape.merge(self.right.get_instructions(self))
        self.type = VYPaInt()
        self.check_types()
        self.add_instruction(self.instruction(self.left, self.right))
        self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
        self.parent.add_expression_stack_offset()
        return self.instruction_tape

    def add_expression_stack_offset(self):
        self.parent.add_expression_stack_offset()

    def __str__(self):
        if not isinstance(self.parent, AST_NOT) and self.parent.left == self and isinstance(self.parent.right, AST_binOperation):
            return str(AST_value(self.type, self.stack.get(-1)))
        return str(AST_value(self.type, self.stack.get()))

    def check_types(self):
        pass
