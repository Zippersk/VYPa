"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
from src.VYPcode.Registers.Registers import RegisterBase


class VYPaBaseType:
    def __init__(self, name, default):
        self.default = default
        self.name = name

    def get_name(self):
        return self.name

    def get_default(self):
        return self.default

    def __eq__(self, other):
        return self.name == other.name
