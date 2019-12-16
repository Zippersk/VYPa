from collections import OrderedDict

from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.common import CallType
from src.error import Exit, Error


class AST_class(AST_block):
    def __init__(self, name, predecessor):
        super().__init__()
        self.predecessor_name = predecessor
        self.predecessor = None
        self.name = name
        self.functions = OrderedDict()

    def add_function(self, function):
        if not self.functions.get(function.name, None) is not None:
            function.set_parent(self)
            function.add_param(AST_variable(VYPaClass(self.name), "this"))
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

    def get_instructions(self, parent):
        self.parent = parent
        self.add_instruction(COMMENT(""))
        self.add_instruction(COMMENT(f"Start of class {self.name}"))

        for function in self.functions.values():
            self.merge_instructions(function.get_instructions(self))

        self.add_instruction(COMMENT(f"End of class {self.name}"))
        self.add_instruction(COMMENT(""))

        return self.instruction_tape

