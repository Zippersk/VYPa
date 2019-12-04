class OperationBase:
    pass


class NoArgsInstruction(OperationBase):
    def __init__(self, operation):
        self.operation = operation

    def __str__(self):
        return f'{self.operation}'


class OneArgsInstruction(OperationBase):
    def __init__(self, operation, first):
        self.operation = operation
        self.first_str = str(first)
        self.first = first

    def __str__(self):
        return f'{self.operation} {self.first_str}'


class TwoArgsInstruction(OperationBase):
    def __init__(self, operation, first, second):
        self.operation = operation
        self.first_str = str(first)
        self.second_str = str(second)
        self.first = first
        self.second = second

    def __str__(self):
        return f'{self.operation} {self.first_str} {self.second_str}'


class ThreeArgsInstruction(OperationBase):
    def __init__(self, operation, first, second, third):
        self.operation = operation
        self.first_str = str(first)
        self.second_str = str(second)
        self.third_str = str(third)
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return f'{self.operation} {self.first_str} {self.second_str} {self.third_str}'
