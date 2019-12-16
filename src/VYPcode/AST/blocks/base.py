from src.common import CallType, VariablesStore


class AST_block:
    def __init__(self):
        self.parent = None

        from src.instructionsTape import InstructionTape
        self.instruction_tape = InstructionTape()

        from src.VYPcode.Stack import Stack
        self.stack = Stack(self.instruction_tape)
        self.AST_blocks = []
        self.variables = VariablesStore()

    def add_block(self, block):
        self.AST_blocks.append(block)
        block.set_parent(self)
        return self

    def add_instruction(self, instruction):
        self.instruction_tape.add(instruction)
        return self

    def merge_instructions(self, instructions_tape):
        self.instruction_tape.merge(instructions_tape)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_instructions(self, parent):
        self.parent = parent
        for block in self.AST_blocks:
            self.instruction_tape.merge(block.get_instructions(self))
        return self.instruction_tape

    def get_variable(self, name):
        if self.variables.get(name, None) is not None:
            return self.variables.get(name)
        return self.parent.get_variable(name)

    def get_variable_offset(self, name, call_type):
        if call_type == CallType.SCOPE and self.variables.get(name, None) is not None:
            return list(self.variables)[::-1].index(name)
        else:
            return len(self.variables) + self.parent.get_variable_offset(name, call_type)
