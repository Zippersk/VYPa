"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Types.VYPaClass import VYPaClass


class AST_variable(AST_block):
    def __init__(self, type, name):
        super().__init__()
        self.name = name
        self.type = type

    def get_size(self):
        if isinstance(self.type, VYPaClass):
            size = 0
            if self.name is "this":
                return 1

            class_name = self.type.name
            while class_name is not None:
                size += len(AST.root.get_class(class_name).variables)
                class_name = AST.root.get_class(class_name).predecessor_name

            return size
        else:
            return 1
