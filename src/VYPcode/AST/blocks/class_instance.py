from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import SET, COMMENT
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.common import CallType
from src.error import Exit, Error


class AST_class_instance(AST_block):
    def __init__(self, class_name):
        super().__init__()
        self.class_name = class_name
        self.class_block = None
        self.type = VYPaClass(class_name)

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exit(Error.SyntaxError, f"Variable {variable.name} already exists")

    def get_variable(self, name):
        if self.variables.get(name, None) is not None:
            return self.variables[name]
        else:
            if self.class_block.name != "Object":
                self.class_block.predecessor.get_variable(name)
            else:
                Exit(Error.SyntaxError, f"Variable {name} was not defined")

    def get_variable_offset(self, name, call_type):
        if name == "this":
            return len(self.variables) - 1
        if call_type == CallType.THIS and self.variables.get(name, None) is not None:
            return list(self.variables)[::-1].index(name)
        elif call_type == CallType.SUPER:
            return self.class_block.predecessor.get_variable_offset(name, CallType.THIS)
        else:
            Exit(Error.SyntaxError, f"Variable {name} not found in function scope")

    def get_size(self):
        size = 0
        if self.class_block.name != "Object":
            size = self.class_block.predecessor.get_size()

        return size + len(self.variables)

    def get_constructor(self):
        constructor = self.class_block.functions.get(self.class_block.name, None)
        if constructor and len(constructor.params) == 0 and constructor.type == VYPaVoid():
            return constructor
        return None

    def get_instructions(self, parent):
        self.parent = parent
        self.class_block = AST.root.get_class(self.class_name)
        self.add_instruction(COMMENT(f"Start constructor of {self.class_block.name}"))
        if self.class_block.name != "Object":
            self.class_block.predecessor = AST_class_instance(self.class_block.predecessor_name)
            self.instruction_tape.merge(self.class_block.predecessor.get_instructions(self))

        for variable in self.class_block.AST_blocks:
            self.merge_instructions(variable.get_instructions(self))

        constructor = self.get_constructor()
        if constructor:
            self.instruction_tape.merge(AST_function_call(self.class_block.name, [], CallType.THIS))

        self.add_instruction(COMMENT(f"End constructor of {self.class_block.name}"))
        self.instruction_tape.add(SET(VYPaRegister.Accumulator, VYPaRegister.StackPointer))

        return self.instruction_tape

    def __str__(self):
        return str(AST_value(VYPaClass(self.class_name), str(VYPaRegister.Accumulator)))
