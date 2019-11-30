from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable


def declare_variable(type, name):
    if type == "int":
        IntVariable(name).declare()
    elif type == "string":
        StringVariable(name).declare()
    elif type == "void":
        Exception("variable can not have type void")
