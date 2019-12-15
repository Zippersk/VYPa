from collections import OrderedDict

from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL
from src.error import Exit, Error


class AST_class(AST_block):
    def __init__(self, name, predecessor, body):
        super().__init__()
        self.body = body
        self.predecessor_name = predecessor
        self.predecessor = None
        self.name = name
        self.functions = OrderedDict()

    def add_function(self, function):
        if not self.functions.get(function.name, None) is not None:
            function.set_parent(self)
            self.functions[function.name] = function
            return function
        else:
            Exit(Error.SyntaxError, f"Function {function.name} already exists")

    def get_function(self, function_name):
        if self.functions.get(function_name, None) is not None:
            return self.functions[function_name]
        else:
            if self.name != "Object":
                self.predecessor.get_variable(function_name)
            else:
                Exit(Error.SyntaxError, f"Function {function_name} was not defined")

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exit(Error.SyntaxError, f"Variable {variable.name} already exists")

    def get_variable(self, name):
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
        self.add_instruction(COMMENT(""))
        self.add_instruction(COMMENT(f"Start of class {self.name}"))

        if self.name != "Object":
            self.predecessor = AST.root.get_class(self.predecessor_name)
            self.merge_instructions(self.predecessor.get_instructions())

        for variable in self.variables.values():
            self.merge_instructions(variable.get_instructions(self))

        for statement in self.AST_blocks:
            self.merge_instructions(statement.get_instructions(self))

        self.add_instruction(COMMENT(f"End of class {self.name}"))
        self.add_instruction(COMMENT(""))

        return self.instruction_tape

