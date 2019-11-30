class OperationBase:
    pass


class NoArgsOperation(OperationBase):
    def __init__(self, operation):
        self.operation = operation

    def evaluate_operands(self):
        pass

    def __str__(self):
        return f'{self.operation}'


class OneArgsOperation(OperationBase):
    def __init__(self, operation, first):
        self.operation = operation
        self.first = first

    def evaluate_operands(self):
        self.first = str(self.first)

    def __str__(self):
        return f'{self.operation} {self.first}'


class TwoArgsOperation(OperationBase):
    def __init__(self, operation, first, second):
        self.operation = operation
        self.first = first
        self.second = second

    def evaluate_operands(self):
        self.first = str(self.first)
        self.second = str(self.second)

    def __str__(self):
        return f'{self.operation} {self.first} {self.second}'


class ThreeArgsOperation(OperationBase):
    def __init__(self, operation, first, second, third):
        self.operation = operation
        self.first = first
        self.second = second
        self.third = third

    def evaluate_operands(self):
        self.first = str(self.first)
        self.second = str(self.second)
        self.third = str(self.third)

    def __str__(self):
        return f'{self.operation} {self.first} {self.second} {self.third}'
