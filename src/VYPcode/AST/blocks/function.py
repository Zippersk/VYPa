from collections import OrderedDict

from src.VYPcode.AST.blocks.assigment import AST_assigment
from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.AST.blocks.function_call import AST_function_call
from src.VYPcode.AST.blocks.variable import AST_variable
from src.VYPcode.Instructions.Instructions import JUMP, COMMENT, LABEL, RETURN
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.error import Exit, Error


class AST_function(AST_block):
    def __init__(self, previous, type, name, params):
        super().__init__(previous)
        self.params = OrderedDict()
        self.variables = OrderedDict()
        self.function_body_statements = []
        self.type = type
        self.name = name
        self.label = f"func_{name}"
        self.function_body_statements = []

        for param in params:
            param.set_parent(self)
            if self.params.get(param.name, None) is not None:
                Exception(f"Param with name {name} already exists")
            else:
                self.params[param.name] = param

    def add_variable(self, type, name):
        if self.variables.get(name, None) is None and self.params.get(name, None) is None:
            variable = AST_variable(self, type, name)
            self.variables[name] = variable
            return variable
        else:
            Exception(f"Variable {name} already exists")

    def get_variable(self, name):
        if self.variables.get(name, None) is not None:
            return self.variables[name]
        elif self.params.get(name, None) is not None:
            return self.params[name]
        else:
            Exception(f"Variable {name} not found in function scope")

    def add_assigment(self, name, expression):
        variable = self.get_variable(name)
        self.function_body_statements.append(AST_assigment(self, variable, expression))

    # used only with build in functions
    def add_body(self, body):
        self.function_body_statements.append(body)

    def add_function_call(self, name, calling_params):
        self.function_body_statements.append(AST_function_call(self, name, calling_params))

    def add_return(self, expression):
        if not expression and self.type != VYPaVoid():
            Exit(Error.SyntaxError, "Function has empty return and is not void")

        self.deallocate_and_return(expression)

    def deallocate_and_return(self, expression=None):

        dealloc_count = len(self.variables) + len(self.params)
        self.instruction_tape.add(COMMENT(f"Deallocate {dealloc_count} scope variables and paramters"))
        self.stack.deallocate(dealloc_count)

        if self.type != VYPaVoid():
            if not expression:
                self.instruction_tape.add(COMMENT(f"Set default return value"))
                self.stack.set(self.type.get_default(), -1)
            else:
                self.instruction_tape.add(COMMENT(f"Set return value"))
                self.stack.set(expression, -1)

        self.instruction_tape.add(RETURN(self.stack.pop()))

    def get_variable_index(self, name):
        if self.params.get(name, None) is not None:
            return list(self.params).index(name)
        elif self.variables.get(name, None) is not None:
            return len(self.params) + list(self.variables).index(name)
        else:
            Exception(f"Variable {name} not found in function scope")

    def get_instructions(self):
        self.add_instruction(COMMENT(""))
        self.add_instruction(COMMENT(f"Start of function {self.name}"))
        self.add_instruction(LABEL(self.label))

        for variable in self.variables.values():
            self.merge_instructions(variable.get_instructions())

        for statement in self.function_body_statements:
            self.merge_instructions(statement.get_instructions())

        if str(self.get_parent()) == "program" and self.name == "main" and self.type == VYPaVoid():
            self.add_instruction(JUMP("END"))
        else:
            self.deallocate_and_return()

        self.add_instruction(COMMENT(f"End of function {self.name}"))
        self.add_instruction(COMMENT(""))

        return self.instruction_tape

    def __str__(self):
        return self.label