from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL, CALL
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.error import Exit, Error


class AST_function_call(AST_block):
    def __init__(self, previous, name, calling_params):
        super().__init__(previous)
        self.calling_params = calling_params
        self.name = name
        self.label = f"func_{name}"

    def check_params(self, function):
        if len(function.params) != len(self.calling_params):
            Exit(Error.SyntaxError, "Wrong number of parameters")
        for calling_param, declared_param in zip(self.calling_params, function.params):
            if calling_param.type != declared_param.type:
                Exit(Error.TypesIncompatibility, "Parameters types mismatch")

    def get_instructions(self):
        self.stack.allocate(2)  # Allocate memory for SP (it will be used for return) and function return value

        # print is a special function which can be called with multiple parameters
        # so internally we call PrintInt or PrintString for each parameter...
        if self.name == "print":
            if len(self.calling_params) == 0:
                Exit(Error.SemanticError, "Print called with zero params")

            for param in self.calling_params:
                if param.type == VYPaInt():
                    function = AST.root.get_function("printInt")
                    self.stack.push(self.stack.get(-param.get_stack_offset() - 2))
                    self.add_instruction(CALL(self.stack.get(-1), function))
                elif param.type == VYPaString():
                    function = AST.root.get_function("printString")
                    self.stack.push(self.stack.get(-param.get_stack_offset() - 2))
                    self.add_instruction(CALL(self.stack.get(-1), function))

        else:
            function = AST.root.get_function(self.name)
            self.check_params(function)

            for param in self.calling_params:
                self.stack.push(self.stack.get(-param.get_stack_offset() - 2))

            self.add_instruction(CALL(self.stack.get(-len(function.params)), function))

        return self.instruction_tape


