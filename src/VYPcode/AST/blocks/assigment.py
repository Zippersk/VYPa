"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Instructions.Instructions import SET, DUMPREGS, DUMPSTACK
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.error import Exit, Error


class AST_assigment(AST_block):
    def __init__(self, variable_call, expression):
        super().__init__()
        self.variable = variable_call
        self.expression = expression

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.expression.get_instructions(self))
        self.variables["_"] = AST_variable(VYPaInt(), "_")
        self.stack.push(AST_value(self.expression.type, VYPaRegister.Accumulator))
        self.instruction_tape.merge(self.variable.get_instructions(self))

        if self.variable.type != self.expression.type:
            if self.variable.name != "this":
                Exit(Error.SemanticError, "Type check error!")

        if isinstance(self.variable.type, VYPaClass) and self.variable.name != "this":
            this_offset = 0
            class_name = self.expression.type.name
            self.add_instruction(SET(VYPaRegister.ClassCallReg, self.stack.top()))
            while self.variable.type.name != class_name:
                this_offset -= len(AST.root.get_class(class_name).variables)
                class_name = AST.root.get_class(class_name).predecessor_name
            self.instruction_tape.add(SET(self.variable, self.stack.get(this_offset, VYPaRegister.ClassCallReg)))
        else:
            self.instruction_tape.add(SET(self.variable, self.stack.top()))
        self.stack.pop()
        return self.instruction_tape
