from collections import OrderedDict
from enum import Enum


class CallType(Enum):
    SCOPE = 1
    INSTANCE = 2
    THIS = 3
    SUPER = 4


class VariablesStore(OrderedDict):
    def __len__(self):
        size = 0
        variables = self.values()
        for variable in variables:
            size += variable.get_size()
        return size


def get_class(block):
    class_instance = block.parent
    from src.VYPcode.AST.blocks.class_block import AST_class
    while not isinstance(class_instance, AST_class):
        class_instance = block.parent
    return class_instance
