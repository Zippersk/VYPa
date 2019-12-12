from collections import OrderedDict

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.program import AST_program
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL
from src.VYPcode.Types.VYPaVoid import VYPaVoid


class AST_function(AST_block):
    def __init__(self, type, name, params):
        super().__init__()
        self.params = OrderedDict()
        self.type = type
        self.name = name
        self.label = f"func_{name}"

        for param in params:
            param.set_parent(self)
            if self.params.get(param.name, None) is not None:
                Exception(f"Param with name {name} already exists")
            else:
                self.params[param.name] = param

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None and \
                self.params.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exception(f"Variable {variable.name} already exists")

    def get_variable(self, name):
        if self.variables.get(name, None) is not None:
            return self.variables[name]
        elif self.params.get(name, None) is not None:
            return self.params[name]
        else:
            super().get_variable(name)

    def get_variable_offset(self, name):
        if self.params.get(name, None) is not None:
            return list(self.params)[::-1].index(name)
        elif self.variables.get(name, None) is not None:
            return len(self.params) + list(self.variables)[::-1].index(name)
        else:
            Exception(f"Variable {name} not found in function scope")

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