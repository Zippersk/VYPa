"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
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

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exit(Error.SyntaxError, f"Variable {variable.name} already exists")

    def add_declaration(self, declaration):
        self.declarations.append(declaration)
        self.merge_instructions(declaration.get_instructions(self))

    def get_variable(self, name):
        if name == "super":
            return self.predecessor.get_variable("this")
        if self.variables.get(name, None) is not None:
            return self.variables[name]
        else:
            if self.name != "Object":
                self.predecessor.get_variable(name)
            else:
                Exit(Error.SyntaxError, f"Variable {name} was not defined")

    def get_variable_offset(self, name):
        if self.variables.get(name, None) is not None:
            return list(self.variables)[::-1].index(name)
        else:
            Exit(Error.SyntaxError, f"Variable {name} not found in function scope")

    def get_instructions(self, parent):
        self.parent = parent
        if self.name != "Object":
            self.predecessor = AST.root.get_class(self.predecessor_name)
        return InstructionTape()

