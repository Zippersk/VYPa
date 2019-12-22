"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Instructions.Instructions import SET
from src.VYPcode.Registers.Registers import VYPaRegister


class AST_class_variable_call(AST_block):
    def __init__(self, class_variable_name, name):
        super().__init__()
        self.class_variable_name = class_variable_name
        self.class_variable = None
        self.name = name
        self.variable = None
        self.type = None
        self.stack_offset = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.class_variable = AST_variable_call(self.class_variable_name)
        self.instruction_tape.merge(self.class_variable.get_instructions(self))
        self.add_instruction(SET(VYPaRegister.ClassCallReg, self.class_variable))

        self.variable = AST.root.get_class(self.class_variable.type.name).get_variable(self.name)
        self.type = self.variable.type
        self.instruction_tape.add(SET(AST_value(self.type, str(VYPaRegister.Accumulator)), str(self)))
        return self.instruction_tape

    def __str__(self):
        self.stack_offset = AST.root.get_class(self.class_variable.type.name).get_variable_offset(self.name)
        return self.stack.get(-self.stack_offset, VYPaRegister.ClassCallReg)


