"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.Types.baseType import VYPaBaseType


class VYPaClass(VYPaBaseType):
    def __init__(self, name):
        super().__init__(name, 0)

    def __eq__(self, other):
        # TODO rewrite to compare with parent class also
        return self.name == other.name
