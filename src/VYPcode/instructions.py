from src.VYPcode.operationsBaseClasses import *


class ADDI(ThreeArgsOperation):
    def __init__(self, first, second, third):
        super().__init__("ADDI", first, second, third)


class ALIAS(TwoArgsOperation):
    def __init__(self, first, second):
        super().__init__("ALIAS", first, second)


class WRITES(OneArgsOperation):
    def __init__(self, first):
        super().__init__("WRITES", first)


class SETWORD(ThreeArgsOperation):
    def __init__(self, first, second, third):
        super().__init__("SETWORD", first, second, third)


class CREATE(TwoArgsOperation):
    def __init__(self, first, second):
        super().__init__("CREATE", first, second)
