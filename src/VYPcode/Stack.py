from src.VYPcode.Instructions.Instructions import SET, ADDI, SUBI, COMMENT
from src.VYPcode.Registers.Registers import VYPaRegister
from src.VYPcode.Scopes.ProgramTree import PT


class Stack:
    @staticmethod
    def set(value, offset=0, instruction_tape=None):
        if instruction_tape is None:
            instruction_tape = PT.get_current_scope().instruction_tape

        instruction_tape.add(SET(Stack.get(offset), value))
        return value

    @staticmethod
    def get(offset=0):
        if offset > 0:
            return f"[{VYPaRegister.StackPointer}+{offset}]"
        elif offset < 0:
            return f"[{VYPaRegister.StackPointer}-{abs(offset)}]"
        else:
            return f"[{VYPaRegister.StackPointer}]"

    @staticmethod
    def push(value, instruction_tape=None):
        if instruction_tape is None:
            instruction_tape = PT.get_current_scope().instruction_tape

        instruction_tape.add(SET(Stack.get(1), value))
        instruction_tape.add(ADDI(VYPaRegister.StackPointer, 1, VYPaRegister.StackPointer))
        return value

    @staticmethod
    def allocate(how_much_variables_to_allocate=1, instruction_tape=None):
        if instruction_tape is None:
            instruction_tape = PT.get_current_scope().instruction_tape
        PT.get_current_scope().add_relative_SP(how_much_variables_to_allocate)
        instruction_tape.add(ADDI(VYPaRegister.StackPointer, how_much_variables_to_allocate, VYPaRegister.StackPointer))

    @staticmethod
    def deallocate(how_much_variables_to_remove=1, instruction_tape=None):
        if instruction_tape is None:
            instruction_tape = PT.get_current_scope().instruction_tape

        PT.get_current_scope().add_relative_SP(-how_much_variables_to_remove)
        instruction_tape.add(SUBI(VYPaRegister.StackPointer, how_much_variables_to_remove, VYPaRegister.StackPointer))

    @staticmethod
    def pop(instruction_tape=None):
        if instruction_tape is None:
            instruction_tape = PT.get_current_scope().instruction_tape

        instruction_tape.add(SUBI(VYPaRegister.StackPointer, 1, VYPaRegister.StackPointer))
        return Stack.get(1)

    @staticmethod
    def top():
        return Stack.get(0)
