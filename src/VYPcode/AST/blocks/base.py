

class AST_block:
    def __init__(self, previous):
        self.parent = previous

        from src.instructionsTape import InstructionTape
        self.instruction_tape = InstructionTape()

        from src.VYPcode.Stack import Stack
        self.stack = Stack(self.instruction_tape)

    def add_instruction(self, instruction):
        self.instruction_tape.add(instruction)

    def merge_instructions(self, instructions_tape):
        self.instruction_tape.merge(instructions_tape)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_instructions(self):
        return self.instruction_tape

    def jump_out(self):
        from src.VYPcode.AST.AbstractSyntaxTree import AST
        if str(self.parent) != "program":
            AST.current = self.parent

    def jump_in(self):
        from src.VYPcode.AST.AbstractSyntaxTree import AST
        AST.current = self