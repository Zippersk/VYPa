"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.binaryOperations.binaryOperationBase import AST_binOperation
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Instructions.Instructions import SET, CALL, DUMPREGS, DUMPSTACK, WRITES
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.error import Exit, Error


class AST_class_function_call(AST_binOperation):
    def __init__(self, class_variable_name, name, calling_params):
        super().__init__(None, None, None)
        self.class_variable_name = class_variable_name
        self.calling_params = calling_params
        self.name = name
        self.label = None
        self.type = None

    def check_params(self, function):
        if len(function.params) != len(self.calling_params):
            Exit(Error.SyntaxError, "Wrong number of parameters")
        for calling_param, declared_param in zip(self.calling_params, function.params.values()):
            if calling_param.type != declared_param.type:
                Exit(Error.TypesIncompatibility, "Parameters types mismatch")

    def get_instructions(self, parent):
        self.parent = parent
        self.stack_offset += parent.stack_offset

        this_offset = 0
        if self.class_variable_name == "super":
            this_variable = AST_variable_call("this")
            self.instruction_tape.merge(this_variable.get_instructions(self))
            this_offset += len(AST.root.get_class(this_variable.type.name).variables)
            class_name = AST.root.get_class(this_variable.type.name).predecessor_name
            self.class_variable_name = "this"
        else:
            this_variable = AST_variable_call(self.class_variable_name)
            self.instruction_tape.merge(this_variable.get_instructions(self))
            class_name = this_variable.type.name

        function = None
        while function is None:
            if AST.root.functions.get(f"{class_name}_{self.name}", None):
                self.stack.set(self.stack.get(- this_offset, VYPaRegister.Accumulator), 3)
                function = AST.root.get_function(f"{class_name}_{self.name}")
            else:
                this_offset += len(AST.root.get_class(class_name).variables)
                class_name = AST.root.get_class(class_name).predecessor_name


        self.type = function.type

        self.calling_params.insert(0, AST_value(VYPaClass(class_name), None))
        for offset, param in enumerate(self.calling_params[1:], 4):
            self.instruction_tape.merge(param.get_instructions(self))
            self.stack.set(param, offset)

        self.check_params(function)
        self.add_instruction(CALL(self.stack.get(2), function))
        self.add_expression_stack_offset()
        return self.instruction_tape
