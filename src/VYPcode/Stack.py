from src.VYPcode.AST.blocks.value import AST_value
from src.VYPcode.Instructions.Instructions import SET, ADDI, SUBI, COMMENT
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Types.VYPaInt import VYPaInt


class Stack:
    def __init__(self, instruction_tape):
        self.instruction_tape = instruction_tape

    def set(self, value, offset=0):
        self.instruction_tape.add(SET(self.get(offset), value))
        return value

    def get(self, offset=0):
        if offset > 0:
            return f"[{VYPaRegister.StackPointer}+{offset}]"
        elif offset < 0:
            return f"[{VYPaRegister.StackPointer}-{abs(offset)}]"
        else:
            return f"[{VYPaRegister.StackPointer}]"

    def push(self, value):
        self.instruction_tape.add(SET(self.get(1), value))
        self.instruction_tape.add(ADDI(VYPaRegister.StackPointer, AST_value(VYPaInt, 1), VYPaRegister.StackPointer))
        return value

    def allocate(self, how_much_variables_to_allocate=1):
        self.instruction_tape.add(ADDI(VYPaRegister.StackPointer,
                                  AST_value(VYPaInt, how_much_variables_to_allocate),
                                  VYPaRegister.StackPointer))

    def deallocate(self, how_much_variables_to_remove=1):
        self.instruction_tape.add(SUBI(VYPaRegister.StackPointer,
                                       AST_value(VYPaInt, how_much_variables_to_remove),
                                  VYPaRegister.StackPointer))

    def pop(self):
        self.instruction_tape.add(SUBI(VYPaRegister.StackPointer,  AST_value(VYPaInt, 1), VYPaRegister.StackPointer))
        return self.get(1)

    def top(self):
        return self.get(0)
