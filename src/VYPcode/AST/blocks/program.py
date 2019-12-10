from collections import OrderedDict

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import COMMENT


class AST_program(AST_block):
    def __init__(self):
        super().__init__(None)
        self.functions = OrderedDict()
        self.classes = OrderedDict()

    def add_function(self, type, name, params):
        if not self.functions.get(name, None) is not None:

            from src.VYPcode.AST.blocks.function import AST_function
            function = AST_function(self, type, name, params)
            self.functions[name] = function
            return function
        else:
            Exception(f"Function {name} already exists")

    def add_class(self, classe):
        # TODO create AST block for class
        pass

    def get_class(self, class_name):
        return self.classes[class_name]

    def get_function(self, function_name):
        return self.functions[function_name]

    def get_instructions(self):
        self.add_instruction(COMMENT("Program body start"))

        for function in self.functions.values():
            self.merge_instructions(function.get_instructions())

        for clas in self.classes.values():
            self.merge_instructions(clas.get_instructions())

        self.add_instruction(COMMENT("Program body end"))
        return self.instruction_tape

    def __str__(self):
        return "program"
