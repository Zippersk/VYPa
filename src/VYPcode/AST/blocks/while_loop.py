from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import JUMPZ, LABEL, JUMP
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt

WHILE_BLOCK_COUNTS = 1


class AST_while(AST_block):
    def __init__(self, condition, body):
        super().__init__()
        self.body = body
        self.condition = condition

    def get_instructions(self, parent):
        self.parent = parent
        global WHILE_BLOCK_COUNTS
        self.instruction_tape.add(LABEL(f"loop_{WHILE_BLOCK_COUNTS}"))
        self.instruction_tape.merge(self.condition.get_instructions(self))
        self.instruction_tape.add(
            JUMPZ(f"end_loop_{WHILE_BLOCK_COUNTS}",
                  AST_value(VYPaInt(), str(VYPaRegister.Accumulator))
                  )
        )

        for statement in self.body:
            self.instruction_tape.merge(statement.get_instructions(self))

        self.instruction_tape.add(JUMP(f"loop_{WHILE_BLOCK_COUNTS}"))
        self.instruction_tape.add(LABEL(f"end_loop_{WHILE_BLOCK_COUNTS}"))

        WHILE_BLOCK_COUNTS += 1
        return self.instruction_tape

