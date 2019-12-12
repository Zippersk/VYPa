from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import JUMPZ, LABEL, JUMP
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt

IF_BLOCK_COUNTS = 1


class AST_ifelse(AST_block):
    def __init__(self, condition, if_body, else_body):
        super().__init__()
        self.else_body = AST_condition_body(else_body)
        self.if_body = AST_condition_body(if_body)
        self.condition = condition

    def get_instructions(self, parent):
        self.parent = parent
        global IF_BLOCK_COUNTS
        self.instruction_tape.merge(self.condition.get_instructions(self))
        self.instruction_tape.add(
            JUMPZ(f"else_{IF_BLOCK_COUNTS}",
                  AST_value(VYPaInt(), str(VYPaRegister.Accumulator))
                  )
        )

        self.instruction_tape.merge(self.if_body.get_instructions(self))

        self.instruction_tape.add(JUMP(f"end_else_if_{IF_BLOCK_COUNTS}"))
        self.instruction_tape.add(LABEL(f"else_{IF_BLOCK_COUNTS}"))

        self.instruction_tape.merge(self.else_body.get_instructions(self))

        self.instruction_tape.add(LABEL(f"end_else_if_{IF_BLOCK_COUNTS}"))
        IF_BLOCK_COUNTS += 1
        return self.instruction_tape


class AST_condition_body(AST_block):
    def __init__(self, body):
        super().__init__()
        self.body = body

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exception(f"Variable {variable.name} already exists")

    def get_instructions(self, parent):
        self.parent = parent
        for statement in self.body:
            self.instruction_tape.merge(statement.get_instructions(self))

        self.stack.deallocate(len(self.variables))
        return self.instruction_tape


