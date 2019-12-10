﻿from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import COMMENT, RETURN
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Exit, Error


class AST_return(AST_block):
    def __init__(self, function, expression):
        super().__init__(function)
        self.function = function
        self.expression = expression
        self.type = None

    def get_instructions(self):
        if self.function.type == VYPaVoid():
            if self.expression is not None:
                Exit(Error.SyntaxError, "Void can not have return value")
        else:
            self.instruction_tape.merge(self.expression.get_instructions())
            self.type = self.expression.type
            if self.type != self.function.type:
                Exit(Error.SemanticError, "Different return type and function type")

        dealloc_count = len(self.function.variables) + len(self.function.params)
        self.instruction_tape.add(COMMENT(f"Deallocate {dealloc_count} scope variables and paramters"))
        self.stack.deallocate(dealloc_count)

        if self.function.type != VYPaVoid():
            self.instruction_tape.add(COMMENT(f"Set return value"))
            self.stack.set(self.expression, -1)

        self.instruction_tape.add(RETURN(self.stack.pop()))
        return self.instruction_tape

