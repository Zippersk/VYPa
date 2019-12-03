from src.VYPcode.Types.VYPaInt import VYPaInt
from src.VYPcode.Types.VYPaString import VYPaString
from src.VYPcode.Types.VYPaVoid import VYPaVoid
from src.VYPcode.Variables.VYPaIntVariable import VYPaIntVariable
from src.VYPcode.Variables.VYPaStringVariable import VYPaStringVariable


def declare_variable(type, name):
    if type == VYPaInt():
        return VYPaIntVariable(name).declare()
    elif type == VYPaString():
        return VYPaStringVariable(name).declare()
    elif type == VYPaVoid():
        Exception("variable can not have type void")

