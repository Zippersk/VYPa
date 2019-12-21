"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.assigment import AST_assigment
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.LT import AST_LT
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.expression import AST_expression
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.ifelse import AST_condition_body
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.AST.blocks.while_loop import AST_while
from src.VYPcode.AST.blocks.word import AST_RESIZE, AST_GETWORD, AST_SETWORD
from src.VYPcode.Instructions.Instructions import ADDI, DUMPSTACK, DUMPREGS, COPY, RESIZE, SET, DUMPHEAP
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_ADD(AST_binOperation):
    def __init__(self, left, right):
        super().__init__(left, None, right)

    def check_types(self):
        if self.left.type != self.right.type:
            Exit(Error.SemanticError, "Type check error!")

    def get_instructions(self, parent):
        self.parent = parent
        self.stack_offset += parent.stack_offset
        self.instruction_tape.merge(self.left.get_instructions(self))
        self.instruction_tape.merge(self.right.get_instructions(self))

        if self.left.type == VYPaInt() and self.right.type == VYPaInt():
            self.instruction = ADDI
            self.check_types()
            self.type = VYPaInt()
            self.add_instruction(self.instruction(self.left, self.right))
            self.stack.push(AST_value(self.type, str(VYPaRegister.Accumulator)))
            self.add_expression_stack_offset()
        elif self.left.type == VYPaString() and self.right.type == VYPaString():
            self.check_types()
            self.type = VYPaString()
            self.instruction_tape.merge(
                AST_function_call("stringConcat", [self.left, self.right]).get_instructions(self)
            )
        else:
            Exit(Error.SemanticError, "Can not add other types as primitives")

        return self.instruction_tape
