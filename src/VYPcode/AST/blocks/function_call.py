from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL, CALL, DUMPSTACK, DUMPHEAP, DUMPREGS
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.common import CallType, get_class
from src.error import Exit, Error


class AST_function_call(AST_binOperation):
    def __init__(self, name, calling_params, call_type=CallType.SCOPE, instance_name=None):
        super().__init__(None, None, None)
        self.call_type = call_type
        self.instance_name = instance_name
        self.calling_params = calling_params
        self.name = name
        self.label = f"func_{name}"
        self.type = None

    def check_params(self, function):
        if len(function.params) != len(self.calling_params):
            Exit(Error.SyntaxError, "Wrong number of parameters")
        for calling_param, declared_param in zip(self.calling_params, function.params.values()):
            if calling_param.type != declared_param.type:
                Exit(Error.TypesIncompatibility, "Parameters types mismatch")

    def get_function(self, name):
        if self.call_type == CallType.SCOPE:
            return AST.root.get_function(name)
        elif self.call_type == CallType.INSTANCE:
            instance = AST_variable_call("this", CallType.INSTANCE, self.instance_name)
            self.instruction_tape.merge(instance.get_instructions(self))
            self.calling_params.insert(0, AST_value(instance.type, str(instance)))
            return self.get_variable(self.instance_name).get_function(name)
        elif self.call_type == CallType.THIS:
            instance = AST_variable_call("this", CallType.THIS)
            self.instruction_tape.merge(instance.get_instructions(self))
            self.calling_params.insert(0, AST_value(instance.type, str(instance)))
            return get_class(self).get_function(name)
        elif self.call_type == CallType.SUPER:
            instance = AST_variable_call("this", CallType.SUPER)
            self.instruction_tape.merge(instance.get_instructions(self))
            self.calling_params.insert(0, AST_value(instance.type, str(instance)))
            return get_class(self).predecessor.get_function(name)

    def get_instructions(self, parent):
        self.parent = parent

        # print is a special function which can be called with multiple parameters
        # so internally we call PrintInt or PrintString for each parameter...
        if self.name == "print" and self.call_type == CallType.SCOPE:
            self.type = VYPaVoid()
            if len(self.calling_params) == 0:
                Exit(Error.SemanticError, "Print called with zero params")

            for idx, param in enumerate(self.calling_params, 1):
                self.instruction_tape.merge(param.get_instructions(self))
                if param.type == VYPaInt():
                    function = self.get_function("printInt")

                elif param.type == VYPaString():
                    function = self.get_function("printString")
                else:
                    Exit(Error.SemanticError, "argument of print can be only int or str")

                self.stack.set(param, 3)
                self.add_instruction(CALL(self.stack.get(2), function))
                if idx != len(self.calling_params):
                    self.stack.pop()

        else:
            function = self.get_function(self.name)
            self.type = function.type

            for offset, param in enumerate(self.calling_params, 3):
                self.instruction_tape.merge(param.get_instructions(self))
                self.stack.set(param, offset)

            self.check_params(function)
            self.add_instruction(CALL(self.stack.get(2), function))
        self.add_expression_stack_offset()
        return self.instruction_tape


