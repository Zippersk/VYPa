from collections import OrderedDict

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import COMMENT
from src.error import Exit, Error


class AST_program(AST_block):
    def __init__(self):
        super().__init__()
        self.functions = OrderedDict()
        self.classes = OrderedDict()

    def add_function(self, function):
        if not self.functions.get(function.name, None) is not None:
            function.set_parent(self)
            self.functions[function.name] = function
            return function
        else:
            Exit(Error.SyntaxError, f"Function {function.name} already exists")

    def get_class(self, class_name):
        try:
            return self.classes[class_name]
        except KeyError:
            Exit(Error.SyntaxError, f"Class {class_name} was not defined")

    def get_function(self, function_name):
        try:
            return self.functions[function_name]
        except KeyError:
            Exit(Error.SyntaxError, f"Function {function_name} was not defined")

    def get_instructions(self, parent):
        self.parent = parent
        self.add_instruction(COMMENT("Program body start"))

        for function in self.functions.values():
            self.merge_instructions(function.get_instructions(self))

        for clas in self.classes.values():
            self.merge_instructions(clas.get_instructions(self))

        self.add_instruction(COMMENT("Program body end"))
        return self.instruction_tape

    def get_variable(self, name):
        return Exception("Variable not found")