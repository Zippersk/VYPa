"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.class_variable_call import AST_class_variable_call
from src.VYPcode.AST.blocks.expression import AST_expression
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import ADDI, LTI, LTS, GTS, GTI, EQI, EQS, SET, DUMPREGS, DUMPSTACK, DUMPHEAP
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_EQ(AST_binOperation):
    def __init__(self, left, right):
        super().__init__(left, None, right)

    def get_instructions(self, parent):
        self.parent = parent
        self.stack_offset += parent.stack_offset
        self.instruction_tape.merge(self.left.get_instructions(self))
        self.instruction_tape.merge(self.right.get_instructions(self))

        if self.left.type == VYPaInt() and self.right.type == VYPaInt():
            self.instruction = EQI
            self.type = VYPaInt()
            self.add_instruction(self.instruction(self.left, self.right))
        elif self.left.type == VYPaString() and self.right.type == VYPaString():
            self.instruction = EQS
            self.type = VYPaInt()
            self.add_instruction(self.instruction(self.left, self.right))
        elif isinstance(self.left.type, VYPaClass) and isinstance(self.right.type, VYPaClass):
            self.instruction = EQI
            self.type = VYPaInt()

            left_class = AST_expression(AST_class_variable_call(self.left.name, "**runtime_name**"))
            self.merge_instructions(left_class.get_instructions(self))
            self.add_instruction(SET("$6", VYPaRegister.Accumulator))

            right_class = AST_expression(AST_class_variable_call(self.right.name, "**runtime_name**"))
            self.merge_instructions(right_class.get_instructions(self))
            self.add_instruction(SET("$7", VYPaRegister.Accumulator))
            self.add_instruction(DUMPREGS())
            self.add_instruction(DUMPSTACK())
            self.add_instruction(DUMPHEAP())

            self.add_instruction(self.instruction(AST_value(VYPaInt(), "$6"), AST_value(VYPaInt(), "$7")))
        else:
            Exit(Error.SemanticError, "Types mismatch")
            pass
        self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
        self.add_expression_stack_offset()
        return self.instruction_tape
