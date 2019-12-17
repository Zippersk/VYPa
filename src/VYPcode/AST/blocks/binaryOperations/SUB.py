"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.Instructions.Instructions import DIVI, SUBI
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.error import Exit, Error


class AST_SUBI(AST_binOperation):
    def __init__(self, left, right):
        super().__init__(left, SUBI, right)

    def check_types(self):
        if self.left.type != VYPaInt() or self.right.type != VYPaInt():
            Exit(Error.SemanticError, "Type check error!")

