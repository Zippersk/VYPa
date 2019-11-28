from src.VYPcode.VYPaVariables.IntVariable import IntVariable
from src.VYPcode.VYPaVariables.StringVariable import StringVariable


def declare_variable(type, name):
    if type == "int":
        IntVariable(name)
    elif type == "string":
        StringVariable(name)
    elif type == "void":
        Exception("variable can not have type void")