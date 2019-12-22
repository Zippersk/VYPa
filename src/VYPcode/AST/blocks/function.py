"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from collections import OrderedDict

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.program import AST_program
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL, DUMPSTACK, DUMPREGS
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Exit, Error


class AST_function(AST_block):
    def __init__(self, type, name, params):
        super().__init__()
        self.params = OrderedDict()
        self.type = type
        self.name = name
        self.label = f"func_{name}"

        for param in params:
            self.add_param(param)

    def set_label(self, label):
        self.label = label

    def set_name(self, name):
        self.name = name

    def add_param(self, param):
        param.set_parent(self)
        if self.params.get(param.name, None) is not None:
            Exit(Error.SemanticError, f"Param with name {param.name} already exists")
        else:
            self.params[param.name] = param

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None and \
                self.params.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exit(Error.SemanticError, f"Variable {variable.name} already exists")

    def get_variable(self, name):
        if self.variables.get(name, None) is not None:
            return self.variables[name]
        elif self.params.get(name, None) is not None:
            return self.params[name]
        else:
            Exit(Error.SemanticError, f"Variable {name} was not defined")

    def get_variable_offset(self, name):
        if self.params.get(name, None) is not None:
            return len(self.variables) + list(self.params)[::-1].index(name)
        elif self.variables.get(name, None) is not None:
            offset = 0
            for variable in list(self.variables.values())[::-1]:
                if variable.name == name:
                    return offset
                else:
                    offset += variable.get_size()

        else:
            Exit(Error.SemanticError, f"Variable {name} not found in function scope")

    def get_instructions(self, parent):
        self.parent = parent
        self.add_instruction(COMMENT(""))
        self.add_instruction(COMMENT(f"Start of function {self.name}"))
        self.add_instruction(LABEL(self.label))
        self.stack.allocate(2 + len(self.params))
        for variable in self.variables.values():
            self.merge_instructions(variable.get_instructions(self))

        for statement in self.AST_blocks:
            self.merge_instructions(statement.get_instructions(self))

        if isinstance(self.get_parent(), AST_program) and self.name == "main" and self.type == VYPaVoid():
            self.add_instruction(JUMP("END"))
        else:
            from src.VYPcode.AST.blocks.function_return import AST_return
            if self.type == VYPaVoid():
                default_return = AST_return(None)
            else:
                default_return = AST_return(AST_value(self.type, self.type.get_default()))
            default_return.set_parent(self)
            self.merge_instructions(default_return.get_instructions(self))

        self.add_instruction(COMMENT(f"End of function {self.name}"))
        self.add_instruction(COMMENT(""))

        return self.instruction_tape

    def __str__(self):
        return self.label