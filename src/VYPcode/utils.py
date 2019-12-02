from src.VYPcode.VYPaTypes.VYPaInt import VYPaInt
from src.VYPcode.VYPaTypes.VYPaString import VYPaString
from src.VYPcode.VYPaTypes.VYPaVoid import VYPaVoid
from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable


def declare_variable(type, name):
    if type == VYPaInt():
        return IntVariable(name).declare()
    elif type == VYPaString():
        return StringVariable(name).declare()
    elif type == VYPaVoid():
        Exception("variable can not have type void")

