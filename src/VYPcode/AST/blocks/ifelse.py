from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import JUMPZ, LABEL, JUMP
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt

IF_BLOCK_COUNTS = 1


class AST_ifelse(AST_block):
    def __init__(self, condition, if_body, else_body):
        super().__init__()
        self.else_body = else_body
        self.if_body = if_body
        self.condition = condition

    def get_instructions(self):
        global IF_BLOCK_COUNTS
        self.instruction_tape.merge(self.condition.get_instructions())
        self.instruction_tape.add(
            JUMPZ(f"else_{IF_BLOCK_COUNTS}",
                  AST_value(VYPaInt(), str(VYPaRegister.Accumulator))
                  )
        )

        for statement in self.if_body:
            self.instruction_tape.merge(statement.get_instructions())

        self.instruction_tape.add(JUMP(f"end_else_if_{IF_BLOCK_COUNTS}"))
        self.instruction_tape.add(LABEL(f"else_{IF_BLOCK_COUNTS}"))

        for statement in self.else_body:
            self.instruction_tape.merge(statement.get_instructions())

        self.instruction_tape.add(LABEL(f"end_else_if_{IF_BLOCK_COUNTS}"))
        IF_BLOCK_COUNTS += 1
        return self.instruction_tape

