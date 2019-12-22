"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.blocks.assigment import AST_assigment
from src.VYPcode.AST.blocks.binaryOperations.SUB import AST_SUBI
from src.VYPcode.AST.blocks.declaration import AST_declaration
from src.VYPcode.AST.blocks.expression import AST_expression
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.AST.blocks.variable_call import AST_variable_call
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaClass import VYPaClass
from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.instructionsTape import InstructionTape
from collections import OrderedDict

from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL, DUMPSTACK, DUMPREGS, SET
from src.error import Exit, Error


class AST_class_instance(AST_block):
    def __init__(self, name):
        super().__init__()
        self.class_block = None
        self.name = name
        self.type = VYPaClass(name)
        self.predecessor = None

    def add_variable(self, variable):
        if self.variables.get(variable.name, None) is None:
            variable.set_parent(self)
            self.variables[variable.name] = variable
            return variable
        else:
            Exit(Error.SyntaxError, f"Variable {variable.name} already exists")

    def get_variable(self, name):
        if name == "super":
            return self.predecessor.get_variable("this")
        if self.variables.get(name, None) is not None:
            return self.variables[name]
        else:
            if self.name != "Object":
                self.class_block.predecessor.get_variable(name)
            else:
                Exit(Error.SyntaxError, f"Variable {name} was not defined")

    def get_variable_offset(self, name):
        if self.variables.get(name, None) is not None:
            return list(self.variables)[::-1].index(name)
        else:
            Exit(Error.SyntaxError, f"Variable {name} not found in function scope")

    def get_instructions(self, parent):
        self.parent = parent
        self.class_block = AST.root.get_class(self.name)

        if self.name != "Object":
            self.predecessor = AST_class_instance(self.class_block.predecessor_name)
            self.merge_instructions(self.predecessor.get_instructions(self))

        self.add_instruction(COMMENT(f"Constructor of class {self.name}"))
        for declaration in self.class_block.declarations:
            self.merge_instructions(declaration.get_instructions(self))

        if self.name == "Object":
            top_most_children = self
            while isinstance(top_most_children.parent, AST_class_instance):
                top_most_children = top_most_children.parent
            self.merge_instructions(
                AST_assigment(AST_variable_call("**runtime_name**"), AST_value(VYPaString(), f'"{top_most_children.name}"')).get_instructions(self))

        self.merge_instructions(AST_declaration(VYPaClass(self.name), ["this"]).get_instructions(self))
        self.merge_instructions(AST_assigment(
            AST_variable_call("this"),
            AST_value(VYPaInt(), VYPaRegister.StackPointer)).get_instructions(self))

        constructor = AST.root.functions.get(f"{self.name}_{self.name}", None)
        if constructor and constructor.type == VYPaVoid() and len(constructor.params) == 1:
            self.merge_instructions(
                AST_expression(
                    AST_function_call(f"{self.name}_{self.name}", [AST_variable_call("this")])
                ).get_instructions(self)
            )

        self.add_instruction(SET(VYPaRegister.Accumulator, self.stack.top()))
        self.add_instruction(COMMENT(f"End of {self.name} constructor"))

        return self.instruction_tape

