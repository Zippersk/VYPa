"""
|**********************************************************************;
* Project           : VYPcode compiler 2019
* Authors           : Michal Horky (xhorky23), Matus Mucka (xmucka03)
|**********************************************************************;
"""
﻿from src.VYPcode.Types.baseType import VYPaBaseType


class VYPaString(VYPaBaseType):
    def __init__(self):
        super().__init__("string", '""')