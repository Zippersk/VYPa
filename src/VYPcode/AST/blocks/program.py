from collections import OrderedDict

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import COMMENT


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
            Exception(f"Function {function.name} already exists")

    def get_class(self, class_name):
        return self.classes[class_name]

    def get_function(self, function_name):
        return self.functions[function_name]

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