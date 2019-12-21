"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.AST.AbstractSyntaxTree import AST
from src.VYPcode.Types.baseType import VYPaBaseType


class VYPaClass(VYPaBaseType):
    def __init__(self, name):
        super().__init__(name, 0)

    def __eq__(self, other):
        class_name = self.name

        while class_name is not None:
            other_class_name = other.name
            while other_class_name is not None:
                if class_name == other_class_name:
                    return True
                else:
                    other_class_name = AST.root.get_class(other_class_name).predecessor_name \
                        if AST.root.classes.get(other_class_name, None) else None

            class_name = AST.root.get_class(class_name).predecessor_name \
                if AST.root.classes.get(class_name, None) else None

        return False
