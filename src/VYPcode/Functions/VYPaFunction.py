from src.VYPcode.Stack import Stack
from src.VYPcode.Functions.FunctionResult import FunctionResult
from src.VYPcode.Instructions.Instructions import ADDI, JUMP, LABEL, SUBI, SET, CALL, DUMPSTACK, RETURN, COMMENT
from src.VYPcode.Types.VYPaVoid import VYPaVoid

from src.VYPcode.Scopes.ProgramTree import PT
from src.VYPcode.utils import declare_variable
from src.error import Exit, Error


class VYPaFunction:
    def __init__(self, type, name, params):
        self.declared = type is not None
        self.type = type
        self.params = params
        self.name = name
        self.label = f"func_{name}"

    def declare(self):
        PT.get_current_scope().instruction_tape.add(LABEL(self.label))
        PT.get_current_scope().add_function(self)
        PT.push_scope()
        for param in self.params:
            PT.get_current_scope().add_variable(param)
        return self

    def get_type(self):
        return self.type

    def call(self, calling_params):
        for param in calling_params:
            Stack.push(param)

        PT.get_current_scope().instruction_tape.add(CALL(Stack.get(-len(self.params)), self, calling_params))

        # after all params are pushed in stack we can deallocate return value and return address from scope
        PT.get_current_scope().add_relative_SP(-2)
        return FunctionResult(self)

    def throw_if_not_declared(self):
        if not self.declared:
            Exit(Error.SyntaxError, "Function not declared")

    def deallocate_and_return(self, expression=None):

        PT.get_current_scope().deallocate_variables()

        if self.get_type() != VYPaVoid():
            if not expression:
                PT.get_current_scope().instruction_tape.add(COMMENT(f"Set default return value"))
                Stack.set(self.type.get_default(), -1)
            else:
                PT.get_current_scope().instruction_tape.add(COMMENT(f"Set return value"))
                Stack.set(expression, -1)

        PT.get_current_scope().instruction_tape.add(RETURN(Stack.pop()))

    def __str__(self):
        return self.label
