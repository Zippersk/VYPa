from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import DIVI, AND, OR, NOT
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.error import Exit, Error


class AST_NOT(AST_block):
    def __init__(self, expression):
        super().__init__(None)
        self.expression = expression
        self.type = None

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.expression.get_instructions(self))
        self.type = VYPaInt()
        self.check_types()
        self.add_instruction(NOT(self.expression))
        self.pop_function_calls()
        return self.instruction_tape

    def pop_function_calls(self):
        if isinstance(self.expression, AST_function_call):
            self.stack.pop()

    def get_variable_offset(self, name):
        from src.VYPcode.AST.blocks.function_call import AST_function_call
        if isinstance(self.expression, AST_function_call):
            return 1 + self.parent.get_variable_offset(name)
        else:
            return self.parent.get_variable_offset(name)

    def __str__(self):
        return str(AST_value(self.type, str(VYPaRegister.Accumulator)))

    def check_types(self):
        if self.expression.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")