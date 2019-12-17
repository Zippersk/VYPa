"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import INT2STRING
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_cast(AST_block):
    def __init__(self, casting_type, expression):
        super().__init__()
        self.casting_type = casting_type
        self.expression = expression
        self.type = None
        self.stack_offset = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.expression.get_instructions(self))
        self.type = VYPaString()
        self.check_types()
        self.add_instruction(INT2STRING(self.expression))
        self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
        self.add_expression_stack_offset()
        return self.instruction_tape

    def add_expression_stack_offset(self):
        self.stack_offset += 1
        self.parent.add_expression_stack_offset()

    def __str__(self):
        return str(AST_value(self.type, self.stack.get()))

    def check_types(self):
        # TODO: support classes for casting (maybe we will need to decide this in runtime)
        if self.expression.type != VYPaInt() and self.casting_type != VYPaString():
            Exit(Error.SemanticError, "Type check error!")
