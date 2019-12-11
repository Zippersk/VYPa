class AST_block:
    def __init__(self):
        self.parent = None

        from src.instructionsTape import InstructionTape
        self.instruction_tape = InstructionTape()

        from src.VYPcode.Stack import Stack
        self.stack = Stack(self.instruction_tape)
        self.AST_blocks = []

    def add_block(self, block):
        self.AST_blocks.append(block)
        block.set_parent(self)
        return block

    def add_instruction(self, instruction):
        self.instruction_tape.add(instruction)

    def merge_instructions(self, instructions_tape):
        self.instruction_tape.merge(instructions_tape)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_instructions(self, parent):
        self.parent = parent
        return self.instruction_tape

    def get_variable(self, name):
        return self.parent.get_variable(name)
