from src.VYPcode.Stack import Stack
from src.VYPcode.VYPaFunctions.VYPaFunction import VYPaFunction
from src.VYPcode.VYPaOperations.operations import LABEL, WRITEI, RETURN, DUMPSTACK, WRITES
from src.VYPcode.VYPaTypes.VYPaVoid import VYPaVoid
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable
from src.VYPcode.scopes.ProgramTree import PT
from src.VYPcode.utils import declare_variable


class VYPaBuildInFunctionClass(VYPaFunction):
    def __init__(self, type, name, params):
        super().__init__(type, name, params)
        self.label = f"buildIn_{name}"
        super().declare()

        from src.instructionsTape import InstructionTape  # TODO: fix circular dependencies
        self.instructions = InstructionTape()

    def register(self):
        PT.push_scope()

        for instruction in self.instructions.get_instructions():
            PT.get_current_scope().instruction_tape.add(instruction)

        self.deallocate_and_return()
        PT.pop_scope()


class PrintIntVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printInt", [IntVariable("number")])
        self.instructions.add(WRITEI(Stack.top()))


class PrintStringVYPa(VYPaBuildInFunctionClass):
    def __init__(self):
        super().__init__(VYPaVoid(), "printString", [StringVariable("string")])
        self.instructions.add(WRITES(Stack.top()))




# readInt
# readString
# length
# subStr
