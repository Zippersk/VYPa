class NoArgsOperation:
    def __init__(self, operation):
        self.operation = operation

    def __str__(self):
        return f'{self.operation}'


class OneArgsOperation:
    def __init__(self, operation, first):
        self.operation = operation
        self.first = first

    def __str__(self):
        return f'{self.operation} {self.first}'


class TwoArgsOperation:
    def __init__(self, operation, first, second):
        self.operation = operation
        self.first = first
        self.second = second

    def __str__(self):
        return f'{self.operation} {self.first} {self.second}'


class ThreeArgsOperation:
    def __init__(self, operation, first, second, third):
        self.operation = operation
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return f'{self.operation} {self.first} {self.second} {self.third}'
