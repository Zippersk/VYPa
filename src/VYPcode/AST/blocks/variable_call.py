from enum import Enum

from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import SET
from src.VYPcode.Registers.Registers import VYPaRegister
from src.common import CallType, get_class


class AST_variable_call(AST_block):
    def __init__(self, name, call_type=CallType.SCOPE, instance_name=None):
        super().__init__()
        self.call_type = call_type
        self.instance_name = instance_name
        self.name = name
        self.variable = None
        self.type = None
        self.stack_offset = 0

    def get_instructions(self, parent):
        self.parent = parent
        self.variable = self.get_variable(self.name)
        self.type = self.variable.type
        self.instruction_tape.add(SET(AST_value(self.type, str(VYPaRegister.Accumulator)), str(self))) # TODO is this necessary?
        return self.instruction_tape

    def get_variable(self, name):
        if self.call_type == CallType.SCOPE:
            return super().get_variable(name)
        elif self.call_type == CallType.INSTANCE:
            return super().get_variable(self.instance_name).get_variable(name)
        elif self.call_type == CallType.THIS:
            self.instruction_tape.merge(AST_variable_call("this").get_instructions(self))
            return get_class(self).get_variable(name)
        elif self.call_type == CallType.SUPER:
            self.instruction_tape.merge(AST_variable_call("this").get_instructions(self))
            return get_class(self).predecessor.get_variable(name)

    def __str__(self):
        if self.call_type == CallType.SCOPE:
            self.stack_offset = self.get_variable_offset(self.name, self.call_type)
            return self.stack.get(-self.stack_offset)
        elif self.call_type == CallType.INSTANCE:
            class_instance = super().get_variable(self.instance_name)
            class_offset = self.get_variable_offset(self.instance_name, CallType.SCOPE)
            variable_offset = class_instance.get_variable_offset(self.name, CallType.SCOPE)
            return self.stack.get(-class_offset - variable_offset)
        elif self.call_type == CallType.THIS or self.call_type == CallType.SUPER:
            class_instance = get_class(self)

            if self.call_type == CallType.THIS:
                self.stack_offset = class_instance.get_variable_offset(self.name, self.call_type)
            elif self.call_type == CallType.SUPER:
                self.stack_offset = class_instance.get_size() + class_instance.predecessor.get_variable_offset(self.name, self.call_type)
            return self.stack.get(-self.stack_offset, VYPaRegister.Accumulator)
