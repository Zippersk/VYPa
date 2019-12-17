"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""

from src.instructionsTape import InstructionTape
from src.VYPcode.AST.blocks.base import AST_block
from src.error import Exit, Error


class AST_class(AST_block):
    def __init__(self, name, predecessor):
        super().__init__()
        self.predecessor_name = predecessor
        self.predecessor = None
        self.name = name
        self.declarations = []

    def add_declaration(self, variable):
        self.declarations.append(variable)

    def get_instructions(self, parent):
        self.parent = parent
        # return empty instruction tape because we do not want to initialize class yet
        return InstructionTape()

