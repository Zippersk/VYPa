from src.VYPcode.operationsBaseClasses import *


class ADDI(ThreeArgsOperation):
    def __init__(self, first, second, third):
        super().__init__("ADDI", first, second, third)


class ALIAS(TwoArgsOperation):
    def __init__(self, first, second):
        super().__init__("ALIAS", first, second)
