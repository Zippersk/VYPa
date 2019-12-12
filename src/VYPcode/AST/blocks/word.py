from src.VYPcode.AST.blocks.base import AST_block
from src.VYPcode.Instructions.Instructions import GETWORD, SETWORD


class AST_GETWORD(AST_block):
    def __init__(self, first, second, third):
        super().__init__()
        self.first = first
        self.second = second
        self.third = third

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.second.get_instructions(self))
        self.instruction_tape.merge(self.third.get_instructions(self))

        self.add_instruction(GETWORD(self.first, self.second, self.third))
        return self.instruction_tape


class AST_SETWORD(AST_block):
    def __init__(self, first, second, third):
        super().__init__()
        self.first = first
        self.second = second
        self.third = third

    def get_instructions(self, parent):
        self.parent = parent
        self.instruction_tape.merge(self.first.get_instructions(self))
        self.instruction_tape.merge(self.second.get_instructions(self))

        self.add_instruction(SETWORD(self.first, self.second, self.third))
        return self.instruction_tape
