from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL, CALL, DUMPSTACK
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Exit, Error


class AST_function_call(AST_block):
    def __init__(self, name, calling_params):
        super().__init__()
        self.calling_params = calling_params
        self.name = name
        self.label = f"func_{name}"
        self.type = None

    def check_params(self, function):
        if len(function.params) != len(self.calling_params):
            Exit(Error.SyntaxError, "Wrong number of parameters")
        for calling_param, declared_param in zip(self.calling_params, function.params):
            if calling_param.type != declared_param.type:
                Exit(Error.TypesIncompatibility, "Parameters types mismatch")

    def get_instructions(self, parent):
        self.parent = parent

        # print is a special function which can be called with multiple parameters
        # so internally we call PrintInt or PrintString for each parameter...
        if self.name == "print":
            self.type = VYPaVoid()
            if len(self.calling_params) == 0:
                Exit(Error.SemanticError, "Print called with zero params")

            for param in self.calling_params:
                self.instruction_tape.merge(param.get_instructions(self))
                if param.type == VYPaInt():
                    function = AST.root.get_function("printInt")

                elif param.type == VYPaString():
                    function = AST.root.get_function("printString")
                else:
                    # TODO: print objects?
                    pass

                self.stack.set(param, 3)
                self.add_instruction(CALL(self.stack.get(2), function))

        else:
            function = AST.root.get_function(self.name)
            self.type = function.type
            self.check_params(function)

            for offset, param in enumerate(self.calling_params, 2):
                self.instruction_tape.merge(param.get_instructions(self))
                self.stack.set(param, offset)

            self.add_instruction(CALL(self.stack.get(-len(function.params) + 2), function))
            self.add_instruction(DUMPSTACK())
        return self.instruction_tape

    def __str__(self):
        return str(AST_value(self.type, self.stack.get(1)))

