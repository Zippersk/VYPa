from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.function import AST_function
from src.VYPcode.Instructions.Instructions import COMMENT, RETURN, DUMPSTACK
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Exit, Error


class AST_return(AST_block):
    def __init__(self, expression):
        super().__init__()
        self.expression = expression
        self.type = None

    def find_function(self):
        block = self
        while block.get_parent() is not None:
            block = block.get_parent()
            if isinstance(block, AST_function):
                return block

    def get_instructions(self):
        function = self.find_function()
        if function.type == VYPaVoid():
            if self.expression is not None:
                Exit(Error.SyntaxError, "Void can not have return value")
        else:
            self.instruction_tape.merge(self.expression.get_instructions())
            self.type = self.expression.type
            if self.type != function.type:
                Exit(Error.SemanticError, "Different return type and function type")

        dealloc_count = len(function.variables) + len(function.params)

        if function.type != VYPaVoid():
            self.instruction_tape.add(COMMENT(f"Set return value"))
            self.stack.set(self.expression, -dealloc_count - 1)

        self.instruction_tape.add(COMMENT(f"Deallocate {dealloc_count} scope variables and paramters"))
        self.stack.deallocate(dealloc_count)

        self.stack.deallocate(2)
        self.instruction_tape.add(DUMPSTACK())
        self.instruction_tape.add(RETURN(self.stack.get(2)))
        return self.instruction_tape

