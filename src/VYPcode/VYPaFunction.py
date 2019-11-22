from src.VYPcode import scopes
from src.instructionsTape import InstructionTape


class VYPaFunction:
    def __init__(self, type, name, params):
        self.body = None
        self.type = type
        self.params = params
        self.name = name

    def add_function_body(self, instructions: InstructionTape):
        self.body = instructions

    @staticmethod
    def declare(type, name, params):
        return scopes.add_function(VYPaFunction(type, name, params))