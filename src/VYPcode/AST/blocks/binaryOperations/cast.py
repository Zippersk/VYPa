"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import INT2STRING, SET
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaClass import VYPaClass
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
        self.stack_offset += parent.stack_offset
        self.instruction_tape.merge(self.expression.get_instructions(self))
        self.check_types()

        if self.expression.type == VYPaInt() and self.casting_type == VYPaString():
            self.type = VYPaString()
            self.add_instruction(INT2STRING(self.expression))
            self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
        else:
            this_offset = 0
            class_name = self.expression.type.name
            self.add_instruction(SET(VYPaRegister.ClassCallReg, VYPaRegister.Accumulator))
            while self.casting_type.name != class_name:
                this_offset -= len(AST.root.get_class(class_name).variables)
                class_name = AST.root.get_class(class_name).predecessor_name
            self.type = self.casting_type
            self.stack.push(AST_value(self.type, self.stack.get(this_offset, VYPaRegister.ClassCallReg)))

        self.add_expression_stack_offset()
        return self.instruction_tape

    def add_expression_stack_offset(self):
        self.stack_offset += 1
        self.parent.add_expression_stack_offset()

    def __str__(self):
        return str(AST_value(self.type, self.stack.get()))

    def check_types(self):
        if (self.expression.type != VYPaInt() and self.casting_type != VYPaString()) and \
                (not isinstance(self.expression.type, VYPaClass) and not AST.root.classes.get(self.casting_type.name, False)):
            Exit(Error.TypesIncompatibility, "Type check error!")
