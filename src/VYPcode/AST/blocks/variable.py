"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.base import AST_block


class AST_variable(AST_block):
    def __init__(self, type, name):
        super().__init__()
        self.name = name
        self.type = type
